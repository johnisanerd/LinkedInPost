# Frontend review A (features: add-topic, ai-draft, editor, review, review-editor, content-flow, content-review, generation, content-schedule-calendar, scheduled-publish, variant, draft-selection-target, persistence, workflows, topic-navigation, news-research, feed; stores; services)
Counts: P0=1, P1=8, P2=16, P3=6 (total 31). All findings are static code reading; nothing was executed.
Convention: line numbers are from the working tree on branch `launch-readiness-review`. "(hypothesis)" = reasoning needs a run to confirm.

### FEA-001 Calendar / bulk reschedule of an already queued post silently kills the queued publish
- **Sev:** P0
- **Area:** frontend/src/components/dashboard/index.tsx (handleCalendarRescheduleCommit, handleBulkSetSchedule, handleUpdatePostSchedule), frontend/src/features/scheduled-publish/usePendingScheduledPublish.ts; cross-ref worker/src/index.ts:4777
- **Journeys:** J-082, J-083, J-084, J-087
- **Evidence:** index.tsx:521-580 only calls `api.updatePostSchedule(row, postTime)`, which rewrites `row.postTime`. The worker alarm handler returns early when `String(row.postTime).trim() !== task.scheduledTime.trim()` (worker/src/index.ts:4777), so the Durable Object task queued for the old time becomes a no-op. The frontend never calls `cancelScheduledPublish` or re-queues via `publishContent`, and the in-memory `pending` banner state is not updated. The post never goes out and no one is told.
- **Repro:** (static reasoning) Schedule a LinkedIn post for T+10 min from the editor (deliveryMode `queued`). Open the calendar, drag the same post to T+20 min and confirm. Wait past both times: nothing publishes, row stays Approved.
- **Fix hint:** On any schedule change for a row with status Approved, cancel the queued task for the old time and call `publishContent` again for the new time (or have the worker `updatePostSchedule` action re-queue). At minimum block drag/reschedule for rows that have a queued publish.
- **Status:** open
- **Verified:** read-only: frontend/src/components/dashboard/index.tsx, frontend/src/features/scheduled-publish/*, frontend/src/features/content-schedule-calendar/adapters/sheetRowAdapter.ts, worker/src/index.ts (4765-4785), worker/src/scheduled-publish/time.ts

### FEA-002 Editor stores post time as UTC, calendar and drag-reschedule treat the same string as local wall-clock
- **Sev:** P1
- **Area:** frontend/src/features/review/context/useReviewFlowActions.ts (handleApprove/handlePublishNow), frontend/src/features/review/context/useReviewFlowState.ts (getInitialPostTime), frontend/src/features/content-schedule-calendar/adapters/sheetRowAdapter.ts, frontend/src/features/content-schedule-calendar/scheduleValidation.ts, frontend/src/components/dashboard/index.tsx
- **Journeys:** J-086, J-087, J-085, J-082
- **Evidence:** useReviewFlowActions.ts:632-641 converts the `datetime-local` value to UTC (`getUTC*`) before sending `YYYY-MM-DD HH:mm`; useReviewFlowState.ts:92-104 reads it back as UTC. The worker parses it as UTC (`Date.UTC` in worker/src/scheduled-publish/time.ts). But `deriveCalendarFieldsFromSheetRow` (sheetRowAdapter.ts:9-23) shows the raw string's HH:mm as the local time, `handleCalendarRescheduleCommit` writes `${date} ${time}` (local wall-clock picked on the grid) back as if it were UTC, and `isLocalScheduleInPast` checks local time. In any non-UTC browser a post scheduled for 09:00 local shows at the UTC hour on the calendar, and a drag to 10:00 schedules it at 10:00 UTC.
- **Repro:** (static reasoning) Set browser TZ to Asia/Kolkata, schedule 09:00 in the editor; observe the sheet value `03:30`; open calendar: event at 03:30. Drag to 10:00: sheet value `10:00`, editor then shows 15:30.
- **Fix hint:** Pick one canonical representation. Smallest: make the calendar adapter and reschedule commit convert UTC<->local the same way the editor does (shared helper), and run the past-time check on the converted value.
- **Status:** open
- **Verified:** read-only: useReviewFlowActions.ts, useReviewFlowState.ts, sheetRowAdapter.ts, scheduleValidation.ts, dashboard/index.tsx 505-580, worker/src/scheduled-publish/time.ts

### FEA-003 Pending scheduled publish exists only in React memory and holds a single slot
- **Sev:** P1
- **Area:** frontend/src/features/scheduled-publish/usePendingScheduledPublish.ts, frontend/src/features/scheduled-publish/matchPending.ts, frontend/src/features/scheduled-publish/ScheduledPublishBanner.tsx
- **Journeys:** J-082, J-084, J-088
- **Evidence:** `pending` is a `useState` (usePendingScheduledPublish.ts:15). It is set only from the response of `publishContent` in this tab (applyQueuedPublishResult, lines 17-28), never hydrated from the server on load, and a second queued publish overwrites the first. After a reload, navigation that remounts the hook, a second tab, or scheduling a second topic, the banner, the Cancel button, and the "already queued" guard (`rowMatchesPendingScheduledPublish`, used at useReviewFlowActions.ts:672 and useDashboardQueue.ts:542/615) all disappear. The user cannot cancel the earlier queued post from the UI and can queue the same post a second time (double publish).
- **Repro:** (static reasoning) Schedule post A, schedule post B (A's banner is gone), or schedule A then reload: no banner, "Publish" is enabled again and re-queues A.
- **Fix hint:** Have the worker return queued tasks in `bootstrap`/`getRows` (or a `listScheduledPublishes` read) and keep a map keyed by topicId+channel; at minimum derive the banner from `row.status/postTime` plus a server query.
- **Status:** open
- **Verified:** read-only: usePendingScheduledPublish.ts, matchPending.ts, ScheduledPublishBanner.tsx, useDashboardQueue.ts, EditorScreen.tsx

### FEA-004 "Send to Generation" navigates away without consuming the SSE stream; topic left Pending with no refresh or error
- **Sev:** P1 (hypothesis on worker-side cancellation)
- **Area:** frontend/src/components/dashboard/components/TopicPostPreviewCard.tsx, frontend/src/services/backendApi.ts (sendTopicToGeneration), frontend/src/features/topic-navigation/screens/TopicVariantsPage.tsx; cross-ref worker/src/index.ts:1165-1270
- **Journeys:** J-056, J-054, J-055, J-053
- **Evidence:** TopicPostPreviewCard.tsx:62-66: on `response.ok` it immediately `navigate(...)` and never reads `response.body`, so `error`/`complete` SSE events are discarded. The worker flips the row to Pending (index.ts:1217) and relays the generation stream through an un-awaited async IIFE with no `waitUntil` (index.ts:1235-1262); if the client drops the stream the relay or upstream may be cancelled. Nothing in the dashboard polls or reloads rows (no interval anywhere under components/dashboard), so the variants page shows the "pending" detail view until the user manually refreshes. A generation error is never shown and the row stays Pending.
- **Repro:** Create a Draft topic, click "Send to Generation", then watch the variants page: it stays on the pending view; kill the generation worker beforehand and confirm no error is shown and status stays Pending.
- **Fix hint:** Read the SSE stream on the client (or poll `getRows` until variants arrive), show progress/errors, and have the worker run the relay under `ctx.waitUntil` and revert status to Draft on failure.
- **Status:** open
- **Verified:** read-only: TopicPostPreviewCard.tsx, backendApi.ts 1456-1474, worker/src/index.ts 1160-1270, TopicVariantsPage.tsx, dashboard/index.tsx (TopicVariantsOrDetail)

### FEA-005 `topicGenerationRules` is used for two different things: Add-Topic JSON metadata and the "Topic rules" text that overrides global/template rules
- **Sev:** P1
- **Area:** frontend/src/features/add-topic/AddTopicPage.tsx, frontend/src/features/rules/RulesPanel.tsx, frontend/src/features/review/context/useReviewFlowState.ts (resolveEffectiveGenerationRulesWithTemplate), worker/src/index.ts:1639,1658,1186; worker/src/generation/rules.ts:10
- **Journeys:** J-035, J-037, J-071, J-072, J-075, J-053, J-056
- **Evidence:** AddTopicPage handleSubmit (≈line 283-300) sends `{about, meaning, style, pros, cons, notes, audience}`; the worker stores `JSON.stringify(topicMeta)` into the same `topic_generation_rules` column (worker index.ts:1639/1658) that the editor Rules panel treats as free-text "Topic rules". `resolveEffectiveGenerationRulesWithTemplate` (useReviewFlowState.ts:65-81, worker rules.ts:10-20) returns the local value first when non-empty, so for every topic created with any metadata the JSON blob replaces the user's personal rules, global rules and the selected template as the "rules" fed to the prompt, and RulesPanel shows raw JSON as the topic's rules. Conversely, saving topic rules in the editor overwrites the metadata JSON, so `sendTopicToGeneration` (worker index.ts:1186-1200) silently loses about/meaning/audience/tone, and editing a topic in Add-Topic after that wipes the saved rules (non-JSON text fails `JSON.parse` in AddTopicPage.tsx:203-208 and is then overwritten on save).
- **Repro:** Add a topic with an "About" text and a Style. Open it in the editor: Rules panel shows `{"about":...}` and `Topic overrides` is on; generate a draft: the user's global rules are not applied. Then type rules in the panel and save: reopen Add-Topic edit and the fields are empty.
- **Fix hint:** Store Add-Topic metadata in its own column/field (e.g. `topic_meta`) and keep `topicGenerationRules` for rules only; until then, exclude values that parse as the metadata object from the rules resolution.
- **Status:** open
- **Verified:** read-only: AddTopicPage.tsx, TopicDetailView.tsx (parseTopicMeta), useReviewFlowState.ts 65-81 and 530-540, RulesPanel.tsx, worker/src/index.ts 1030-1060, 1180-1200, 1630-1670, worker/src/generation/rules.ts

### FEA-006 Auto-saved editor drafts are never offered for recovery on the editor route
- **Sev:** P1
- **Area:** frontend/src/features/review/context/useReviewFlowState.ts, frontend/src/features/review/components/ReviewDialogs.tsx
- **Journeys:** J-064, J-021
- **Evidence:** The editor autosaves to `draft-autosave-<topicId>` (useReviewFlowState.ts:615-679). Recovery is only armed in `buildInitialState` when `routed?.screen === 'variants'` (lines 273-282); the routed `editor` branch hard-codes `draftRecoveryPending: false` (line 258). So after a tab close, crash, or Google token expiry during editing, reopening the editor URL discards the work. Reaching the variants screen first and then picking a variant calls `applySheetVariantBase`, which replaces the editor text with the sheet variant, so the restored text is thrown away too.
- **Repro:** Open `/topics/<id>/editor/0`, type 300 words, wait 3 s (autosave), close the tab, reopen the same URL: original sheet text, no restore prompt.
- **Fix hint:** Arm `draftRecoveryPending` for the editor screen too (compare against the slot text), and show the prompt before applying.
- **Status:** open
- **Verified:** read-only: useReviewFlowState.ts, ReviewDialogs.tsx, services/draftService.ts

### FEA-007 Draft recovery restores before the user answers; "Start fresh" does not revert
- **Sev:** P2
- **Area:** frontend/src/features/review/context/useReviewFlowState.ts:682-690, frontend/src/features/review/components/ReviewDialogs.tsx:36-52
- **Journeys:** J-064
- **Evidence:** The effect at useReviewFlowState.ts:682-690 immediately writes the saved draft into `editorText`/`postTime`/`selectedImageUrls` as soon as `draftRecoveryPending` is true. The dialog then asks "Restore previous draft?", but its cancel path ("Start fresh") only clears localStorage and hides the dialog (ReviewDialogs.tsx:41-44); the restored (possibly up-to-24h-old) text stays in the editor and the baseline is also overwritten (`setEditorBaselineText`), so it no longer shows as dirty.
- **Repro:** (static reasoning) Reach variants screen with a differing autosave, click "Start fresh": editor text is still the stale draft.
- **Fix hint:** Move the restore into the dialog's confirm handler and leave state untouched on cancel.
- **Status:** open
- **Verified:** read-only: useReviewFlowState.ts 270-290 and 680-692, ReviewDialogs.tsx

### FEA-008 "Continue editing" on a saved Draft opens a blank new-topic form and saving creates a duplicate
- **Sev:** P1
- **Area:** frontend/src/components/dashboard/components/TopicPostPreviewCard.tsx:122,210; frontend/src/components/dashboard/index.tsx:75-80; frontend/src/features/add-topic/AddTopicPage.tsx
- **Journeys:** J-035, J-037, J-056
- **Evidence:** The button navigates to `${addTopic}?topicId=<id>`, but `AddTopicPageWithEdit` only reads `searchParams.get('edit')` (index.tsx:76; TopicDetailView uses `?edit=`). With no `edit`, `editRow` is undefined, the form starts empty (plus the module-level draft), and "Save Draft" calls `addTopic`, creating a second topic while the original Draft stays.
- **Repro:** Add a topic (Draft), open it from the list, click "Continue editing": empty form, title empty. Type a title and save: two topics.
- **Fix hint:** Use `?edit=` in TopicPostPreviewCard (one-line fix) or accept both params in `AddTopicPageWithEdit`.
- **Status:** open
- **Verified:** read-only: TopicPostPreviewCard.tsx, dashboard/index.tsx 60-95, TopicDetailView.tsx, AddTopicPage.tsx

### FEA-009 Browser-stored workspace data is not scoped to the signed-in user and is not cleared on sign-out
- **Sev:** P1
- **Area:** frontend/src/stores/feedStore.ts (`feed-store-v1`), frontend/src/features/feed/FeedPage.tsx (`feed-clips-v2`, `read_articles`, `feed-followed-groups`), frontend/src/features/review/context/useReviewFlowState.ts / services/draftService.ts (`draft-autosave-*`, `version-history-*`), frontend/src/features/feed/components/DraftContextView.tsx (`feed_draft_*`), frontend/src/features/add-topic/AddTopicPage.tsx (module-level `draft`), frontend/src/App.tsx:359-375
- **Journeys:** J-026, J-142, J-044, J-041, J-140
- **Evidence:** Sign-out removes only `google_id_token` (App.tsx:359/375, WorkspaceShell.tsx:63). All of the keys above are unkeyed by user. FeedPage initialises `clips` from localStorage (FeedPage.tsx:168-173) and only replaces it with the server list `if (result.clips.length > 0)` (lines 308-312), so a second user on the same browser (or a user with zero server clips) sees and can assign the previous user's clips; the Zustand feed store restores the previous user's cached articles for the same group id; the Add-Topic form (module-level object, SPA sign-out does not reload) shows the previous user's half-written topic; autosaved post text stays in localStorage.
- **Repro:** Sign in as user A, clip two articles and start a topic, sign out, sign in as user B (no clips): B sees A's clips in the dock and A's topic text in Add Topic.
- **Fix hint:** On sign-out and on `session.email` change clear these keys (and `useFeedStore.getState().clear()`); prefix keys with a user hash; always replace local clips with the server response (including empty).
- **Status:** open
- **Verified:** read-only: feedStore.ts, FeedPage.tsx 120-200 and 300-330, App.tsx, WorkspaceShell.tsx, draftService.ts, AddTopicPage.tsx 14-30

### FEA-010 Clip creation, passage clip, delete, assign and update failures are silent (feed clips)
- **Sev:** P1
- **Area:** frontend/src/features/feed/FeedPage.tsx:184-233, 280-296; frontend/src/features/feed/components/ClipsDock.tsx:66-76
- **Journeys:** J-044, J-045
- **Evidence:** `handleClip` and `handleClipPassage` catch and ignore (`// silently skip`, `/* silent */`), so a failed clip shows nothing (the clip button looks like nothing happened, or the SelectionClipper tooltip dismisses as if it saved). `handleDeleteClip` removes the clip locally first and ignores the failure, so it reappears at the next load; `handleAssignClipToPost`/`handleUnassignClip` also silent, and `handleSaveClipEdit` closes nothing and shows nothing on failure.
- **Repro:** Block the worker (or use an expired token) and clip an article: no message. Delete a clip while offline: gone until reload.
- **Fix hint:** Surface an error notice in each catch and roll back optimistic state; handle auth-expired via `onAuthExpired`.
- **Status:** open
- **Verified:** read-only: FeedPage.tsx 184-300, ClipsDock.tsx 40-100

### FEA-011 Bulk and calendar schedule operations swallow errors; bulk delete leaves queued publishes
- **Sev:** P2
- **Area:** frontend/src/components/dashboard/index.tsx:496-580
- **Journeys:** J-087, J-039, J-083
- **Evidence:** `handleBulkDelete`, `handleBulkSetSchedule`, `handleUpdatePostSchedule` and the per-topic loop of `handleCalendarRescheduleCommit` all use empty `catch {}` and then `loadData(true)` (which itself ignores failures when `quiet`). The optimistic `applyOptimisticPostSchedule` is applied first, so a failed write briefly shows the new time. `handleBulkDelete` never cancels queued scheduled publishes (only the single-topic `handleDeleteTopic` does, and only for the in-memory pending), so a deleted row may still have an alarm (the alarm checks row existence server-side; see FEA-001 for the related guard).
- **Repro:** Select several rows, bulk delete with the worker returning errors: no message, rows reappear after reload.
- **Fix hint:** Collect failures and show one summary notice; cancel queued tasks before deleting.
- **Status:** open
- **Verified:** read-only: dashboard/index.tsx, useDashboardQueue.ts handleDeleteTopic

### FEA-012 Retrying publish after a failure creates another draft copy of an already published post
- **Sev:** P2
- **Area:** frontend/src/components/dashboard/hooks/useDashboardQueue.ts:602-750
- **Journeys:** J-091, J-089, J-088
- **Evidence:** For a `published` row, `publishFromReviewEditor` calls `createDraftFromPublished` (line 646), refetches rows, then `updateRowStatus` and `publishContent`. If `publishContent` fails (token expired, validation), the copy remains; the user's retry from the same editor (still bound to the published row) creates a second and third copy. `handleApproveVariant` (lines 161-181) does the same for "Save edits".
- **Repro:** Open a Published post, edit, click Publish while the LinkedIn token is revoked; click again: two draft copies in the queue.
- **Fix hint:** Remember the created copy's topicId in component state and reuse it on retry, or delete the copy on failure.
- **Status:** open
- **Verified:** read-only: useDashboardQueue.ts

### FEA-013 In-flight AI/image/save responses are applied to whatever topic is on screen (workspace not keyed by topic)
- **Sev:** P2
- **Area:** frontend/src/features/review/context/useReviewFlowActions.ts:229-274, 462-480, 576-622; frontend/src/features/topic-navigation/screens/TopicEditorPage.tsx; frontend/src/features/review/ReviewWorkspace.tsx
- **Journeys:** J-065, J-066, J-067, J-064
- **Evidence:** `ReviewWorkspace`/`ReviewFlowProvider` is not given `key={topicId}`; navigation between topic editor URLs only dispatches `INIT_ROW` (useReviewFlowState.ts:395-397). `handleGenerateQuickChange`, `handleGenerateVariants`, image fetch/upload/generate handlers have no request token or abort: a slow response for topic A calls `setQuickChangePreview(previewA)` / `setAlternateImageOptions` / `autoSelectNewImage` after the user moved to topic B, so "Review changes" would offer A's rewrite for B and an image from A's search can be auto-selected for B's post. State outside the reducer (`researchContextArticles`, `contextDocuments`, `postType`, `dimensionWeights`, `rewriteIntensity`) also survives topic changes.
- **Repro:** Start Quick Change on topic A (slow LLM), use browser back/forward to topic B before it returns.
- **Fix hint:** `key={row.topicId}` on `ReviewWorkspace` (or ReviewFlowProvider), which resets all state and drops late updates.
- **Status:** open
- **Verified:** read-only: ReviewWorkspace.tsx, TopicEditorPage.tsx, useReviewFlowState.ts, useReviewFlowActions.ts

### FEA-014 Review state re-init is keyed on topic text, not topicId (hypothesis)
- **Sev:** P2
- **Area:** frontend/src/features/review/context/useReviewFlowState.ts:376-397
- **Journeys:** J-063, J-064, J-091
- **Evidence:** `initKey = ${row.topic}:${screen}:${slot}:...`. Two rows with the same topic text (e.g. the draft copy made by `createDraftFromPublished`, or duplicate topics) produce the same key, so moving between their editor routes keeps the previous row in `state.sheetRow` while `TopicEditorPage` passes the new `row` to `onApprove`/`onPublishNow`. `handleSaveDraft` (line 739) writes `onSaveVariants(sheetRow, ...)`, i.e. to the previous row. Conversely, renaming the topic via Add-Topic resets the whole editor (including unsaved edits) because the key changes.
- **Repro:** Open published post P editor slot 0, then navigate to its copy's editor slot 0 via history: Save Draft writes into P.
- **Fix hint:** Include `row.topicId` in `initKey` (FEA-013's `key` also fixes this).
- **Status:** open
- **Verified:** read-only: useReviewFlowState.ts, useReviewFlowActions.ts 723-745

### FEA-015 `editorVariantIndex` (index in the filtered variants list) is used as a sheet column slot
- **Sev:** P2
- **Area:** frontend/src/features/review/context/useReviewFlowState.ts:241,264-268; frontend/src/features/review/context/useReviewFlowActions.ts:194-212,732-738; frontend/src/features/review/context/utils.ts:32-60
- **Journeys:** J-063, J-064
- **Evidence:** `buildSheetVariants` drops empty columns, and `editorVariantIndex` is set to the index into that filtered array (`slotIdx`, `applySheetVariantBase(variant, index)`), while `handleSaveDraft` treats it as the column number (`const slot = editorVariantIndex ?? 0`; lines 732-738). With a hole (e.g. variant 2 empty, V3 open => index 1) Save Draft writes V3's text into column 2, leaving V3 unchanged; when `editorVariantIndex` is null (selectedText was edited and matches no variant) it overwrites column 1 (variant 1) instead.
- **Repro:** Row with variant1, variant3 and variant4 filled; open `/editor/2`, edit, "Save draft": variant2 gets the text, variant3 unchanged.
- **Fix hint:** Store `variant.originalIndex` in state (or use `routed.editorVariantSlot`) and refuse to save when it is unknown.
- **Status:** open
- **Verified:** read-only: useReviewFlowState.ts 236-268, useReviewFlowActions.ts, utils.ts

### FEA-016 "Save" on an AI preview overwrites the matching sheet slot, and rapid saves clobber each other
- **Sev:** P2
- **Area:** frontend/src/features/review/context/useReviewFlowActions.ts:416-460; frontend/src/features/generation/GenerationPanel.tsx (Save button)
- **Journeys:** J-066, J-063
- **Evidence:** Saving preview N writes `variant.fullText` into column N, replacing the original generated variant N without a confirm. The merge array is built from `sheetRow.variant1..4` captured at click time (lines 429-434) and the whole four-column set is sent to `saveDraftVariants`; two quick saves (e.g. preview 1 then preview 2) each start from the same stale `sheetRow`, so the later response/request undoes the earlier slot. The call also fires an unauthenticated-looking `fetch(\`${VITE_WORKER_URL}/v1/variants/save\`)` that is a no-op (see FEA-027).
- **Repro:** Generate 4 variants, click Save on preview 1 and, before "Saved" appears, on preview 2; reload: only one slot holds the preview.
- **Fix hint:** Serialize saves (disable the other Save buttons while one is in flight, merge from the latest `sheetRow`) and confirm before overwriting an existing non-empty slot.
- **Status:** open
- **Verified:** read-only: useReviewFlowActions.ts, GenerationPanel.tsx

### FEA-017 Context-document upload control is wired to nothing in the editor
- **Sev:** P2
- **Area:** frontend/src/features/topic-navigation/screens/TopicEditorPage.tsx; frontend/src/features/topic-navigation/types.ts; frontend/src/features/review/context/useReviewFlowActions.ts:1038-1065; frontend/src/components/dashboard/index.tsx:415
- **Journeys:** J-070
- **Evidence:** The dashboard puts `onUploadContextDocument` into `topicReviewBase`, but `TopicReviewPagesBaseProps` does not declare it and `TopicEditorPage` never forwards it to `ReviewWorkspace`. In `uploadContextDocument`, `props.onUploadContextDocument?.(...)` is therefore undefined, `result` is undefined and the function returns without error (line 1051). The user picks a file, sees the spinner end, and no document appears; the generation request then lacks the context the user intended. (`onSaveGenerationLlm` is likewise never provided; its handler returns silently.)
- **Repro:** Editor > Refine panel > "Context documents" > upload a .txt: nothing is listed.
- **Fix hint:** Add the prop to `TopicReviewPagesBaseProps` and pass it through in `TopicEditorPage`; show an error when the handler is missing.
- **Status:** open
- **Verified:** read-only: TopicEditorPage.tsx, topic-navigation/types.ts, dashboard/index.tsx 380-430, useReviewFlowActions.ts

### FEA-018 Feed refresh replaces a multi-topic group's articles with only the first topic's results; cache is not invalidated on group edit
- **Sev:** P2
- **Area:** frontend/src/features/feed/FeedPage.tsx:235-250, 330-375, 530-560; frontend/src/stores/feedStore.ts
- **Journeys:** J-041, J-042, J-043
- **Evidence:** The initial load calls `getFeedArticles(group.topics)` (all topics), but `handleRefresh` and the stale background refresh call `refreshFeedArticles({ topic: group.topics[0] })` and then `setFeedArticles(fresh)`, so the user's feed shrinks to one topic after a refresh. The session cache check (`isSessionFetched && groupId === activeGroupId && !isStale`) is not invalidated by `handleUpdateGroup`, so editing a group's topics keeps serving the old article set for up to 23 h.
- **Repro:** Group with topics A,B: feed shows both; click refresh: only A's articles.
- **Fix hint:** Refresh per topic (or send all topics) and merge; call `feedStore.clear()` when a group is saved.
- **Status:** open
- **Verified:** read-only: FeedPage.tsx, feedStore.ts

### FEA-019 Feed load has no cancellation or error state; switching groups can show the previous group's articles
- **Sev:** P2
- **Area:** frontend/src/features/feed/FeedPage.tsx:328-378
- **Journeys:** J-041, J-042
- **Evidence:** The effect keyed on `activeGroupId` has no `cancelled` flag: a slow `getFeedArticles`/`refreshFeedArticles` for group A resolves after the user selected group B and calls `setFeedArticles(A's)`. Failures run `.catch(() => setFeedLoading(false))` and the background refresh `.catch(() => {})`, so an unreachable backend / provider-key error looks like an empty feed with no message.
- **Repro:** Throttle network, click group A then B quickly; or disable provider keys and open the feed: empty list, no error.
- **Fix hint:** Add a cancelled/request-id guard and an `error` state rendered in the list.
- **Status:** open
- **Verified:** read-only: FeedPage.tsx 300-380

### FEA-020 Article analysis can show another article's summary (late response overwrites)
- **Sev:** P2
- **Area:** frontend/src/features/feed/components/ArticleDetailView.tsx:150-176
- **Journeys:** J-046
- **Evidence:** `fetchAnalysis` has no abort/active flag; `useEffect([article.url])` fires a new request per article, and an earlier slow response calls `setAnalysis(oldArticleAnalysis)` after a newer article is open (DebateModeView does guard with `active`). The same applies to the connections effect (lines 184-202). Post angles for the wrong article can be copied into a draft.
- **Repro:** Open article A, immediately open article B with the keyboard shortcut; A's summary can replace B's.
- **Fix hint:** Use a cancelled flag keyed to `article.url` in both effects.
- **Status:** open
- **Verified:** read-only: ArticleDetailView.tsx

### FEA-021 "Opinion Leaders" shows LLM-generated named people as if real, without any AI disclaimer
- **Sev:** P2
- **Area:** frontend/src/features/feed/components/DraftContextView.tsx:531-545; frontend/src/features/feed/components/DebateModeView.tsx (has a disclaimer at its footer)
- **Journeys:** J-048, J-047
- **Evidence:** Leaders render `name · role` plus a perspective and a copyable post angle with no "AI-generated, may be fictional" note, unlike Debate Mode. Users may attribute positions to real people in a published post.
- **Repro:** Open a draft in the feed > Opinion Leaders tab.
- **Fix hint:** Add the same disclaimer (or label as "illustrative personas").
- **Status:** open
- **Verified:** read-only: DraftContextView.tsx, DebateModeView.tsx

### FEA-022 No request timeout or abort on any backend call, JSON or SSE
- **Sev:** P2
- **Area:** frontend/src/services/backendApi.ts:559-595 (post), 597-630 (postForBlob), 653-702 (streamGenerateQuickChange), 1399-1454 (streamCallGenerationWorker)
- **Journeys:** J-054, J-076, J-088, J-065, J-053, J-023
- **Evidence:** `fetch` is called without `AbortSignal`/timeout everywhere; stream readers have no idle timeout and are not cancelled when the component unmounts. A stalled worker leaves "Publishing…", "Generating…" and `actionLoading` stuck indefinitely (buttons stay disabled; `if (actionLoading !== null) return` in useDashboardQueue.ts:537/613 blocks every other publish) and users reload and retry, which can double publish if the first request actually completed. SSE parsing also drops a final event that lacks the trailing blank line (leftover `buffer` is never flushed).
- **Repro:** Point the worker at a hung generation worker; click Quick Change; observe an endless spinner, no cancel.
- **Fix hint:** Wrap with `AbortSignal.timeout` (e.g. 60 s JSON, 120 s idle for SSE), expose cancel, flush the trailing buffer.
- **Status:** open
- **Verified:** read-only: backendApi.ts 540-720, 1380-1475; useDashboardQueue.ts

### FEA-023 News-research selections keep feeding the prompt after the panel is closed or the topic changes
- **Sev:** P2
- **Area:** frontend/src/features/news-research/ResearcherPanel.tsx:87-120; frontend/src/features/review/context/useReviewFlowState.ts:407; frontend/src/features/review/context/useReviewFlowActions.ts:175; frontend/src/features/review-editor/components/EditorSidebar.tsx:584-600
- **Journeys:** J-052, J-065, J-066
- **Evidence:** Selected article refs live in `researchContextArticles` (provider state, never reset), while the panel's `results`/`selectedUrls` are local state that vanish when the sidebar tab switches (the panel unmounts). `buildGenerationRequest` keeps sending `researchArticles` for every Quick Change / 4 Variants with no indicator, and they persist when moving to another topic (FEA-013). Wrong sources can be woven into a post.
- **Repro:** Select 2 articles, switch to Styles tab, run Quick Change: request includes the articles; open another topic: still included.
- **Fix hint:** Reset `researchContextArticles` on topic change and show a "N sources attached" chip outside the News tab.
- **Status:** open
- **Verified:** read-only: ResearcherPanel.tsx, useReviewFlowState.ts, useReviewFlowActions.ts, EditorSidebar.tsx

### FEA-024 Queue refresh after publish can fail silently and in-flight loads are not ordered
- **Sev:** P2
- **Area:** frontend/src/components/dashboard/hooks/useDashboardQueue.ts:106-125, 572-587, 716-731
- **Journeys:** J-089, J-088, J-091, J-040
- **Evidence:** After a successful `publishContent` the code calls `await loadData(true)`; with `quiet` set a failed `getRows` is swallowed, leaving the row displayed as Approved/unpublished while the post is live, which invites a second publish (the "Republish" path asks for confirmation, but "Publish" in the queue does not). `loadData` has no sequence guard, so an older slow `getRows` (e.g. the effect-triggered load) can overwrite the rows just refreshed after an action. If `updateRowStatus`/`getRows` fail after the post is live (J-089), the user only sees a generic "Failed to send" notice.
- **Repro:** (static reasoning) Make `getRows` fail once after a successful publish; the row stays Approved.
- **Fix hint:** On refresh failure after a send, mark the row published locally and show a "published, refresh failed" notice; add a request counter to `loadData`.
- **Status:** open
- **Verified:** read-only: useDashboardQueue.ts

### FEA-025 No client-side channel length/format limits before Approve/Publish (hypothesis)
- **Sev:** P2
- **Area:** frontend/src/features/review/context/useReviewFlowActions.ts:624-721; frontend/src/components/dashboard/hooks/useDashboardQueue.ts:474-534
- **Journeys:** J-076, J-077, J-080, J-078
- **Evidence:** Only an empty-text check exists (`describePublishPrerequisiteFailure`); a grep for character limits (3000/2200/4096) in review, editor and channel preview code finds none. The row is first set to Approved, then `publishContent` is attempted, so a long post produces a provider error after the status change (unless the worker validates; not checked here).
- **Repro:** Paste >3000 characters, click Publish to LinkedIn.
- **Fix hint:** Show a counter and block Approve/Publish above the channel limit.
- **Status:** open
- **Verified:** read-only: useReviewFlowActions.ts, useDashboardQueue.ts, grep over review/editor/channel-previews

### FEA-026 AI generation handlers rethrow into un-awaited click handlers (unhandled promise rejections)
- **Sev:** P3
- **Area:** frontend/src/features/review/context/useReviewFlowActions.ts:229-274; frontend/src/features/generation/GenerationPanel.tsx (onClick={onGenerateVariants}); frontend/src/features/review-editor/screens/EditorScreen.tsx:~92 (runManualContentReview); frontend/src/features/news-research/ResearcherPanel.tsx:144-170
- **Journeys:** J-065, J-066, J-069, J-052
- **Evidence:** `handleGenerateQuickChange`/`handleGenerateVariants` use `try/finally` only; the dashboard wrapper shows a notice then rethrows (`useDashboardQueue.ts:293-297,303-305`), so each failure also surfaces as an unhandled rejection. Same for `runManualContentReview` (`void` without catch, and an `onAfterContentReview` failure hides the successful report), `handleToggleHistory` and `handleLoadSnapshot`.
- **Repro:** Break the LLM key and click Quick Change: console shows an unhandled rejection in addition to the notice.
- **Fix hint:** Catch at the call site (the wrapper already notified the user).
- **Status:** open
- **Verified:** read-only: files above

### FEA-027 Dead variant-KV code paths read `globalThis.VITE_WORKER_URL` and `window.__idToken`, which are never set
- **Sev:** P3
- **Area:** frontend/src/services/backendApi.ts:708-815, 827-890; frontend/src/features/review/context/useReviewFlowActions.ts:439-454
- **Journeys:** J-044, J-066
- **Evidence:** `saveVariantsToCloudflareKv`, `getSavedVariantsFromCloudflareKv`, `_kvFetch` (clips KV) and the fire-and-forget fetch in `handleSavePreviewVariantAtIndex` build the URL from `globalThis.VITE_WORKER_URL` (Vite exposes `import.meta.env`, so it is undefined) and `window.__idToken` (no assignment anywhere), and target `/v1/variants/save`, `/v1/clips` which the main worker does not route. They either throw "Missing VITE_WORKER_URL" or silently skip. `features/feed/README.md` still claims a KV clip sync that does not run.
- **Repro:** grep `__idToken` / `globalThis).VITE_WORKER_URL`; no setter exists.
- **Fix hint:** Delete the dead calls and the README claim.
- **Status:** open
- **Verified:** read-only: backendApi.ts, useReviewFlowActions.ts, grep over frontend/src and worker/src for `variants/save`

### FEA-028 Optimistic UI is not rolled back on failure (feedback votes, persona delete, workflows)
- **Sev:** P3
- **Area:** frontend/src/features/feed/FeedPage.tsx:260-278; frontend/src/features/add-topic/AddTopicPage.tsx:484-505; frontend/src/features/workflows/useCustomWorkflows.ts:44-76
- **Journeys:** J-049, J-035, J-061
- **Evidence:** `handleThumbsUp/Down` apply the vote locally and ignore a failing `setArticleFeedback` (comment says revert but none exists). Persona delete swallows errors although the comment says the user sees them. `useCustomWorkflows` list failure becomes an empty list and `remove` returns false with no message, so a failed load can make the user re-create a workflow that exists.
- **Repro:** Fail the call and click thumbs up: stays highlighted.
- **Fix hint:** Revert state and show a toast in each catch.
- **Status:** open
- **Verified:** read-only: files above

### FEA-029 "Generate and save workflow" may never save because the card is returned from a setState updater (hypothesis)
- **Sev:** P3
- **Area:** frontend/src/features/review/context/useReviewFlowActions.ts:344-357; frontend/src/features/review-editor/components/EditorSidebar.tsx:221-246
- **Journeys:** J-061
- **Evidence:** `newCard` is assigned inside the `setGeneratedCards` updater function and returned right after; React may run the updater lazily during render, so `handleGenerateFromStyle` can return `null` and `handleGenerateAndSave` exits at `if (!card ...) return`. Also, `handleGenerateAndSave` has no catch, so a failure during generation rejects unhandled, and the generation overwrites the editor text without a prompt (recoverable only through the Version tab).
- **Repro:** Styles tab > pick a card > "Generate and save"; check whether a custom workflow appears.
- **Fix hint:** Build the card object before calling `setGeneratedCards` and return it.
- **Status:** open
- **Verified:** read-only: useReviewFlowActions.ts 279-361, EditorSidebar.tsx 215-246

### FEA-030 Footer "Publish to <channel>" really schedules when the time input is in the future, and defaults to the editor-open time
- **Sev:** P3
- **Area:** frontend/src/features/review-editor/screens/EditorScreen.tsx:~370-460; frontend/src/features/review/context/useReviewFlowState.ts:92-104
- **Journeys:** J-082, J-085, J-076
- **Evidence:** The Schedule input is initialised to the mount time (or the stored postTime) and is always sent; the button label is always "Publish to X" and the result is only distinguishable by the post-hoc "Scheduled" alert. A user who approved with a future time yesterday and clicks Publish today (time still future) schedules instead of sending, and a stale default (opened 30 min ago) is "in the past" by the time of the click.
- **Repro:** Approve with a future time, reopen the editor, click Publish.
- **Fix hint:** Relabel to "Schedule for <time>" when the time is in the future and warn when it is in the past.
- **Status:** open
- **Verified:** read-only: EditorScreen.tsx, useReviewFlowState.ts, useDashboardQueue.ts

### FEA-031 Feed draft-context text shadows the real draft via a localStorage copy
- **Sev:** P3
- **Area:** frontend/src/features/feed/components/DraftContextView.tsx:66-85
- **Journeys:** J-045
- **Evidence:** The initial text is `localStorage[feed_draft_<topicId>]` if present, else the row text, and is autosaved on each change; it is never written back to the sheet. After the post is edited or regenerated elsewhere, the feed view keeps showing, clustering and analysing the old local copy.
- **Repro:** Open a draft in feed, change text, edit the post in the editor, reopen in feed: old text.
- **Fix hint:** Prefer the row text unless the local copy is newer, or drop the shadow copy.
- **Status:** open
- **Verified:** read-only: DraftContextView.tsx
