# worker-a: worker core review (index.ts, auth, db, persistence, scheduled-publish, services, routes)

Counts: P0 = 5, P1 = 14, P2 = 16, P3 = 3 (total 38). Read-only static review; nothing was run. Every item is a code-reading hypothesis until reproduced.
Not re-filed (see ARCH-AUDIT): ARCH-001 dev bypass secret, ARCH-002 allowlist never read and default status 'active', ARCH-004 cron cadence, ARCH-007 DEPLOYMENT_MODE, ARCH-010 DO retry (extended in WKA-003/007), ARCH-011 audience check and CORS `*` default, ARCH-012 owner admin fallback. Frontend action names all resolve to a dispatcher case (checked: 106 frontend actions vs 120 backend cases; only `__admin__` and `downloadDraftImage` are handled before `dispatchAction`).
Paths are under `worker/` unless noted. Line numbers refer to `worker/src/index.ts` unless a file is named.

### WKA-001 Channel credentials are one global config; any user publishes through, and can overwrite, the shared account
- **Sev:** P0
- **Area:** src/index.ts (loadStoredConfig, publishContent, persist*Connection, start*Auth)
- **Journeys:** J-076, J-078, J-094, J-095, J-096, J-103, J-140
- **Evidence:** `loadStoredConfig` reads one KV key `shared-config` for every user (3092, 3148-3170). `publishContent` tries the caller's `social_integrations` row, then falls back to the shared token for LinkedIn (4986-5011), Instagram (4921-4946) and Gmail (5076-5100); WhatsApp and Telegram use only the shared token (5152-5176, 5038). The per-user decrypt failure is swallowed (`catch { // Fall through to shared config }` at 4981, 4916, 5071), so a corrupted personal token also posts as the shared account. The OAuth callbacks call `persistLinkedInConnection` etc. (3556, 3632, 3801, 3878) which rewrite the global KV config (4212-4288), and `startLinkedInAuth/Instagram/Gmail/YouTube` are not admin-gated (2371-2381; only WhatsApp is). So any approved user who connects LinkedIn replaces the shared token for everyone, and any user with no connection posts to the owner's (or last connector's) LinkedIn or mailbox.
- **Repro:** static reasoning. Executor: admin connects LinkedIn; user B (no connection) calls `publishContent` channel `linkedin`; observe the post on the admin's profile. Then user B connects; user C without a connection now posts as B.
- **Fix hint:** make publish use only the caller's `social_integrations` row (fail with "connect your account" if absent or undecryptable); stop calling `persist*Connection` from user callbacks (store per-user only); keep the global config for explicitly shared channels (WhatsApp/Telegram) admin-only.
- **Status:** open
- **Verified:** read-only: index.ts 2371-2384, 3092-3170, 3509-3905, 4212-4337, 4824-5197; db/socialIntegrations.ts.

### WKA-002 Scheduled publish loses the user identity and reads the wrong tenant
- **Sev:** P0
- **Area:** src/scheduled-publish/ScheduledPublishAlarm.ts, src/index.ts (executeScheduledPublish, handleScheduledLinkedInPublishRequest), src/services.ts
- **Journeys:** J-082, J-083, J-092
- **Evidence:** `ScheduledPublishTask` has a `userId` field (types.ts:16) and `publishContent` passes it to `armScheduledPublish` (4886), but `handleArm` persists only topicId/topic/date/scheduledTime/intent/channel/recipientId (ScheduledPublishAlarm.ts:36-44), dropping `userId`. `alarm()` then calls `executeScheduledPublish`, which uses `loadStoredConfig(env)` with no user (4751, so spreadsheetId = the legacy KV sheet or empty, per 3134-3136) and `buildServices(env)` with `userId=''` (4754, services.ts:15). `PipelineStore` queries `WHERE user_id = ?` with that empty id (pipeline.ts `fetchPipelineMapByTopicIds`). `publishContent` is called with `task.userId || ''` (4787) so the per-user token lookup also misses and falls to the shared token (see WKA-001). Result: for non-admin tenants the row is not found (silent return, WKA-003) or the post goes out through the shared account; if no KV sheet exists, `ensureSpreadsheetConfigured` throws and the alarm retries forever.
- **Repro:** static. Executor: as a non-admin user with own sheet, approve a post, schedule 2 minutes ahead, wait; check LinkedIn, D1 `pipeline_state.status` and worker logs.
- **Fix hint:** include `userId` in the DO stored task, and in `executeScheduledPublish` load config with `loadStoredConfig(env, task.userId)` and `buildServices(env, task.userId)`.
- **Status:** open
- **Verified:** read-only: ScheduledPublishAlarm.ts, types.ts, services.ts, index.ts 3087-3136, 4750-4799, persistence/pipeline-db/pipeline.ts 124-176.

### WKA-003 Every early exit in executeScheduledPublish counts as success; the schedule is deleted with no trace
- **Sev:** P0
- **Area:** src/index.ts:4750-4799, src/scheduled-publish/ScheduledPublishAlarm.ts:85-100
- **Journeys:** J-083, J-085, J-086, J-087, J-092
- **Evidence:** `executeScheduledPublish` does a bare `return` when topicId is empty, row not found, status is blocked or not exactly `approved`, `postTime` differs from `task.scheduledTime`, or `selectedText` is empty (4756-4783). `alarm()` then deletes the stored task (`storage.delete` at ScheduledPublishAlarm.ts:92). Nothing is logged, no status such as Failed is written, and the user is not told. Rescheduling in the calendar (`updatePostSchedule`, 2283-2288) changes `postTime` without re-arming, so the old alarm hits the `postTime !==` check and silently drops, while the new time has no alarm unless `publishContent` is called again. When publish throws, the task stays and the runtime retries (ARCH-010), with no cap and no terminal state.
- **Repro:** static. Executor: schedule a post, then edit its `postTime` with `updatePostSchedule` and wait for the original time.
- **Fix hint:** log and persist a reason for every skip (write `status='Failed'`/error note on the row), arm the new alarm inside `updatePostSchedule`, and cap alarm retries with a terminal failure state.
- **Status:** open
- **Verified:** read-only: index.ts 2283-2288, 4750-4799; ScheduledPublishAlarm.ts.

### WKA-004 Newsletter by-id actions have no tenant or ownership check
- **Sev:** P0
- **Area:** src/index.ts:2849-2957, src/newsletter/handlers.ts, src/newsletter/persistence.ts
- **Journeys:** J-112, J-109, J-110, J-140
- **Evidence:** `newsletter.approveIssue/rejectIssue/sendApproved/update/delete/listIssuesByNewsletter/createDraftByNewsletter/regenerateIssue/issue.update` take only an id from the payload and the handlers query `WHERE id = ?` (handlers.ts:69, 83, 136, 189; persistence.ts:150, 165-196, 246, 300, 354, 363). Only the list/create/config actions are scoped by `spreadsheetId`. A user who knows or obtains another tenant's newsletter or issue id (UUID, so unguessable but not secret: it is returned in lists and may appear in logs/URLs) can read, edit, delete, approve, send, or burn LLM budget on it. `createDraftByNewsletter` also bills the caller's budget check path inconsistently (no budget check at all, see WKA-012).
- **Repro:** static. Executor: tenant A creates a newsletter; tenant B calls `newsletter.delete` with A's id.
- **Fix hint:** load the row, compare its `spreadsheet_id` (or an added `user_id`) with the caller's, and reject otherwise, in a single helper used by all by-id handlers.
- **Status:** open
- **Verified:** read-only: index.ts 2828-2957, newsletter/handlers.ts, newsletter/persistence.ts (grep of WHERE clauses).

### WKA-005 completeOnboarding stores an unverified spreadsheet id, which scopes other tenants' D1 data
- **Sev:** P0
- **Area:** src/index.ts:2819-2826 (also saveConfig 4746, setUserSpreadsheetId)
- **Journeys:** J-029, J-030, J-140, J-141
- **Evidence:** `connectSpreadsheet` proves access (shares via the user's Drive token and verifies with the service account, 2738-2779), but `completeOnboarding` calls `setUserSpreadsheetId(userId, payload.spreadsheetId)` with any string and no check (2821-2824). `spreadsheetId` is the tenant key for `news_snapshots`, `llm_settings`, `template_assignments`, `newsletters`, `newsletter_configs`, and feed caches are stored under `spreadsheet_id = 'feed:<userId>'` (db/feedArticles.ts:10-12). A user can set `spreadsheetId` to another tenant's sheet id (or to `feed:other@x.com`) and then read via `listNewsResearchHistory`, `getNewsResearchSnapshot`, `listPatternAssignments`, `newsletter.list/getConfig/listIssues`, and write via `newsletter.saveConfig`. If the service account has access to that sheet (it does for every connected tenant), Sheets reads and writes (`getRows`, `deleteRow`, `createPostTemplate`) also work on the other tenant's sheet.
- **Repro:** static. Executor: tenant B calls `completeOnboarding` with tenant A's sheet id, then `getRows`.
- **Fix hint:** remove `spreadsheetId` from `completeOnboarding` (use `connectSpreadsheet` only), or run the same share-and-verify step, and reject ids with the `feed:` prefix.
- **Status:** open
- **Verified:** read-only: index.ts 2738-2826, db/feedArticles.ts, persistence/pipeline-db/news.ts.

### WKA-006 Durable Object names are not tenant-scoped; cancel and re-arm by topicId from any user
- **Sev:** P1
- **Area:** src/scheduled-publish/durablePublishScheduler.ts:11-13, handleCancelDispatch.ts, src/index.ts:2406-2408, 1343-1351
- **Journeys:** J-084, J-082, J-140, J-144
- **Evidence:** the DO id is `idFromName("<topicId>::<channel>")` (time.ts `buildScheduledPublishTaskName`), with no user component. `cancelScheduledPublish` (dispatcher 2406) only checks that the sheet is configured, then cancels whatever task is armed for that topicId/channel/time. Topic ids are UUIDs, so exploitation needs the id, but nothing verifies the caller owns the row. Arming from `publishContent` uses a client-supplied `row.topicId` the same way, so a user can overwrite another tenant's alarm for the same key (the stored task is replaced by `storage.put`). Also if two tenants import the same campaign JSON with identical `topicId`s (bulk import accepts caller ids), they share one DO and cancel or clobber each other.
- **Repro:** static.
- **Fix hint:** prefix the DO name with `userId`; verify the row exists under `session.userId` before arm and cancel.
- **Status:** open
- **Verified:** read-only: durablePublishScheduler.ts, handleCancelDispatch.ts, ScheduledPublishAlarm.ts, time.ts.

### WKA-007 Publish has no server-side idempotency; client row is trusted for status and text
- **Sev:** P1
- **Area:** src/index.ts:4824-5197 (publishContent), 2403-2405
- **Journeys:** J-088, J-089, J-092, J-091
- **Evidence:** `publishContent` builds everything from `payload.row` supplied by the client (4840). It never re-reads the stored row and never checks `status` (not already `Published`, not `Blocked`), so a double click or a retry sends twice. The state write (`markPublishedForChannel`, 4850-4869) happens after the external send; if `cleanupUnusedGeneratedImages` (Google calls), `markRowPublished` or the Doc append throws, the caller sees an error although the post is live, and the retry posts again. `appendToPostedDoc` swallows errors but `cleanupUnusedGeneratedImages` does not. The DO path has the same flaw (alarm retries after a publish that succeeded but whose mark step threw; extends ARCH-010). Telegram/WhatsApp/Gmail have no dedupe key either.
- **Repro:** static. Executor: click Publish twice quickly, or make `GOOGLE_SERVICE_ACCOUNT_JSON` invalid after send to force a mark failure and retry.
- **Fix hint:** server-side load the row by (userId, topicId); claim it atomically with `UPDATE ... SET status='Publishing' WHERE status='Approved'` and proceed only if one row changed; make the mark step best-effort-with-retry and non-fatal after the external send succeeded.
- **Status:** open
- **Verified:** read-only: index.ts 4824-5197, ScheduledPublishAlarm.ts.

### WKA-008 loadStoredConfig never returns imageGen, enrichmentSkills or YouTube fields; saved settings are ignored and later wiped
- **Sev:** P1
- **Area:** src/index.ts:3138-3177 vs 4659-4715, 4271-4287, 3250-3255
- **Journeys:** J-097, J-081, J-068, J-113, J-120
- **Evidence:** the object returned by `loadStoredConfig` omits `imageGen`, `enrichmentSkills`, and every `youtube*` field, although `StoredConfig` declares them (272-276, 317-319) and `saveConfig` writes `imageGen`/`enrichmentSkills` (4709-4714). Consequences: (1) `generateImageFromText/WithReference` read `storedConfig.imageGen?.provider` (5904, 5987) which is always undefined, so the admin's chosen image model is ignored; `callGenerationWorker` and the SSE route never forward `imageGen`/`enrichmentSkills` (880-881, 2543-2544). (2) `saveConfig` builds the next config from `current.imageGen` (undefined) so a save without those fields erases them from KV. (3) YouTube tokens written by `persistYouTubeConnection` are dropped by the next `persist*`/`saveConfig` write because they are not carried through `loadStoredConfig`/`saveConfig`, and `toPublicConfig` (3213-3214) always reports `hasYouTubeAccessToken=false`, so the UI never shows YouTube connected. (4) `toPublicConfig` returns early (3233-3235) when both news-research and content-review flags are off, skipping imageGen/enrichmentSkills even if present.
- **Repro:** static. Executor: save an image provider in Settings, reload; connect YouTube, reload `bootstrap` and inspect `config.hasYouTubeAccessToken`.
- **Fix hint:** add the missing fields to `loadStoredConfig` and `saveConfig`, and move the imageGen/enrichmentSkills block ahead of the early return.
- **Status:** open
- **Verified:** read-only: index.ts 3087-3257, 4635-4748, 5890-5995.

### WKA-009 Tenants without a Google Sheet cannot publish, delete, or run several core actions
- **Sev:** P1
- **Area:** src/index.ts (dispatchAction `ensureSpreadsheetConfigured` calls at 1573, 1584, 2269, 2290, 2341, 2404, 2407, 2430, 2530 and others)
- **Journeys:** J-031, J-076, J-039, J-082, J-065
- **Evidence:** `loadStoredConfig` deliberately gives tenants without a sheet an empty `spreadsheetId` and the code comment says they "use D1 only" (3111-3114), and `addTopic`/`getRows` honor that. But `publishContent`, `cancelScheduledPublish`, `deleteRow`, `createDraftFromPublished`, `generateQuickChange`, `generateVariantsPreview`, `runContentReview`, `callGenerationWorker`, and the SSE `/api/quickchange/stream` call `ensureSpreadsheetConfigured` and throw "Ask an admin to configure the shared workspace." So a D1-only user can add a topic but not generate with the main worker path or publish. Also `executeScheduledPublish` requires a sheet (WKA-002).
- **Repro:** static. Executor: new non-admin user, skip onboarding sheet, add topic, try Quick Change and Publish.
- **Fix hint:** drop the guard in actions that only need D1 (publish, delete, generation), or make onboarding require a sheet and document it.
- **Status:** open
- **Verified:** read-only: index.ts 1572-1614, 2268-2299, 2403-2408, 2526-2540, 3087-3136.

### WKA-010 deleteRow trusts client row indexes and client image URLs
- **Sev:** P1
- **Area:** src/index.ts:2289-2299, 5251-5363; src/persistence/drafts.ts:427-470
- **Journeys:** J-039, J-143, J-140
- **Evidence:** `deleteRow` takes the whole `row` from the client. In `SheetsGateway.deleteRow` the Draft and Post row indexes are re-derived by topic+date but the Topics row index is `row.topicRowIndex` straight from the payload (drafts.ts:436-441). If the sheet changed since the list was loaded (another tab, another delete, an import), a different topic row is deleted. Before that, `deleteGcsObjectsForTopicRow` deletes every `imageLink1-4` and `selectedImageUrlsJson` URL in the supplied row that lives in the shared bucket (5309-5362), without checking the row belongs to the caller, so a forged row deletes any object URL the attacker knows in the bucket (J-143). Order is also non-atomic: D1 row and snapshots are deleted in parallel first (2294-2297), then the Sheets delete; if Sheets fails the D1 side is gone but the sheet row remains and re-hydrates stale.
- **Repro:** static. Executor: open two tabs, delete a topic in one, delete another in the stale tab, check which Topics row disappeared.
- **Fix hint:** re-read the row server-side by (userId, topicId) and use its indexes and URLs; delete Sheets first, then D1, treating "already gone" as success.
- **Status:** open
- **Verified:** read-only: index.ts 2289-2299, 5251-5363; drafts.ts 427-470.

### WKA-011 Every row mutation upserts the full client-supplied row (INSERT OR REPLACE), enabling stale overwrites and forged status
- **Sev:** P1
- **Area:** src/persistence/pipeline-db/pipeline.ts (upsertFull and callers), src/index.ts:2245-2288, 1652-1664
- **Journeys:** J-063, J-064, J-088, J-091, J-087
- **Evidence:** `updateRowStatus`, `saveEmailFields`(partial), `saveDraftVariants`, `updatePostSchedule`, `saveTopicGenerationRules`, `saveGenerationTemplateId`, `saveTopicDeliveryPreferences`, `assignPattern`, `updateTopicMeta` all do `INSERT OR REPLACE` of `{...clientRow, field}` keyed by (user_id, topic_id) (pipeline.ts `INSERT_PIPELINE_ROW_SQL`). So (a) a stale client copy overwrites newer server state: a tab that still shows `Approved` and calls `updatePostSchedule` after the alarm marked the row `Published` resets it to `Approved`, enabling republish; generation results saved by the server in the SSE complete handler (917-933) can be reverted by the client's old row; (b) a client can set any `status`, `selectedText`, `publishedAt`-adjacent fields directly (`updateRowStatus` accepts any status string, 2245-2258) with no state machine; (c) concurrent edits are last-write-wins with no version column.
- **Repro:** static. Executor: two tabs, publish in one, then change the schedule in the other.
- **Fix hint:** use column-targeted `UPDATE ... WHERE user_id=? AND topic_id=?` per action, whitelist status transitions, and add an `updated_at` precondition.
- **Status:** open
- **Verified:** read-only: pipeline.ts 124-330, index.ts 1615-1665, 2245-2288.

### WKA-012 Several LLM-spending paths skip the monthly token budget
- **Sev:** P1
- **Area:** src/index.ts:835-990 (`/api/generate/stream`), 1165-1268 (sendTopicToGeneration), 1878-2244 (analyze*/insight actions), 2400-2402, 2891-2940 (newsletter draft/regenerate/preview)
- **Journeys:** J-058, J-125, J-045, J-046, J-109
- **Evidence:** `checkTokenBudget` is called only in `generateQuickChange` (1574), `generateVariantsPreview` (1586), `callGenerationWorker` (2532) and the quickchange stream (1004). The SSE `/api/generate/stream`, `sendTopicToGeneration`, `analyzeTopicInsights`, `analyzeFeedArticle`, `extractArticleInsights`, `clusterDraftClips`, `findDraftConnections`, `findDebateArticle`, `crossDomainInsight`, `opinionLeaderInsights`, `generateImage*`, and the newsletter draft actions never check it (the generation worker's own usage is also not logged by the main worker for the stream path). A user over budget keeps generating through the stream route, which is the main UI path.
- **Repro:** static. Executor: set a user's budget to 1 token, run a generation via the queue stream.
- **Fix hint:** do the budget check once in the dispatcher/stream entry for every action that is in an "LLM-spending" set.
- **Status:** open
- **Verified:** read-only: index.ts 835-1010, 1165-1231, 1878-2244, 2400-2402.

### WKA-013 sendTopicToGeneration: racy status flip, no server-side result save, can strand a topic in Pending
- **Sev:** P1
- **Area:** src/index.ts:1165-1268
- **Journeys:** J-056, J-054, J-055
- **Evidence:** the status check reads the merged row then later `UPDATE ... SET status='Pending'` with no compare-and-set (1176, 1218-1220), so two clicks both pass and start two generation runs (double LLM cost, two result streams). The relay only forwards blocks (1237-1261); unlike `/api/generate/stream` it does not process the `complete` event, so if the browser tab closes or the SSE breaks (1256-1258 only logs), the result is lost and the row stays `Pending` with no way back except manual edit. `Pending` can also be set only if a D1 row exists (1221-1223 logs "Sheet-only" and continues), so the UI shows a state the DB does not hold.
- **Repro:** static. Executor: click Send to Generation, close the tab at 50%.
- **Fix hint:** atomic `UPDATE ... WHERE status='Draft'` claim, persist the completed result server-side (reuse the SSE complete handler), and reset to Draft on stream error via `ctx.waitUntil`.
- **Status:** open
- **Verified:** read-only: index.ts 835-990, 1165-1268.

### WKA-014 Monthly token usage misses the first day of every month
- **Sev:** P2
- **Area:** src/db/users.ts:123-137 (getMonthlyTokenUsage), src/db/llm-usage.ts:31-45
- **Journeys:** J-125, J-124
- **Evidence:** `llm_usage_log.created_at` is written with SQLite `datetime('now')` (`YYYY-MM-DD HH:MM:SS`) but the query compares `created_at >= start.toISOString()` (`YYYY-MM-DDT00:00:00.000Z`). As strings, a space sorts before `T`, so every row from the first calendar day is `<` the bound and excluded from usage; budget enforcement and `/api/usage` under-count. The 30-day `expires_at` TTL (llm-usage.ts:29, migration 0013) also deletes rows from the start of a 31-day month.
- **Repro:** static. Executor: insert a log row dated the 1st via the app and read `/api/usage`.
- **Fix hint:** compare with `datetime(?)` or format the bound as `YYYY-MM-DD HH:MM:SS`; keep usage rows at least 31 days.
- **Status:** open
- **Verified:** read-only: users.ts, llm-usage.ts, migrations 0008 and 0013.

### WKA-015 Per-user OAuth tokens expire with no refresh path; refresh logic writes and reads the global config
- **Sev:** P1
- **Area:** src/index.ts:5060-5132, 4004-4031, 3805-3815, 3889; src/db/socialIntegrations.ts:125
- **Journeys:** J-078, J-090, J-096, J-097, J-105
- **Evidence:** `tokenExpiresAt` is stored (Gmail/YouTube one hour, 3813, 3889) but never read anywhere (grep shows only writes). `needs_reauth` is never set: `markSocialIntegrationNeedsReauth` has no caller. On a Gmail 401, `refreshGmailAccessToken(env, config)` uses the shared config's refresh token and writes the new access token back to the shared KV config (5120-5127), not to the user's row. A user who connected their own Gmail gets a one-hour token, then the retry uses another account's refresh token (or throws), and their stored row stays stale. The per-user refresh token (`refresh_token_enc`) is never used. LinkedIn tokens (60 days) just fail with an HTTP error and the UI never learns it needs reconnecting.
- **Repro:** static. Executor: connect Gmail as user B, wait over one hour, send.
- **Fix hint:** refresh from the user's `refresh_token_enc`, persist back to `social_integrations`, and call `markSocialIntegrationNeedsReauth` on terminal 401.
- **Status:** open
- **Verified:** read-only: index.ts 3754-3829, 4004-4031, 5060-5146; socialIntegrations.ts; grep for callers.

### WKA-016 Env secrets and legacy plaintext tokens are copied into KV shared-config in plain text
- **Sev:** P2
- **Area:** src/index.ts:3148-3170, 4212-4337 (spread of `current`), 4340-4365
- **Journeys:** J-132, J-140
- **Evidence:** `loadStoredConfig` fills `instagramAccessToken`, `linkedinAccessToken`, `telegramBotToken`, `whatsappAccessToken` from Worker env (3151, 3154, 3165, 3169) and keeps legacy KV plaintext `gmailAccessToken`/`gmailRefreshToken` (3161, 3163). The persist/disconnect/reauth paths write `{...current, ...}` back with `JSON.stringify` (4221, 4235, 4248, 4267, 4286, 4335, 4358), so connecting LinkedIn copies the Telegram bot token, WhatsApp token and Instagram token from env into the KV record in clear (only the provider being changed has its plaintext field nulled). They stay there after the env secret is rotated, and `ciphertext` encryption gives a false sense of protection. Tokens are not returned to the client (`toPublicConfig` only returns booleans: pass).
- **Repro:** static. Executor: set `TELEGRAM_BOT_TOKEN` in env, connect LinkedIn, `wrangler kv key get shared-config` and look for the token.
- **Fix hint:** persist only fields that came from KV (read the raw KV object, modify, write), never the env-merged view.
- **Status:** open
- **Verified:** read-only: index.ts 3087-3178, 4212-4337.

### WKA-017 Read-modify-write of one KV key with no versioning loses concurrent updates
- **Sev:** P2
- **Area:** src/index.ts (all `CONFIG_KV.put(CONFIG_KEY, ...)` sites: 4221, 4235, 4248, 4267, 4286, 4335, 4358, 4745, 4938, 5003, 5093, 5127, 5170)
- **Journeys:** J-094, J-096, J-102, J-105
- **Evidence:** every connection, disconnect, token-clear and `saveConfig` loads the full config, edits, and puts the whole object. KV is eventually consistent and has no compare-and-swap. A publish-time "token could not be decrypted" cleanup writes a snapshot taken at request start (e.g., 5003), and a Gmail 401 refresh writes `{...config, gmailAccessTokenCiphertext}` (5122-5127), which can overwrite an OAuth connect or `saveConfig` that landed in between. KV writes also propagate with delay, so a user can connect and immediately read an old config.
- **Repro:** static; low-probability race.
- **Fix hint:** split per-feature records into separate keys or D1 rows; write only the changed key.
- **Status:** open
- **Verified:** read-only: index.ts sites listed.

### WKA-018 CORS allows only GET, POST, OPTIONS; the automations PUT and DELETE calls cannot work cross-origin
- **Sev:** P1
- **Area:** src/index.ts:6313-6318 (buildCorsHeaders)
- **Journeys:** J-114, J-118, J-131
- **Evidence:** `Access-Control-Allow-Methods: GET,POST,OPTIONS`. The frontend calls `DELETE /automations/rules` (frontend/src/features/automations/api.ts:55) and `PUT /automations/youtube/schedule` (api.ts:80). The Pages frontend and the workers.dev API are different origins, so the browser preflight fails and the rule delete and YouTube schedule save never reach the worker (the worker handles both methods, automations/routes.ts:113, 143). Related: preflight responses also lack `Access-Control-Allow-Credentials`, which is fine for Bearer-token auth.
- **Repro:** static. Executor: delete an automation rule in the browser and watch the network tab for a failed preflight.
- **Fix hint:** add `PUT,DELETE` (and `PATCH`) to the allowed methods.
- **Status:** open
- **Verified:** read-only: index.ts 6302-6325, frontend automations/api.ts, automations/routes.ts grep.

### WKA-019 All failures return HTTP 400 with the raw message; budget, auth and outage cases are indistinguishable
- **Sev:** P2
- **Area:** src/index.ts:1272-1275, 3043-3052, 23-33 (safeFetch)
- **Journeys:** J-021, J-022, J-125, J-023
- **Evidence:** the dispatcher catch returns `400 {ok:false,error:message}` for every thrown error: expired token, suspended user, validation, budget, upstream 5xx. The 429 `httpStatus`, `used`, `budget` attached to the budget error (1576, 1588, 2534) are discarded because only `error.message` is read. `safeFetch` converts a network failure into a 503 `Response` instead of throwing, so in `verifySession` the "Google token verification unavailable" catch (3046-3048) is dead; a tokeninfo outage becomes `!response.ok` and reports "invalid or expired Google token", which the frontend treats as a forced sign-out (J-022). Raw upstream error text (provider bodies, up to 200-300 chars, e.g. 889, 2651) is passed through to the client; no stack or secret values were seen in error paths (pass).
- **Repro:** static. Executor: block `oauth2.googleapis.com` and call any action.
- **Fix hint:** map known error classes to status codes (401/403/429/502), return a machine `code` field, and make `safeFetch` rethrow outside sandbox.
- **Status:** open
- **Verified:** read-only: index.ts 23-33, 1131-1275, 3031-3085, 1572-1590; frontend backendApi.ts 559-595.

### WKA-020 Every request re-verifies the Google token over the network and runs 3-5 sequential D1/KV reads
- **Sev:** P2
- **Area:** src/index.ts:3031-3085, 1137-1163
- **Journeys:** J-015, J-021, J-040, J-145
- **Evidence:** `verifySession` calls `oauth2.googleapis.com/tokeninfo` (a debug endpoint with a quota that Google does not guarantee for production use) on each action, then `upsertUser` (2 D1 statements), `getUserStatus` (1), then `loadStoredConfig` does KV get + a D1 users read (3092, 3119). The app fires many actions on load (bootstrap, getRows, listClips, ...), so each page load multiplies this. No caching of verified tokens (exp is known from the response). `upsertUser(...).catch(() => undefined)` (3068) swallows D1 failures, then `checkUserAccess` sees no row and tells the user "Access not granted. Request access at the homepage", which misreports a DB outage as an authorization decision.
- **Repro:** static. Executor: time `bootstrap` and watch the subrequest log; run 20 parallel actions.
- **Fix hint:** verify the JWT signature locally against Google JWKS (cache keys), cache `{sub,email,exp}` per token for a short TTL, and surface DB errors as 5xx.
- **Status:** open
- **Verified:** read-only: index.ts 3031-3136, db/users.ts.

### WKA-021 Streaming and REST routes throw outside any try/catch (opaque 500 without CORS headers)
- **Sev:** P2
- **Area:** src/index.ts:835-1010 (`/api/generate/stream`, `/api/quickchange/stream`), 6432-6644 (feed and clips handlers)
- **Journeys:** J-053, J-065, J-044, J-050, J-054
- **Evidence:** `await request.json()` (854, 1011, 6500, 6600), `loadStoredConfig` (853, 1009) and `ensureSpreadsheetConfigured` (1010) run outside any try/catch, as do the feed/clip D1 calls and `JSON.parse(row.topics_json)` / `versions_json` (6454, 6581-6582). A bad body, a user without a sheet (WKA-009) or a corrupt row makes the Worker throw; Cloudflare returns its own 500 page with no `Access-Control-Allow-Origin`, so the browser reports a CORS error instead of a message. Also the SSE relay never aborts the upstream when the client disconnects, and `writer.close()` in `finally` can throw if the client is gone.
- **Repro:** static. Executor: POST `/api/quickchange/stream` as a no-sheet user.
- **Fix hint:** wrap the whole `fetch` handler in a single try/catch that always builds CORS headers.
- **Status:** open
- **Verified:** read-only: index.ts 835-1129, 6432-6644.

### WKA-022 `/api/feed` pagination is wrong and `limit` is unvalidated
- **Sev:** P2
- **Area:** src/index.ts:6432-6488, 6546-6588
- **Journeys:** J-041, J-044, J-050
- **Evidence:** `limit = Math.min(parseInt(...), 100)`: `limit=abc` gives NaN and binds the string `NaN` (SQL error), `limit=-1` is passed to SQLite where a negative LIMIT means no limit, so one call can read the whole table (`clips` is `SELECT *`, unbounded for the user); `cursor` NaN likewise. In `handleFeedGet`, LIMIT/OFFSET page over snapshot rows (up to 3 per topic) but each row holds many articles, and `hasMore = articles.length === limit` compares article count to a snapshot count, so `nextCursor` is almost always null or wrong. With no `interest_group_id` the handler returns an empty list (topics stay empty).
- **Repro:** static. Executor: `GET /api/feed?limit=-1`, `?interest_group_id=<id>&limit=2`.
- **Fix hint:** clamp `limit` to 1..100 integers, page on articles after flattening, and return all-groups feed when no group is given.
- **Status:** open
- **Verified:** read-only: index.ts 6432-6588; db/feedArticles.ts.

### WKA-023 Unbounded list queries and an N+1 in the admin users list
- **Sev:** P2
- **Area:** src/db/clips.ts:55-62 (listClips), src/db/feedArticles.ts (listArticleFeedback), src/modes/saas/admin.ts:9-18, src/db/users.ts (listAllUsers, listAllUserTenantSettings), src/persistence/pipeline-db/pipeline.ts (getRowsByUserId), src/persistence/pipeline-db/news.ts:132-170
- **Journeys:** J-044, J-049, J-123, J-040, J-119
- **Evidence:** `listClips`, `listArticleFeedback`, `getRowsByUserId`, `listAllUsers`, `listAllUserTenantSettings` have no LIMIT and grow with usage; the action API has no pagination. The admin users handler runs one `getMonthlyTokenUsage` query per user in `Promise.all` (admin.ts:11-16): with a few hundred users this exceeds D1's per-invocation query limits and degrades the admin screen. `pruneOldNewsSnapshots` runs a `SELECT DISTINCT spreadsheet_id, topic_id` over the full table plus one windowed delete statement per pair in sequential batches of 128 every night; this grows with tenants and risks the cron CPU/time limit (errors are swallowed, WKA-024).
- **Repro:** static.
- **Fix hint:** add LIMIT/cursor to the list actions, aggregate usage in one `GROUP BY user_id` query, and prune per tenant incrementally.
- **Status:** open
- **Verified:** read-only: files listed.

### WKA-024 Cron handler: no lock, errors swallowed, and the newsletter email path marks issues sent without sending
- **Sev:** P1
- **Area:** src/index.ts:1277-1295, src/newsletter/scheduler.ts:13-107
- **Journeys:** J-111, J-110, J-119
- **Evidence:** `scheduled()` fires five tasks with `ctx.waitUntil(... .catch(() => undefined))` (1278-1294); failures of retention pruning, catalog sync and automation cleanup are invisible. The newsletter scheduler has no lease or claim: `sendNewsletterToRecipients` marks the issue sent after sending (scheduler.ts:96-98) with no compare-and-set on `status='approved'`, so a manual `newsletter.sendApproved` racing the cron (or two cron invocations after a deploy) sends twice. The email branch (scheduler.ts:78-91) only logs "Wire sendGmailMessage..." and sets `sent = true`, so every email newsletter is marked Sent with nothing delivered. When no approved issue exists in the 2h send window (scheduler.ts:35-47), `next_send_at` is never advanced and, once the window passes, neither branch matches, so that newsletter is stuck permanently (extends ARCH-004). `processNewsletter` also drives `Promise.all` over all active newsletters of all tenants in one cron run.
- **Repro:** static. Executor: create an email newsletter, approve an issue, wait for the send window.
- **Fix hint:** implement email delivery or block creating email newsletters; claim issues with `UPDATE ... SET status='sending' WHERE status='approved'`; advance `next_send_at` after every window; log cron failures.
- **Status:** open
- **Verified:** read-only: index.ts 1277-1296, newsletter/scheduler.ts, newsletter/handlers.ts.

### WKA-025 addTopic swallows a Sheets failure, then the topic disappears from the list for sheet users
- **Sev:** P1
- **Area:** src/index.ts:1632-1651, src/persistence/pipeline-db/pipeline.ts:197-226 (getMergedRows)
- **Journeys:** J-035, J-040, J-130, J-129
- **Evidence:** `addTopic` writes the D1 row, then tries `sheets.addTopic` and only logs on failure (1643-1649). For a user with a connected sheet, `getRows` uses `getMergedRows`, which builds the list from the Sheets Topics tab (`topics.map(...)`, pipeline.ts ~226-231) and only merges D1 into those; a D1-only row is never listed. The UI had shown the new topic (returned `newRow`), but after reload it is gone, and the D1 row is orphaned. `createDraftFromPublished` and `bulkImportCampaign` have the reverse order: append to Sheets first, then write D1, and a D1 failure after the append leaves a sheet row that retry duplicates or reports as a conflict (pipeline.ts:522-531, 620-640).
- **Repro:** static. Executor: connect a sheet, revoke the service-account share, add a topic, reload.
- **Fix hint:** fail the request (or enqueue a retry and show "not synced") when Sheets append fails; list D1-only rows in `getMergedRows`.
- **Status:** open
- **Verified:** read-only: index.ts 1558-1571, 1632-1651; pipeline.ts 134-231, 506-640.

### WKA-026 One Topics row without an id breaks every read that goes through getMergedRows; every lookup reads the whole sheet
- **Sev:** P2
- **Area:** src/persistence/pipeline-db/pipeline.ts:157-231 (getMergedRows, getRowByTopicId)
- **Journeys:** J-040, J-129, J-056, J-082
- **Evidence:** `getMergedRows` throws "Every Topics row must have a Topic Id in column C" if any row lacks one (pipeline.ts ~170). `getRows` falls back to D1, but `getRowByTopicId` (used by `updateTopicMeta`, `sendTopicToGeneration`, the generation auto-saves, `savePatternMetadata`, `executeScheduledPublish`) does not, so a single hand-edited sheet row blocks editing, generating and scheduled publishing for that tenant. Each such lookup also calls `ensurePipelineSheets` and reads the Topics, Draft and Post tabs in full plus a D1 query, then may upsert hydrated rows (writes on read). For an alarm this is on the critical path.
- **Repro:** static. Executor: add a row with an empty column C in the Topics tab, then press Send to Generation.
- **Fix hint:** skip (and report) rows without ids; make `getRowByTopicId` a keyed D1 read with sheet fallback only on miss.
- **Status:** open
- **Verified:** read-only: pipeline.ts 134-235.

### WKA-027 Migration 0010 can orphan legacy rows and rewrites topic_key (hypothesis)
- **Sev:** P2
- **Area:** worker/migrations/0010_pipeline_user_primary.sql
- **Journeys:** J-137, J-138, J-140
- **Evidence:** the backfill sets `user_id = COALESCE(users.id matching spreadsheet_id, spreadsheet_id)`. Admin's legacy rows only match if `users.spreadsheet_id` was already set when the migration ran, but the admin's sheet is copied from KV lazily on first login after deploy (`loadStoredConfig` 3125-3128), so those rows land with `user_id = <spreadsheet id>` and no user ever reads them; D1-only data (edited variants, schedules, patterns) is invisible until Sheets re-hydrates the sheet fields. `topic_key` is rewritten to `topic_id` (the SELECT maps `topic_id AS topic_key`), while code writes `buildTopicKey(topic, date)` (pipeline.ts `bindPipelineInsert`), so migrated rows have a different key shape. `INSERT OR IGNORE` silently drops duplicates on the new primary key. `DROP TABLE` + rename is not re-runnable and has no data-count check.
- **Repro:** static. Executor: apply 0010 to a copy of production data and compare row counts per user.
- **Fix hint:** backfill from the KV/admin mapping before the swap, preserve `topic_key`, and assert row counts.
- **Status:** open
- **Verified:** read-only: migrations 0007, 0010, 0019, pipeline.ts. Whether production data existed before 0010 was not checked.

### WKA-028 Pattern assignments and other spreadsheet-keyed tables are shared by all tenants with an empty sheet id
- **Sev:** P1
- **Area:** src/persistence/pipeline-db/pipeline.ts (savePatternMetadata, getTemplateAssignment, listTemplateAssignments), src/routes/patterns.ts, migration 0005
- **Journeys:** J-059, J-140, J-142
- **Evidence:** `template_assignments` has `PRIMARY KEY (spreadsheet_id, topic_id)` and no user column. For tenants without a sheet (`storedConfig.spreadsheetId = ''`) the dispatcher passes `''` (2624, 2627, 2663), so `listPatternAssignments` returns every sheetless tenant's topic ids, patterns and rationales, and `INSERT OR REPLACE` collides across tenants on equal topic ids (also across sheet users who share a sheet, J-141). The same pattern applies to `news_snapshots` and `llm_settings` keyed by `spreadsheet_id`.
- **Repro:** static. Executor: two sheetless users each assign a pattern; call `listPatternAssignments` as one of them.
- **Fix hint:** add `user_id` to these tables or key by `(user_id, topic_id)`; require a non-empty tenant key.
- **Status:** open
- **Verified:** read-only: pipeline.ts 345-420, routes/patterns.ts, migration 0005.

### WKA-029 Per-user Gmail, Telegram and WhatsApp recipients come from the request, sent through shared credentials
- **Sev:** P1
- **Area:** src/index.ts:4842-4845, 5102-5109, 5033-5058, 5148-5187
- **Journeys:** J-078, J-079, J-080, J-103
- **Evidence:** `recipientId` and `emailTo/Cc/Bcc/Subject` are read from the payload with no allowlist against the saved recipients (`telegramRecipients`, `whatsappRecipients`, `gmailDefault*`) and no per-user rate limit. With the shared-token fallback (WKA-001), any approved user can send arbitrary messages to arbitrary Telegram chats or phone numbers via the owner's bot/WhatsApp number, and arbitrary email via the owner's Gmail (spam/phishing from a trusted sender). Gmail attachments fetch arbitrary image URLs (`fetchImageAsset`, 5111).
- **Repro:** static. Executor: user B with no Gmail connection calls `publishContent` channel `gmail` with `emailTo` set to an external address.
- **Fix hint:** only allow recipients present in the saved list for shared channels, and require per-user credentials for Gmail.
- **Status:** open
- **Verified:** read-only: index.ts 4840-5197.

### WKA-030 Waitlist endpoint is unauthenticated, unthrottled, with unbounded fields
- **Sev:** P2
- **Area:** src/modes/saas/waitlist.ts, src/db/users.ts (createAccessRequest), src/index.ts:817-819
- **Journeys:** J-018, J-019, J-017
- **Evidence:** any caller can POST unlimited rows (only the email is validated; `name` and `reason` are stored unbounded; no rate limit, no captcha, no body-size cap). `INSERT OR IGNORE` on a unique email means repeat requests are silently ignored while the response is always 201 "You will hear back by email" even though no email mechanism exists in the worker (grep: none), so the promise is not backed. JSON error responses have no CORS headers, so browser callers see an opaque failure on bad input. Admin approve: `setUserStatus` updates only an existing users row, so approving a person who never signed in updates 0 rows but marks the request approved (works only because new rows default to active, ARCH-002); admin budget `0` is rejected as invalid (admin.ts:55), so a hard block via budget is not possible.
- **Repro:** static.
- **Fix hint:** cap field lengths, add a rate limit (KV counter per IP), send or remove the email promise, and create the users row (status active) on approve.
- **Status:** open
- **Verified:** read-only: waitlist.ts, admin.ts, db/users.ts.

### WKA-031 Image fetch/upload helpers have no size caps and no host rules
- **Sev:** P2
- **Area:** src/integrations/media.ts:187-205 (fetchImageAsset), src/index.ts:5761-5827, 6143-6161
- **Journeys:** J-067, J-143
- **Evidence:** `downloadDraftImage`, `promoteDraftImageUrl` and the Gmail attachment path fetch a caller-supplied URL with `redirect: 'follow'`, accept any `image/*` content type, read the entire body into memory with `arrayBuffer()` and re-upload it to the shared bucket or return it. No byte limit, no allowed-host list, so authenticated users get an open image proxy and can exhaust Worker memory (128 MB). `uploadDraftImage` base64-decodes a data URL of any size (`decodeDataUrl` regex on the whole string, 5747-5759) and accepts `image/svg+xml` into a public bucket (script-capable file on storage.googleapis.com). The object prefix comes from the client `topicId` (`gcsObjectPrefixFromTopicId`, 5695), not from the caller's ownership of the row.
- **Repro:** static. Executor: upload a 100 MB data URL.
- **Fix hint:** cap bytes (stream with a limit), allowlist content types excluding SVG, verify the topic belongs to the caller, key objects by `userId/`.
- **Status:** open
- **Verified:** read-only: media.ts, index.ts 5603-5830, 6143-6161.

### WKA-032 Trending panels and several actions use deployment-wide env credentials for every user
- **Sev:** P2
- **Area:** src/index.ts:2670-2726
- **Journeys:** J-051
- **Evidence:** `trendingYouTube` (YOUTUBE_API_KEY), `trendingLinkedIn` (LINKEDIN_ACCESS_TOKEN, caller-chosen `orgId`), `trendingInstagram` (INSTAGRAM_ACCESS_TOKEN) take no per-user credentials, have no rate limit and no budget; the LinkedIn call lets any user query statistics for any organization id with the owner's token. Response bodies are returned as-is.
- **Repro:** static.
- **Fix hint:** admin-gate or per-user-scope these actions; restrict `orgId` to ones the owner administers.
- **Status:** open
- **Verified:** read-only: index.ts 2670-2726.

### WKA-033 OAuth callbacks report success after silently failing the per-user save; decode errors escape the handler
- **Sev:** P2
- **Area:** src/index.ts:3553-3582, 3629-3658, 3798-3828, 3875-3904, 3533-3541
- **Journeys:** J-094, J-095, J-096, J-098, J-100
- **Evidence:** `upsertSocialIntegration(...).catch(() => undefined)` follows each global persist, so a failed per-user write (for example 0007 not applied, J-133) still posts `ok: true` to the opener; the user then publishes through the shared token (WKA-001). `decodeURIComponent(errorMessage)` on an already-decoded query value throws `URIError` on `%` and runs outside the try, giving a raw 500 popup. The state record includes `origin` from the request `Origin` header (3329), which is attacker-controlled only for an authenticated caller, so the `postMessage` target is safe, but a missing `Origin` (some clients) makes `start*Auth` throw a user-visible "Missing frontend origin". State is single-use and bound to provider and email (pass), but the callback does not verify a session cookie, so a victim who is lured into opening an attacker-started authorization URL links the victim's LinkedIn to the attacker's account (login-CSRF on account linking).
- **Repro:** static. Executor: remove the `social_integrations` table, run a connect, check the popup result.
- **Fix hint:** let the per-user save failure fail the callback; drop `decodeURIComponent`; bind state to a nonce also stored client-side and returned via the opener.
- **Status:** open
- **Verified:** read-only: index.ts 3300-3470, 3509-3905.

### WKA-034 `trending`/feed read path blocks on live news providers and shows only one topic of an interest group
- **Sev:** P2
- **Area:** src/index.ts:1746-1811, src/db/feedArticles.ts:25-65
- **Journeys:** J-041, J-042, J-043
- **Evidence:** `getFeedArticles` returns cached data only when fresh (under 24h); when stale it synchronously runs `trendingSearch` for the first topic (multi-provider network calls) inside the read action, then swallows any error and returns the stale result with `stale: true`, so the UI cannot tell a failed refresh from an old cache. The cache query returns `LIMIT 1`, the single newest snapshot among all the group's topics (feedArticles.ts:41-50), and only the first topic is ever fetched and saved (1760-1773), so a group of several topics shows articles for one topic. `refreshFeedArticles` saves under `req.topic` while `getFeedArticles` looks up by the group's topic list, so topic string differences (case, spacing) miss the cache.
- **Repro:** static. Executor: create a group with 3 topics, open the feed.
- **Fix hint:** fetch per topic in parallel with a timeout, merge and dedupe, and return the refresh error.
- **Status:** open
- **Verified:** read-only: index.ts 1746-1811, feedArticles.ts.

### WKA-035 Internal scheduler routes load the global config and arm without a user; secret compared non-constant-time
- **Sev:** P2
- **Area:** src/index.ts:1298-1387
- **Journeys:** J-144, J-082
- **Evidence:** `/internal/schedule-linkedin-publish`, `/internal/merged-rows`, `/internal/pipeline-upsert` use `loadStoredConfig(env)` (legacy KV sheet) and `buildServices(env)` with user `''`: `pipeline-upsert` therefore writes rows into `user_id=''` (never visible to a tenant), and `merged-rows` reads that same empty-user view; `armScheduledPublish` is called without a `userId` (1343-1351). `verifySchedulerSecret` uses `!==` on the header (1301), and the `/automations/internal/*` route is unauthenticated when `WORKER_SCHEDULER_SECRET` is unset only if the guard is bypassed (guard checks `!expectedSecret`: pass).
- **Repro:** static.
- **Fix hint:** require a `userId` in these payloads or remove the routes if unused; use a timing-safe compare.
- **Status:** open
- **Verified:** read-only: index.ts 1298-1387.

### WKA-036 `getNodeCatalog` returns a `Response` object inside the JSON envelope
- **Sev:** P3
- **Area:** src/index.ts:1875-1877
- **Journeys:** J-113
- **Evidence:** the case returns `Response.json({ nodes: ... })`; the caller wraps it as `{ok:true, data: <Response>}` and `JSON.stringify` of a Response is `{}`. The Enrichment page's node list therefore arrives empty. (Hypothesis on the UI impact; the serialization is certain.)
- **Repro:** static. Executor: call `getNodeCatalog` and inspect `data`.
- **Fix hint:** return the plain object `{ nodes: [...] }`.
- **Status:** open
- **Verified:** read-only: index.ts 1270-1271, 1875-1877; frontend action list.

### WKA-037 Process-wide lifecycle event bus leaks other requests' node events into every SSE stream
- **Sev:** P3
- **Area:** src/index.ts:859-873, src/engine/events/LifecycleEventBus.ts:51
- **Journeys:** J-053, J-113
- **Evidence:** `lifecycleEventBus` is a module singleton; each `/api/generate/stream` request subscribes to `node:completed` with no run or user filter (859-872). Workflow runs from other users in the same isolate emit to all subscribers, so one user's stream shows another user's node ids and durations, and `insightSummary` is built from an empty `{}` payload. Only metadata leaks (no content), and the subscription is removed in `finally`, but if `genResponse` is not ok before the relay starts, `unsubscribeEnrichment` is never called (887-890 return early), leaking a handler per failed call.
- **Repro:** static.
- **Fix hint:** filter by a per-request run id, and unsubscribe on every early return.
- **Status:** open
- **Verified:** read-only: index.ts 835-990, LifecycleEventBus.ts.

### WKA-038 Misc small defects in the access and admin layer
- **Sev:** P3
- **Area:** src/db/llm-usage.ts:57-62, src/index.ts:1530-1538, src/modes/saas/admin.ts
- **Journeys:** J-124, J-123
- **Evidence:** `getUsageSummary` interpolates `days` into the SQL text (`datetime('now', '-${days} days')`); callers clamp it today (1532) so it is safe, but it is an injection-shaped pattern that breaks on the next caller. `__admin__` and the `/automations/*` routes verify admin via `verifySession` but a suspended or removed admin is still admin because `isAdmin` is derived from env only (3083); `suspend` on an admin email has no effect (checkUserAccess admin bypass). The 3-line `DEFAULT_ADMIN_EMAIL` fallback is ARCH-012.
- **Repro:** static.
- **Fix hint:** bind `days` as a parameter; refuse to suspend admin emails explicitly in the admin handler.
- **Status:** open
- **Verified:** read-only: llm-usage.ts, auth.ts, admin.ts, index.ts 1523-1538, 3070-3084.
