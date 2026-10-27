# Test coverage map — P0/P1 CORE journeys

Read-only. Built by grepping the test files and reading their test titles; no test was run. Test inventory: worker/src (auth.test.ts, automations/cleanup.test.ts, a few workflow/newsletter/waitlist unit tests), frontend/src (11 component/hook tests), frontend/tests/e2e (Playwright, worker mocked through helpers/mockApi.ts unless noted), tests-e2e/e2e (older copy of the same suite; not the one frontend/playwright.config.ts runs), tests/ and setup/ (Python), generation-worker (3 player unit tests plus tests/smoke.spec.ts).

How to read the table: **covered** means a test asserts the user-visible pass check; **partial** means a test asserts only part of it (named in the cell); **none** means no test asserts it, and each of those has a TST item below. A mocked Playwright test proves the UI reacts to a canned reply, not that the worker does the right thing, so server-side pass checks are not counted as covered by it. Several e2e cases call test.skip when the target button is absent, so a green run can mean not exercised. The 'Confidence' column is how sure I am about the row, from the greps.

Totals: 70 P0/P1 CORE journeys checked; covered 9, partial 24, none 37. Of the 15 P0 journeys, 10 have no covering test.

Discounted evidence: the tests-e2e/e2e/journeys/*-wiring-loop*.spec.ts files (about 50 files) call page.evaluate(fetch) against a mocked route set up by setupApiMocks and then assert on the mock's own reply (for example findDebateArticle, fetchDraftImages, newsletter.approveIssue, publishContent deliveryMode 'queued'), so they do not exercise worker code and were not counted as coverage. Other gaps noted while mapping: worker/src has no test for publishContent, scheduling (Durable Object alarm), tenancy scoping, CORS, OAuth callbacks or the generation routes; tests/smoke.test.ts asserts `true`; frontend/tests/e2e/scheduling.spec.ts 'should handle timezone considerations' has no assertion; tests-e2e/e2e duplicates frontend/tests/e2e with drift (cloud.spec.ts and feed-page.spec.ts exist only in the frontend copy).

| J-ID | Priority | Test files that cover it | Coverage | Confidence |
|---|---|---|---|---|
| J-001 | P1 | setup/wizard/tests/test_flow_happy.py (Flask client, mocked subprocess) | covered | medium |
| J-002 | P1 | none | none | high |
| J-003 | P1 | none | none | high |
| J-006 | P1 | setup/wizard/tests/test_mode.py, tests/wizard/test_mode.py, tests/scripts/test_generate_features.py, frontend/tests/e2e/setup/wizard-deployment-mode.spec.ts | covered | high |
| J-008 | P1 | tests/setup/test_verification.py, setup/wizard/tests/test_verify.py (header parsing and backend marker only; no live probe, no 204 CORS echo assertion) | partial | low |
| J-015 | P0 | frontend/tests/e2e/journeys/01-auth-onboarding.spec.ts (dev bypass login, mocked bootstrap; D1 users row not asserted) | partial | low |
| J-017 | P0 | none | none | high |
| J-020 | P1 | worker/src/auth.test.ts (checkUserAccess suspended only; bootstrap message and the suspended screen not asserted) | partial | low |
| J-021 | P1 | frontend/tests/e2e/integration/error-states.spec.ts (mock 401 shows sign-in; the real HTTP 400 text and the session-expired message are not asserted) | partial | low |
| J-027 | P1 | frontend/tests/e2e/journeys/16-admin-panel.spec.ts, frontend/tests/e2e/journeys/17-navigation-deep-links.spec.ts (UI redirect and hidden links; server-side 403 not asserted) | partial | low |
| J-028 | P1 | none | none | high |
| J-029 | P1 | frontend/tests/e2e/journeys/01-auth-onboarding.spec.ts, frontend/tests/e2e/onboarding.spec.ts (modal, skip; completeOnboarding and redirect to /connections not asserted) | partial | low |
| J-030 | P1 | none | none | high |
| J-031 | P0 | none | none | high |
| J-032 | P1 | frontend/tests/e2e/connections.spec.ts (sheet section and accessible status via mocked getSpreadsheetStatus; connectSpreadsheet not asserted) | partial | low |
| J-035 | P1 | frontend/tests/e2e/add-topic.spec.ts, frontend/tests/e2e/journeys/02-create-topic.spec.ts (addTopic fires, navigates, error shown; mocked worker, D1 row and validation errors not asserted) | partial | low |
| J-039 | P1 | none | none | high |
| J-040 | P1 | none | none | high |
| J-044 | P1 | frontend/tests/e2e/feed-page.spec.ts (clip click fires createClip REST call; validation and per-user listing not asserted) | partial | low |
| J-047 | P1 | none | none | high |
| J-050 | P1 | none | none | high |
| J-053 | P0 | frontend/tests/e2e/journeys/03-generate-draft.spec.ts (mocked SSE progress, variants, saveDraftVariants), generation-worker/tests/smoke.spec.ts (live /v1/generate, needs keys) | covered | medium |
| J-054 | P1 | frontend/tests/e2e/integration/error-states.spec.ts (SSE error does not crash; truncated stream and invalid-response message not asserted) | partial | low |
| J-055 | P1 | frontend/tests/e2e/integration/error-states.spec.ts (generation HTTP 500 does not crash; 502 text not asserted) | partial | low |
| J-056 | P1 | none | none | high |
| J-057 | P0 | none | none | high |
| J-058 | P1 | none | none | high |
| J-060 | P0 | none | none | high |
| J-063 | P0 | frontend/tests/e2e/journeys/04-review-edit.spec.ts, frontend/tests/e2e/journeys/17-navigation-deep-links.spec.ts | covered | medium |
| J-064 | P1 | frontend/tests/e2e/journeys/04-review-edit.spec.ts (undo/redo, typing); survival across navigation not asserted | covered | medium |
| J-065 | P1 | frontend/tests/e2e/journeys/04-review-edit.spec.ts (Quick Change preview and apply, mocked); error events not asserted | covered | low |
| J-067 | P1 | none | none | high |
| J-076 | P0 | frontend/tests/e2e/journeys/05-publish-linkedin.spec.ts (publishContent channel:linkedin, success alert; several cases test.skip when button absent), frontend/tests/e2e/journeys/20-full-lifecycle.spec.ts | covered | low |
| J-077 | P1 | frontend/tests/e2e/journeys/06-publish-channels.spec.ts (payload includes imageUrls; 'requires a selected image' not asserted) | partial | low |
| J-078 | P1 | frontend/tests/e2e/journeys/06-publish-channels.spec.ts (Email fields, saveEmailFields; send and empty-To notice not asserted) | partial | low |
| J-079 | P1 | none | none | high |
| J-080 | P1 | frontend/tests/e2e/journeys/07-connections-setup.spec.ts (verifyTelegramChat valid/invalid; actual publish to Telegram not asserted) | partial | low |
| J-082 | P0 | frontend/tests/e2e/journeys/11-scheduled-publish.spec.ts (updatePostSchedule, queued alert; cases test.skip when UI absent) | covered | low |
| J-083 | P0 | none | none | high |
| J-084 | P1 | frontend/tests/e2e/journeys/11-scheduled-publish.spec.ts (UI fires cancelScheduledPublish, mocked; Durable Object cancel not asserted) | partial | low |
| J-085 | P1 | none | none | high |
| J-086 | P1 | none | none | high |
| J-087 | P1 | none | none | high |
| J-088 | P1 | none | none | high |
| J-089 | P1 | none | none | high |
| J-090 | P1 | frontend/tests/e2e/integration/error-states.spec.ts (publishContent failure shows error), frontend/tests/e2e/connections.spec.ts (Reconnect button for needs-reauth) | partial | low |
| J-094 | P1 | frontend/tests/e2e/journeys/07-connections-setup.spec.ts (Connect triggers startLinkedInAuth; popup, callback, social_integrations row not asserted) | partial | low |
| J-095 | P1 | frontend/tests/e2e/journeys/07-connections-setup.spec.ts (Connect triggers startInstagramAuth; callback not asserted) | partial | low |
| J-096 | P1 | frontend/tests/e2e/journeys/07-connections-setup.spec.ts, frontend/tests/e2e/journeys/06-publish-channels.spec.ts (Connect triggers startGmailAuth; access_type=offline not asserted) | partial | low |
| J-101 | P1 | none | none | high |
| J-102 | P1 | frontend/tests/e2e/journeys/07-connections-setup.spec.ts (Disconnect calls deleteIntegration; publish-after-disconnect not asserted) | partial | low |
| J-103 | P0 | none | none | high |
| J-112 | P0 | none | none | high |
| J-122 | P1 | none | none | high |
| J-123 | P1 | frontend/tests/e2e/journeys/16-admin-panel.spec.ts (approve, suspend, budget vs usage display; budget update validation not asserted) | covered | medium |
| J-125 | P1 | worker/src/auth.test.ts (checkTokenBudget allowed:false at/over budget), frontend/tests/e2e/journeys/19-token-usage.spec.ts (over-quota meter renders); HTTP 429 and UI message not asserted | partial | low |
| J-126 | P1 | worker/src/auth.test.ts (selfHosted mode returns Infinity budget when mode is passed explicitly; the unset-DEPLOYMENT_MODE default is not asserted) | partial | low |
| J-127 | P0 | none | none | high |
| J-128 | P1 | worker/src/auth.test.ts (checkUserAccess suspended); mid-session action and stream paths not asserted | partial | low |
| J-129 | P1 | none | none | high |
| J-131 | P1 | none | none | high |
| J-132 | P1 | none | none | high |
| J-133 | P1 | none | none | high |
| J-134 | P1 | none | none | high |
| J-135 | P1 | none | none | high |
| J-136 | P0 | none | none | high |
| J-137 | P1 | none | none | high |
| J-140 | P0 | none | none | high |
| J-142 | P1 | none | none | high |
| J-145 | P1 | generation-worker/tests/smoke.spec.ts (GET /v1/patterns without the bearer secret; main worker health and the authenticated call not asserted) | partial | low |

## Journeys with no covering test

### TST-001 P1 First-run, setup and install - No automated test asserts: Headless full bootstrap with `python setup.py --all`
- **Journeys:** J-002
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'setup.py --all|exit code|GENERATION_WORKER_URL'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned 2 file(s): setup/tests/test_cli.py, tests/test_mutation_tester.py. None of these asserts the pass check (they match the term in an unrelated assertion or a mock).
- **Repro:** Exit code 0; `GET {WORKER_URL}/` returns `{"ok":true,"data":{"status":"ok","backend":"cloudflare-worker"}}`; the main worker `GENERATION_WORKER_URL` var points at the generation worker URL.
- **Fix hint:** add a test that asserts: run the --all pipeline with subprocess and network mocked and assert exit code 0 and the GENERATION_WORKER_URL var written. Test file suggestion: tests/setup/test_cli.py

### TST-002 P1 First-run, setup and install - No automated test asserts: Fresh Cloudflare account against the committed wrangler ids
- **Journeys:** J-003
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'wrangler.jsonc|ALLOWED_EMAILS|ADMIN_EMAILS'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned 6 file(s): setup/wizard/tests/test_verify.py, setup/wizard/steps/test_verify.py, tests/setup/test_setup_wiring.py, tests/wizard/test_verify.py, tests/test_wrangler_reload_fix.py. None of these asserts the pass check (they match the term in an unrelated assertion or a mock).
- **Repro:** After setup, `worker/wrangler.jsonc` `d1_databases[0].database_id` equals an id returned by `npx wrangler d1 list` for the operator's account, and `ADMIN_EMAILS` / `ALLOWED_EMAILS` contain the operator's email, not the owner's.
- **Fix hint:** add a test that asserts: assert wrangler.jsonc d1 database_id and ADMIN_EMAILS/ALLOWED_EMAILS are rewritten to the operator's values. Test file suggestion: tests/setup/test_worker_config.py

### TST-003 P0 Sign-in and session - No automated test asserts: Non-approved Google account signs in
- **Journeys:** J-017
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'Access not granted|Request access at the homepage'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned no files. No test touches this journey.
- **Repro:** Desired: Step 3 returns `{"ok":false,"error":"Access not granted. Request access at the homepage."}` and no `users` row with `status='active'` is created. (Currently expected to FAIL: bootstrap returns a session.)
- **Fix hint:** add a test that asserts: bootstrap with a Google email that is not approved returns 'Access not granted' and writes no active users row. Test file suggestion: worker/src/index.bootstrap.test.ts

### TST-004 P1 Sign-in and session - No automated test asserts: Worker without `GOOGLE_CLIENT_ID` accepts tokens minted for other apps
- **Journeys:** J-028
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'audience does not match|GOOGLE_CLIENT_ID'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned 5 file(s): setup/tests/test_github_bugfix.py, setup/wizard/tests/test_google.py, tests/setup/test_github.py, tests-e2e/e2e/journeys/22-wiring-issues-round1.spec.ts, tests-e2e/e2e/setup-flow.spec.ts. None of these asserts the pass check (they match the term in an unrelated assertion or a mock).
- **Repro:** Desired: `Unauthorized: Google token audience does not match this app.` or a startup refusal. CODE-READING FINDING: the audience check is `if (env.GOOGLE_CLIENT_ID && tokenInfo.aud !== env.GOOGLE_CLIENT_ID)`, so with the variable unset the check is skipped and token verification relies on Google tokeninfo only. Combined with J-017 any Google user gets in.
- **Fix hint:** add a test that asserts: verifySession with GOOGLE_CLIENT_ID unset rejects a token whose aud is another app. Test file suggestion: worker/src/auth.test.ts

### TST-005 P1 Onboarding and workspace connection - No automated test asserts: Onboarding with a sheet URL (Drive consent and share)
- **Journeys:** J-030
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'connectSpreadsheet|spreadsheet_id|completeOnboarding'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned no files. No test touches this journey.
- **Repro:** Step 3 returns `{"ok":true,"title":"<sheet title>"}` and D1 `users.spreadsheet_id=<ID>`. Failure cases: CODE-READING FINDING: `handleCompleteOnboarding` catches any error, logs to console only, still calls `completeOnboarding`, and redirects to `/connections`; the user never sees why the sheet was not connected.
- **Fix hint:** add a test that asserts: connect a sheet during onboarding, assert users.spreadsheet_id is set and a failure is shown to the user. Test file suggestion: tests-e2e style: frontend/tests/e2e/journeys/01-auth-onboarding.spec.ts plus worker/src/onboarding.test.ts

### TST-006 P0 Onboarding and workspace connection - No automated test asserts: Non-admin without a connected sheet is locked out of the whole workspace
- **Journeys:** J-031
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'Workspace setup pending'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned no files. No test touches this journey.
- **Repro:** Desired: A sheetless user can reach `/connections`, connect a sheet, and use the app (or the app works D1-only). Currently expected to FAIL: the user sees only "Workspace setup pending".
- **Fix hint:** add a test that asserts: a non-admin with no sheet can reach /connections and use the app. Test file suggestion: frontend/tests/e2e/journeys/01-auth-onboarding.spec.ts

### TST-007 P1 Topic capture and scratchpad - No automated test asserts: Delete a topic (and its generated images)
- **Journeys:** J-039
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'deleteRow|deleteTopic'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned no files. No test touches this journey.
- **Repro:** D1 `pipeline_state` row and news snapshots removed, GCS objects for the topic prefix removed, sheet row removed. Order in code is: GCS delete, then D1 delete in parallel with snapshot delete, then `sheets.deleteRow` last; a Sheets failure leaves the D1 row gone but the sheet row present, and the next merge may resurrect it (CODE-READING FINDING). No soft-delete / undo.
- **Fix hint:** add a test that asserts: deleteRow removes the D1 row, snapshots, GCS objects and the sheet row, and reports a Sheets failure. Test file suggestion: worker/src/topics.test.ts

### TST-008 P1 Topic capture and scratchpad - No automated test asserts: Topic list merges Sheets and D1
- **Journeys:** J-040
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'Sheets merge failed|mergeRows|merged-rows'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned no files. No test touches this journey.
- **Repro:** New sheet row appears after reload with `topicId` assigned; counts per status match; no duplicate rows for topics that exist in both stores.
- **Fix hint:** add a test that asserts: getRows merges Sheets and D1 with no duplicates and correct status counts. Test file suggestion: worker/src/topics.test.ts

### TST-009 P1 Feed and clipping - No automated test asserts: "Debate mode" returns an invented opposing article
- **Journeys:** J-047
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'findDebateArticle|Debate'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned 15 file(s): tests-e2e/e2e/journeys/65-wiring-loop40.spec.ts, tests-e2e/e2e/journeys/51-wiring-loop30.spec.ts, tests-e2e/e2e/journeys/62-wiring-loop36.spec.ts, tests-e2e/e2e/journeys/57-wiring-loop33.spec.ts, tests-e2e/e2e/journeys/65-wiring-loop43.spec.ts. None of these asserts the pass check (they match the term in an unrelated assertion or a mock).
- **Repro:** CODE-READING FINDING: the prompt says "Generate a realistic opposing article ... Plausible publication name (e.g. Harvard Business Review)". The result is fabricated (title, source, summary) and the UI offers "Clip". Pass requires that the UI visibly labels it AI-generated / not a real article and that clipping does not save a fake URL as a source. A user quoting it on LinkedIn would publish a false citation.
- **Fix hint:** add a test that asserts: the debate-mode article is labelled AI-generated and cannot be clipped as a real article. Test file suggestion: frontend/tests/e2e/journeys/12-feed-feature.spec.ts

### TST-010 P1 Feed and clipping - No automated test asserts: REST feed and clip endpoints require auth
- **Journeys:** J-050
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'api/feed/items|api/clips|Unauthorized'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned 6 file(s): frontend/tests/e2e/integration/error-states.spec.ts, frontend/tests/e2e/feed-page.spec.ts, tests/setup/test_github.py, tests/wizard/test_apikeys.py, tests/automations/test_youtube_poller.py. None of these asserts the pass check (they match the term in an unrelated assertion or a mock).
- **Repro:** Step 1 HTTP 401 `Unauthorized`; step 2 200 with only the caller's data (`interest_group_id` filtered by `user_id`); bad bodies get 4xx. Note the feed SELECT filters `news_snapshots` by `spreadsheet_id` (shared sheet = shared snapshots, see J-141).
- **Fix hint:** add a test that asserts: /api/feed and /api/clips return 401 without a token and only the caller's rows with one. Test file suggestion: worker/src/feed-routes.test.ts

### TST-011 P1 Draft generation (SSE) - No automated test asserts: "Send to Generation" button on a saved Draft topic
- **Journeys:** J-056
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'sendTopicToGeneration|Send to Generation'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned no files. No test touches this journey.
- **Repro:** Desired: Row moves Draft -> Pending -> has 4 variants and the UI shows them on `/topics/:topicId`. Currently expected to FAIL.
- **Fix hint:** add a test that asserts: Send to Generation moves a Draft topic to Pending and shows 4 variants. Test file suggestion: frontend/tests/e2e/journeys/03-generate-draft.spec.ts

### TST-012 P0 Draft generation (SSE) - No automated test asserts: Client-supplied `spreadsheetId` overrides the server's in generation
- **Journeys:** J-057
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'storedConfig|spreadsheetId override'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned no files. No test touches this journey.
- **Repro:** Desired: server ignores client `spreadsheetId` and uses `storedConfig.spreadsheetId`. CODE-READING FINDING: both handlers build `{ spreadsheetId: storedConfig.spreadsheetId, ...payload }`, so the client value wins (spread order). Check which downstream reads/writes in generation-worker use `spreadsheetId` (feedback, variants/clips by session, LLM settings keyed by spreadsheet) and whether B's data can be read or p...
- **Fix hint:** add a test that asserts: a client-supplied spreadsheetId is ignored in favour of the stored one. Test file suggestion: worker/src/generation-routes.test.ts

### TST-013 P1 Draft generation (SSE) - No automated test asserts: Streaming generation bypasses the monthly token budget
- **Journeys:** J-058
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'checkTokenBudget|Monthly token budget exceeded|429'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned 2 file(s): worker/src/auth.test.ts, setup/wizard/tests/test_apikeys.py. None of these asserts the pass check (they match the term in an unrelated assertion or a mock).
- **Repro:** Desired: 429-style refusal on both. CODE-READING FINDING: `/api/quickchange/stream`, `generateQuickChange`, `generateVariantsPreview` and `callGenerationWorker` call `checkTokenBudget`; `/api/generate/stream` does not. Also `analyzeTopicInsights`, `analyzeFeedArticle`, `extractArticleInsights`, `clusterDraftClips`, `findDraftConnections`, `findDebateArticle`, `crossDomainInsight`, `opinionLeaderInsights`, `generat...
- **Fix hint:** add a test that asserts: POST /api/generate/stream refuses with 429 when the monthly budget is exhausted. Test file suggestion: worker/src/generation-routes.test.ts

### TST-014 P0 Draft generation (SSE) - No automated test asserts: Generation worker is open when `WORKER_SHARED_SECRET` is empty
- **Journeys:** J-060
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'WORKER_SHARED_SECRET|checkAuth'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned 2 file(s): setup/wizard/tests/test_apikeys.py, tests/setup/test_setup_wiring.py. None of these asserts the pass check (they match the term in an unrelated assertion or a mock).
- **Repro:** Desired: 401 `{"error":"Unauthorized"}`. CODE-READING FINDING: `checkAuth` returns `true` when the secret is empty, and CORS is `Access-Control-Allow-Origin: *`; anyone can run the LLM pipeline on the operator's keys. The setup path generates the secret, but a manual deploy or a skipped secret leaves it open with no warning. Also, `Authorization` is compared as `Bearer <secret>` or the bare secret (string `===`, n...
- **Fix hint:** add a test that asserts: checkAuth rejects requests when WORKER_SHARED_SECRET is empty. Test file suggestion: generation-worker/src/auth.test.ts

### TST-015 P1 Review, edit, variants and images - No automated test asserts: Pick and upload images for a post
- **Journeys:** J-067
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'uploadDraftImage|Only image uploads|fetchDraftImages'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned 4 file(s): tests-e2e/e2e/journeys/47-wiring-loop28.spec.ts, tests-e2e/e2e/journeys/60-wiring-loop35.spec.ts, tests-e2e/e2e/journeys/39-wiring-loop25.spec.ts, tests-e2e/e2e/journeys/48-wiring-loop29.spec.ts. None of these asserts the pass check (they match the term in an unrelated assertion or a mock).
- **Repro:** Search returns at most 8 URLs; upload returns `{imageUrl}` pointing into the bucket; non-image -> `Only image uploads are supported.`; missing `topicId` -> `topicId is required to upload an image.` No explicit size cap in `uploadDraftImage` (CODE-READING FINDING: only the Worker request limit applies; check behaviour and message for a 20 MB image). Selected URLs end up in `selected_image_urls_json`.
- **Fix hint:** add a test that asserts: image search returns at most 8 URLs and non-image or missing-topicId uploads give the documented errors. Test file suggestion: frontend/tests/e2e/journeys/04-review-edit.spec.ts

### TST-016 P1 Scheduling and publishing - No automated test asserts: Send via WhatsApp
- **Journeys:** J-079
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'WhatsApp|wamid'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned 24 file(s): frontend/tests/e2e/add-topic.spec.ts, frontend/tests/e2e/connections.spec.ts, frontend/tests/e2e/journeys/07-connections-setup.spec.ts, frontend/tests/e2e/journeys/18-channel-previews.spec.ts, frontend/tests/e2e/journeys/06-publish-channels.spec.ts. None of these asserts the pass check (they match the term in an unrelated assertion or a mock).
- **Repro:** `messageId` = wamid; invalid number -> normalizer error; the code sends non-template messages ("Send non-template WhatsApp messages through Meta Cloud API"), which Meta rejects outside the customer service window: the error text from Meta must reach the user.
- **Fix hint:** add a test that asserts: a WhatsApp send returns a wamid, and invalid numbers or Meta errors reach the user. Test file suggestion: worker/src/channels/whatsapp.test.ts

### TST-017 P0 Scheduling and publishing - No automated test asserts: Alarm fires: what the scheduled run actually executes
- **Journeys:** J-083
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'executeScheduledPublish|armScheduledPublish|alarm'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned 2 file(s): tests-e2e/e2e/journeys/40-wiring-loop26.spec.ts, tests-e2e/e2e/journeys/69-wiring-loop50.spec.ts. None of these asserts the pass check (they match the term in an unrelated assertion or a mock).
- **Repro:** At the scheduled time the post appears on the right account, D1 row `status='Published'`. Currently expected to FAIL for multi-tenant (non-admin or non-KV-sheet) users; for the single-owner self-hosted deployment (admin sheet == KV sheet, global LinkedIn token) it likely works. A row that stays `Approved` after the time with no log line is the symptom.
- **Fix hint:** add a test that asserts: when the Durable Object alarm fires, executeScheduledPublish posts to the right account and sets status Published. Test file suggestion: worker/src/scheduling.test.ts

### TST-018 P1 Scheduling and publishing - No automated test asserts: Schedule in the past
- **Journeys:** J-085
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'scheduledAt|past slot|Schedule in the past'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned 3 file(s): frontend/tests/e2e/journeys/11-scheduled-publish.spec.ts, tests-e2e/e2e/journeys/11-scheduled-publish.spec.ts, tests-e2e/e2e/journeys/69-wiring-loop50.spec.ts. None of these asserts the pass check (they match the term in an unrelated assertion or a mock).
- **Repro:** UI blocks or warns on a past slot. API: because the arm branch requires `scheduledAt > Date.now() + 60000`, a past or near-now `postTime` is NOT queued: the call publishes immediately and returns `deliveryMode:"sent"`. The user who typed a past time must be told this will publish now before they confirm.
- **Fix hint:** add a test that asserts: a postTime in the past (or within 60s) publishes now and the UI warns before confirming. Test file suggestion: worker/src/scheduling.test.ts

### TST-019 P1 Scheduling and publishing - No automated test asserts: Timezone semantics of a scheduled time
- **Journeys:** J-086
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'timezone|UTC'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned 2 file(s): frontend/tests/e2e/scheduling.spec.ts, tests-e2e/e2e/scheduling.spec.ts. None of these asserts the pass check (they match the term in an unrelated assertion or a mock).
- **Repro:** Desired: fires at 09:30 local. CODE-READING FINDING: the string is interpreted as UTC, so a UTC+5:30 user's 09:30 post fires at 15:00 local; a UTC-8 user's fires 8 h early (and a "future" local time may be already "in the past" in UTC, see J-085). The same applies to the DO check `row.postTime === task.scheduledTime`. No timezone is stored with the row.
- **Fix hint:** add a test that asserts: a local 09:30 schedule fires at 09:30 local, not UTC. Test file suggestion: worker/src/scheduling.test.ts

### TST-020 P1 Scheduling and publishing - No automated test asserts: Calendar drag-reschedule of an already queued post
- **Journeys:** J-087
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'updatePostSchedule|reschedul|drag'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned 7 file(s): frontend/tests/e2e/journeys/11-scheduled-publish.spec.ts, frontend/tests/e2e/journeys/13-enrichment-pipeline.spec.ts, tests-e2e/e2e/journeys/11-scheduled-publish.spec.ts, tests-e2e/e2e/journeys/13-enrichment-pipeline.spec.ts, tests-e2e/e2e/journeys/69-wiring-loop50.spec.ts. None of these asserts the pass check (they match the term in an unrelated assertion or a mock).
- **Repro:** Desired: post fires at the new time only. CODE-READING FINDING: `updatePostSchedule` only updates the row's `postTime`; nothing re-arms a Durable Object (`armScheduledPublish` is called only from `publishContent`). At the old time the DO runs `executeScheduledPublish`, sees `row.postTime != task.scheduledTime` and silently returns; no DO exists for the new time, so the post never fires. Errors in the drag handler...
- **Fix hint:** add a test that asserts: updatePostSchedule re-arms the Durable Object so the post fires only at the new time. Test file suggestion: worker/src/scheduling.test.ts

### TST-021 P1 Scheduling and publishing - No automated test asserts: Double-click on Publish
- **Journeys:** J-088
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'double-click|actionLoading|idempotency'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned 1 file(s): setup/wizard/test_state.py. None of these asserts the pass check (they match the term in an unrelated assertion or a mock).
- **Repro:** Exactly one post on LinkedIn. UI guard: `if (actionLoading !== null) return;` is React state, so two clicks in one tick may both pass; server guard: `publishContent` has no idempotency key and no "already Published" check for the immediate path (only `executeScheduledPublish` checks status). Expect two posts for the parallel curl (CODE-READING FINDING). A second click after completion goes through the "Republish"...
- **Fix hint:** add a test that asserts: two rapid clicks on Publish send exactly one publishContent call and one LinkedIn post. Test file suggestion: frontend/tests/e2e/journeys/05-publish-linkedin.spec.ts

### TST-022 P1 Scheduling and publishing - No automated test asserts: Post is live but marking it Published fails
- **Journeys:** J-089
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'markRowPublished|Failed to send the approved message'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned no files. No test touches this journey.
- **Repro:** Order in code: send to channel first, then `markRowPublished` and `appendToPostedDoc`. A failure after a successful send surfaces "Failed to send the approved message..." to the user, the row stays `Approved`, and a retry posts a duplicate (CODE-READING FINDING). Pass requires the success to be reported or the retry to detect the existing post.
- **Fix hint:** add a test that asserts: when markRowPublished fails after a successful send, the user is told it posted and a retry does not duplicate. Test file suggestion: worker/src/publish.test.ts

### TST-023 P1 Connections and OAuth - No automated test asserts: OAuth misconfiguration: missing or wrong client id/secret, wrong redirect URI
- **Journeys:** J-101
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'LinkedIn OAuth is not configured|linkedinAuthAvailable'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned no files. No test touches this journey.
- **Repro:** (a) HTTP 400 `LinkedIn OAuth is not configured in the Worker environment. Add LINKEDIN_CLIENT_ID and LINKEDIN_CLIENT_SECRET first.`; the UI card should hide Connect when `linkedinAuthAvailable` is false. CODE-READING FINDING: for every failure `handleConnect` only does `console.error('OAuth connect failed:', err)`, so the user sees nothing happen. (b)-(d) fail inside the provider popup page; the operator needs a d...
- **Fix hint:** add a test that asserts: a failed startLinkedInAuth shows the missing client id message and hides Connect. Test file suggestion: frontend/tests/e2e/journeys/07-connections-setup.spec.ts

### TST-024 P0 Connections and OAuth - No automated test asserts: A user with no LinkedIn connection publishes through someone else's token
- **Journeys:** J-103
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'LinkedIn publishing is not configured|shared-config'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned no files. No test touches this journey.
- **Repro:** Desired: B gets `LinkedIn publishing is not configured...`/"connect your account" and nothing is posted. Expected to FAIL today in multi-tenant deployments (single-owner self-hosted is fine and relies on this fallback).
- **Fix hint:** add a test that asserts: a user without a LinkedIn connection gets 'connect your account' and nothing is posted with the shared KV token. Test file suggestion: worker/src/publish.test.ts

### TST-025 P0 Newsletter - No automated test asserts: Newsletter actions are not tenant-scoped
- **Journeys:** J-112
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'approveNewsletterIssue|newsletter\.approveIssue|handleDeleteNewsletter'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned 3 file(s): tests-e2e/e2e/journeys/65-wiring-loop40.spec.ts, tests-e2e/e2e/journeys/57-wiring-loop33.spec.ts, tests-e2e/e2e/journeys/63-wiring-loop37.spec.ts. None of these asserts the pass check (they match the term in an unrelated assertion or a mock).
- **Repro:** Desired: all refused (not found / forbidden). CODE-READING FINDING: these handlers take only `issueId`/`newsletterId` and run `WHERE id = ?` with no `spreadsheet_id` or user check (`handleApproveNewsletterIssue(db, issueId)`, `handleSendApprovedNewsletterIssue`, `handleDeleteNewsletter(db, newsletterId)`). Ids are UUID-like so exploitation needs the id, but ids appear in URLs/UI/exports. Cross-tenant read/modify/s...
- **Fix hint:** add a test that asserts: approve, send and delete newsletter actions on another tenant's id are refused. Test file suggestion: worker/src/newsletter/__tests__/tenancy.test.ts

### TST-026 P1 Settings, models and providers - No automated test asserts: LLM provider failure and fallback
- **Journeys:** J-122
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'resolveFallbackForGeneration|llmProvider'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned no files. No test touches this journey.
- **Repro:** Where a fallback is configured (`resolveFallbackForGeneration`) the call succeeds and `llmProvider` in the result names the fallback; otherwise a readable error reaches the user (not `[object Object]`, not a raw API key in the text); usage rows recorded in `llm_usage_log` only for successful calls (check token accounting on failures).
- **Fix hint:** add a test that asserts: on provider failure the fallback is used and llmProvider names it; otherwise a readable error is returned. Test file suggestion: worker/src/llm-fallback.test.ts

### TST-027 P0 Admin, tenant and budget - No automated test asserts: Empty `ADMIN_EMAILS` makes the repo owner an admin
- **Journeys:** J-127
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'DEFAULT_ADMIN_EMAIL|ADMIN_EMAILS|99pratyush'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned no files. No test touches this journey.
- **Repro:** Desired: with no `ADMIN_EMAILS`, nobody is admin (or deploy refuses). CODE-READING FINDING: `resolveAdminEmailAllowlist` falls back to `DEFAULT_ADMIN_EMAIL = '99pratyush@gmail.com'`, so on any customer's deployment missing the variable, the project author gets admin (shared config, tokens, all users) and the real operator is not admin. The committed `worker/wrangler.jsonc` also lists the owner's and another person...
- **Fix hint:** add a test that asserts: with ADMIN_EMAILS unset nobody is admin. Test file suggestion: worker/src/auth.test.ts

### TST-028 P1 Failure and recovery - No automated test asserts: Google Sheets unavailable or unshared during topic list
- **Journeys:** J-129
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'falling back to D1|out of sync'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned no files. No test touches this journey.
- **Repro:** `getRows` falls back to D1 rows (`console.error('[getRows] Sheets merge failed, falling back to D1')`) and the UI loads; no banner tells the user the sheet is out of sync (CODE-READING FINDING). Writes: D1 updates succeed; sheet mirroring errors in `updateRowStatus`/`publishContent` must not block publishing or must be reported. After restore, rows reconcile without duplicates or lost edits.
- **Fix hint:** add a test that asserts: getRows falls back to D1 when Sheets merge fails and the UI shows an out-of-sync notice. Test file suggestion: worker/src/topics.test.ts

### TST-029 P1 Failure and recovery - No automated test asserts: CORS: frontend origin not allowed, or allowlist empty
- **Journeys:** J-131
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'buildCorsHeaders|Access-Control-Allow-Origin|CORS'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned 2 file(s): tests/setup/test_verification.py, tests-e2e/e2e/setup-flow.spec.ts. None of these asserts the pass check (they match the term in an unrelated assertion or a mock).
- **Repro:** Case 1: browser blocks the call; UI message built by `formatFetchNetworkFailure` explains the CORS variable and mixed content (if `http://` worker on an https page). Case 2: `buildCorsHeaders` returns `Access-Control-Allow-Origin: *` when the list is empty (fail-open) — acceptable only with token auth, but note `/api/waitlist` and webhooks are then callable from any site. Origins with a trailing slash or `127.0.0....
- **Fix hint:** add a test that asserts: a disallowed origin gets no ACAO header and an empty allowlist does not return *. Test file suggestion: worker/src/cors.test.ts

### TST-030 P1 Failure and recovery - No automated test asserts: Missing `SECRET_ENCRYPTION_KEY`
- **Journeys:** J-132
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'SECRET_ENCRYPTION_KEY'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned 2 file(s): setup/wizard/tests/test_apikeys.py, tests/setup/test_setup_wiring.py. None of these asserts the pass check (they match the term in an unrelated assertion or a mock).
- **Repro:** Popup shows `Missing SECRET_ENCRYPTION_KEY in the Worker environment.` CODE-READING FINDING: in `handleLinkedInCallback`, `persistLinkedInConnection` (KV) runs before `requireSecretEncryptionKey`; the per-user D1 upsert is wrapped in `.catch(() => undefined)` only for the DB call, so the error ends the flow after the shared token was already saved: the popup says failed while the shared slot changed. `startLinkedI...
- **Fix hint:** add a test that asserts: LinkedIn callback without SECRET_ENCRYPTION_KEY fails before persisting any token. Test file suggestion: worker/src/oauth.test.ts

### TST-031 P1 Failure and recovery - No automated test asserts: Missing D1 binding or unapplied migrations
- **Journeys:** J-133
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'Unable to start|no such table|D1_ERROR'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned no files. No test touches this journey.
- **Repro:** Step 2 returns OK (health check does not touch D1, so setup "verify" can pass while the app is broken). Step 1 returns HTTP 400 with the raw runtime message (e.g. `Cannot read properties of undefined (reading 'prepare')` or `D1_ERROR: no such table: users`) and the frontend shows it as "Unable to start the session"/access error. Desired: a clear "database not initialised: run migrations" message and a health endpo...
- **Fix hint:** add a test that asserts: bootstrap with a missing D1 binding or unmigrated table returns a clear setup message. Test file suggestion: worker/src/bootstrap.test.ts

### TST-032 P1 Failure and recovery - No automated test asserts: Missing or invalid `GOOGLE_SERVICE_ACCOUNT_JSON`
- **Journeys:** J-134
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'GOOGLE_SERVICE_ACCOUNT_JSON|getServiceAccountEmail'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned 2 file(s): setup/wizard/tests/test_google.py, tests/wizard/test_verify.py. None of these asserts the pass check (they match the term in an unrelated assertion or a mock).
- **Repro:** Step 1 returns `{email:""}`; step 2 `Service account email not configured on this Worker.` or `GOOGLE_SERVICE_ACCOUNT_JSON is not valid JSON.`; step 3 `{accessible:false,title:""}` (errors swallowed). The SheetConnectionCard then shows no service-account email to share with: confirm the card tells the user it is a server misconfiguration, not their sheet.
- **Fix hint:** add a test that asserts: missing or invalid GOOGLE_SERVICE_ACCOUNT_JSON returns the documented errors and the card tells the user. Test file suggestion: worker/src/sheets.test.ts

### TST-033 P1 Failure and recovery - No automated test asserts: Frontend built with the wrong Google client id
- **Journeys:** J-135
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'origin_mismatch|audience does not match'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned no files. No test touches this journey.
- **Repro:** Google popup shows `origin_mismatch`/`invalid_client` (origins) or bootstrap fails with `Unauthorized: Google token audience does not match this app.` shown in the red error box on the sign-in card; the operator doc (SETUP.md Step 2) lists the exact origins (`http://localhost:5173` only; `5174` used by `npm run dev` is not listed: CODE-READING FINDING).
- **Fix hint:** add a test that asserts: a wrong audience shows the red audience-mismatch error on the sign-in card. Test file suggestion: frontend/tests/e2e/journeys/01-auth-onboarding.spec.ts

### TST-034 P0 Failure and recovery - No automated test asserts: Dev auth bypass secret present in production
- **Journeys:** J-136
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'tryResolveDevGoogleAuthBypassSession|DEV_GOOGLE_AUTH_BYPASS_SECRET'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned 2 file(s): frontend/tests/e2e/cloud.spec.ts, setup/tests/test_github_bugfix.py. None of these asserts the pass check (they match the term in an unrelated assertion or a mock).
- **Repro:** Desired: never accepted outside local dev. CODE-READING FINDING: `verifySession` calls `tryResolveDevGoogleAuthBypassSession` before any Google call and returns `{isAdmin:true}` if the secret matches; there is no environment guard (`wrangler dev` vs deployed). The only protection is the comment "Do not set these variables in production Worker secrets". Also if `VITE_DEV_GOOGLE_AUTH_BYPASS_SECRET` is baked into a p...
- **Fix hint:** add a test that asserts: the bypass secret is rejected when not running under wrangler dev. Test file suggestion: worker/src/plugins/dev-google-auth-bypass/resolve-session.test.ts

### TST-035 P1 Upgrade and migration - No automated test asserts: Apply new D1 migrations on upgrade
- **Journeys:** J-137
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE '0019|monthly_token_budget|migrations'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned 5 file(s): frontend/tests/e2e/journeys/16-admin-panel.spec.ts, worker/src/auth.test.ts, setup/tests/test_cloudflare_bugfix_bug2.py, setup/tests/test_cloudflare_bugfix.py, tests-e2e/e2e/journeys/16-admin-panel.spec.ts. None of these asserts the pass check (they match the term in an unrelated assertion or a mock).
- **Repro:** Lists 0001..0021 as applied; existing users keep working and become `status='active'` with `monthly_token_budget=500000` (defaults from 0019); `pipeline_state` rows preserved by the rebuild in 0010 (verify row counts before/after on a copy). Deploying code BEFORE migrating gives runtime `no such column/table` errors (J-133): the deploy workflow/docs must order migrate-then-deploy. The 0019 file header comment says...
- **Fix hint:** add a test that asserts: migrations 0001..0021 apply in order to a populated copy and keep users and pipeline_state rows. Test file suggestion: tests/setup/test_migrations.py

### TST-036 P0 Data isolation between tenants - No automated test asserts: Tenant A cannot read or modify tenant B's topics
- **Journeys:** J-140
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'user_id|getNodeRuns|Topic not found'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned 5 file(s): frontend/tests/e2e/journeys/13-enrichment-pipeline.spec.ts, tests-e2e/e2e/journeys/13-enrichment-pipeline.spec.ts, tests-e2e/e2e/journeys/60-wiring-loop34.spec.ts, tests-e2e/e2e/journeys/28-wiring-loop20.spec.ts, tests-e2e/e2e/journeys/44-wiring-loop28.spec.ts. None of these asserts the pass check (they match the term in an unrelated assertion or a mock).
- **Repro:** Step 2 empty of B's rows. Step 3: every write is scoped by `user_id = A` in `pipeline_state` (PK `(user_id, topic_id)` per migration 0010), so none change B's data (A's call creates/updates only A's own row or fails with `Topic not found.`); `getNodeRuns` returns only rows with `user_id = A`. Verify by reading B's row afterwards. Note that `updateRowStatus` / `upsertFull` accept a client-supplied full row (includi...
- **Fix hint:** add a test that asserts: tenant A cannot read or write tenant B's topics, and getNodeRuns returns only A's rows. Test file suggestion: worker/src/tenancy.test.ts

### TST-037 P1 Data isolation between tenants - No automated test asserts: Per-user lists are scoped (clips, groups, feedback, integrations, personas, workflows)
- **Journeys:** J-142
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'listCustomPersonas|listInterestGroups|user_id'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned 15 file(s): frontend/tests/e2e/feed-page.spec.ts, frontend/tests/e2e/journeys/21-wiring-issues.spec.ts, frontend/tests/e2e/journeys/10-trending-research.spec.ts, frontend/tests/e2e/journeys/12-feed-feature.spec.ts, tests-e2e/e2e/journeys/51-wiring-loop30.spec.ts. None of these asserts the pass check (they match the term in an unrelated assertion or a mock).
- **Repro:** Lists contain only A's rows; mutations on B's ids change nothing / error (statements are `WHERE user_id = ?`).
- **Fix hint:** add a test that asserts: clips, groups, feedback, integrations, personas and workflows are scoped to user_id. Test file suggestion: worker/src/tenancy.test.ts
