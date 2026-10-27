# Launch-readiness ledger — LinkedInPost

- Date: 2026-10-27
- Branch: `launch-readiness-review`
- Status: read-only review; nothing executed; every item Verified = read-only until an executor runs its Repro.
- Source files: PLAN.md, journeys/JOURNEYS.md, findings/ARCH-AUDIT.md, findings/raw/{fe-a,fe-b,worker-a,worker-b,gen-pkg,setup,existing-reviews}.md

## Summary

**Open items by severity** (total 193): P0 = 16, P1 = 58, P2 = 87, P3 = 32.

**Open items by area group:** worker = 72, frontend = 67, setup = 25, generation-worker = 12, deploy = 8, docs = 4, packages = 4, automations = 1.

**Hypothesis items:** 11 (LR-061, LR-094, LR-101, LR-147, LR-149, LR-152, LR-159, LR-168, LR-187, LR-191, LR-193).

**Raw findings merged:** 224 raw IDs (ARCH 20, FEA 31, FEB 29, WKA 38, WKB 46, GWP 26, SET 34) plus open or partial existing-review IDs; rejected: 1 (partial, see below); frozen: see Frozen.

**Top 10 P0/P1 by LR-ID:**

1. LR-001 (P0): The E2E/dev auth-bypass secret is built into the public Pages bundle and also pushed to the production worker, so anyone who reads the JS can call the API as an admin.
2. LR-002 (P0): Calendar or bulk reschedule of an already queued post rewrites postTime without re-queuing, so the old alarm no-ops and the post never goes out.
3. LR-003 (P0): When the rule filter drops every variant the selector returns the unfiltered ones, and a review block verdict is stored as completed, so banned or over-length text reaches the user.
4. LR-004 (P0): The generation worker has no per-user identity: clips, variants and runs are keyed by caller-supplied sessionId and any holder of the shared secret can read or delete any tenant data.
5. LR-005 (P0): SECRET_ENCRYPTION_KEY is printed in clear in the bootstrap summary and streamed to the wizard browser.
6. LR-006 (P0): Re-running setup on a machine without worker/.dev.vars generates a new SECRET_ENCRYPTION_KEY and pushes it to production, making stored channel tokens undecryptable.
7. LR-007 (P0): The Node setup wizard binds all interfaces without auth and returns raw secret values from /api/setup/state.
8. LR-008 (P0): The Node wizard trusts projectDir, args and env from the request body (RCE via run-setup-py, command injection in reset-database, newline injection in write-config).
9. LR-009 (P0): ALLOWED_EMAILS is never read by the worker and new users default to status active, so any verified Google account gets in.
10. LR-010 (P0): Newsletter by-id actions (approve, send, update, delete, regenerate, issue.update) have no tenant or ownership check.

## Open items

### P0 (16)

| ID | Sev | Area | Journeys | Summary (one sentence) | Evidence (file:line) | Aliases (raw IDs) | Status | Verified | Confidence |
|---|---|---|---|---|---|---|---|---|---|
| LR-001 | P0 | deploy/auth | J-012, J-015, J-027, J-136 | The E2E/dev auth-bypass secret is built into the public Pages bundle and also pushed to the production worker, so anyone who reads the JS can call the API as an admin. | .github/workflows/deploy-pages.yml:51-52; worker/src/plugins/dev-google-auth-bypass/resolve-session.ts:20-36 | ARCH-001, FEB-001, SET-006, FEB-026 | open | read-only | confirmed-by-reading |
| LR-002 | P0 | frontend/schedule | J-082..J-084, J-087 | Calendar or bulk reschedule of an already queued post rewrites postTime without re-queuing, so the old alarm no-ops and the post never goes out. | frontend/src/components/dashboard/index.tsx:521-580; worker/src/index.ts:4777 | FEA-001, WKA-003 (reschedule path) | open | read-only | confirmed-by-reading |
| LR-003 | P0 | generation-worker | J-053, J-063, J-065 | When the rule filter drops every variant the selector returns the unfiltered ones, and a review block verdict is stored as completed, so banned or over-length text reaches the user. | generation-worker/src/modules/_shared/selector.ts:170-178; generation-worker/src/players/review.ts:45-53 | GWP-006 | open | read-only | confirmed-by-reading |
| LR-004 | P0 | generation-worker | J-044, J-045, J-053, J-140, J-142 | The generation worker has no per-user identity: clips, variants and runs are keyed by caller-supplied sessionId and any holder of the shared secret can read or delete any tenant data. | generation-worker/src/players/clips.ts:8-14,32; generation-worker/src/index.ts:258-270 | GWP-002 | open | read-only | confirmed-by-reading |
| LR-005 | P0 | setup/cli | J-001, J-002, J-005 | SECRET_ENCRYPTION_KEY is printed in clear in the bootstrap summary and streamed to the wizard browser. | setup/worker_config.py:439; setup/wizard/steps/deploy.py:35-36,90 | SET-005 | open | read-only | confirmed-by-reading |
| LR-006 | P0 | setup/cli | J-002, J-007, J-105, J-132 | Re-running setup on a machine without worker/.dev.vars generates a new SECRET_ENCRYPTION_KEY and pushes it to production, making stored channel tokens undecryptable. | setup/worker_config.py:115-122; setup/cloudflare.py:635-642 | SET-007 | open | read-only | confirmed-by-reading |
| LR-007 | P0 | setup/wizard | J-001, J-011 | The Node setup wizard binds all interfaces without auth and returns raw secret values from /api/setup/state. | frontend/server/setupWizard.js:595; frontend/server/setupWizard.js:131-141 | SET-001 | open | read-only | confirmed-by-reading |
| LR-008 | P0 | setup/wizard | J-001..J-003, J-011 | The Node wizard trusts projectDir, args and env from the request body (RCE via run-setup-py, command injection in reset-database, newline injection in write-config). | frontend/server/setupWizard.js:270-310; frontend/server/setupWizard.js:355-370 | SET-002, SET-003, SET-004 | open | read-only | confirmed-by-reading |
| LR-009 | P0 | worker/auth | J-015, J-017, J-140 | ALLOWED_EMAILS is never read by the worker and new users default to status active, so any verified Google account gets in. | worker/src/index.ts:136 (type only); worker/src/db/users.ts:21-30 with worker/migrations/0019_user_status_budget.sql:2 | ARCH-002 | open | read-only | confirmed-by-reading |
| LR-010 | P0 | worker/newsletter | J-109, J-110, J-112, J-140 | Newsletter by-id actions (approve, send, update, delete, regenerate, issue.update) have no tenant or ownership check. | worker/src/newsletter/handlers.ts:69,83,136,189; worker/src/newsletter/persistence.ts:150,165-196 | WKA-004, WKB-006 | open | read-only | confirmed-by-reading |
| LR-011 | P0 | worker/newsletter | J-110, J-111 | Email newsletter send is a stub that logs a TODO and marks the issue sent, so nothing is delivered while the user is told it shipped. | worker/src/newsletter/scheduler.ts:91-101; worker/src/newsletter/handlers.ts:63-90 | WKB-005, WKA-024 (email branch) | open | read-only | confirmed-by-reading |
| LR-012 | P0 | worker/publish | J-076..J-080, J-090, J-094..J-096, J-103, J-140 | Channel credentials are one shared KV config: publish falls back to the shared owner token for any user without a connection, and any user connecting a channel overwrites the shared token. | worker/src/index.ts:4986-5011 (LinkedIn shared-token fallback); worker/src/index.ts:3092,3148-3170 (single shared-config key) | WKA-001, WKB-002 | open | read-only | confirmed-by-reading |
| LR-013 | P0 | worker/schedule | J-082, J-083, J-092, J-103, J-140 | The scheduled-publish Durable Object drops userId, so the alarm reads the wrong tenant sheet and posts through the shared account. | worker/src/scheduled-publish/ScheduledPublishAlarm.ts:36-44; worker/src/index.ts:4751,4754 | WKA-002, WKB-001 | open | read-only | confirmed-by-reading |
| LR-014 | P0 | worker/schedule | J-083, J-085..J-087, J-092 | Every early exit in executeScheduledPublish (row missing, status, changed postTime, empty text) counts as success and the schedule is deleted with no trace or failed status. | worker/src/index.ts:4756-4783; worker/src/scheduled-publish/ScheduledPublishAlarm.ts:85-100 | WKA-003, WKB-011 | open | read-only | confirmed-by-reading |
| LR-015 | P0 | worker/tenancy | J-029, J-030, J-140, J-141 | completeOnboarding stores any spreadsheet id with no ownership proof, which scopes another tenant D1 data and gives Sheets access to their sheet. | worker/src/index.ts:2819-2826 | WKA-005, WKB-003 | open | read-only | confirmed-by-reading |
| LR-016 | P0 | worker/tenancy | J-053, J-057, J-140 | /api/generate/stream spreads the client payload after the server spreadsheetId, so a caller controls tenant id, llm, imageGen, contextDocuments and research config. | worker/src/index.ts:877-882 | WKB-004, GWP-001 | open | read-only | confirmed-by-reading |

### P1 (58)

| ID | Sev | Area | Journeys | Summary (one sentence) | Evidence (file:line) | Aliases (raw IDs) | Status | Verified | Confidence |
|---|---|---|---|---|---|---|---|---|---|
| LR-017 | P1 | deploy/config | J-011, J-013, J-131 | The frontend dev port (5175) is not in worker CORS (5173/5174) or the documented Google origins, and Playwright waits on 5174, so local sign-in and E2E fail on a clean machine. | frontend/vite.config.ts:78; worker/wrangler.jsonc:57,91 | ARCH-006 | open | read-only | confirmed-by-reading |
| LR-018 | P1 | deploy/config | J-002, J-003 | Root wrangler.jsonc has the same worker name as the API worker, no main, and uploads the frontend source folder as assets, so a root wrangler deploy would replace the API worker. | wrangler.jsonc:3-10 | ARCH-009 | open | read-only | confirmed-by-reading |
| LR-019 | P1 | deploy/config | J-001..J-003 | Committed owner ids (D1, KV, emails, client id, workers.dev URL) make --cloudflare skip creation and migrate the owner D1, which fails on any other account. | worker/wrangler.jsonc:10-20,52-65; setup/cloudflare.py:315-323 | SET-011, ARCH-012 (owner data) | open | read-only | confirmed-by-reading |
| LR-020 | P1 | deploy/config | J-002..J-004 | Generation worker KV namespaces are never provisioned and the committed ids are the owner, so deploy fails on any other account. | generation-worker/wrangler.jsonc:14-21; setup/cloudflare.py:386-438 | SET-012 | open | read-only | confirmed-by-reading |
| LR-021 | P1 | frontend/automations | J-094, J-101 | The in-app LinkedIn guide tells users to register /api/auth/linkedin/callback but the worker route is /auth/linkedin/callback. | frontend/src/features/automations/LinkedInSetupGuide.tsx:33; worker/src/index.ts:772 | ARCH-008 | open | read-only | confirmed-by-reading |
| LR-022 | P1 | frontend/campaign | J-107 | CSV campaign import splits on commas and newlines, so quoted post bodies are truncated or misaligned before being written to the sheet. | frontend/src/features/campaign/CampaignPage.tsx:497-515 | FEB-007 | open | read-only | confirmed-by-reading |
| LR-023 | P1 | frontend/editor | J-035, J-037, J-053, J-056, J-071, J-072, J-075 | topicGenerationRules is used both for Add-Topic JSON metadata and for the Topic rules text, so metadata replaces the user and global rules in the prompt and saving rules wipes the metadata. | frontend/src/features/review/context/useReviewFlowState.ts:65-81; worker/src/index.ts:1639,1658,1186-1200 | FEA-005 | open | read-only | confirmed-by-reading |
| LR-024 | P1 | frontend/editor | J-021, J-064 | Auto-saved editor drafts are never offered for recovery on the editor route because draftRecoveryPending is hard-coded false there. | frontend/src/features/review/context/useReviewFlowState.ts:258,273-282,615-679 | FEA-006 | open | read-only | confirmed-by-reading |
| LR-025 | P1 | frontend/editor | J-035, J-037, J-056 | Continue editing on a saved Draft opens a blank new-topic form (wrong query param) and saving creates a duplicate topic. | frontend/src/components/dashboard/components/TopicPostPreviewCard.tsx:122,210; frontend/src/components/dashboard/index.tsx:75-80 | FEA-008 | open | read-only | confirmed-by-reading |
| LR-026 | P1 | frontend/editor | J-076, J-088 | The editor footer Publish calls handlePublishNow directly with no confirmation and Approve and Publish remain separate buttons, so one click posts live (the queue has a confirm, the editor does not). | frontend/src/features/review-editor/screens/EditorScreen.tsx:340-430; frontend/src/features/review/context/useReviewFlowActions.ts:700 | C07-1, C07-4, C07-6 | open | read-only | confirmed-by-reading |
| LR-027 | P1 | frontend/feed | J-044, J-045, J-050 | Feed and clip REST methods build their URL from globalThis.VITE_WORKER_URL (never set), so requests hit the Pages host and 404 while the UI swallows the error. | frontend/src/services/backendApi.ts:827,844,867,884; frontend/src/features/feed/FeedPage.tsx:283,308 | FEB-002, FEA-027, FEB-025 | open | read-only | confirmed-by-reading |
| LR-028 | P1 | frontend/feed | J-042..J-045, J-049 | Clip create, passage clip, delete, assign, group edits, refresh and votes fail silently, with optimistic state not rolled back. | frontend/src/features/feed/FeedPage.tsx:184-233,280-296; frontend/src/features/feed/components/ClipsDock.tsx:66-76 | FEA-010, FEB-019 | open | read-only | confirmed-by-reading |
| LR-029 | P1 | frontend/newsletter | J-109, J-110 | Newsletter Send, Approve and Reject have no confirmation, no per-issue pending state and swallow errors. | frontend/src/features/campaign/components/newsletter/NewsletterDashboard.tsx:229-260 | FEB-008 | open | read-only | confirmed-by-reading |
| LR-030 | P1 | frontend/onboarding | J-029, J-030 | Onboarding marks itself complete even when the sheet connect fails, with no message, and never reappears. | frontend/src/App.tsx:449-465; frontend/src/features/onboarding/OnboardingModal.tsx:31-40 | FEB-004 | open | read-only | confirmed-by-reading |
| LR-031 | P1 | frontend/schedule | J-082, J-085..J-087 | The editor stores post time as UTC while the calendar and drag-reschedule treat the same string as local wall-clock, and the editor shows no timezone caption. | frontend/src/features/review/context/useReviewFlowActions.ts:632-641; frontend/src/features/content-schedule-calendar/adapters/sheetRowAdapter.ts:9-23 | FEA-002, C05-4 | open | read-only | confirmed-by-reading |
| LR-032 | P1 | frontend/schedule | J-082, J-084, J-088 | The pending scheduled-publish state lives only in React memory in a single slot, so after reload the banner and Cancel vanish and the same post can be queued twice. | frontend/src/features/scheduled-publish/usePendingScheduledPublish.ts:15,17-28; frontend/src/features/scheduled-publish/matchPending.ts | FEA-003 | open | read-only | confirmed-by-reading |
| LR-033 | P1 | frontend/shell | J-026, J-041, J-044, J-140, J-142 | Browser-stored workspace data (clips, feed cache, draft autosave, Add-Topic draft) is not scoped to the user and not cleared on sign-out. | frontend/src/features/feed/FeedPage.tsx:168-173,308-312; frontend/src/App.tsx:359,375 | FEA-009, FEB-018 | open | read-only | confirmed-by-reading |
| LR-034 | P1 | frontend/shell | J-094..J-099 | The OAuth connect hangs forever when the popup is blocked, and consent refusals or disconnect failures are only logged to the console. | frontend/src/App.tsx:397-418,432-447 | FEB-005, FEB-006 | open | read-only | confirmed-by-reading |
| LR-035 | P1 | generation-worker | J-053, J-067, J-068 | Gemini/Seedance image providers return base64 data URIs that are persisted into D1 generation_runs and the SSE payload, risking oversized rows and a lost run. | generation-worker/src/modules/image-generation/providers/gemini.ts:46-47; generation-worker/src/pipeline.ts:259 | GWP-004 | open | read-only | confirmed-by-reading |
| LR-036 | P1 | generation-worker | J-053 | A failed generation_runs INSERT after all LLM and image spend discards the successful result, and the retry regex retries deterministic failures. | generation-worker/src/pipeline.ts:240-272 | GWP-005 | open | read-only | confirmed-by-reading |
| LR-037 | P1 | generation-worker | J-053, J-063, J-076 | The enriched path hard-caps LinkedIn posts at 800 chars (legacy path at 100) while review and adapters allow 3000 and pattern.maxPostChars is ignored. | generation-worker/src/modules/_shared/creator.ts:17-24,184; generation-worker/src/modules/_shared/selector.ts:13-20 | GWP-007 | open | read-only | confirmed-by-reading |
| LR-038 | P1 | generation-worker | J-053, J-122 | The enriched creator swallows every group error (including 401/403/429), has no retry or concurrency limit, and hides the real cause behind a generic message. | generation-worker/src/modules/_shared/creator.ts:187-212; generation-worker/src/modules/_shared/orchestrator.ts:160-189 | GWP-008 | open | read-only | confirmed-by-reading |
| LR-039 | P1 | packages/researcher | J-041, J-052, J-053 | RSS feed URLs from request or config are fetched server-side with no scheme, host or size limits (SSRF and memory), and the URL list is client-controlled via the generate payload. | packages/researcher/src/providers/rss.ts:81-94; packages/researcher/src/config.ts:5-38 | GWP-011, WKB-026 (RSS part) | open | read-only | confirmed-by-reading |
| LR-040 | P1 | setup/cli | J-001, J-011, J-014 | start.sh looks for setup/setup.py (does not exist), silently skips provisioning in production mode, and never starts the worker. | start.sh:176-178,204 | ARCH-005 | open | read-only | confirmed-by-reading |
| LR-041 | P1 | setup/cli | J-001, J-002, J-005 | --deploy-worker aborts on a clean .env because the secrets-file builder rejects the empty bypass secret, after the generation worker is already deployed. | setup/worker_config.py:282; setup/cloudflare.py:600-604 | SET-008 | open | read-only | confirmed-by-reading |
| LR-042 | P1 | setup/cli | J-001, J-002, J-007 | setup.py imports dotenv at module top before the dependency installer can run, so a clean interpreter fails and --web never installs anything. | setup.py:55; setup/python_requirements.py:11-16 | SET-009 | open | read-only | confirmed-by-reading |
| LR-043 | P1 | setup/cli | J-001, J-002, J-009 | run_typescript_dry_run calls npx tsc in frontend/ that setup never installs, so setup aborts on a clean clone; the gate also does not run on every path as documented. | setup/cloudflare.py:575-586; setup.py:98-104 | SET-010, ARCH-015 | open | read-only | confirmed-by-reading |
| LR-044 | P1 | setup/cli | J-002, J-007 | Copying .env.example yields a deployed worker with the public placeholder SECRET_ENCRYPTION_KEY and other placeholder values pushed as real secrets. | .env.example:9-10,22-23,32-33; setup/worker_config.py:115-122 | SET-017 | open | read-only | confirmed-by-reading |
| LR-045 | P1 | setup/cli | J-003, J-007, J-015 | Re-running --cloudflare rewrites wrangler vars from env only, so a blank allow-list reopens sign-up and migrations, services and the env section are overwritten. | setup/worker_config.py:144-207; setup/github.py:50-51 | SET-018 | open | read-only | confirmed-by-reading |
| LR-046 | P1 | setup/wizard | J-001, J-134 | The web wizard dead-ends at the Cloudflare step: the Google step writes GOOGLE_SERVICE_ACCOUNT_JSON but setup.py needs GOOGLE_CREDENTIALS_JSON, and the required bucket is never collected. | setup/wizard/steps/google.py:72; setup/google_resources.py:133-143 | SET-013, ARCH-014 (credential name) | open | read-only | confirmed-by-reading |
| LR-047 | P1 | setup/wizard | J-001, J-005 | The wizard shells out to python (not sys.executable) and to cwd-relative setup.py, features.yaml and state files. | setup/wizard/steps/cloudflare.py:75-78; setup/wizard/state.py:6 | SET-014 | open | read-only | confirmed-by-reading |
| LR-048 | P1 | setup/wizard | J-001, J-008, J-145 | The wizard verify step cannot pass: the worker URL depends on CLOUDFLARE_SUBDOMAIN which nothing sets, it reads stale os.environ, and its JSONC comment strip corrupts URLs. | setup/wizard/steps/verify.py:15-32,20-24,46-47,56-58 | SET-015, SET-016 | open | read-only | confirmed-by-reading |
| LR-049 | P1 | worker/api | J-114, J-118, J-131 | CORS allows only GET, POST and OPTIONS, so the automations DELETE and PUT calls fail preflight from the Pages origin. | worker/src/index.ts:6313-6318 | WKA-018 | open | read-only | confirmed-by-reading |
| LR-050 | P1 | worker/auth | J-053, J-055, J-060, J-145 | The generation worker accepts requests when WORKER_SHARED_SECRET is empty (CORS *, timing-comparable compare), and the main worker sends no auth header when its secret is unset. | generation-worker/src/index.ts:41-44,18-24; worker/src/generation/generationWorkerClient.ts:89 | ARCH-003, GWP-003 | open | read-only | confirmed-by-reading |
| LR-051 | P1 | worker/config | J-006, J-126 | DEPLOYMENT_MODE never reaches the worker, so a selfHosted deploy runs with SaaS token budgets and can block generation. | worker/src/index.ts:1004,1574,1586,2532; worker/src/auth.ts:34-37 | ARCH-007, SET-034 | open | read-only | confirmed-by-reading |
| LR-052 | P1 | worker/config | J-068, J-081, J-097, J-113, J-120 | loadStoredConfig omits imageGen, enrichmentSkills and YouTube fields, so saved settings are ignored and later wiped and YouTube never shows connected. | worker/src/index.ts:3138-3177 vs 4659-4715; worker/src/index.ts:3213-3214 | WKA-008 | open | read-only | confirmed-by-reading |
| LR-053 | P1 | worker/cron | J-111, J-119 | The only cron is daily 03:00 UTC but the newsletter scheduler needs a 2-hour send window and never advances next_send_at, so most newsletters never send. | worker/wrangler.jsonc:17-21; worker/src/newsletter/scheduler.ts (processNewsletter window branches) | ARCH-004, WKA-024 (window stuck) | open | read-only | confirmed-by-reading |
| LR-054 | P1 | worker/db | J-063, J-064, J-087, J-088, J-091 | Every row mutation upserts the full client-supplied row with INSERT OR REPLACE, so stale tabs overwrite newer server state and clients can set any status. | worker/src/persistence/pipeline-db/pipeline.ts (INSERT_PIPELINE_ROW_SQL); worker/src/index.ts:2245-2258 | WKA-011 | open | read-only | confirmed-by-reading |
| LR-055 | P1 | worker/db | J-035, J-040, J-129, J-130 | addTopic swallows a Sheets failure and for sheet users the topic then disappears from the merged list; createDraftFromPublished and bulkImport have the reverse-order problem. | worker/src/index.ts:1632-1651; worker/src/persistence/pipeline-db/pipeline.ts:197-231 | WKA-025 | open | read-only | confirmed-by-reading |
| LR-056 | P1 | worker/generation | J-053..J-056 | Send to Generation navigates away without consuming the SSE stream, flips status with a non-atomic check, has no server-side result save or error path, and can strand the topic in Pending. | frontend/src/components/dashboard/components/TopicPostPreviewCard.tsx:62-66; worker/src/index.ts:1165-1268 | FEA-004, WKA-013, WKB-017 | open | read-only | confirmed-by-reading |
| LR-057 | P1 | worker/generation | J-065, J-066 | Quick change and preview endpoints accept truncated or off-schema model output (or echo the original text on JSON parse mismatch) as the replacement text. | worker/src/generation/normalize.ts:19-76; generation-worker/src/preview.ts:54-71,110-116 | WKB-023, GWP-020 | open | read-only | confirmed-by-reading |
| LR-058 | P1 | worker/integrations | J-076..J-080, J-088 | fetchWithRetry retries non-idempotent POSTs (posts, emails, WhatsApp) and honours Retry-After without a cap, producing duplicates or parked requests; Telegram has no retry at all. | worker/src/integrations/_shared/fetchWithRetry.ts:55-77 | WKB-009, WKB-046 | open | read-only | confirmed-by-reading |
| LR-059 | P1 | worker/integrations | J-078, J-103 | Gmail To/Cc/Bcc/Subject from the client go unsanitised into raw MIME headers (header injection) and are sent from the shared mailbox. | worker/src/integrations/gmail/index.ts:133-137; worker/src/index.ts:5104-5110 | WKB-008 | open | read-only | confirmed-by-reading |
| LR-060 | P1 | worker/llm | J-036, J-045..J-048, J-052, J-053, J-058, J-068, J-069, J-109, J-125, J-126 | Many LLM and paid-API paths (stream generation, send-to-generation, insight actions, trending, images, newsletter drafts, generation worker) skip checkTokenBudget and usage metering. | worker/src/index.ts:835-1010 (no checkTokenBudget); budget checked only at worker/src/index.ts:1004,1574,1586,2532 | WKA-012, WKB-016, WKB-020, GWP-010 | open | read-only | confirmed-by-reading |
| LR-061 | P1 | worker/llm | J-058, J-124..J-126 | Gemini token usage is read from candidates[0].usageMetadata instead of the top-level field, so Gemini calls log 0 tokens and the budget never moves. | worker/src/llm/providers/gemini.ts:115,177; worker/src/generation/types.ts:139-142 | WKB-013 | open | read-only | hypothesis |
| LR-062 | P1 | worker/media | J-067, J-076, J-077, J-079, J-080 | normalizeDeliveryImageUrl rewrites any URL with an id= query parameter into a Drive thumbnail URL, breaking or swapping the post image. | worker/src/integrations/media.ts:12-16,28-41 | WKB-012 | open | read-only | confirmed-by-reading |
| LR-063 | P1 | worker/newsletter | J-110..J-112 | Newsletter send has no claim or lock, so a manual send racing the cron sends twice, partial Telegram failures still mark the issue sent, and the cron sends the oldest approved issue regardless of window. | worker/src/newsletter/handlers.ts:63-90; worker/src/newsletter/scheduler.ts:37-49,60-107 | WKB-018, WKA-024 (lock and swallowed cron errors) | open | read-only | confirmed-by-reading |
| LR-064 | P1 | worker/newsletter | J-109..J-111 | Newsletter bodies are generated in Gemini JSON mode, so the stored email body is an escaped JSON string rather than HTML. | worker/src/newsletter/emailRenderer.ts:80-103,117-130; worker/src/llm/providers/gemini.ts:145 | WKB-014 | open | read-only | confirmed-by-reading |
| LR-065 | P1 | worker/newsletter | J-052, J-109, J-110 | Fetched article and LLM text is inserted into newsletter HTML unescaped (attribute and HTML injection, possible stored XSS in the dashboard). | worker/src/newsletter/emailRenderer.ts:202,206,261-262; worker/src/researcher/providers/rss.ts:7-12 | WKB-015 | open | read-only | confirmed-by-reading |
| LR-066 | P1 | worker/newsletter | J-110, J-111 | Newsletter preview and approval messages can never be delivered (client id used as Gmail token, email used as Telegram chat id, no approve command handler) and autoApprove is never used. | worker/src/newsletter/draftCreator.ts:242-291; worker/src/newsletter/persistence.ts:224-250 | WKB-019, WKB-035 | open | read-only | confirmed-by-reading |
| LR-067 | P1 | worker/publish | J-078..J-080, J-103 | Gmail, Telegram and WhatsApp recipients come from the request with no allow-list against saved recipients, so any user can message arbitrary targets through shared credentials. | worker/src/index.ts:4842-4845,5102-5109 | WKA-029 | open | read-only | confirmed-by-reading |
| LR-068 | P1 | worker/publish | J-078, J-090, J-096, J-097, J-105 | Per-user OAuth tokens expire with no refresh path, needs_reauth is never set, and the Gmail 401 refresh uses the shared refresh token and rewrites the shared KV config. | worker/src/index.ts:5117-5133,4004-4031; worker/src/db/socialIntegrations.ts:125 | WKA-015, WKB-007 | open | read-only | confirmed-by-reading |
| LR-069 | P1 | worker/researcher | J-041, J-044, J-052, J-053 | Articles without a parseable date are stamped now, so old news passes the window and reaches prompts as fresh. | worker/src/researcher/providers/rss.ts:28-35,60-67; worker/src/researcher/providers/newsApis.ts:46,97,146,198-200 | WKB-021, GWP-015 | open | read-only | confirmed-by-reading |
| LR-070 | P1 | worker/schedule | J-076, J-088, J-089, J-091, J-092 | Publish has no server-side idempotency: the client row is trusted, status is not checked, and a failed mark step after a successful send lets a retry or alarm replay post twice. | worker/src/index.ts:4824-4869; worker/src/scheduled-publish/ScheduledPublishAlarm.ts:85-100 | WKA-007, WKB-010, ARCH-010, WKB-011 (replay path) | open | read-only | confirmed-by-reading |
| LR-071 | P1 | worker/schedule | J-082, J-084, J-087, J-140, J-144 | Durable Object names are topicId plus channel with no user component, and cancel or arm accepts any topicId and ignores the arm response, so tenants can cancel or clobber each other schedule. | worker/src/scheduled-publish/durablePublishScheduler.ts:11-13; worker/src/index.ts:2406-2408,4878-4890 | WKA-006, WKB-036 | open | read-only | confirmed-by-reading |
| LR-072 | P1 | worker/tenancy | J-029, J-031, J-039, J-065, J-076, J-082 | Tenants without a sheet are supported by D1 but the frontend shows a pending wall to non-admins without a spreadsheet and the worker throws on publish, delete and generation actions. | frontend/src/components/dashboard/index.tsx:581-595; worker/src/index.ts:3111-3114,1573,2404 | FEB-003, WKA-009 | open | read-only | confirmed-by-reading |
| LR-073 | P1 | worker/tenancy | J-039, J-140, J-143 | deleteRow trusts the client row index and client image URLs, so a stale tab deletes the wrong sheet row and a forged row deletes any object in the shared bucket. | worker/src/index.ts:2289-2299,5309-5362; worker/src/persistence/drafts.ts:436-441 | WKA-010 | open | read-only | confirmed-by-reading |
| LR-074 | P1 | worker/tenancy | J-059, J-140..J-142 | template_assignments, news_snapshots and llm_settings are keyed by spreadsheet_id with no user column, so sheetless tenants share one empty key and collide. | worker/src/persistence/pipeline-db/pipeline.ts (savePatternMetadata, listTemplateAssignments); worker/migrations/0005 | WKA-028 | open | read-only | confirmed-by-reading |

### P2 (87)

| ID | Sev | Area | Journeys | Summary (one sentence) | Evidence (file:line) | Aliases (raw IDs) | Status | Verified | Confidence |
|---|---|---|---|---|---|---|---|---|---|
| LR-075 | P2 | automations | J-118 | The YouTube poller workflow loses its already-replied state on every run (duplicate replies) and its schedule block is commented out. | .github/workflows/youtube-comment-poll.yml:13-31; automations/youtube_poller.py:19,140-159 | SET-032 | open | read-only | confirmed-by-reading |
| LR-076 | P2 | deploy/ci | J-002, J-145 | The deploy workflow applies remote D1 migrations on every push with cancel-in-progress, uses an unpinned third-party action, runs workers in parallel with no needs, and the typecheck needs PyYAML the runner lacks. | .github/workflows/deploy-workers.yml:12-14,38-52,74-88; worker/package.json:7 | ARCH-019, SET-030 | open | read-only | confirmed-by-reading |
| LR-077 | P2 | deploy/ci | J-002, J-013 | No CI runs tests or type checks on pull requests and the Pages build proceeds with unset repo secrets. | .github/workflows/deploy-workers.yml; .github/workflows/deploy-pages.yml | SET-031 | open | read-only | confirmed-by-reading |
| LR-078 | P2 | deploy/config | J-012, J-136 | A literal DEV_GOOGLE_AUTH_BYPASS_SECRET is committed in worker/wrangler.jsonc env.local and tracked frontend/.env.development. | worker/wrangler.jsonc:100; frontend/.env.development | ARCH-012 (committed secret) | open | read-only | confirmed-by-reading |
| LR-079 | P2 | docs/env | J-001, J-002 | Several env names read by the code (YOUTUBE_CLIENT_ID, OAUTH_REDIRECT_BASE_URL, WORKER_SHARED_SECRET, DEV_SPREADSHEET_ID and others) are missing from .env.example and the credential variable name is inconsistent. | worker/src/index.ts:3276,3457,3108; worker/src/automations/routes.ts:24 | ARCH-014 | open | read-only | confirmed-by-reading |
| LR-080 | P2 | frontend/campaign | J-106, J-108 | Bulk campaign import has no idempotency key or duplicate check, so a retry after a timeout adds every topic twice. | frontend/src/features/campaign/CampaignPage.tsx:463-493 | FEB-022 | open | read-only | confirmed-by-reading |
| LR-081 | P2 | frontend/editor | J-064 | Draft recovery writes the saved draft into the editor before the user answers, and Start fresh does not revert. | frontend/src/features/review/context/useReviewFlowState.ts:682-690; frontend/src/features/review/components/ReviewDialogs.tsx:36-52 | FEA-007 | open | read-only | confirmed-by-reading |
| LR-082 | P2 | frontend/editor | J-088, J-089, J-091 | Retrying publish after a failure creates another draft copy of an already published post. | frontend/src/components/dashboard/hooks/useDashboardQueue.ts:602-750 | FEA-012 | open | read-only | confirmed-by-reading |
| LR-083 | P2 | frontend/editor | J-063..J-067, J-091 | The review workspace is not keyed by topic and re-init is keyed on topic text, so late AI, image or save responses land on whichever topic is on screen. | frontend/src/features/review/context/useReviewFlowActions.ts:229-274; frontend/src/features/review/context/useReviewFlowState.ts:376-397 | FEA-013, FEA-014 | open | read-only | confirmed-by-reading |
| LR-084 | P2 | frontend/editor | J-063, J-064 | editorVariantIndex is an index into the filtered variants list but is used as the sheet column slot, so Save draft writes into the wrong column. | frontend/src/features/review/context/useReviewFlowState.ts:241,264-268; frontend/src/features/review/context/useReviewFlowActions.ts:732-738 | FEA-015 | open | read-only | confirmed-by-reading |
| LR-085 | P2 | frontend/editor | J-063, J-066 | Saving an AI preview overwrites the matching sheet slot without confirmation and rapid saves clobber each other. | frontend/src/features/review/context/useReviewFlowActions.ts:416-460 | FEA-016 | open | read-only | confirmed-by-reading |
| LR-086 | P2 | frontend/editor | J-070 | The context-document upload control is not wired through TopicEditorPage, so the upload silently does nothing. | frontend/src/features/topic-navigation/screens/TopicEditorPage.tsx; frontend/src/features/review/context/useReviewFlowActions.ts:1038-1065 | FEA-017 | open | read-only | confirmed-by-reading |
| LR-087 | P2 | frontend/editor | J-052, J-065, J-066 | News-research selections keep feeding every prompt after the panel is closed or the topic changes, with no indicator. | frontend/src/features/news-research/ResearcherPanel.tsx:87-120; frontend/src/features/review/context/useReviewFlowActions.ts:175 | FEA-023 | open | read-only | confirmed-by-reading |
| LR-088 | P2 | frontend/editor | J-076 | No permalink or View-on-channel link after publish: users get a generic Success modal although USE-CASES.md claims a link. | frontend/src/components/dashboard/hooks/useDashboardQueue.ts:587 | C07-2, U-J1.10 | open | read-only | confirmed-by-reading |
| LR-089 | P2 | frontend/editor | J-064 | The editor has no beforeunload guard for unsaved edits, and the three discard dialogs all use identical copy. | frontend/src/features/review/components/ReviewDialogs.tsx:60,95,110 | C06-5, C06-3 | open | read-only | confirmed-by-reading |
| LR-090 | P2 | frontend/feed | J-041..J-043 | Feed refresh replaces a multi-topic group with only the first topic results (frontend and worker), and the cache is not invalidated on group edit. | frontend/src/features/feed/FeedPage.tsx:235-250,330-375; worker/src/index.ts:1746-1811 | FEA-018, WKA-034 | open | read-only | confirmed-by-reading |
| LR-091 | P2 | frontend/feed | J-041, J-042 | Feed load has no cancellation or error state, so switching groups can show the previous group articles and failures look like an empty feed. | frontend/src/features/feed/FeedPage.tsx:328-378 | FEA-019 | open | read-only | confirmed-by-reading |
| LR-092 | P2 | frontend/feed | J-046 | Article analysis can show another article summary because late responses overwrite state. | frontend/src/features/feed/components/ArticleDetailView.tsx:150-176 | FEA-020 | open | read-only | confirmed-by-reading |
| LR-093 | P2 | frontend/feed | J-047, J-048 | Opinion Leaders presents LLM-generated named people as real without an AI disclaimer. | frontend/src/features/feed/components/DraftContextView.tsx:531-545 | FEA-021 | open | read-only | confirmed-by-reading |
| LR-094 | P2 | frontend/feed | J-041, J-051 | Trending falls back to hard-coded mock data when no API is enabled, with no clear sample label. | frontend/src/features/trending/hooks/useTrending.ts:213-225,280-292 | FEB-020, NEW-6, U-J11 | open | read-only | hypothesis |
| LR-095 | P2 | frontend/feed | J-041, J-044 | Feed vote and clip actions are hover-only, the trending rail disappears below lg, and clips cannot be assigned without drag-drop, so touch users cannot use them. | frontend/src/features/feed/components/FeedArticleCard.tsx:97; frontend/src/features/feed/FeedPage.tsx:1340 | C02-1, C02-10, C03-6, C13-7 | open | read-only | confirmed-by-reading |
| LR-096 | P2 | frontend/onboarding | J-030, J-032 | Onboarding requests the full Google Drive scope and forwards the access token to the worker just to share one sheet. | frontend/src/features/onboarding/OnboardingModal.tsx:30-33; frontend/src/App.tsx:453-455 | FEB-012 | open | read-only | confirmed-by-reading |
| LR-097 | P2 | frontend/queue | J-040, J-076 | The queue row has no channel pill although the onboarding Tour copy promises one, which risks publishing to the wrong channel. | frontend/src/components/dashboard/tabs/DashboardQueue.tsx:435,768 | C04-2, NEW-2 | open | read-only | confirmed-by-reading |
| LR-098 | P2 | frontend/saas | J-018 | Waitlist signup shows success even when the server rejects the request. | frontend/src/services/backendApi.ts:1612-1622; frontend/src/features/saas/Landing.tsx:179-191 | FEB-015 | open | read-only | confirmed-by-reading |
| LR-099 | P2 | frontend/saas | J-016 | Pricing and landing pages contradict each other and promise a no-card trial, SLA and analytics that have no backing flow. | frontend/src/pages/PricingPage.tsx:50-160; frontend/src/features/saas/Landing.tsx:277-315 | FEB-021 | open | read-only | confirmed-by-reading |
| LR-100 | P2 | frontend/saas-admin | J-019, J-123 | Admin panel actions have no error handling, Suspend has no confirmation, budget edit uses native prompt, and the waitlist has no Deny. | frontend/src/features/saas/AdminPanel.tsx:63-81,79,172 | FEB-016, C12-1, C12-2 | open | read-only | confirmed-by-reading |
| LR-101 | P2 | frontend/saas-admin | J-017, J-019 | Waitlist approve passes the email as the user id, and approving a person who never signed in updates zero users rows. | frontend/src/features/saas/AdminPanel.tsx (handleApprove(r.email)); worker/src/modes/saas/admin.ts:27-34 | FEB-017, WKA-030 (approve path) | open | read-only | hypothesis |
| LR-102 | P2 | frontend/schedule | J-039, J-083, J-087 | Bulk delete, bulk schedule and calendar reschedule swallow errors, and bulk delete never cancels queued publishes. | frontend/src/components/dashboard/index.tsx:496-580 | FEA-011 | open | read-only | confirmed-by-reading |
| LR-103 | P2 | frontend/shell | J-023, J-053, J-054, J-065, J-076, J-088 | No backend call (JSON or SSE) has a timeout or abort, so a stalled worker leaves Publishing/Generating stuck and invites double publish; the SSE parser drops a final unterminated event. | frontend/src/services/backendApi.ts:559-595,653-702,1399-1454 | FEA-022 | open | read-only | confirmed-by-reading |
| LR-104 | P2 | frontend/shell | J-040, J-088, J-089, J-091 | Queue refresh after publish can fail silently and loads are unordered, so a live post can still show as Approved and be published again. | frontend/src/components/dashboard/hooks/useDashboardQueue.ts:106-125,572-587,716-731 | FEA-024 | open | read-only | confirmed-by-reading |
| LR-105 | P2 | frontend/shell | J-021..J-023, J-125 | Auth errors are detected by regex on message text and the worker returns every failure as HTTP 400, so unrelated errors containing expired or not allowed force sign-out and budget cases lose their status. | frontend/src/services/backendApi.ts:471,526; worker/src/index.ts:1272-1275,3043-3052 | FEB-013, WKA-019 | open | read-only | confirmed-by-reading |
| LR-106 | P2 | frontend/shell | J-021, J-026 | The Google ID token is kept in localStorage and never refreshed, and Automations, Connections, Feed, Usage, Admin and SSE ignore expiry. | frontend/src/components/GoogleLoginButton.tsx:94; frontend/src/App.tsx:49-61,293-367 | FEB-014 | open | read-only | confirmed-by-reading |
| LR-107 | P2 | frontend/shell | J-094..J-099 | The OAuth message listener does not check event.origin or event.source and is not removed when the popup closes. | frontend/src/App.tsx:407-417 | FEB-009 | open | read-only | confirmed-by-reading |
| LR-108 | P2 | frontend/shell | J-079, J-099 | WhatsApp connect silently picks the first phone number. | frontend/src/App.tsx:420-429 | FEB-010 | open | read-only | confirmed-by-reading |
| LR-109 | P2 | frontend/shell | J-082, J-102 | Disconnecting a channel or sheet has no confirmation and no error state even with posts scheduled against it. | frontend/src/pages/connections/ConnectionsPage.tsx:408-416; frontend/src/App.tsx:439-447 | FEB-011 | open | read-only | confirmed-by-reading |
| LR-110 | P2 | frontend/shell | J-023, J-024 | User-facing network errors expose operator text (CORS_ALLOWED_ORIGINS, VITE_WORKER_URL, workers.dev firewall advice). | frontend/src/services/backendApi.ts:485-525 | C13-1, NEW-4 | open | read-only | confirmed-by-reading |
| LR-111 | P2 | frontend/shell | J-021, J-023, J-125 | There is no retry action, offline banner or 401/429/5xx message mapping, and the ErrorBanner, EmptyState and LoadingSkeleton primitives are unused. | frontend/src/components/ui/ErrorBanner.tsx (zero imports); frontend/src/components/useAlert.ts | C13-2, C13-3, C13-4, C13-5, NEW-3 | open | read-only | confirmed-by-reading |
| LR-112 | P2 | generation-worker | J-053, J-062 | Enrichment modules fall back to a default signal on any error but record the node as completed. | generation-worker/src/modules/emotion/index.ts:94; generation-worker/src/modules/_shared/orchestrator.ts:36-67 | GWP-009 | open | read-only | confirmed-by-reading |
| LR-113 | P2 | generation-worker | J-067, J-068 | Image search and provider calls do not check r.ok or response shape and have no timeout, so one hung provider blocks the whole generate response. | generation-worker/src/modules/image-search/index.ts:38-40; generation-worker/src/modules/image-generation/providers/pixazo.ts:28-32 | GWP-017 | open | read-only | confirmed-by-reading |
| LR-114 | P2 | generation-worker | J-067, J-076 | SerpAPI image results are hot-linked from arbitrary hosts with no https or content validation. | generation-worker/src/modules/image-search/index.ts:51-60 | GWP-018 | open | read-only | confirmed-by-reading |
| LR-115 | P2 | generation-worker | J-044, J-045 | Saved-variants and clips KV routes use Date.now keys, no TTL, 1000-key listing, unvalidated url/title and sessionId prefix aliasing, and appear to have no caller. | generation-worker/src/players/variants.ts:6-12,24-25; generation-worker/src/players/clips.ts:51-89 | GWP-022, GWP-023 | open | read-only | confirmed-by-reading |
| LR-116 | P2 | generation-worker | J-053, J-054 | The /v1/generate SSE has no client-disconnect handling, unhandled emit rejections, and an exact Accept match that falls back to a 5-minute single response. | generation-worker/src/index.ts:132-174; worker/src/index.ts:893-945 | GWP-026 | open | read-only | confirmed-by-reading |
| LR-117 | P2 | packages/researcher | J-041, J-044, J-053 | RSS parsing does not decode entities, Atom detection is brittle, and parse failures return zero items silently. | worker/src/researcher/providers/rss.ts:3-12,81-94; packages/researcher/src/providers/rss.ts:3-12 | WKB-037, GWP-014 | open | read-only | confirmed-by-reading |
| LR-118 | P2 | packages/researcher | J-052, J-053 | The news window excludes the end day because a date-only windowEnd parses to midnight UTC, dropping todays articles. | packages/researcher/src/search.ts:14-21; generation-worker/src/pipeline.ts:80-81 | GWP-012 | open | read-only | confirmed-by-reading |
| LR-119 | P2 | packages/researcher | J-052, J-053 | Research sources have no overall deadline (up to about 3 minutes) and the wrapping withRetry never retries because the runner never throws. | packages/researcher/src/search.ts:23-64; generation-worker/src/pipeline.ts:82-97 | GWP-013 | open | read-only | confirmed-by-reading |
| LR-120 | P2 | setup/cli | J-002, J-007 | KV/D1 provisioning is not idempotent and has no rollback, orphaning namespaces and hiding the real create error. | setup/cloudflare.py:226-254,305-356,386-438; setup.py:119-124 | SET-019 | open | read-only | confirmed-by-reading |
| LR-121 | P2 | setup/cli | J-002, J-005, J-008 | Deploy steps report success when sub-steps failed or the worker URL was not found. | setup/cloudflare.py:141-193,547-572,644-650; setup/wizard/steps/deploy.py:46-51 | SET-020 | open | read-only | confirmed-by-reading |
| LR-122 | P2 | setup/cli | J-001, J-002 | Secret and config files (.env, .dev.vars) are written with default permissions rather than 0600. | setup/cloudflare.py:511,543,663; setup/github.py:141 | SET-021 | open | read-only | confirmed-by-reading |
| LR-123 | P2 | setup/cli | J-001, J-007, J-012 | .dev.vars regeneration overwrites the whole file, dropping values from earlier steps so E2E_BYPASS_SECRET regenerates and the GitHub secret goes stale. | setup/cloudflare.py:504-543,659-663; setup/github.py:129-141 | SET-022 | open | read-only | confirmed-by-reading |
| LR-124 | P2 | setup/cli | J-002 | gh secret set --body puts every secret on the process command line and is not scoped with --repo. | setup/github.py:203 | SET-023 | open | read-only | confirmed-by-reading |
| LR-125 | P2 | setup/cli | J-001, J-002 | ensure_cloudflare_auth runs npx wrangler at the repo root before deps are installed, and the root pins wrangler 3.x while workers need 4.x. | setup.py:100-103; setup/cloudflare.py:43-49 | SET-027 | open | read-only | confirmed-by-reading |
| LR-126 | P2 | setup/cli | J-001, J-002, J-011 | setup-production.sh swallows setup.py failure and prints Setup Complete, and the local launchers need frontend deps they never install. | scripts/setup-production.sh:83,98,103-106; scripts/setup-local.sh:55-56 | SET-028 | open | read-only | confirmed-by-reading |
| LR-127 | P2 | setup/cli | J-001, J-011, J-014 | start.sh sources .env as shell code (mangles JSON values, executes content) and has no cleanup trap on Ctrl+C. | start.sh:80-85,221-240,255-273 | SET-029 | open | read-only | confirmed-by-reading |
| LR-128 | P2 | setup/wizard | J-001, J-005 | The Python wizard has no CSRF or Host/Origin protection, so a visited web page can trigger a deploy or overwrite config. | setup/wizard/server.py:14,44; setup/wizard/steps/deploy.py | SET-024 | open | read-only | confirmed-by-reading |
| LR-129 | P2 | setup/wizard | J-005 | The wizard deploy step timeout cannot fire on a silent hang, concurrent starts race, and the stream blocks forever. | setup/wizard/steps/deploy.py:20-91 | SET-025 | open | read-only | confirmed-by-reading |
| LR-130 | P2 | setup/wizard | J-001, J-004 | The wizard API-key step requires a live Gemini call, sends the key in the URL, and fails closed on any network error with no skip. | setup/wizard/steps/apikeys.py:46-57,111-117 | SET-026 | open | read-only | confirmed-by-reading |
| LR-131 | P2 | worker/api | J-044, J-050, J-053, J-054, J-065 | Streaming and REST routes parse bodies and load config outside any try/catch, so failures return a 500 page without CORS headers that browsers report as CORS errors. | worker/src/index.ts:854,1009-1011,6500,6600 | WKA-021 | open | read-only | confirmed-by-reading |
| LR-132 | P2 | worker/api | J-041, J-044, J-050 | /api/feed limit is unvalidated (NaN or negative returns the whole table), pagination compares article count to snapshot count, and no group returns an empty feed. | worker/src/index.ts:6432-6488,6546-6588 | WKA-022 | open | read-only | confirmed-by-reading |
| LR-133 | P2 | worker/auth | J-028, J-131, J-135 | The Google audience check runs only if GOOGLE_CLIENT_ID is set, and CORS falls back to * when CORS_ALLOWED_ORIGINS is empty. | worker/src/index.ts:6304-6308 and the audience check near 3061 | ARCH-011 | open | read-only | confirmed-by-reading |
| LR-134 | P2 | worker/auth | J-003, J-127 | DEFAULT_ADMIN_EMAIL is hard-coded to the owner, so a fork with empty ADMIN_EMAILS makes the original owner admin. | worker/src/index.ts:3020-3027 | ARCH-012 (admin fallback) | open | read-only | confirmed-by-reading |
| LR-135 | P2 | worker/auth | J-015, J-021, J-040, J-145 | Every request re-verifies the Google token over the network and runs 3-5 sequential D1/KV reads, and a swallowed upsert failure is reported as Access not granted. | worker/src/index.ts:3031-3085,3068 | WKA-020 | open | read-only | confirmed-by-reading |
| LR-136 | P2 | worker/automations | J-114, J-118 | Automation rules and YouTube schedules expire from KV after 30 days with no notice. | worker/src/automations/kv.ts:44-64,94-100 | WKB-030 | open | read-only | confirmed-by-reading |
| LR-137 | P2 | worker/automations | J-114, J-116, J-117 | Gmail auto-reply registration needs a KV key nothing writes, the push endpoint has no sender authentication, and LinkedIn automation uses an unset env token. | worker/src/automations/platforms/gmail.ts:38-116; worker/src/automations/routes.ts:55-58,253-263 | WKB-031 | open | read-only | confirmed-by-reading |
| LR-138 | P2 | worker/automations | J-114, J-115 | Instagram comment automation can reply to its own comments and re-fires on webhook redelivery. | worker/src/automations/platforms/instagram.ts:42-81 | WKB-032 | open | read-only | confirmed-by-reading |
| LR-139 | P2 | worker/config | J-011 | env.local has no generation-worker service binding or cron and points GENERATION_WORKER_URL at the owner production worker. | worker/wrangler.jsonc:67-117,99 | ARCH-013 | open | read-only | confirmed-by-reading |
| LR-140 | P2 | worker/config | J-132, J-140 | Env secrets and legacy plaintext tokens are copied into the KV shared-config in clear by every persist and disconnect path. | worker/src/index.ts:3148-3170,4212-4337 | WKA-016 | open | read-only | confirmed-by-reading |
| LR-141 | P2 | worker/config | J-094, J-096, J-102, J-105 | All connection, disconnect and settings writes are whole-object read-modify-write on one KV key with no versioning, losing concurrent updates. | worker/src/index.ts:4221,4286,4745,5003,5127 | WKA-017 | open | read-only | confirmed-by-reading |
| LR-142 | P2 | worker/content-review | J-069, J-076 | Content review is advisory only: publish and the scheduled run never read the verdict or fingerprint. | worker/src/features/content-review/orchestrator.ts; worker/src/index.ts:4824 | WKB-028 | open | read-only | confirmed-by-reading |
| LR-143 | P2 | worker/content-review | J-069, J-124 | Content review usage is logged against the topic id and non-Gemini fenced outputs fail to parse, so the verdict falls to flag. | worker/src/features/content-review/orchestrator.ts:51-59; worker/src/features/content-review/textReviewRunner.ts:6-35 | WKB-029 | open | read-only | confirmed-by-reading |
| LR-144 | P2 | worker/db | J-124, J-125 | Monthly token usage misses the first day of each month because a space-separated timestamp is compared with an ISO T string. | worker/src/db/users.ts:123-140; worker/src/db/llm-usage.ts:31-45 | WKA-014, WKB-041 | open | read-only | confirmed-by-reading |
| LR-145 | P2 | worker/db | J-040, J-044, J-049, J-119, J-123 | List queries (clips, feedback, rows, users, tenant settings) have no LIMIT and the admin users list is N+1 per user; the nightly prune scales with tenants. | worker/src/db/clips.ts:55-62; worker/src/modes/saas/admin.ts:9-18 | WKA-023 | open | read-only | confirmed-by-reading |
| LR-146 | P2 | worker/db | J-040, J-056, J-082, J-129 | One Topics row without an id breaks every read through getMergedRows, and getRowByTopicId reads the whole sheet on the critical path of generation and the alarm. | worker/src/persistence/pipeline-db/pipeline.ts:157-235 | WKA-026 | open | read-only | confirmed-by-reading |
| LR-147 | P2 | worker/db | J-137, J-138, J-140 | Migration 0010 may orphan legacy rows (backfill before admin sheet is copied from KV) and rewrites topic_key. | worker/migrations/0010_pipeline_user_primary.sql | WKA-027 | open | read-only | hypothesis |
| LR-148 | P2 | worker/generation | J-044, J-046, J-053, J-109 | Fetched article text, client-sent research and RSS snippets go into prompts unfenced, and LLM output is returned unsanitised. | worker/src/generation/prompts.ts:16-37; generation-worker/src/modules/_shared/creator.ts:26-32 | WKB-039, GWP-024 | open | read-only | confirmed-by-reading |
| LR-149 | P2 | worker/image-gen | J-068 | The dall-e provider defaults to gpt-image-1 but reads url (not b64_json) and uses DALL-E 3 sizes, and Stability 4:3 is invalid. | worker/src/image-gen/providers/dall-e.ts:4-15; worker/src/image-gen/providers/stability.ts:4-12 | WKB-027 | open | read-only | hypothesis |
| LR-150 | P2 | worker/integrations | J-051 | Trending panels use deployment-wide env credentials for every user, and LinkedIn statistics accept a caller-chosen orgId. | worker/src/index.ts:2670-2726 | WKA-032 | open | read-only | confirmed-by-reading |
| LR-151 | P2 | worker/integrations | J-094..J-096, J-098, J-100 | OAuth callbacks report success after a silent per-user save failure, decodeURIComponent can throw outside the try, and linking is exposed to login-CSRF. | worker/src/index.ts:3553-3582,3533-3541 | WKA-033 | open | read-only | confirmed-by-reading |
| LR-152 | P2 | worker/integrations | J-067, J-076 | LinkedIn commentary is sent raw to rest/posts, where reserved little-text characters may truncate multi-image posts. | worker/src/integrations/linkedin/index.ts:60-63,75 | WKB-022 | open | read-only | hypothesis |
| LR-153 | P2 | worker/integrations | J-077, J-079, J-080 | Multi-part sends leave partial deliveries on error, Instagram publishes without waiting for the container, and Telegram has no 4096-char split. | worker/src/integrations/telegram/index.ts:159-233; worker/src/integrations/instagram/index.ts:162-183 | WKB-033 | open | read-only | confirmed-by-reading |
| LR-154 | P2 | worker/llm | J-053, J-055, J-065, J-122 | No LLM provider call has a timeout, so a stalled provider holds the request and the fallback model is never tried. | worker/src/llm/providers/gemini.ts:84,157; generation-worker/src/players/retryUtils.ts | WKB-025, GWP-019 | open | read-only | confirmed-by-reading |
| LR-155 | P2 | worker/llm | J-069, J-121, J-122 | Provider and model are silently substituted (unknown provider, vision to Gemini, newsletter fixed model) without telling the user. | worker/src/llm/genWorkerDefaults.ts:23-38; worker/src/llm/gateway.ts:105-129 | WKB-024 | open | read-only | confirmed-by-reading |
| LR-156 | P2 | worker/llm | J-053 | Gemini and news API keys are sent in the URL query string, exposed to logs and proxies. | packages/researcher/src/providers/newsApis.ts:20-29; worker/src/llm/providers/gemini.ts:52,85,158 | GWP-016 | open | read-only | confirmed-by-reading |
| LR-157 | P2 | worker/media | J-067, J-143 | Image fetch and upload helpers follow redirects, read whole bodies into memory with no size cap or host rules, and accept SVG into a public bucket. | worker/src/integrations/media.ts:187-205; worker/src/index.ts:5747-5759 | WKA-031, WKB-026 (image part) | open | read-only | confirmed-by-reading |
| LR-158 | P2 | worker/newsletter | J-109, J-111 | Newsletter schedule logic uses UTC, ignores frequency and extra time slots, resets next_send_at on any edit, and queries news with the literal word news. | worker/src/newsletter/persistence.ts:3-44,264-303; worker/src/newsletter/contentAssembler.ts:79-88 | WKB-034 | open | read-only | confirmed-by-reading |
| LR-159 | P2 | worker/publish | J-076..J-080 | There is no per-channel length or format validation before publish (LinkedIn 3000, Instagram 2200, Telegram 4096, WhatsApp limits), so users get provider errors after status change or partial upload. | frontend/src/features/review/context/useReviewFlowActions.ts:624-721; worker/src/index.ts publishContent | FEA-025, WKB-038 | open | read-only | hypothesis |
| LR-160 | P2 | worker/saas | J-017..J-019, J-123 | The public waitlist endpoint is unthrottled with unbounded fields and a promised email that is never sent; admin budget cannot be set to 0. | worker/src/modes/saas/waitlist.ts:4-26; worker/src/modes/saas/admin.ts:44-59 | WKA-030, WKB-040 | open | read-only | confirmed-by-reading |
| LR-161 | P2 | worker/schedule | J-082, J-115, J-117, J-144 | Internal scheduler routes load the global config and arm without a user, and the scheduler secret and webhook verify token are compared non-constant-time or are predictable. | worker/src/index.ts:1298-1387; worker/src/automations/platforms/instagram.ts:15 | WKA-035, WKB-043 | open | read-only | confirmed-by-reading |

### P3 (32)

| ID | Sev | Area | Journeys | Summary (one sentence) | Evidence (file:line) | Aliases (raw IDs) | Status | Verified | Confidence |
|---|---|---|---|---|---|---|---|---|---|
| LR-162 | P3 | docs | J-011, J-013 | Developer docs drift from the code (React version, ports, Anthropic and Firebase claims, researcher providers, migration counts, wizard ports, missing worker test script, llm-core catalog lacks openrouter). | AGENTS.md; worker/AGENTS.md; packages/AGENTS.md; packages/llm-core/src/static-models.ts:3-27 | ARCH-017, SET-033, GWP-025 | open | read-only | confirmed-by-reading |
| LR-163 | P3 | docs | J-076, J-106 | USE-CASES.md and related docs make stale or false claims (3-panel editor, Publish Now label, Save and Continue, CSV append, debate in editor, 100% wired E2E matrix). | USE-CASES.md; frontend/src/features/review-editor/screens/EditorScreen.tsx:227-250 | U-J1.6, U-J1.7, U-J1.9, U-J6, U-J8, U-J12b, U-E2E, F-2 | open | read-only | confirmed-by-reading |
| LR-164 | P3 | docs/env | J-001 | .env.example has dead or duplicated keys, a stale line reference, and inconsistent separators. | .env.example:40-50,117 | ARCH-016 | open | read-only | confirmed-by-reading |
| LR-165 | P3 | frontend/campaign | J-106 | Bulk campaign schedule and channel are still modal dialogs and no template gallery or JSON diff exists. | frontend/src/features/campaign/CampaignPage.tsx:305-308,379-420 | C05c, C05e | open | read-only | confirmed-by-reading |
| LR-166 | P3 | frontend/editor | J-052, J-065, J-066, J-069 | AI generation handlers rethrow into un-awaited click handlers, causing unhandled promise rejections. | frontend/src/features/review/context/useReviewFlowActions.ts:229-274 | FEA-026 | open | read-only | confirmed-by-reading |
| LR-167 | P3 | frontend/editor | J-035, J-049, J-061 | Optimistic UI is not rolled back on failure for votes, persona delete and custom workflows. | frontend/src/features/feed/FeedPage.tsx:260-278; frontend/src/features/workflows/useCustomWorkflows.ts:44-76 | FEA-028 | open | read-only | confirmed-by-reading |
| LR-168 | P3 | frontend/editor | J-061 | Generate-and-save workflow may never save because the card is returned from inside a setState updater. | frontend/src/features/review/context/useReviewFlowActions.ts:344-357 | FEA-029 | open | read-only | hypothesis |
| LR-169 | P3 | frontend/editor | J-076, J-082, J-085 | The footer button always says Publish to X but schedules when the time is in the future, the editor still uses a bare datetime-local, and the scheduled banner has no countdown or send-now-anyway. | frontend/src/features/review-editor/screens/EditorScreen.tsx:310,370-460 | FEA-030, C05-1, C05-7, C07-3, C07-5 | open | read-only | confirmed-by-reading |
| LR-170 | P3 | frontend/editor | J-066 | Dimension sliders in the editor sidebar have no explanatory tooltips. | frontend/src/features/review-editor/components/EditorSidebar.tsx:25-35,360-400 | C06-2 | open | read-only | confirmed-by-reading |
| LR-171 | P3 | frontend/enrichment | J-053, J-113 | Enrichment node failures are not surfaced with a warning or re-run. | frontend/src/features/generation/EnrichmentProgressPanel.tsx | C10-2 | open | read-only | confirmed-by-reading |
| LR-172 | P3 | frontend/feed | J-045 | The feed draft-context text shadows the real draft via a localStorage copy. | frontend/src/features/feed/components/DraftContextView.tsx:66-85 | FEA-031 | open | read-only | confirmed-by-reading |
| LR-173 | P3 | frontend/feed | J-041 | The feed card Bookmark button is a dead control (onClick only stops propagation). | frontend/src/features/feed/components/FeedArticleCard.tsx:131 | NEW-1, C02-16 | open | read-only | confirmed-by-reading |
| LR-174 | P3 | frontend/feed | J-041 | Evergreen and Top 10 are ranked by description length and recency, not a real signal. | frontend/src/features/feed/components/FeedCuratedPanel.tsx:89-92,152-154 | C02-13 | open | read-only | confirmed-by-reading |
| LR-175 | P3 | frontend/feed | J-044 | Clip delete is only via right-click or hover buttons and a drop gives no success toast. | frontend/src/features/feed/components/ClipsDock.tsx:206,332-367 | C03-1, C03-2 | open | read-only | confirmed-by-reading |
| LR-176 | P3 | frontend/newsletter | J-109 | Newsletter subject template variables are not verified end to end and validation lacks character counts. | frontend/src/features/campaign/components/newsletter/NewsletterConfigDrawer.tsx:125-137 | C08-7, C08-2 | open | read-only | confirmed-by-reading |
| LR-177 | P3 | frontend/onboarding | J-029 | The onboarding modal has no dialog semantics, focus trap or escape; accessibility labels and focus rings are only partly audited. | frontend/src/features/onboarding/OnboardingModal.tsx:56-60 | FEB-029, C13-8 | open | read-only | confirmed-by-reading |
| LR-178 | P3 | frontend/queue | J-035, J-091 | Queue and AddTopic polish: no required-field asterisk and the republish tooltip does not say it creates a new draft. | frontend/src/features/add-topic/AddTopicPage.tsx:275; frontend/src/components/dashboard/tabs/DashboardQueue.tsx:925 | C04-6, C04-17 | open | read-only | confirmed-by-reading |
| LR-179 | P3 | frontend/settings | J-120 | Settings is a 2251-line single component with no URL subpaths, section descriptions or channel-card extraction, and save/validators are admin-only or missing. | frontend/src/components/dashboard/DashboardSettingsDrawer.tsx:1235-1256,1282 | C09-1, C09-2, C09-4, C09-5, C09-13, C09-14, DE-5 | open | read-only | confirmed-by-reading |
| LR-180 | P3 | frontend/setup | J-010 | The embedded setup wizard hard-codes http://localhost:3456 and is reachable in production at /setup. | frontend/src/features/setup-wizard/setupService.ts:68-132; frontend/src/features/setup-wizard/steps/FinalStep.tsx:144 | FEB-028 | open | read-only | confirmed-by-reading |
| LR-181 | P3 | frontend/shell | J-025 | Deep-link restore after login covers only four route prefixes. | frontend/src/lib/postLoginRedirect.ts:6-16 | FEB-023 | open | read-only | confirmed-by-reading |
| LR-182 | P3 | frontend/shell | J-023 | The bootstrap failure screen has no Retry and a timeout leaves a stale token. | frontend/src/App.tsx:301-367,683-689 | FEB-024 | open | read-only | confirmed-by-reading |
| LR-183 | P3 | frontend/shell | J-035, J-076 | There is no transient toast system, so Save draft, Approve and AddTopic give no success feedback. | frontend/src/features/add-topic/AddTopicPage.tsx:296; frontend/src/components/useAlert.ts | C04-5, NEW-5 | open | read-only | confirmed-by-reading |
| LR-184 | P3 | frontend/videos | J-146 | The videos live panel polls http://127.0.0.1:8765 from the deployed HTTPS app. | frontend/src/features/videos/LiveRunsPanel.tsx:6 | FEB-027 | open | read-only | confirmed-by-reading |
| LR-185 | P3 | generation-worker | J-059 | Pattern outcome recording is awaited without catch and pattern stats are global across tenants. | generation-worker/src/players/patternFinder.ts:23-36,93; generation-worker/src/pipeline.ts:186 | GWP-021 | open | read-only | confirmed-by-reading |
| LR-186 | P3 | setup/cli | J-011, J-014 | start.sh db reset targets a D1 and tables that do not exist, uses grep -oP (not on macOS) and hides errors. | start.sh:90-118 | ARCH-020 | open | read-only | confirmed-by-reading |
| LR-187 | P3 | worker/api | J-113 | getNodeCatalog returns a Response object inside the JSON envelope, so the node list arrives empty. | worker/src/index.ts:1875-1877 | WKA-036 | open | read-only | hypothesis |
| LR-188 | P3 | worker/auth | J-123, J-124 | Small access/admin defects: SQL text interpolation of days, suspended or removed admins stay admin via env, suspend on an admin email has no effect. | worker/src/db/llm-usage.ts:57-62; worker/src/index.ts:3070-3084 | WKA-038 | open | read-only | confirmed-by-reading |
| LR-189 | P3 | worker/config | J-139 | scripts/generate_features.py defaults differ from features.yaml, so a missing yaml silently turns flags off, and videoEpisodes contradicts the yaml comment for saas. | scripts/generate_features.py:23-32; features.yaml:9-24 | ARCH-018 | open | read-only | confirmed-by-reading |
| LR-190 | P3 | worker/engine | J-061, J-062, J-113 | The workflow engine is not run by any route and its validator truncation would destroy line breaks. | worker/src/engine/executor/WorkflowRunner.ts; worker/src/engine/nodes/definitions/constraint-validator.ts:58-64 | WKB-044 | open | read-only | confirmed-by-reading |
| LR-191 | P3 | worker/generation | J-053, J-113 | The process-wide lifecycle event bus can leak node metadata between SSE streams and handlers are not unsubscribed on early return (conflicts with WKB-044 that the engine is never run). | worker/src/index.ts:859-873; worker/src/engine/events/LifecycleEventBus.ts:51 | WKA-037 | open | read-only | hypothesis |
| LR-192 | P3 | worker/llm | J-068, J-124 | Image generation cost keys do not match model ids so image cost logs as 0 USD. | worker/src/llm/pricing.ts:36-60; worker/src/image-gen/model-catalog.ts:11-37 | WKB-042 | open | read-only | confirmed-by-reading |
| LR-193 | P3 | worker/llm | J-121, J-122 | The static Gemini model list and defaults are likely stale. | worker/src/llm/providers/gemini.ts:4-9; worker/src/llm/google-model-policy.ts:1 | WKB-045 | open | read-only | hypothesis |

## Fix hints (per item)

LR-001: Remove VITE_E2E_BYPASS_SECRET from deploy-pages.yml, stop pushing DEV_GOOGLE_AUTH_BYPASS_SECRET as a prod worker secret (setup/worker_config.py:270-283, setup/cloudflare.py:156-175), gate the bypass on import.meta.env.DEV; use a separate staging worker for cloud E2E.
LR-002: On any schedule change for an Approved row cancel the old queued task and call publishContent again (or re-arm in the worker updatePostSchedule); at minimum block drag-reschedule for queued rows.
LR-003: On an empty filter result retry the creator once then return an error or flag every variant; surface review verdict block as status blocked and make the main worker withhold it.
LR-004: Drop the unused /v1/clips and /v1/variants routes (no caller found) or derive sessionId from the verified session; add user_id to generation_runs.
LR-005: Print a masked placeholder like the other secrets.
LR-006: Persist generated keys to .env (0600) at creation and refuse to deploy a freshly generated key if the worker already has the secret unless --rotate-keys.
LR-007: server.listen(PORT, 127.0.0.1); return only isSet flags; reject non-localhost Host headers.
LR-008: Fix projectDir to the server repo root, allow-list args and env keys, use spawn with argument arrays (no bash -c), validate key names and reject control chars, merge instead of truncate, write 0600.
LR-009: Read ALLOWED_EMAILS in verifySession and reject before upsertUser, or insert new users as pending in selfHosted mode; fix the SETUP.md verification line.
LR-010: Load the row and compare spreadsheet_id (or add user_id) with the caller in one shared helper used by all by-id handlers; assert changes > 0.
LR-011: Implement the Gmail send with a per-user token, or fail loudly and leave the issue approved (block creating email newsletters).
LR-012: Publish only with the caller social_integrations row and throw connect-your-account when absent or undecryptable; stop calling persist*Connection from user OAuth callbacks; keep shared channels admin-only.
LR-013: Persist userId in the DO task and call loadStoredConfig(env, task.userId) and buildServices(env, task.userId) in executeScheduledPublish.
LR-014: Log and persist a reason (status Failed plus note) on each skip, cap alarm retries with a terminal failed state, and re-arm in updatePostSchedule.
LR-015: Remove spreadsheetId from completeOnboarding (use connectSpreadsheet only) or run the same share-and-verify step; reject ids with the feed: prefix and ids bound to another user.
LR-016: Build the generation request from an allow-listed schema and put server-owned fields (spreadsheetId, imageGen, enrichmentSkills) last; same for the callGenerationWorker action.
LR-017: Pick one port and set it in vite.config.ts, playwright.config.ts, CORS vars, start.sh and the docs.
LR-018: Point assets at frontend/dist, add .assetsignore, and merge into worker/wrangler.jsonc or give the root file a distinct name.
LR-019: Commit a template with placeholders and generate wrangler.jsonc, or verify ids via wrangler d1 info before trusting them.
LR-020: Create and patch both KV namespaces in provision_generation_worker_d1 and use placeholders in the tracked config.
LR-021: Change the guide text to /auth/linkedin/callback.
LR-022: Use a real CSV parser with quoted-field support or require the JSON path.
LR-023: Store Add-Topic metadata in its own field (topic_meta) and keep topicGenerationRules for rules only.
LR-024: Arm draftRecoveryPending for the editor screen too and show the prompt before applying.
LR-025: Use ?edit= in TopicPostPreviewCard or accept both params in AddTopicPageWithEdit.
LR-026: Add a confirm step (channel, time, rendered preview) before handlePublishNow in the editor, reusing the queue publishConfirmRow pattern.
LR-027: Use this.endpointUrl in all call sites, delete the dead variants/save KV code and the window.__idToken read, and surface errors in FeedPage.
LR-028: Surface an error notice in each catch, roll back optimistic state, route auth expiry to onAuthExpired.
LR-029: Add a confirm dialog with recipient count, per-issue pending state and show the thrown error.
LR-030: Keep the modal open on failure and only call completeOnboarding after success or an explicit Skip.
LR-031: Use one shared UTC/local conversion helper in the calendar adapter, reschedule commit and past-time check; add a timezone caption to ScheduleEditor.
LR-032: Return queued tasks from bootstrap or getRows (keyed by topicId+channel) and derive the banner from server state.
LR-033: Clear these keys and the feed store on sign-out and email change, prefix keys with a user hash, always replace local clips with the server response.
LR-034: If window.open returns null show an alert and return; clear the interval and listener on close; route errors through AlertProvider.
LR-035: Upload generated bytes to R2/KV or the image store and return a URL; never persist base64 in D1.
LR-036: Catch the persist error, record trace.persistError, and still return the result.
LR-037: Use one shared channel-limit constant (3000 for LinkedIn), honour pattern.maxPostChars, fix the legacy 100.
LR-038: Wrap group calls in withRetry for 429/5xx, cap concurrency, collect errors into trace.creatorErrors and include the first in the thrown message.
LR-039: Require https, block private and loopback names, cap Content-Length and read at most about 1 MB.
LR-040: Point to $PROJECT_ROOT/setup.py, fail loudly if missing, and start the worker or correct AGENTS.md.
LR-041: Move the bypass key to the optional dict and delete the prod push per the bypass item.
LR-042: Wrap the dotenv import in try/except, run the ensure-deps step first, probe all of requirements.txt.
LR-043: npm ci in frontend/ first (or skip when absent), and fix the docs or run the check on all paths including generation-worker.
LR-044: Comment out placeholder lines in .env.example and reject values matching REPLACE_WITH_ or your_*_here and non-32-byte base64 keys.
LR-045: Overwrite a var only when the new value is non-empty, keep unknown keys and migrations, refuse empty ALLOWED_EMAILS in selfHosted mode.
LR-046: Write the canonical name, add a bucket field, or pass --skip-google when the wizard has no Drive bootstrap.
LR-047: Use [sys.executable, ROOT/setup.py] and ROOT-anchored paths everywhere.
LR-048: Persist VITE_WORKER_URL from the deploy output, re-read .env via dotenv_values, parse wrangler.jsonc with json5, probe the endpoint setup/verification.py uses.
LR-049: Add PUT and DELETE (and PATCH) to Access-Control-Allow-Methods.
LR-050: Fail closed (503) when the secret is empty outside an explicit dev flag, constant-time compare, drop the bare-secret form and CORS *.
LR-051: Use the generated deploymentMode constant in the worker, or have setup write DEPLOYMENT_MODE into wrangler vars; delete the no-op regex in generate_features.py.
LR-052: Add the missing fields to loadStoredConfig and saveConfig and move the imageGen block ahead of the early return in toPublicConfig.
LR-053: Run the cron hourly or every 15 minutes, or send anything with next_send_at <= now and not yet sent; advance next_send_at after every window.
LR-054: Use column-targeted UPDATE ... WHERE user_id=? AND topic_id=? per action, whitelist status transitions, add an updated_at precondition.
LR-055: Fail the request when the Sheets append fails and list D1-only rows in getMergedRows.
LR-056: Claim with UPDATE ... WHERE status=Draft, persist the completed result server-side under ctx.waitUntil, emit an error event and revert to Draft on failure, and read the stream or poll on the client.
LR-057: Ask for {text} consistently and read result.text, throw when empty instead of echoing the input, fail when parsing fails or finishReason is not STOP.
LR-058: Do not retry the final create call (retry only idempotent upload steps and pre-connection errors), cap Retry-After, honour Telegram retry_after.
LR-059: Reject CR/LF in header values, validate addresses, RFC 2047-encode the subject, cap recipient count.
LR-060: Check the budget once in the dispatcher or stream entry for an LLM-spending action set, filter client llm through an allow-list, pass userId into the usage context, add per-user rate limits for paid search and image actions.
LR-061: Read payload.usageMetadata first, fall back to the candidate path, fix the type; confirm with one live call.
LR-062: Apply the id= and thumbnail patterns only when the host is drive.google.com or docs.google.com.
LR-063: Atomic UPDATE status=sending WHERE status=approved and proceed only if one row changed, record per-recipient results, restrict the cron to the current window issue, log cron failures.
LR-064: Add a plain-text/HTML generation path or request {html} and parse it.
LR-065: HTML-escape all interpolated strings, allow only http(s) URLs, sanitise LLM HTML with an allow-list.
LR-066: Send previews with the admin stored integration token or a real chat id, or remove the preview promise and the auto-approve toggle.
LR-067: Allow only saved recipients for shared channels and require per-user credentials for Gmail.
LR-068: Refresh from the user refresh_token_enc, persist to social_integrations only, and call markSocialIntegrationNeedsReauth on terminal 401.
LR-069: Keep publishedAt empty when unknown, exclude undated items from windowed searches, parse SerpApi relative dates through one date function.
LR-070: Load the row server-side, claim it atomically (UPDATE status=Publishing WHERE status=Approved), store the channel post id, make the mark step best-effort after a successful send, and bound alarm retries.
LR-071: Prefix the DO name with userId, verify row ownership before arm and cancel, and check response.ok on arm.
LR-072: Drop ensureSpreadsheetConfigured in actions that only need D1 and always allow /connections, /usage, /rules; or require a sheet in onboarding and document it.
LR-073: Re-read the row by (userId, topicId) server-side and use its indexes and URLs; delete Sheets first then D1.
LR-074: Add user_id to these tables or key by (user_id, topic_id); require a non-empty tenant key.
LR-075: Persist replied ids in the worker (KV/D1) or restore and save the file via actions/cache.
LR-076: Pin the action to a SHA, cancel-in-progress false, deploy the generation worker first, add Python/PyYAML and permissions: contents: read.
LR-077: Add a pull_request workflow running tsc for all three packages, npm run test and pytest setup/wizard/tests; fail Pages when secrets are empty.
LR-078: Move the local secret to untracked .dev.vars and untrack .env.development values.
LR-079: Add the missing keys with comments and unify GOOGLE_CREDENTIALS_JSON versus GOOGLE_SERVICE_ACCOUNT_JSON.
LR-080: Client-generated import id stored by the worker, or dedupe by topic and date; show a row-count confirm.
LR-081: Move the restore into the dialog confirm handler and leave state untouched on cancel.
LR-082: Remember the created copy topicId and reuse it on retry, or delete the copy on failure.
LR-083: Put key={row.topicId} on ReviewWorkspace (or ReviewFlowProvider) and include topicId in initKey.
LR-084: Store variant.originalIndex in state and refuse to save when it is unknown.
LR-085: Serialize saves, merge from the latest sheetRow and confirm before overwriting a non-empty slot.
LR-086: Add the prop to TopicReviewPagesBaseProps, pass it through, and show an error when the handler is missing.
LR-087: Reset researchContextArticles on topic change and show a sources-attached chip outside the News tab.
LR-088: Show channel and time (and post id if the API returns one) in the success message, or correct the USE-CASES.md claim.
LR-089: Add a beforeunload guard while the editor is dirty and differentiate the dialog copy.
LR-090: Refresh per topic in parallel with a timeout, merge and dedupe, clear the feed store when a group is saved, return the refresh error.
LR-091: Add a cancelled/request-id guard and an error state in the list.
LR-092: Use a cancelled flag keyed to article.url in both effects.
LR-093: Add the same disclaimer as Debate Mode or label them illustrative personas.
LR-094: Return an empty connect-a-source state or label the data as sample; confirm production always has real APIs.
LR-095: Make the action buttons visible on touch (CSS) and add an Add-to-topic menu per clip; defer the carousel.
LR-096: Use drive.file plus Picker or the manual share path; verify the worker does not persist the token.
LR-097: Render the channel pill on each row or correct the Tour copy.
LR-098: Throw when !res.ok or !body.ok.
LR-099: Use a single source of plan data and remove or mark coming-soon claims with no backing.
LR-100: Add try/catch with inline errors, confirm before suspend, replace prompt() with an input, add a deny action or remove the pending list.
LR-101: Approve by access-request id or email via a route that creates or activates the user row.
LR-102: Collect failures into one summary notice and cancel queued tasks before deleting.
LR-103: Wrap fetches with AbortSignal.timeout (60 s JSON, 120 s idle for SSE), expose cancel, flush the trailing buffer.
LR-104: Mark the row published locally and show a published-refresh-failed notice; add a request counter to loadData.
LR-105: Return 401/403/429/502 with a machine code from the worker and key off it in post(); make safeFetch rethrow outside sandbox.
LR-106: Central 401 handling in BackendApi.post, or exchange the ID token for a worker session.
LR-107: Require event.origin to equal the worker origin and event.source to equal the popup; remove the listener on close.
LR-108: Show a picker listing verifiedName and displayPhoneNumber before completeWhatsAppConnection.
LR-109: Confirm with the count of scheduled posts on that channel and show failures.
LR-110: Show a plain-language message to users and log the operator hint to the console only.
LR-111: Adopt ErrorBanner in the load paths already touched by the silent-failure fixes and map status codes to copy.
LR-112: Return {signal, degraded, error} or rethrow into the failed path while substituting the default.
LR-113: Shared fetchJson with timeout and expectOk, validate imageUrl.
LR-114: Require https, prefer thumbnail when original fails, validate at promote time.
LR-115: Delete the routes if unused, else validate sessionId and url, add a TTL and loop cursors.
LR-116: Use includes(text/event-stream), thread an AbortSignal, catch emit errors.
LR-117: Decode entities then strip tags, detect Atom by root element, prefer rel=alternate, warn when 0 items.
LR-118: Treat a date-only end as end-of-day or compare by slice(0,10).
LR-119: One AbortSignal with a 15-20 s overall budget, run API providers in parallel with the RSS batch, drop the dead retry.
LR-120: List before create (kv namespace list, d1 list) and write ids to config immediately after each create.
LR-121: Collect failures and exit non-zero; require a resolved URL before reporting success.
LR-122: Shared write_secret_file helper using os.open with 0o600 and chmod existing files.
LR-123: Merge into the existing file and strip quotes when reading.
LR-124: Pass the value via stdin and add --repo owner/repo.
LR-125: Install deps first, use npx --no-install wrangler from worker/, align the root devDependency.
LR-126: Remove || true, propagate exit codes, install deps first, poll the port instead of sleep 3.
LR-127: Parse .env with python-dotenv or grep, add a trap to kill background processes.
LR-128: Per-run random CSRF token, validate Host and Origin, random secret_key.
LR-129: Use communicate(timeout) or a Timer, lock around start, per-run queue.
LR-130: Header auth, accept any one LLM key, downgrade validation failure to a warning with Continue anyway.
LR-131: Wrap the whole fetch handler in one try/catch that always builds CORS headers.
LR-132: Clamp limit to 1..100 integers, page on flattened articles, return the all-groups feed when none is given.
LR-133: Reject when GOOGLE_CLIENT_ID is unset and default CORS to deny.
LR-134: Remove the fallback and fail closed when ADMIN_EMAILS is empty.
LR-135: Verify the JWT locally against cached Google JWKS, cache verified sessions briefly, surface DB errors as 5xx.
LR-136: Drop the TTL (cleanup already removes disabled rules) or refresh on read.
LR-137: Wire the OAuth token and Pub/Sub JWT verification or hide the feature.
LR-138: Skip events from the page own id, store a seen-set by comment id, ack first and process in waitUntil.
LR-139: Add the service binding or a local URL to env.local and document running the generation worker locally.
LR-140: Persist only fields that came from KV (read raw, modify, write), never the env-merged view.
LR-141: Split per-feature records into separate keys or D1 rows and write only the changed key.
LR-142: Enforce block and re-review on fingerprint change at publish, or relabel the feature as advisory in the UI.
LR-143: Pass the session user id and reuse stripJsonCodeFences.
LR-144: Compare with datetime(?) or format the bound as YYYY-MM-DD HH:MM:SS; keep usage rows at least 31 days.
LR-145: Add LIMIT and cursor, aggregate usage in one GROUP BY query, prune per tenant incrementally.
LR-146: Skip and report rows without ids, make getRowByTopicId a keyed D1 read with sheet fallback on miss.
LR-147: Backfill from the KV/admin mapping before the swap, preserve topic_key and assert row counts; test on a copy of production data.
LR-148: Wrap sources in delimiters with an untrusted-data instruction, strip non-source URLs, keep a human approval gate before any send.
LR-149: Handle b64_json, set sizes per model, map unsupported aspect ratios; confirm with a live call.
LR-150: Admin-gate or per-user-scope these actions and restrict orgId.
LR-151: Let a per-user save failure fail the callback, drop decodeURIComponent, bind state to a client-side nonce.
LR-152: Escape reserved characters for rest/posts or use ugcPosts consistently; add real alt text.
LR-153: Return partial-delivery info, throw on container-ready timeout, split text by channel limit.
LR-154: Wrap provider fetches with a 60-90 s AbortSignal.timeout mapped to a retryable error and an overall pipeline deadline; cache the model catalog.
LR-155: Return {requested, used, reason} and show it in the UI; honour workspace refs in the newsletter.
LR-156: Use x-goog-api-key for Gemini and headers where the vendor supports them; keep error text free of the URL.
LR-157: Cap bytes with a stream limit, allow-list content types excluding SVG, https-only, verify topic ownership, key objects by userId/.
LR-158: Store a timezone, implement frequency, recompute only on schedule fields, bound cron concurrency, use topic keywords as the query.
LR-159: Validate per channel in publishContent before any upload and show a counter that blocks Approve/Publish above the limit.
LR-160: Cap field lengths, add a KV/IP rate limit, send or remove the email promise, allow budget === 0.
LR-161: Require userId in these payloads or remove the routes, use timing-safe compare and a random per-registration verify token.
LR-162: One docs pass after the P0/P1 fixes; update ARCHITECTURE.md as the spec and add openrouter: [] to the static catalog.
LR-163: Correct the docs to match the shipped behaviour.
LR-164: Prune dead keys, dedupe and fix the stale reference.
LR-165: Defer; low value for release.
LR-166: Catch at the call site since the wrapper already notified the user.
LR-167: Revert state and show a notice in each catch.
LR-168: Build the card object before calling setGeneratedCards and return it.
LR-169: Relabel to Schedule for <time> when in the future, warn when in the past, and use ScheduleEditor in the editor.
LR-170: Add short tooltips.
LR-171: Show a warning notice for failed nodes.
LR-172: Prefer the row text unless the local copy is newer, or drop the shadow copy.
LR-173: Remove the button or wire it.
LR-174: Relabel the sections or use a real signal.
LR-175: Add a visible delete control and a drop confirmation.
LR-176: Verify variables end to end or remove the claim.
LR-177: Use the shared Dialog primitive and run an accessibility pass.
LR-178: Add the asterisk and clarify the tooltip.
LR-179: Defer the split; add one-line section descriptions and validators for Telegram id and similar fields.
LR-180: Hide Setup unless dev/local and align the port.
LR-181: Capture any WORKSPACE_PATHS value.
LR-182: Retry button that re-runs the bootstrap effect; structured error codes.
LR-183: Reuse the existing local toast from SelectionClipper.tsx for success messages.
LR-184: Keep the flag off for release or hide the panel unless VITE_PIPELINE_LIVE_URL is set.
LR-185: Wrap in try/catch and scope stats by spreadsheet if desired.
LR-186: Remove or retarget.
LR-187: Return the plain object { nodes: [...] }.
LR-188: Bind days as a parameter and refuse to suspend admin emails explicitly.
LR-189: Align defaults with the yaml and set videoEpisodes per mode.
LR-190: Treat engine/ as dead until wired; when wired validate variant count and truncate by sentence.
LR-191: Filter by a per-request run id and unsubscribe on every return.
LR-192: Key by the real model id.
LR-193: Update defaults to a current model and surface discovery failure.

## Frozen

Real items that would need a new capability, with the smallest in-scope alternative. Status: frozen. Not counted in open totals.

| ID | Item (source IDs) | Smallest in-scope alternative |
|---|---|---|
| FZ-001 | Sidebar grouping, breadcrumbs from location, sidebar search, command palette, RouteGuard, recently viewed (C01-1, C01-2, C01-3, C01-4, C01-5, C01-6, C01-9, C01-10). | Keep the flat sidebar; fix only labels and the dead tour/pill claims. |
| FZ-002 | Feed redesign: thumbnails, masonry, source dedupe grouping, per-source mute/boost, compose-from-card CTA, search-description toggle, tablet trending carousel (C02-3, C02-5, C02-8, C02-9, C02-11, C02-14, C02-15, C02-17, C02-18). | Ship the current text-only feed; make existing actions touch-visible (see the touch-gap item). |
| FZ-003 | Passage clipping from the stream card, bulk clip select, clip groups, drag-into-editor context blocks (C03-5, C03-7, C03-10, D3-4, D3-6). | Keep passage clipping in the article detail view only. |
| FZ-004 | Article detail redesign: single scrollable stack, lightbox, read-full primary (C03-8, C03-9). | Leave the tab layout as is. |
| FZ-005 | Multi-channel deliveryChannels[] per post and multi-channel chips (C05-10, C07-8). | Document single channel per post; show the channel on the queue row. |
| FZ-006 | Test connection per credential and a connection-health page (C09-6, C05-11, C09-15). | Show getIntegrations status and needs_reauth state on /connections. |
| FZ-007 | Undo-send window (C07-7). | Use the editor publish confirmation instead. |
| FZ-008 | Editor layout redesign: 3 tab groups, 60/40 flip, versions drawer, 2-up compare, selection toggle (C06-1, C06-8, C06-9, C06-10, C06-11). | Leave layout unchanged; add tooltips only. |
| FZ-009 | Newsletter full-page editor, CodeMirror, voice chip, dedicated issue view, subject A/B and segmentation (C08-5, C08-8, C08-9, C08-10, C08-12). | Keep the drawer; fix send safety only. |
| FZ-010 | Variant-pick logging and post-publish rating signals (C11-1, C11-3). | No signal capture this release. |
| FZ-011 | Admin panel search, sort, batch, audit log, CSV (C12-3). | Keep the plain list with error handling. |
| FZ-012 | zod validation of API responses (C13-6). | Hand-written guards on bootstrap and getRows only. |
| FZ-013 | Enrichment DAG page and re-run for standard users, run filters and metrics (C10-4, C10-5, C10-6). | Leave admin-only; show failed nodes in progress panel. |
| FZ-014 | Real per-user Gmail auto-reply and LinkedIn DM automation infrastructure (WKB-031 deeper fix). | Hide the Gmail/LinkedIn automation UI for this release. |

## Rejected or already fixed

- FEA-027 (partly rejected): it claims the main worker does not route /api/clips, but ARCH-AUDIT lists /api/clips and /api/feed routes (worker/src/index.ts:714-717,804-807). The real defect is the unset globalThis.VITE_WORKER_URL, which FEB-002 covers; kept as an alias there and the dead /v1/variants/save part stays valid.
- FEB-026: not wrong, but obsolete once the bypass secret is removed; folded into the bypass item as an alias, not a separate item.
- Existing-review rows with status fixed (for example C02-2, C02-4, C02-7, C03-3, C04-1, C04-3, C04-4, C05-2, C05-3, C05-9, C06-4, C08-1, C08-6, C09-3, C09-8..C09-12, C10-1, C11-2, C13-9, P1/P2 plan tasks) were not re-listed, per the rules.

## Journey coverage

| J-ID | Priority | CORE | Open ledger items (LR-IDs) | Coverage note |
|---|---|---|---|---|
| J-001 | P1 | yes | LR-005, LR-007, LR-008, LR-019, LR-040, LR-041, LR-042, LR-043, LR-046, LR-047, LR-048, LR-079, LR-122, LR-123, LR-125, LR-126, LR-127, LR-128, LR-130, LR-164 |  |
| J-002 | P1 | yes | LR-005, LR-006, LR-008, LR-018, LR-019, LR-020, LR-041, LR-042, LR-043, LR-044, LR-076, LR-077, LR-079, LR-120, LR-121, LR-122, LR-124, LR-125, LR-126 |  |
| J-003 | P1 | yes | LR-008, LR-018, LR-019, LR-020, LR-045, LR-134 |  |
| J-004 | P2 | yes | LR-020, LR-130 |  |
| J-005 | P2 | yes | LR-005, LR-041, LR-047, LR-121, LR-128, LR-129 |  |
| J-006 | P1 | yes | LR-051 |  |
| J-007 | P2 | yes | LR-006, LR-042, LR-044, LR-045, LR-120, LR-123 |  |
| J-008 | P1 | yes | LR-048, LR-121 |  |
| J-009 | P2 | yes | LR-043 |  |
| J-010 | P2 | no | LR-180 |  |
| J-011 | P2 | no | LR-007, LR-008, LR-017, LR-040, LR-126, LR-127, LR-139, LR-162, LR-186 |  |
| J-012 | P2 | no | LR-001, LR-078, LR-123 |  |
| J-013 | P3 | no | LR-017, LR-077, LR-162 | NOT IMPLEMENTED per journey designer |
| J-014 | P3 | no | LR-040, LR-127, LR-186 |  |
| J-015 | P0 | yes | LR-001, LR-009, LR-045, LR-135 |  |
| J-016 | P2 | yes | LR-099 |  |
| J-017 | P0 | yes | LR-009, LR-101, LR-160 |  |
| J-018 | P2 | no | LR-098, LR-160 |  |
| J-019 | P2 | no | LR-100, LR-101, LR-160 |  |
| J-020 | P1 | yes | - | no finding |
| J-021 | P1 | yes | LR-024, LR-105, LR-106, LR-111, LR-135 |  |
| J-022 | P2 | yes | LR-105 |  |
| J-023 | P2 | yes | LR-103, LR-105, LR-110, LR-111, LR-182 |  |
| J-024 | P2 | yes | LR-110 |  |
| J-025 | P3 | no | LR-181 |  |
| J-026 | P2 | yes | LR-033, LR-106 |  |
| J-027 | P1 | yes | LR-001 |  |
| J-028 | P1 | yes | LR-133 |  |
| J-029 | P1 | yes | LR-015, LR-030, LR-072, LR-177 |  |
| J-030 | P1 | yes | LR-015, LR-030, LR-096 |  |
| J-031 | P0 | yes | LR-072 |  |
| J-032 | P1 | yes | LR-096 |  |
| J-033 | P2 | yes | - | no finding |
| J-034 | P2 | yes | - | no finding |
| J-035 | P1 | yes | LR-023, LR-025, LR-055, LR-167, LR-178, LR-183 |  |
| J-036 | P2 | yes | LR-060 |  |
| J-037 | P2 | yes | LR-023, LR-025 |  |
| J-038 | P3 | no | - | no finding |
| J-039 | P1 | yes | LR-072, LR-073, LR-102 |  |
| J-040 | P1 | yes | LR-055, LR-097, LR-104, LR-135, LR-145, LR-146 |  |
| J-041 | P2 | yes | LR-033, LR-039, LR-069, LR-090, LR-091, LR-094, LR-095, LR-117, LR-132, LR-173, LR-174 |  |
| J-042 | P2 | no | LR-028, LR-090, LR-091 |  |
| J-043 | P2 | no | LR-028, LR-090 |  |
| J-044 | P1 | yes | LR-004, LR-027, LR-028, LR-033, LR-069, LR-095, LR-115, LR-117, LR-131, LR-132, LR-145, LR-148, LR-175 |  |
| J-045 | P2 | yes | LR-004, LR-027, LR-028, LR-060, LR-115, LR-172 |  |
| J-046 | P2 | yes | LR-060, LR-092, LR-148 |  |
| J-047 | P1 | yes | LR-060, LR-093 |  |
| J-048 | P2 | yes | LR-060, LR-093 |  |
| J-049 | P3 | no | LR-028, LR-145, LR-167 |  |
| J-050 | P1 | yes | LR-027, LR-131, LR-132 |  |
| J-051 | P2 | no | LR-094, LR-150 |  |
| J-052 | P2 | yes | LR-039, LR-060, LR-065, LR-069, LR-087, LR-118, LR-119, LR-166 |  |
| J-053 | P0 | yes | LR-003, LR-004, LR-016, LR-023, LR-035, LR-036, LR-037, LR-038, LR-039, LR-050, LR-056, LR-060, LR-069, LR-103, LR-112, LR-116, LR-117, LR-118, LR-119, LR-131, LR-148, LR-154, LR-156, LR-171, LR-191 |  |
| J-054 | P1 | yes | LR-056, LR-103, LR-116, LR-131 |  |
| J-055 | P1 | yes | LR-050, LR-056, LR-154 |  |
| J-056 | P1 | yes | LR-023, LR-025, LR-056, LR-146 |  |
| J-057 | P0 | yes | LR-016 |  |
| J-058 | P1 | yes | LR-060, LR-061 |  |
| J-059 | P2 | yes | LR-074, LR-185 |  |
| J-060 | P0 | yes | LR-050 |  |
| J-061 | P2 | no | LR-167, LR-168, LR-190 |  |
| J-062 | P3 | no | LR-112, LR-190 |  |
| J-063 | P0 | yes | LR-003, LR-037, LR-054, LR-083, LR-084, LR-085 |  |
| J-064 | P1 | yes | LR-024, LR-054, LR-081, LR-083, LR-084, LR-089 |  |
| J-065 | P1 | yes | LR-003, LR-057, LR-072, LR-083, LR-087, LR-103, LR-131, LR-154, LR-166 |  |
| J-066 | P2 | yes | LR-057, LR-083, LR-085, LR-087, LR-166, LR-170 |  |
| J-067 | P1 | yes | LR-035, LR-062, LR-083, LR-113, LR-114, LR-152, LR-157 |  |
| J-068 | P2 | no | LR-035, LR-052, LR-060, LR-113, LR-149, LR-192 |  |
| J-069 | P2 | yes | LR-060, LR-142, LR-143, LR-155, LR-166 |  |
| J-070 | P3 | no | LR-086 |  |
| J-071 | P2 | yes | LR-023 |  |
| J-072 | P2 | yes | LR-023 |  |
| J-073 | P2 | yes | - | no finding |
| J-074 | P2 | yes | - | no finding |
| J-075 | P2 | yes | LR-023 |  |
| J-076 | P0 | yes | LR-012, LR-026, LR-037, LR-058, LR-062, LR-070, LR-072, LR-088, LR-097, LR-103, LR-114, LR-142, LR-152, LR-159, LR-163, LR-169, LR-183 |  |
| J-077 | P1 | yes | LR-012, LR-058, LR-062, LR-153, LR-159 |  |
| J-078 | P1 | yes | LR-012, LR-058, LR-059, LR-067, LR-068, LR-159 |  |
| J-079 | P1 | yes | LR-012, LR-058, LR-062, LR-067, LR-108, LR-153, LR-159 |  |
| J-080 | P1 | yes | LR-012, LR-058, LR-062, LR-067, LR-153, LR-159 |  |
| J-081 | P2 | no | LR-052 | NOT IMPLEMENTED per journey designer |
| J-082 | P0 | yes | LR-002, LR-013, LR-031, LR-032, LR-071, LR-072, LR-109, LR-146, LR-161, LR-169 |  |
| J-083 | P0 | yes | LR-002, LR-013, LR-014, LR-102 |  |
| J-084 | P1 | yes | LR-002, LR-032, LR-071 |  |
| J-085 | P1 | yes | LR-014, LR-031, LR-169 |  |
| J-086 | P1 | yes | LR-014, LR-031 |  |
| J-087 | P1 | yes | LR-002, LR-014, LR-031, LR-054, LR-071, LR-102 |  |
| J-088 | P1 | yes | LR-026, LR-032, LR-054, LR-058, LR-070, LR-082, LR-103, LR-104 |  |
| J-089 | P1 | yes | LR-070, LR-082, LR-104 |  |
| J-090 | P1 | yes | LR-012, LR-068 |  |
| J-091 | P2 | yes | LR-054, LR-070, LR-082, LR-083, LR-104, LR-178 |  |
| J-092 | P2 | yes | LR-013, LR-014, LR-070 |  |
| J-093 | P2 | yes | - | no finding |
| J-094 | P1 | yes | LR-012, LR-021, LR-034, LR-107, LR-141, LR-151 |  |
| J-095 | P1 | yes | LR-012, LR-034, LR-107, LR-151 |  |
| J-096 | P1 | yes | LR-012, LR-034, LR-068, LR-107, LR-141, LR-151 |  |
| J-097 | P2 | no | LR-034, LR-052, LR-068, LR-107 |  |
| J-098 | P2 | yes | LR-034, LR-107, LR-151 |  |
| J-099 | P2 | yes | LR-034, LR-107, LR-108 |  |
| J-100 | P2 | yes | LR-151 |  |
| J-101 | P1 | yes | LR-021 |  |
| J-102 | P1 | yes | LR-109, LR-141 |  |
| J-103 | P0 | yes | LR-012, LR-013, LR-059, LR-067 |  |
| J-104 | P2 | yes | - | no finding |
| J-105 | P2 | yes | LR-006, LR-068, LR-141 |  |
| J-106 | P2 | no | LR-080, LR-163, LR-165 |  |
| J-107 | P2 | no | LR-022 |  |
| J-108 | P2 | no | LR-080 |  |
| J-109 | P2 | no | LR-010, LR-029, LR-060, LR-064, LR-065, LR-148, LR-158, LR-176 |  |
| J-110 | P2 | no | LR-010, LR-011, LR-029, LR-063, LR-064, LR-065, LR-066 |  |
| J-111 | P1 | no | LR-011, LR-053, LR-063, LR-064, LR-066, LR-158 |  |
| J-112 | P0 | yes | LR-010, LR-063 |  |
| J-113 | P2 | no | LR-052, LR-171, LR-187, LR-190, LR-191 |  |
| J-114 | P2 | no | LR-049, LR-136, LR-137, LR-138 |  |
| J-115 | P2 | no | LR-138, LR-161 |  |
| J-116 | P1 | no | LR-137 |  |
| J-117 | P2 | no | LR-137, LR-161 |  |
| J-118 | P2 | no | LR-049, LR-075, LR-136 | NOT IMPLEMENTED per journey designer |
| J-119 | P3 | no | LR-053, LR-145 |  |
| J-120 | P2 | yes | LR-052, LR-179 |  |
| J-121 | P2 | yes | LR-155, LR-193 |  |
| J-122 | P1 | yes | LR-038, LR-154, LR-155, LR-193 |  |
| J-123 | P1 | yes | LR-100, LR-145, LR-160, LR-188 |  |
| J-124 | P2 | no | LR-061, LR-143, LR-144, LR-188, LR-192 |  |
| J-125 | P1 | yes | LR-060, LR-061, LR-105, LR-111, LR-144 |  |
| J-126 | P1 | yes | LR-051, LR-060, LR-061 |  |
| J-127 | P0 | yes | LR-134 |  |
| J-128 | P1 | yes | - | no finding |
| J-129 | P1 | yes | LR-055, LR-146 |  |
| J-130 | P2 | yes | LR-055 |  |
| J-131 | P1 | yes | LR-017, LR-049, LR-133 |  |
| J-132 | P1 | yes | LR-006, LR-140 |  |
| J-133 | P1 | yes | - | no finding |
| J-134 | P1 | yes | LR-046 |  |
| J-135 | P1 | yes | LR-133 |  |
| J-136 | P0 | yes | LR-001, LR-078 |  |
| J-137 | P1 | yes | LR-147 |  |
| J-138 | P2 | yes | LR-147 |  |
| J-139 | P3 | no | LR-189 |  |
| J-140 | P0 | yes | LR-004, LR-009, LR-010, LR-012, LR-013, LR-015, LR-016, LR-033, LR-071, LR-073, LR-074, LR-140, LR-147 |  |
| J-141 | P2 | yes | LR-015, LR-074 |  |
| J-142 | P1 | yes | LR-004, LR-033, LR-074 |  |
| J-143 | P2 | yes | LR-073, LR-157 |  |
| J-144 | P2 | no | LR-071, LR-161 |  |
| J-145 | P1 | yes | LR-048, LR-050, LR-076, LR-135 |  |
| J-146 | P3 | no | LR-184 |  |

## Verification log

Not executed in this pass.

| LR-ID | Repro | Executed by | Result |
|---|---|---|---|
| | | | |

## Notes

- Severity conflicts between reviewers and the journey designer: J-127 (owner is admin when ADMIN_EMAILS is empty) is rated P0 by the journey designer but ARCH-012 is P2; J-060 (open generation worker) is P0 but ARCH-003 and GWP-003 are P1; J-031 is P0 but FEB-003 is a P1 hypothesis; J-116 is P1 but WKB-031 is P2. The ledger follows the finding Sev and the owner may want to raise the three tenancy/admin ones.
- Hypothesis policy: items titled (hypothesis) are tagged Confidence: hypothesis. WKB-022 was downgraded P1 to P2 because it rests on LinkedIn API behaviour not visible in the repo. WKB-013 stays P1 but is tagged hypothesis (Gemini response shape). FEB-003 was merged with the confirmed WKA-009 and kept confirmed-by-reading.
- FEB-002 says FeedPage calls the broken getClipsPage/createClipPage URLs (live), while FEA-027 calls the same code dead. Both point at the same lines (backendApi.ts:827-890); the ledger treats it as live because worker routes /api/clips exist. An executor should confirm which calls FeedPage actually makes.
- WKA-037 (lifecycle bus leaks node events between SSE streams) conflicts with WKB-044 (the workflow engine is never run, so no events fire). Kept as P3 hypothesis.
- WKA-009 says D1-only tenants can add a topic, but FEB-003 says the frontend blocks every route for a non-admin without a spreadsheet. Merged; the frontend wall likely makes the D1-only path unreachable from the UI.
- ARCH-002 caveat: not confirmed whether an earlier migration sets a different default for users.status on a fresh table. Evidence lines are consistent with the claim, so confidence is confirmed-by-reading.
- GWP-002 is P0 per the raw source but exploitation needs the shared secret (or the empty-secret bypass, ARCH-003); if the secret is guaranteed set, treat as P1.
- Existing-review items carry the CEO assigned Sev (the source used HIGH/MED). Rows with status unverified or n-a were not included: unverified examples C01-7, C01-8, C02-6 partial only, C03-11, C04-7, C08-3, C08-4, U-J1.1..U-J1.4, U-J2-5, U-J7, U-J10, D2-1..D2-5. An executor should verify these (especially C03-11 AI analysis cache, U-J7 alarms, U-J1.2 D1 fallback) before launch.
- Merge decisions: SET-001 stays separate from SET-002..004 (bind and leak versus request-body trust). ARCH-012 is split across three items (committed local secret, hard-coded admin, committed owner ids) and appears as an alias on each. WKB-011 and WKA-003 appear on both the silent-exit item and the idempotency item. GWP-002 stays separate from GWP-001 (generation-worker identity versus main-worker payload spread).
- Counts: 193 merged open items from 224 distinct raw IDs; every raw ID in the seven raw files appears as an alias at least once (script-checked, missing: none). Frozen entries are not included in the open counts.
- Not resolved: whether the DO alarm retry actually has a cap on this runtime (ARCH-010 hypothesis), whether production D1 data pre-dates migration 0010 (WKA-027), and whether the frontend renders newsletter HTML unsandboxed (WKB-015 XSS severity).
