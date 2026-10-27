# Existing-review reconciliation (read-only, code as of branch `launch-readiness-review`)

Method: grep + reading of named files only. No tests/builds run. Paths below are relative to `frontend/src/` unless prefixed.
Status key: fixed / partial / open / n-a / unverified. `cons/audits/*` items are 1:1 subsets of the surface files `cons/02..13`; they are reconciled once under the surface ID and not repeated. Phase-3 ("strategic") items in cons that are clearly future-phase (ML personalisation, fine-tuning, A/B, SSO-style tenancy, collab editing) are grouped as n-a at the end of section 1 and not itemised.

Headline: `cons/` checkboxes are almost all unticked, but much of Phase 1 has actually landed (feed card, ClipsDock, status pill, publish-confirm in queue, newsletter preview, setup wizard, settings nav, global shortcuts). The Phase-2 structural work (settings page, sidebar IA, schedule unification in editor, multi-channel, error primitives adoption) has NOT landed.

## 1. cons/ (surface cut; audits mapped inline)

| Src ID | Item (short) | Orig sev | Status | Evidence | Notes |
|---|---|---|---|---|---|
| C01-1 | Sidebar grouped under Plan/Make/Ship/Configure/Admin | HIGH | open | components/workspace/AppSidebar.tsx (flat `link()` list, admin gating inline ~L269) | no group headers |
| C01-2 | Breadcrumb in WorkspaceHeader | HIGH | partial | components/workspace/WorkspaceHeader.tsx:47; WorkspaceChromeContext.tsx:19 | only on topic-review routes via headerOverride, not derived from location |
| C01-3 | `?` help button / workflows modal | MED | partial | App.tsx:125-134, components/HelpOverlay.tsx:4-9 | `?` key opens shortcuts overlay; no visible header button, no workflows content |
| C01-4 | Sidebar search | MED | open | AppSidebar.tsx | none |
| C01-5 | useRouteContext hook | MED | open | grep: no hit | |
| C01-6 | RecentlyViewed topics | MED | open | grep: no hit | |
| C01-7 | Mobile sidebar scrim-tap Drawer | MED | unverified | AppSidebar.tsx `mobileOpen` props | not inspected |
| C01-8 | Deep-link hard-refresh audit | HIGH | unverified | App.tsx:262 stored-path restore | mechanism exists (post-auth return path); no audit seen |
| C01-9 | Global command palette (cmd+k) | MED | open | grep CommandPalette: none | Cmd-K only focuses settings nav search (DashboardSettingsDrawer.tsx:1225) |
| C01-10 | RouteGuard role wrapper | MED | open | grep: none | admin gating still inline |
| C02-1 | Feed: persistent 👍👎✂ (not hover) | HIGH | open | features/feed/components/FeedArticleCard.tsx:~97 (`opacity-0 group-hover:opacity-100 pointer-events-none`) | touch users cannot vote/clip from stream; 26px targets (<40px AC) |
| C02-2 | Favicon next to source | HIGH | fixed | FeedArticleCard.tsx:76-83 | |
| C02-3 | Thumbnail 96px aspect-[4/3] | HIGH | open | FeedArticleCard.tsx (no img at all) | cards are text-only |
| C02-4 | 2-line summary default | HIGH | fixed | FeedArticleCard.tsx:~69 `line-clamp-2` + content fallback | |
| C02-5 | Search input in feed (+desc toggle) | MED/HIGH | partial | FeedPage.tsx:109-111, 536-575 (debounced client filter on loaded items) | no "search description" toggle |
| C02-6 | Source brand colour badge | MED | partial | FeedArticleCard.tsx:6-10,86 hash-colour square | |
| C02-7 | j/k/o/c keyboard nav | MED | fixed | features/feed/hooks/useFeedKeyboard.ts:38; FeedPage.tsx:586-596 | |
| C02-8 | Batch 20 + append skeleton | MED | partial | FeedLeftPanel.tsx:39 BATCH_SIZE=20; :28,:116 skeletons | skeleton only on initial load; "Load more" fallback exists :206 |
| C02-9 | Filter bar Latest/Trending/For You | HIGH | partial | FeedPage.tsx:56,522-534,1063 | "For You" = hide downvoted only (:530); no per-topic pill beyond interest groups |
| C02-10 | Two-panel layout, trending rail top carousel <lg | HIGH | open | FeedPage.tsx:1340 `hidden lg:flex`, no carousel | rail simply disappears on tablet/phone |
| C02-11 | 2-col masonry | HIGH | open | FeedLeftPanel.tsx (single column) | |
| C02-12 | Detail as side-sheet not full-screen | MED | fixed | FeedPage.tsx:1375-1405 (480px sheet, `asSheet`) | overlay darkens feed (modal) |
| C02-13 | Evergreen sort uses real signal | MED | open | FeedCuratedPanel.tsx:89-92,152-154 (description length) | Top10 also uses desc length + recency |
| C02-14 | Source dedupe grouping | MED | open | FeedLeftPanel.tsx | none |
| C02-15 | Curated panel compact + trending-word chips | MED | partial | FeedCuratedPanel.tsx:279-285 | words/topics clickable (FeedPage.tsx:1363-1364) |
| C02-16 | SaveForLater | MED | open | FeedArticleCard.tsx:~131 Bookmark button only calls stopPropagation | **no-op button shipped** (see NEW-1) |
| C02-17 | Compose post from article CTA on card | MED | open | FeedArticleCard.tsx | |
| C02-18 | Per-source mute/boost | MED | open | | |
| C03-1 | ClipsDock visible trash (not right-click) | HIGH | partial | features/feed/components/ClipsDock.tsx:206 onContextMenu confirm; hover-only Edit/Delete :~236 | delete still via right-click or hover buttons |
| C03-2 | Drop-zone affordance + toast | HIGH | partial | ClipsDock.tsx:332-367 (dragOver highlight "Drop to assign") | no success toast on drop |
| C03-3 | "Compose post from clips" CTA | HIGH | fixed | ClipsDock.tsx:133-145 | |
| C03-4 | Floating pill dock, count badge | HIGH | partial | ClipsDock.tsx:158 (magnifying vertical strip + expand panel) | still always-on right strip |
| C03-5 | Bulk select clips | MED | open | ClipsDock.tsx | |
| C03-6 | Per-clip "Add to topic" menu (touch) | HIGH/MED | open | ClipsDock.tsx (drag-drop only) | touch users cannot assign |
| C03-7 | Passage clipping from stream (SelectionClipper in card) | HIGH | open | grep: SelectionClipper only used in ArticleDetailView.tsx:11,150 | cons doc says toast was added; toast exists (SelectionClipper.tsx:19-23) but card wiring absent |
| C03-8 | Detail: Read-full primary, lightbox, details wrapper, opinion textarea | MED | partial | ArticleDetailView.tsx:397,404 `<details>`; no lightbox grep hit | |
| C03-9 | Single scrollable stack vs tabs | MED | open | ArticleDetailView.tsx:134,472-557 (Opinion/Perspectives/Connection/Debate tabs) | |
| C03-10 | clipGroupId / groups | MED | open | grep: none | |
| C03-11 | Cached AI analysis on worker | HIGH | unverified | worker index.ts:1919 `analyzeFeedArticle` | cache not checked |
| C04-1 | Queue row primary CTA always visible | HIGH | fixed | components/dashboard/tabs/DashboardQueue.tsx:~852,896,925 | only delete column is dimmed (`opacity-40`, :942) |
| C04-2 | Per-row channel pill | HIGH | open | DashboardQueue.tsx (only StatusPill at :768; CHANNEL_OPTIONS used only in bulk/confirm :1017,1274) | **onboarding Tour copy at :435 claims "channel pill shows where a post will publish" - it does not** |
| C04-3 | Unified status pill | HIGH | fixed | components/ui/StatusPill.tsx; DashboardQueue.tsx:20,768 | adoption elsewhere (calendar, newsletter) unchecked |
| C04-4 | Empty state starter templates + tour | HIGH | fixed | DashboardQueue.tsx:431-435,585-588 | |
| C04-5 | AddTopic save toast / "Saved Ns ago" | HIGH | open | features/add-topic/AddTopicPage.tsx:296 `onSaved` only; no toast system exists in app | |
| C04-6 | Required-field asterisk + error summary | MED | partial | AddTopicPage.tsx:275 inline title error | no asterisk on title |
| C04-7 | Persona delete visible + confirm | MED | unverified | AddTopicPage.tsx:~660-691 | |
| C04-8 | Generate-with-AI determinate progress | MED | open | AddTopicPage.tsx | |
| C04-9 | Topic Duplicate action | MED | open | grep: none in AddTopicPage | |
| C04-10 | Merge Trending+Research tab, rename Analysis | MED | open | add-topic/TopicRightPanel.tsx:52-54 | still Trending/Research/Analysis |
| C04-11 | MicButton 3 states | LOW | partial | add-topic/MicButton.tsx:23,34,43 (spinner + stop label) | no pulsing recording dot verified |
| C04-12 | AI-Draft modal not nested in drawer | HIGH | fixed | DashboardQueue.tsx:161,187-220 (dialog owned by queue) | TopicDetailPanel is a separate overlay (:55) |
| C04-13 | Deterministic drop-menu in AddTopic | HIGH | unverified | | |
| C04-14 | useTopicDraft localStorage hook | MED | open | grep: none | |
| C04-15 | List filters (status/channel/needs-action/sort) | MED | unverified | DashboardQueue.tsx | not inspected |
| C04-16 | Bulk select + bulk delete/reschedule/channel | MED | partial | DashboardQueue.tsx:146-149,755-760 (checkbox, bulk channel/schedule dialogs) | |
| C04-17 | Republish tooltip; no withdraw | MED | partial | DashboardQueue.tsx:925 title="Republish to channel" | tooltip does not say "creates new draft"; no withdraw |
| C04-18 | "Drafting..." describes what is happening | MED | unverified | | |
| C05-1 | datetime-local in EditorScreen -> ScheduleEditor | HIGH | open | features/review-editor/screens/EditorScreen.tsx:310 | editor still has bare input |
| C05-2 | TopicDetailPanel uses ScheduleEditor | HIGH | fixed | components/dashboard/components/TopicDetailPanel.tsx:369 | |
| C05-3 | Calendar uses ScheduleEditor | HIGH | fixed | content-schedule-calendar/ContentScheduleCalendar.tsx:367 | so 2 of 3 entry points unified; editor remains |
| C05-4 | Timezone caption | MED | open | components/schedule/ScheduleEditor.tsx (no tz hit) | editor posts UTC string (useReviewFlowActions.ts:690-697) |
| C05-5 | Mobile sticky footer in editor | MED | unverified | EditorScreen.tsx | |
| C05-6 | Drag-confirm "these items will move" list | MED | unverified | content-schedule-calendar/EventDetailAndEdit.tsx | |
| C05-7 | ScheduledPublishBanner abs+relative time, destructive Cancel | MED | partial | scheduled-publish/ScheduledPublishBanner.tsx:42-44 ("Cancel schedule") | no countdown |
| C05-8 | Recipient-missing warning in editor footer | MED | unverified | | |
| C05-9 | Single `ChannelPicker` component | HIGH | fixed | components/channels (imported DashboardDelivery.tsx:7, TopicsRightRail.tsx:6,258,390) | bulk modal still separate (DashboardQueue.tsx:1017) |
| C05-10 | deliveryChannels[] multi-channel | HIGH | open | grep: none | single channel only |
| C05-11 | Connection Health panel / Test connection | MED | open | grep ConnectionHealth/testConnection: none | |
| C05-12 | Calendar pending-publish state | MED | unverified | | |
| C05-13 | Recurrence/rrule, per-channel timing | HIGH | n-a | future phase | |
| C06-1 | EditorSidebar 8 tabs -> 3 groups | HIGH | partial | features/review-editor/components/EditorSidebar.tsx:91-98 | now 5 base tabs (+Email) not 3 groups |
| C06-2 | Dimension slider `?` tooltips | HIGH | open | EditorSidebar.tsx:25-35,360-400 (only label + level pill) | |
| C06-3 | Three discard dialogs differentiated | HIGH | open | features/review/components/ReviewDialogs.tsx:60,95,110 all "Discard current editor changes?" | |
| C06-4 | Passive autosave restore | HIGH | fixed | ReviewDialogs.tsx:43 "Restore previous draft?"; useReviewFlowState.ts:645 autoSaveTrigger | |
| C06-5 | beforeunload in editor | HIGH | open | grep beforeunload: only DashboardSettingsDrawer.tsx:1242 | leaving editor with unsaved edits is unguarded at browser level |
| C06-6 | Variant badge font + tooltip | MED | unverified | variant/components/VariantCarousel.tsx | |
| C06-7 | ResizeHandle a11y | MED | unverified | EditorScreen.tsx:24-29 | |
| C06-8 | Flip split to editor 60-65% | HIGH | open | EditorScreen.tsx:234,244 (sidebar 58%, editor 42%) | |
| C06-9 | Versions as toolbar drawer | MED | open | review-editor/components/VersionHistoryStrip.tsx | |
| C06-10 | Variant compare 2-up | MED | partial | ReviewDialogs.tsx:133 compare preview | |
| C06-11 | Edit-selection vs whole toggle | MED | partial | editor/DraftEditor scope toolbar (USE-CASES step 6) | not verified |
| C07-1 | Confirm modal before publish (rendered preview+channel+time) | HIGH | partial | DashboardQueue.tsx:163,852,896,1274 (queue has publishConfirmRow) | **editor footer "Publish to X" calls handlePublishNow directly** (EditorScreen.tsx:~393; useReviewFlowActions.ts:~700) - no confirm |
| C07-2 | Success toast with "View on channel" permalink | HIGH | open | useDashboardQueue.ts:587 modal `showAlert 'Success'`; grep permalink: none for publish | USE-CASES claims link; not present |
| C07-3 | Scheduled state copy + "Send now anyway" | HIGH | open | EditorScreen.tsx:~397 (button just disabled with tooltip) | |
| C07-4 | Footer regroup Save/Schedule/Send | HIGH | open | EditorScreen.tsx:340-430 (Approve, Save edits, Publish, Save draft all present) | |
| C07-5 | Live countdown on banner | MED | open | ScheduledPublishBanner.tsx | |
| C07-6 | Merge Approve+Publish semantics | HIGH | open | EditorScreen.tsx:357,382 handleApprove still in footer | |
| C07-7 | Undo send window | HIGH | open | grep revoke/undo send: none | |
| C07-8 | Multi-channel chips | MED | open | depends C05-10 | |
| C08-1 | Newsletter live preview (desktop/mobile) | HIGH | fixed | campaign/components/newsletter/NewsletterConfigDrawer.tsx:44-51,97-101,192-200 | `[x]` in doc is correct |
| C08-2 | Inline validation (name/subject/emails) | HIGH | partial | NewsletterConfigDrawer.tsx:125-137 | no char counts verified |
| C08-3 | Approve/Send always visible | HIGH | unverified | NewsletterListView.tsx / NewsletterCard.tsx | doc ticks it [x]; not confirmed in code |
| C08-4 | Mini-calendar >=220px | HIGH | unverified | NewsletterCalendarView.tsx | doc ticks [x]; not confirmed |
| C08-5 | Voice&Topics collapsed summary chip | MED | open | NewsletterConfigDrawer.tsx (no "Tone:" hit) | |
| C08-6 | Send test to me | MED | fixed | NewsletterConfigDrawer.tsx:187,304-308 | |
| C08-7 | Subject `{{variable}}` autocomplete / end-to-end vars | MED | open | grep {{subscriber: none | doc itself leaves "[ ] Subject template variables work end-to-end" |
| C08-8 | Full-page editor vs drawer | HIGH | open | still drawer | |
| C08-9 | Dedicated issue view | HIGH | partial | newsletter/IssueDetailDrawer.tsx, NewsletterIssuePanel.tsx exist | still drawer-based |
| C08-10 | CodeMirror for HTML | MED | open | grep: none | |
| C08-11 | Status badge redesign | MED | unverified | | |
| C08-12 | Subject A/B, analytics, segmentation | HIGH | n-a | future phase | |
| C09-1 | Settings -> `/settings` page w/ left nav | HIGH | partial | DashboardSettingsDrawer.tsx (2251 lines; left nav + grouped list ~L1285-1390; `/settings` route exists) | still a monolith component; not split per section |
| C09-2 | URL subpaths `/settings/llm` | HIGH | open | grep: none | |
| C09-3 | Cmd-K settings search | HIGH | fixed | DashboardSettingsDrawer.tsx:1225-1228,1305 | scoped to settings only |
| C09-4 | Unsaved-changes guard | HIGH | partial | DashboardSettingsDrawer.tsx:1235-1244 beforeunload; :1247-1256 saved toast | no in-app route-change guard; save only for admin (:1282) |
| C09-5 | Section one-line descriptions | HIGH | open | SettingsSectionCard titles only (e.g. :1417,1441) | descriptions exist for a few model lists only |
| C09-6 | Test connection per credential | HIGH | open | grep: none (frontend/worker) | highest support-cost item |
| C09-7 | Enrichment skill tooltips | HIGH | partial | DashboardSettingsDrawer.tsx:481-492 shows meta.description | |
| C09-8 | Sticky ToC | HIGH | fixed | DashboardSettingsDrawer.tsx ~L1317-1390 | |
| C09-9 | Setup wizard progress "Step N of M" | HIGH | fixed | features/setup-wizard/SetupWizard.tsx:91-105 | |
| C09-10 | Wizard label rename | HIGH | fixed | SetupWizard.tsx:77-89 ("Trending Sources","Image Generation","Voice Transcription") | |
| C09-11 | Wizard Back buttons | HIGH | fixed | SetupWizard.tsx:538-636; EnvVarsStep.tsx:438 | |
| C09-12 | EnvVars grouped w/ docs links | HIGH | fixed | EnvVarsStep.tsx:456-532 (groups + links) | example values not verified |
| C09-13 | Save diff toast, inline validators (Telegram ID etc.) | MED | open | useDashboardSettings.ts; no regex hits | |
| C09-14 | ChannelSettingsCard extraction | MED | open | grep: none | 6 channel sections still copy/paste |
| C09-15 | Connection health page | MED | open | pages/connections exists (OAuth cards) but no last-error/retry | |
| C09-16 | Deployment-mode card comparison | MED | unverified | SetupWizard.tsx:28,64 | |
| C09-17 | Copy install logs button | LOW | open | | |
| C10-1 | Progress to non-admins in editor | HIGH | fixed | EditorSidebar.tsx:417; GenerationPanel.tsx:312 (EnrichmentProgressPanel) | |
| C10-2 | Node-failure warning toast + re-run | HIGH | open | EnrichmentProgressPanel.tsx (no failed/rerun hits) | |
| C10-3 | nodeProgressLabels full coverage | HIGH | unverified | features/generation/nodeProgressLabels.ts | |
| C10-4 | DAG page for standard users | HIGH | open | AppSidebar.tsx:269 admin-only | |
| C10-5 | Re-run from node / edit-prompt deep link | HIGH | open | pages/EnrichmentFlowPage.tsx | |
| C10-6 | Last-3 runs expanded, filters, metrics | MED | open | EnrichmentFlowPage.tsx | |
| C10-7 | Persist generationProgress | MED | unverified | | |
| C11-1 | Log variant pick signal | HIGH | open | worker index.ts: no pick-logging case | |
| C11-2 | Feed 👍/👎 persisted | HIGH | fixed | worker index.ts:1812 `setArticleFeedback`, :1823 get; FeedPage.tsx:1280 | |
| C11-3 | Post-publish "was this good?" rating | HIGH | open | grep: none | |
| C11-4 | Pre-apply diff in GenerationPanel | HIGH | partial | ReviewDialogs.tsx:133 compare preview exists for editor scope | GenerationPanel diff not verified |
| C12-1 | Admin: replace `prompt()` budget edit | HIGH | open | features/saas/AdminPanel.tsx:79 | native prompt; silently returns on invalid input |
| C12-2 | Admin: Deny waitlist | HIGH | open | AdminPanel.tsx:172-... only Approve (:69); no deny endpoint in worker/service | |
| C12-3 | Admin: search/sort/batch/audit/CSV | HIGH/MED | open | AdminPanel.tsx (278 lines, none) | |
| C13-1 | Strip backend URL / technical hints from user errors | HIGH | open | services/backendApi.ts:485-525 (shows CORS_ALLOWED_ORIGINS, workers.dev, endpoint) | leaks infra detail to end users |
| C13-2 | OfflineBanner | HIGH | open | grep online/offline: none | |
| C13-3 | ErrorBanner/EmptyState/LoadingSkeleton primitives adopted | HIGH | partial | components/ui/ErrorBanner.tsx, EmptyState.tsx, LoadingSkeleton.tsx exist; **zero imports elsewhere** | dead code |
| C13-4 | Retry action on failures (useAlert) | HIGH | open | components/useAlert.ts / AlertProvider.tsx (modal alert, no actions) | |
| C13-5 | 401/429/5xx copy map; Retry-After backoff | HIGH | open | services/backendApi.ts: no backoff/Retry-After | |
| C13-6 | zod validation | HIGH | open | grep `from 'zod'` in frontend: none | |
| C13-7 | Mobile parity (rail, drawer, bulk table scroll) | HIGH | partial | CampaignPage.tsx:852 overflow-x-auto; feed rail hidden (C02-10); settings drawer not verified | |
| C13-8 | A11y labels / focus rings | MED | partial | ~175 aria-label occurrences; feed toolbar buttons labelled | no audit evidence |
| C13-9 | Global shortcuts g+t/g+f/? | MED | fixed | App.tsx:126; components/HelpOverlay.tsx:4-9; hooks/useGlobalShortcuts.ts | |
| C13-10 | Telemetry / report-issue / self-healing | MED | n-a | future phase | |
| C13-11 | First-visit tours | LOW | partial | components/Tour.tsx used in DashboardQueue.tsx:431; feed tour FeedPage.tsx:622 | newsletter tour at NewsletterTab.tsx:229 |
| C05b | Bulk campaign: 3-mode import, file upload | HIGH | fixed | campaign/CampaignPage.tsx:70,591-603 (Prompt/File/Paste) | audits/05 |
| C05c | Bulk: inline column schedule/channel (not modals) | HIGH | open | CampaignPage.tsx:305-308,379-420 dialogs | audits/05 |
| C05d | Bulk: draft persistence, undo delete | MED | fixed | CampaignPage.tsx:247-251 localStorage; :469 undo text | audits/05 |
| C05e | Bulk: template gallery, JSON diff panel | MED | open | | audits/05 |
| C-F | Phase-3 strategic (personalisation model, closed-loop tuning, A/B recipe, cost dashboard, recurrence, collab) | HIGH/MED | n-a | | future phase, not itemised |

## 2. USE-CASES.md WIRING STATUS

| Src ID | Item (short) | Orig tag | Status | Evidence | Notes |
|---|---|---|---|---|---|
| U-052/041 | WhatsApp card on /connections | ✅ | fixed | pages/connections/ConnectionsPage.tsx:22,60 | |
| U-053 | Telegram verification on /connections | ✅ | fixed | ConnectionsPage.tsx:7,15,23 `verifyTelegramChat` | worker index.ts:2388 |
| U-057/060 | listRules/lookupEffectiveRule use checkedFetch | ✅ | fixed | features/automations/api.ts:16,30,67 | |
| U-062 | YouTube: no webhook form | ✅ | fixed | features/automations/AutomationsTab.tsx:120 | |
| U-J1.1 | 401 -> token cleared, redirect to sign-in | ✅ | unverified | services/backendApi.ts (no `401` literal hit; AUTH_ERROR_PATTERN / isAuthErrorMessage :~523, App.tsx onAuthExpired) | message-pattern based, not status based |
| U-J1.2 | Rows from D1 if Sheets fails, no UI error | ✅ | unverified | not traced into worker | |
| U-J1.3 | Fresh account -> onboarding wizard | ✅ | unverified | features/onboarding | |
| U-J1.4 | AddTopic "7 fields", redirect to `/dashboard` | ✅ | unverified | AddTopicPage.tsx:296 navigate | route `/dashboard` not confirmed |
| U-J1.5 | analyzeTopicInsights | ✅ | fixed | worker index.ts:1878; backendApi.ts:1077 | |
| U-J1.6 | Generate -> GenWorkerDraftField dialog, SSE stream | ✅ | partial | DashboardQueue.tsx:161,212-220 | dialog exists; "Save & Continue saveDraftVariants" not traced |
| U-J1.7 | Editor "3-panel layout" w/ tabs Refine/Media/Topic-Rules/Email | ✅ | partial | EditorScreen.tsx:227-250 (2 panels); EditorSidebar.tsx:91-98 tabs = Writing Styles/Refine/News/Media/Topic Rules(+Email) | doc stale |
| U-J1.8 | generateQuickChange | ✅ | fixed | worker index.ts:1572; backendApi.ts:649 | |
| U-J1.9 | Footer button "Publish Now" | ✅ | partial | EditorScreen.tsx:~393 label is `Publish to <channel>` | |
| U-J1.10 | Success alert w/ "View on LinkedIn" link | ✅ | unverified | useDashboardQueue.ts:587 shows generic 'Success' alert; no permalink/“View on” anywhere in frontend or worker | **likely false claim** |
| U-J2-5 | Instagram/Gmail/Telegram/WhatsApp channel flows | ✅ | unverified | not traced end-to-end; Gmail email fields in EditorSidebar (Email tab) | |
| U-J6 | All channels configurable from /connections | ✅ | partial | ConnectionsPage.tsx; Telegram/WhatsApp *recipient* config still in Settings drawer (DashboardSettingsDrawer.tsx:1788,1939) | |
| U-J7 | Scheduled publishing + cancel (Durable Object) | ✅ | unverified | scheduled-publish/ScheduledPublishBanner.tsx:42 cancel UI; worker/src/scheduled-publish present | alarms not traced |
| U-J8 | Bulk campaign "upload CSV -> append Sheet rows" | ✅ | partial | CampaignPage.tsx:597 accepts .json/.jsonc/.csv | doc oversimplified |
| U-J10 | Automations rules admin-only | ✅ | unverified | | |
| U-J11 | Trending: "fallback to mock data" | ✅ | partial | features/trending/hooks/useTrending.ts:280-292 mock-loading timer when `!useRealApis` | mock fallback is real code - confirm it cannot reach prod users |
| U-J12 | 6 enrichment actions in worker | ✅ | fixed | worker index.ts:1919,2024,2070,2118,2159,2201 | all present, all have backendApi methods (:1086,1726-1745) |
| U-J12b | Debate/cluster "in editor" | ✅ | partial | consumers are feed/DraftContextView.tsx:111,143,159, ArticleDetailView.tsx:189 | lives in Feed, not editor sidebar |
| U-E2E | E2E matrix items all unchecked; "100% wired" claim | - | open | tests/e2e/*.spec.ts exist (editor, scheduling, connections, ...) | doc not updated; journeys not run by this review |

## 3. FEED_EXPLORATION_REPORT.md / MCP-PROGRESS.md

| Src ID | Item (short) | Orig tag | Status | Evidence | Notes |
|---|---|---|---|---|---|
| F-1 | Report is a descriptive snapshot (no open items); stale numbers (FeedPage 639 lines, BATCH 10, 5 platform panels, absolute paths under /Users/pratyushmishra) | - | n-a | FeedPage.tsx now 1490 lines; FeedLeftPanel BATCH_SIZE=20 | do not use as source of truth |
| F-2 | Report: right-click delete only; sidebar hidden <lg; hover-only clip | info | open | ClipsDock.tsx:206; FeedPage.tsx:1340; FeedArticleCard.tsx | same as C02/C03 |
| M-1 | MCP-PROGRESS: 24/24 items `[x]` (python setup files); nothing pending | - | n-a | MCP-PROGRESS.md | nothing to reconcile; not product-user-facing |

## 4. docs/superpowers plans

| Src ID | Item (short) | Orig tag | Status | Evidence | Notes |
|---|---|---|---|---|---|
| P1-T1 | AppSidebar active-state / automations nav fix | [ ] | fixed | AppSidebar.tsx:116-148 (`PAGE_TO_PATH` incl. automations; `useEnd` only topics) | checkboxes never ticked; code landed |
| P1-T2 | TrendingSidebar refresh button + refetch, remove AddTopic debounce | [ ] | fixed | add-topic/TrendingSidebar.tsx:8-31; TopicRightPanel.tsx:87,96; useTrending.ts:295-300 | |
| P1-T3 | ContentReview provider revert guard | [ ] | fixed | features/content-review/ContentReviewSettings.tsx:58-62 (empty-catalog guard); services/configService.ts:293-308 normalize | |
| P1-T4 | TopicsRightRail provider/model validation | [ ] | fixed | components/dashboard/components/TopicsRightRail.tsx:111-125 | |
| P2-T1..3 | Feed L/M/Q/R types, 4 worker cases, 4 API methods | [ ] | fixed | worker index.ts:2070,2118,2159,2201; backendApi.ts:1730-1745 | |
| P2-T4 | Tab L connection finder + Debate button | [ ] | fixed | ArticleDetailView.tsx:189,571; FeedPage.tsx onDebate | |
| P2-T5/6 | DebateModeView + wiring | [ ] | fixed | features/feed/components/DebateModeView.tsx; FeedPage.tsx debateMode | |
| P2-T7 | DraftContextView Q/R tabs | [ ] | fixed | DraftContextView.tsx:143,159 | |
| P2-T8 | Final tsc in both packages | [ ] | unverified | not run (read-only rule) | |

## 5. docs/plans acceptance criteria

| Src ID | Item (short) | Orig tag | Status | Evidence | Notes |
|---|---|---|---|---|---|
| D3-1 | `/feed` split layout, group switcher, filters | spec | fixed | FeedPage.tsx; /trending redirects dashboard/index.tsx:899-900 | |
| D3-2 | Interest-group CRUD endpoints | spec | partial | worker index.ts:72,1723-1733 (action-based `listInterestGroups` etc., db/interestGroups.ts) | not REST `/api/interest-groups`; design differs, functionally present |
| D3-3 | Clips CRUD (`/api/clips`) + persistence | spec | fixed | worker index.ts:714-717,804-807 | assign/unassign by action not verified |
| D3-4 | Hover scissor on text passages in feed cards | spec | open | see C03-7 | |
| D3-5 | Dock magnification, expand, drag to draft | spec | fixed | ClipsDock.tsx:158,332-367 | |
| D3-6 | Draft Context Mode: drag clip into editor as context block | spec | partial | DraftContextView.tsx:259-266 ("Generate Post in Editor"), :571 unassign | drag-into-editor insertion not found |
| D3-7 | Article intelligence "streamed, cached after first load" | spec | unverified | | |
| D2-1 | Mode 1 author-voice keeps >=80% of words | AC1 | unverified | worker/src/engine/nodes/definitions/draft-generator.ts | no test seen for 80% |
| D2-2 | Industry Trend post type + HOOK->EVIDENCE->... structure | AC2 | partial | worker/src/engine/workflows/definitions/trend-commentary.ts; __tests__/contentPostTypesPlaybook.spec.test.ts | |
| D2-3 | Per-post dimension override beats workspace | AC3 | unverified | | |
| D2-4 | 4 variants w/ variant_rationale + badges | AC4 | fixed | worker engine/types.ts, draft-generator.ts; frontend VariantCarousel.tsx | |
| D2-5 | tsc passes both packages | AC5 | unverified | not run | |
| DE-1 | Quick change/4-variant preview-only, unsaved marker, explicit Save Variants | EGW | partial | review/context/useReviewFlowActions.ts:~357 openCompare; backendApi.ts `saveVariants` | UI wording not traced |
| DE-2 | Compare never replaces without confirmation | EGW | fixed | useReviewFlowActions.ts:~357-372 (compare onConfirm sets editor text) | |
| DE-3 | Approval doesn't require Save Variants | EGW | unverified | | |
| DE-4 | Old refine path removed after parity | EGW | unverified | | |
| DE-5 | Modularity (no oversized component) | EGW | open | DashboardSettingsDrawer.tsx 2251 lines; FeedPage.tsx 1490; EditorSidebar large | |

## NEW (stumbled on, not in existing reviews)

- NEW-1 Feed card Bookmark button is a dead control: `FeedArticleCard.tsx` Bookmark `onClick` only `stopPropagation()` (no handler, no prop). Ships an icon that does nothing. Also hover-only.
- NEW-2 Onboarding Tour copy in `DashboardQueue.tsx:435` promises a channel pill that is not rendered (see C04-2) - misleading first-run text.
- NEW-3 `components/ui/ErrorBanner.tsx`, `EmptyState.tsx`, `LoadingSkeleton.tsx` are unused dead code; cons doc 13 treats them as the fix, but nothing adopts them.
- NEW-4 `services/backendApi.ts:485-525` network-failure message tells end users to edit `CORS_ALLOWED_ORIGINS`, VITE_WORKER_URL and workers.dev firewall rules (internal operator text in user UI).
- NEW-5 No transient toast system in app at all (only modal `showAlert`); success feedback for Save draft / Approve is absent. Toast exists only locally in SelectionClipper.tsx and NewsletterTab.tsx.
- NEW-6 `useTrending.ts:280-292` mock-data path still present for `!useRealApis`; confirm production always has real APIs or users could see mock trending.

## Summary

Counts of reconciled rows (rows with multiple statuses counted once under their listed status). C = cons (incl. C05b-e; C-F counted n-a).

| Source | fixed | partial | open | n-a | unverified | total |
|---|---|---|---|---|---|---|
| cons/ (C) | 26 | 30 | 69 | 4 | 19 | 148 |
| USE-CASES.md (U) | 7 | 7 | 1 | 0 | 8 | 23 |
| FEED report / MCP (F, M) | 0 | 0 | 1 | 2 | 0 | 3 |
| superpowers plans (P) | 8 | 0 | 0 | 0 | 1 | 9 |
| docs/plans AC (D) | 5 | 4 | 2 | 0 | 6 | 17 |

(Counts tallied by awk over the Status column of each table row.)

## Open items worth a ledger entry (ranked by likely user impact)

1. C07-1/C07-6 Editor publish has no confirmation and Approve/Publish remain separate buttons; a single click posts live (EditorScreen.tsx footer, useReviewFlowActions.ts publish). Queue has a confirm, editor does not.
2. C07-2 / U-J1.10 No permalink/"View on LinkedIn" after publish; USE-CASES claims it. Users get a generic 'Success' modal.
3. C13-1 / NEW-4 User-facing error text exposes worker URL/CORS/env-var guidance (backendApi.ts:485-525).
4. C13-4/C13-5/C13-2 No retry affordance, no 429/5xx mapping or backoff, no offline banner; ErrorBanner primitives exist but are unused.
5. C09-6 No "Test connection" for any credential/channel; C05-11 no connection health.
6. C06-5 No `beforeunload` guard in editor (autosave restore exists, but guard missing); C06-3 three identical "Discard current editor changes?" dialogs.
7. C04-2 / NEW-2 No per-row channel pill (and the tour text claims one) - wrong-channel risk.
8. C02-1 / C02-10 / C03-6 Mobile/touch gaps: feed vote/clip actions hover-only, trending rail vanishes <lg with no carousel, clips cannot be assigned without drag-drop.
9. C05-1/C05-4 Editor still uses bare `datetime-local` with UTC conversion and no timezone caption (schedule-time errors for non-UTC users).
10. C12-1/C12-2 Admin panel: native `prompt()` budget edit (silent failure on bad input) and no Deny for waitlist.
11. NEW-1 Dead Bookmark button in every feed card.
12. C04-5 / NEW-5 No success feedback on AddTopic/Save draft/Approve (no toast system).
13. C09-1/C09-2/C09-5 Settings is still a 2251-line single component, no URL subpaths, no section descriptions; C09-14 six copy-pasted channel sections.
14. C10-2/C10-4/C10-5 Enrichment failure not surfaced with retry; DAG page admin-only.
15. C07-3 Scheduled-state editor button is only disabled (no "send now anyway"), no countdown (C07-5).
16. C03-1/C03-2 Clip delete still right-click/hover; drop gives no success toast.
17. C02-13 "Evergreen"/"Top 10" ranked by description length.
18. C05c Bulk campaign schedule/channel still modal dialogs; C08-7 newsletter subject variables not verified end-to-end.
19. C11-1/C11-3 No variant-pick or post-publish rating signal captured.
20. U-J11 / NEW-6 mock-data fallback in trending hook - confirm unreachable in prod.
