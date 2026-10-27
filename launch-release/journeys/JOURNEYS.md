# Journeys — LinkedInPost launch-readiness review

Status: read-only design pass. Every route, action name, UI label and file below was checked against the code with grep or by reading the file. Nothing was executed. "Pass check" is the observable result a human or executor should see when the journey works; where code reading already shows it will NOT work, the Steps carry an inline note (`NOT IMPLEMENTED per code reading: ...` or `CODE-READING FINDING: ...`).

Core promise and criteria: see [../PLAN.md](../PLAN.md). Journey IDs are stable; the ledger references them.

## Conventions used in the Steps

- `ACTION <name> {payload}` means: `POST {WORKER_URL}/` with header `Content-Type: application/json` and body `{"action":"<name>","idToken":"<Google ID token>","payload":{...}}`. Success: HTTP 200 `{"ok":true,"data":...}`. Every thrown error (including auth errors, budget errors and unknown actions) returns HTTP 400 `{"ok":false,"error":"..."}` (worker/src/index.ts, catch block after `dispatchAction`).
- `{WORKER_URL}` = `VITE_WORKER_URL` for the frontend, `http://localhost:8787` for `cd worker && npm run dev`.
- `T` = a valid Google ID token for the persona in question. In local dev, the value of `DEV_GOOGLE_AUTH_BYPASS_SECRET` (worker/.dev.vars) is accepted as `idToken` and yields an admin session (worker/src/plugins/dev-google-auth-bypass/resolve-session.ts).
- Frontend routes (logged in): `/topics`, `/topics/new`, `/topics/:topicId`, `/topics/:topicId/editor/:variantSlot`, `/settings` (admin), `/rules`, `/campaign` (flag), `/usage`, `/connections`, `/enrichment` (admin), `/feed` (`/trending` redirects to `/feed`), `/automations` (admin), `/setup` (admin), `/admin` (admin), `/videos` (flag). Public: `/terms`, `/privacy-policy`, `/pricing`, `/about`, and `/` + `/landing` in `saas` mode. Source: frontend/src/App.tsx, frontend/src/components/dashboard/index.tsx, frontend/src/features/topic-navigation/utils/workspaceRoutes.ts.
- Non-action HTTP routes on the main worker: `GET /` (health), `GET /v1/image-gen-catalog` (admin), `GET /api/usage`, `GET /auth/{linkedin|instagram|whatsapp|gmail|youtube}/callback`, `GET|POST /api/feed`, `/api/feed/items`, `/api/clips`, `POST /api/waitlist`, `POST /api/generate/stream` (SSE), `POST /api/quickchange/stream` (SSE), `POST /internal/schedule-linkedin-publish`, `POST /internal/merged-rows`, `POST /internal/pipeline-upsert`, `/webhooks/{instagram|linkedin|telegram|gmail}`, `/automations/*` (admin) and `/automations/internal/*` (scheduler secret).
- Generation worker routes (all behind `Authorization: Bearer $WORKER_SHARED_SECRET`): `GET /v1/patterns`, `GET /v1/patterns/full`, `GET /v1/health`, `GET /v1/llm/catalog`, `POST /v1/generate`, `/v1/feedback`, `/v1/suggest-pattern`, `/v1/preview/quick-change`, `/v1/preview/variants`, `/v1/variants/save`, `GET /v1/variants/saved/:sessionId`, `POST /v1/clips`, `GET /v1/clips/:sessionId`, `DELETE /v1/clips/:sessionId/:clipId`.
- Wizard routes (Flask, port 4242): `/`, `/step/mode`, `/step/prereqs`, `/step/prereqs/complete`, `/step/google`, `/step/cloudflare`, `/step/apikeys`, `/step/deploy`, `/step/deploy/start`, `/step/deploy/stream`, `/step/verify`, `/complete`.

Action names the dispatcher accepts (`dispatchAction` in worker/src/index.ts, plus `__admin__`, `downloadDraftImage`, `sendTopicToGeneration` handled before it): bootstrap, getGoogleModels, listLlmModels, getLlmProviderCatalog, getLlmSettings, getUsageSummary, getUsageSummaryByRange, saveLlmSetting, getRows, generateQuickChange, generateVariantsPreview, saveDraftVariants, addTopic, updateTopicMeta, listCustomPersonas, createCustomPersona, deleteCustomPersona, updateCustomPersona, listCustomWorkflows, createCustomWorkflow, updateCustomWorkflow, deleteCustomWorkflow, listInterestGroups, createInterestGroup, updateInterestGroup, deleteInterestGroup, getFeedArticles, refreshFeedArticles, setArticleFeedback, getArticleFeedback, listClips, listEpisodes, createClip, updateClip, deleteClip, assignClipToPost, unassignClipFromPost, getNodeCatalog, analyzeTopicInsights, analyzeFeedArticle, extractArticleInsights, clusterDraftClips, findDraftConnections, findDebateArticle, crossDomainInsight, opinionLeaderInsights, updateRowStatus, saveEmailFields, createDraftFromPublished, updatePostSchedule, deleteRow, saveConfig, saveUserSettings, adminListTenantSettings, getGenerationRulesHistory, saveTopicGenerationRules, listPostTemplates, createPostTemplate, updatePostTemplate, deletePostTemplate, saveGenerationTemplateId, saveTopicDeliveryPreferences, startLinkedInAuth, startInstagramAuth, startWhatsAppAuth, startGmailAuth, startYouTubeAuth, disconnectChannelAuth, completeWhatsAppConnection, verifyTelegramChat, fetchDraftImages, promoteDraftImageUrl, uploadDraftImage, uploadContextDocument, generateImageWithReference, generateImageFromText, publishContent, cancelScheduledPublish, searchNewsResearch, trendingSearch, bulkImportCampaign, listNewsResearchHistory, getNewsResearchSnapshot, runContentReview, callGenerationWorker, getNodeRuns, getPatternAssignment, listPatternAssignments, savePatternMetadata, getTestGroup, listPatterns, assignPattern, trendingYouTube, trendingLinkedIn, trendingInstagram, getIntegrations, deleteIntegration, connectSpreadsheet, disconnectSpreadsheet, syncFromSheets, getSpreadsheetStatus, getServiceAccountEmail, completeOnboarding, newsletter.getConfig, newsletter.saveConfig, newsletter.listIssues, newsletter.approveIssue, newsletter.rejectIssue, newsletter.createDraftNow, newsletter.sendApproved, newsletter.list, newsletter.create, newsletter.update, newsletter.delete, newsletter.listIssuesByNewsletter, newsletter.createDraftByNewsletter, newsletter.regenerateIssue, newsletter.preview, newsletter.issue.update, getTimestamp, __admin__ (admin REST shim), downloadDraftImage, sendTopicToGeneration.

## Summary

| ID | Title | Priority | CORE | External |
|---|---|---|---|---|
| J-001 | Web setup wizard, end to end | P1 | yes | Cloudflare |
| J-002 | Headless full bootstrap with `python setup.py --all` | P1 | yes | Cloudflare |
| J-003 | Fresh Cloudflare account against the committed wrangler ids | P1 | yes | Cloudflare |
| J-004 | Generation worker deploy requires an LLM key | P2 | yes | Cloudflare, LLM provider |
| J-005 | Wizard deploy step: streaming logs, timeout, working directory | P2 | yes | Cloudflare |
| J-006 | Wizard mode step and deploymentMode propagation | P1 | yes | none |
| J-007 | Re-running setup.py is idempotent; `--skip-google` path | P2 | yes | Google Sheets, Cloudflare |
| J-008 | Verify step and worker health probes | P1 | yes | Cloudflare |
| J-009 | `tsc --noEmit` gate inside setup.py | P2 | yes | none |
| J-010 | In-app `/setup` page in a deployed (non-local) build | P2 | no | none |
| J-011 | Local development loop | P2 | no | none |
| J-012 | Dev auth bypass for local work and e2e | P2 | no | none |
| J-013 | Documented developer test commands exist | P3 | no | none |
| J-014 | `start.sh` unified launcher | P3 | no | none |
| J-015 | Approved user signs in (self-hosted) | P0 | yes | Google OAuth |
| J-016 | SaaS landing page and redirect for signed-in users | P2 | yes | Google OAuth |
| J-017 | Non-approved Google account signs in | P0 | yes | Google OAuth |
| J-018 | Waitlist request (public endpoint) | P2 | no | none |
| J-019 | Admin approves a waitlist entry | P2 | no | none |
| J-020 | Suspended user is blocked with a clear screen | P1 | yes | Google OAuth |
| J-021 | Google ID token expires mid-session (401-equivalent) | P1 | yes | Google OAuth |
| J-022 | Non-auth errors that contain "expired" or "not allowed" force a sign-out | P2 | yes | LinkedIn |
| J-023 | Backend unreachable at boot | P2 | yes | Cloudflare |
| J-024 | Frontend built without `VITE_WORKER_URL` | P2 | yes | none |
| J-025 | Deep link while signed out is restored after login | P3 | no | Google OAuth |
| J-026 | Sign out | P2 | yes | Google OAuth |
| J-027 | Admin-only screens and actions are enforced on both sides | P1 | yes | none |
| J-028 | Worker without `GOOGLE_CLIENT_ID` accepts tokens minted for other apps | P1 | yes | Google OAuth |
| J-029 | First sign-in shows onboarding; skipping both steps | P1 | yes | Google OAuth |
| J-030 | Onboarding with a sheet URL (Drive consent and share) | P1 | yes | Google Sheets, Google OAuth |
| J-031 | Non-admin without a connected sheet is locked out of the whole workspace | P0 | yes | Google Sheets |
| J-032 | Connect a sheet from `/connections` (consent and manual-share paths) | P1 | yes | Google Sheets, Google OAuth |
| J-033 | Disconnect a sheet and sync from sheet | P2 | yes | Google Sheets |
| J-034 | Admin inherits the legacy KV spreadsheet once | P2 | yes | Google Sheets |
| J-035 | Add a topic from the scratchpad | P1 | yes | Google Sheets |
| J-036 | Generate Pro/Con insights for a topic | P2 | yes | LLM provider |
| J-037 | Edit a topic's metadata | P2 | yes | none |
| J-038 | Voice dictation in the scratchpad | P3 | no | none |
| J-039 | Delete a topic (and its generated images) | P1 | yes | Google Sheets |
| J-040 | Topic list merges Sheets and D1 | P1 | yes | Google Sheets |
| J-041 | Open the feed (cache-first, auto-fetch when stale) | P2 | yes | other (news providers: RSS / NewsAPI / SerpAPI) |
| J-042 | Refresh the feed on demand | P2 | no | other (news providers) |
| J-043 | Interest groups (create, edit, delete) | P2 | no | none |
| J-044 | Clip an article or a passage | P1 | yes | none |
| J-045 | Attach clips to a draft and cluster them | P2 | yes | LLM provider |
| J-046 | Article analysis and insight extraction | P2 | yes | LLM provider |
| J-047 | "Debate mode" returns an invented opposing article | P1 | yes | LLM provider |
| J-048 | Cross-domain and "opinion leader" angles use fictional people | P2 | yes | LLM provider |
| J-049 | Thumbs up/down on an article | P3 | no | none |
| J-050 | REST feed and clip endpoints require auth | P1 | yes | none |
| J-051 | Trending panels (YouTube, LinkedIn, Instagram) use deployment-wide credentials | P2 | no | YouTube, LinkedIn, Instagram |
| J-052 | Topic news research and history | P2 | yes | other (news providers) |
| J-053 | Generate a draft from the queue (SSE stream) | P0 | yes | LLM provider, Cloudflare |
| J-054 | Network drop in the middle of the generation stream | P1 | yes | LLM provider |
| J-055 | Generation worker down, mis-secreted, or LLM error | P1 | yes | LLM provider, Cloudflare |
| J-056 | "Send to Generation" button on a saved Draft topic | P1 | yes | Cloudflare, LLM provider |
| J-057 | Client-supplied `spreadsheetId` overrides the server's in generation | P0 | yes | Google Sheets |
| J-058 | Streaming generation bypasses the monthly token budget | P1 | yes | LLM provider |
| J-059 | Pick a writing pattern/template for generation | P2 | yes | Cloudflare |
| J-060 | Generation worker is open when `WORKER_SHARED_SECRET` is empty | P0 | yes | Cloudflare, LLM provider |
| J-061 | Custom workflows (post types) | P2 | no | none |
| J-062 | Node runs viewer (pipeline observability) | P3 | no | none |
| J-063 | Open generated variants and pick one | P0 | yes | Google Sheets |
| J-064 | Manual edit with undo/redo; draft survives navigation | P1 | yes | none |
| J-065 | Quick Change via SSE | P1 | yes | LLM provider |
| J-066 | Variants preview for a selection | P2 | yes | LLM provider |
| J-067 | Pick and upload images for a post | P1 | yes | other (Google Cloud Storage, SerpAPI) |
| J-068 | AI image generation (text and reference) | P2 | no | other (image generation provider via generation-worker/worker image-gen) |
| J-069 | Content review checklist before publishing | P2 | yes | LLM provider |
| J-070 | Context document upload (txt, md, pdf) | P3 | no | none |
| J-071 | Personal generation rules ("My rules") | P2 | yes | none |
| J-072 | Global generation rules (admin) and history | P2 | yes | none |
| J-073 | Author profile ("Who am I") | P2 | yes | none |
| J-074 | Post templates CRUD | P2 | yes | Google Sheets |
| J-075 | Per-topic rules and template precedence | P2 | yes | none |
| J-076 | Publish now to LinkedIn | P0 | yes | LinkedIn |
| J-077 | Publish to Instagram (image required) | P1 | yes | Instagram |
| J-078 | Send via Gmail | P1 | yes | Gmail |
| J-079 | Send via WhatsApp | P1 | yes | WhatsApp |
| J-080 | Send via Telegram | P1 | yes | Telegram |
| J-081 | YouTube as a publish target | P2 | no | YouTube |
| J-082 | Schedule a future post (queued via Durable Object) | P0 | yes | LinkedIn, Cloudflare |
| J-083 | Alarm fires: what the scheduled run actually executes | P0 | yes | LinkedIn, Cloudflare, Google Sheets |
| J-084 | Cancel a scheduled post | P1 | yes | Cloudflare |
| J-085 | Schedule in the past | P1 | yes | LinkedIn |
| J-086 | Timezone semantics of a scheduled time | P1 | yes | LinkedIn, Cloudflare |
| J-087 | Calendar drag-reschedule of an already queued post | P1 | yes | Cloudflare |
| J-088 | Double-click on Publish | P1 | yes | LinkedIn |
| J-089 | Post is live but marking it Published fails | P1 | yes | LinkedIn, Google Sheets |
| J-090 | Publish fails because the channel token was revoked or expired | P1 | yes | LinkedIn |
| J-091 | Republish an already published post | P2 | yes | LinkedIn |
| J-092 | Durable Object alarm throws and is retried | P2 | yes | Cloudflare, LinkedIn |
| J-093 | Connections page overview | P2 | yes | none |
| J-094 | Connect LinkedIn (popup OAuth) | P1 | yes | LinkedIn |
| J-095 | Connect Instagram | P1 | yes | Instagram |
| J-096 | Connect Gmail | P1 | yes | Gmail, Google OAuth |
| J-097 | Connect YouTube | P2 | no | YouTube |
| J-098 | OAuth popup closed, blocked or cancelled | P2 | yes | LinkedIn |
| J-099 | Connect WhatsApp (admin only, phone selection) | P2 | yes | WhatsApp |
| J-100 | Replayed or expired OAuth `state` | P2 | yes | LinkedIn |
| J-101 | OAuth misconfiguration: missing or wrong client id/secret, wrong redirect URI | P1 | yes | LinkedIn |
| J-102 | Disconnect a channel: three different "disconnect" behaviours | P1 | yes | LinkedIn |
| J-103 | A user with no LinkedIn connection publishes through someone else's token | P0 | yes | LinkedIn |
| J-104 | Telegram chat verification (admin) | P2 | yes | Telegram |
| J-105 | Stored token can no longer be decrypted (key rotated) | P2 | yes | Instagram |
| J-106 | Bulk import by pasting campaign JSON | P2 | no | Google Sheets |
| J-107 | Bulk import from a file (.json, .jsonc, .csv) | P2 | no | none |
| J-108 | Re-importing the same campaign (duplicate `topicId`) | P2 | no | Google Sheets |
| J-109 | Create a newsletter and preview it | P2 | no | Gmail |
| J-110 | Draft, approve and send a newsletter issue manually | P2 | no | Gmail, Telegram |
| J-111 | Scheduled newsletter send vs a once-a-day cron | P1 | no | Cloudflare, Gmail |
| J-112 | Newsletter actions are not tenant-scoped | P0 | yes | Gmail |
| J-113 | Enrichment page and node catalog (admin) | P2 | no | LLM provider |
| J-114 | Automation rules (admin) | P2 | no | Instagram, LinkedIn, Telegram, Gmail |
| J-115 | Instagram webhook verification handshake | P2 | no | Instagram |
| J-116 | Gmail push webhook has no sender authentication | P1 | no | Gmail |
| J-117 | Telegram and LinkedIn webhooks verify signatures | P2 | no | Telegram, LinkedIn |
| J-118 | YouTube comment polling schedule | P2 | no | YouTube |
| J-119 | Daily cron housekeeping | P3 | no | Cloudflare |
| J-120 | Admin settings: default channel, allowed models, news keys | P2 | yes | none |
| J-121 | Pick provider and model per purpose | P2 | yes | LLM provider |
| J-122 | LLM provider failure and fallback | P1 | yes | LLM provider |
| J-123 | Admin panel: users, approve, suspend, budget | P1 | yes | none |
| J-124 | Usage meter and usage page | P2 | no | none |
| J-125 | Monthly token budget exhausted | P1 | yes | LLM provider |
| J-126 | Self-hosted deployment still enforces the SaaS budget | P1 | yes | LLM provider |
| J-127 | Empty `ADMIN_EMAILS` makes the repo owner an admin | P0 | yes | none |
| J-128 | Admin suspends a user while they are signed in | P1 | yes | none |
| J-129 | Google Sheets unavailable or unshared during topic list | P1 | yes | Google Sheets |
| J-130 | Sheets down while adding a topic | P2 | yes | Google Sheets |
| J-131 | CORS: frontend origin not allowed, or allowlist empty | P1 | yes | Cloudflare |
| J-132 | Missing `SECRET_ENCRYPTION_KEY` | P1 | yes | LinkedIn |
| J-133 | Missing D1 binding or unapplied migrations | P1 | yes | Cloudflare |
| J-134 | Missing or invalid `GOOGLE_SERVICE_ACCOUNT_JSON` | P1 | yes | Google Sheets |
| J-135 | Frontend built with the wrong Google client id | P1 | yes | Google OAuth |
| J-136 | Dev auth bypass secret present in production | P0 | yes | none |
| J-137 | Apply new D1 migrations on upgrade | P1 | yes | Cloudflare |
| J-138 | Legacy rows and shared-config data after upgrade | P2 | yes | Google Sheets |
| J-139 | Feature flags after editing `features.yaml` | P3 | no | none |
| J-140 | Tenant A cannot read or modify tenant B's topics | P0 | yes | none |
| J-141 | Two tenants connect the same Google Sheet | P2 | yes | Google Sheets |
| J-142 | Per-user lists are scoped (clips, groups, feedback, integrations, personas, workflows) | P1 | yes | none |
| J-143 | Generated and uploaded images in a shared bucket | P2 | yes | other (Google Cloud Storage) |
| J-144 | Scheduler-secret internal routes | P2 | no | other (GitHub Actions / external scheduler) |
| J-145 | Operator health check of both workers | P1 | yes | Cloudflare |
| J-146 | Videos page | P3 | no | Google Sheets |

Totals: 146 journeys. P0=15, P1=57, P2=64, P3=10; CORE yes=110.

## First-run, setup and install

### J-001 Web setup wizard, end to end
- **Persona:** Self-hosting operator
- **Priority:** P1
- **CORE:** yes
- **External service:** Cloudflare
- **Preconditions:** Clean machine with Python 3, Node, Git; repo cloned; `pip install -r requirements.txt` done; Cloudflare API token and Google service account key to hand.
- **Steps:**
  1. `python setup.py --web` (setup.py `main()` calls `run_wizard()`; Flask binds 127.0.0.1:4242 and opens the browser).
  2. `/` redirects to `/step/mode`; pick a mode and submit (POST `/step/mode`).
  3. `/step/prereqs` then POST `/step/prereqs/complete`.
  4. `/step/google` (service account JSON, OAuth client id) POST.
  5. `/step/cloudflare` (API token) POST: D1 and KV provisioned.
  6. `/step/apikeys` POST (Gemini required).
  7. `/step/deploy`, press start (POST `/step/deploy/start`), watch `/step/deploy/stream`.
  8. `/step/verify`, then `/complete`.
  - Note: SETUP.md says "6-step wizard"; the code has 7 steps (`mode` is the extra one, `STEPS` in setup/wizard/state.py).
- **Pass check:** Each step redirects to the next; `.wizard_state.json` in the repo root has all seven keys `true`; `/complete` renders; both workers respond (see J-008).
- **Code anchors:** setup.py, setup/cli.py, setup/wizard/server.py, setup/wizard/state.py, setup/wizard/steps/*.py, SETUP.md

### J-002 Headless full bootstrap with `python setup.py --all`
- **Persona:** Self-hosting operator
- **Priority:** P1
- **CORE:** yes
- **External service:** Cloudflare
- **Preconditions:** `.env` populated (GEMINI_API_KEY or XAI_API_KEY, GOOGLE_CLIENT_ID / VITE_GOOGLE_CLIENT_ID, service account JSON, bucket name); `npx wrangler login` done; `gh` authenticated if GitHub secrets sync is wanted.
- **Steps:**
  1. `python setup.py --all` (sets install-worker-deps, cloudflare, deploy-worker, sync-github-secrets).
  2. Observe in order: features regeneration, worker deps install, `tsc --noEmit` in worker and frontend, Google resources, KV namespaces, D1 create and migrations, generation worker D1, `worker/.dev.vars` written, generation worker deployed first then main worker, LLM secrets pushed, GitHub secrets synced, summary printed.
- **Pass check:** Exit code 0; `GET {WORKER_URL}/` returns `{"ok":true,"data":{"status":"ok","backend":"cloudflare-worker"}}`; the main worker `GENERATION_WORKER_URL` var points at the generation worker URL.
- **Code anchors:** setup.py `main()`, setup/cloudflare.py, setup/worker_config.py, setup/google_resources.py, setup/github.py

### J-003 Fresh Cloudflare account against the committed wrangler ids
- **Persona:** Self-hosting operator
- **Priority:** P1
- **CORE:** yes
- **External service:** Cloudflare
- **Preconditions:** Operator whose Cloudflare account is NOT the repo owner's; untouched clone.
- **Steps:**
  1. Open `worker/wrangler.jsonc`: it contains a concrete `database_id` (not a placeholder), concrete KV `id`/`preview_id`, the owner's `GOOGLE_CLIENT_ID`, `ALLOWED_EMAILS`, `ADMIN_EMAILS`, `GOOGLE_CLOUD_STORAGE_BUCKET`, `GENERATION_WORKER_URL`.
  2. Run `python setup.py --cloudflare`.
  3. `provision_d1_database()` treats any id that is not empty / `REPLACE_WITH_*` / `00000000-0000-0000-0000-000000000001` as already provisioned and skips `wrangler d1 create`; it then runs `_apply_d1_migrations(remote=True)` against that id.
  - CODE-READING FINDING: a non-owner operator hits the owner's D1 id (auth error from Cloudflare) or, worse, if the same account, reuses the owner's database. Same for KV ids. The wizard has no "reset ids" step.
- **Pass check:** After setup, `worker/wrangler.jsonc` `d1_databases[0].database_id` equals an id returned by `npx wrangler d1 list` for the operator's account, and `ADMIN_EMAILS` / `ALLOWED_EMAILS` contain the operator's email, not the owner's.
- **Code anchors:** worker/wrangler.jsonc, setup/cloudflare.py (`provision_d1_database`, `_d1_id_is_placeholder`, `_patch_d1_database_id`), setup/worker_config.py

### J-004 Generation worker deploy requires an LLM key
- **Persona:** Self-hosting operator
- **Priority:** P2
- **CORE:** yes
- **External service:** Cloudflare, LLM provider
- **Preconditions:** `.env` without GEMINI_API_KEY and XAI_API_KEY.
- **Steps:**
  1. `python setup.py --deploy-worker`.
  2. Read the error.
  3. Add `GEMINI_API_KEY`, rerun.
- **Pass check:** Step 2 fails fast with an explicit "at least one LLM key" message before any deploy (per SETUP.md); step 3 succeeds and `GET {GEN_WORKER_URL}/v1/health` with `Authorization: Bearer $WORKER_SHARED_SECRET` returns `{"status":"ok","service":"generation-worker",...}`.
- **Code anchors:** setup.py, setup/cloudflare.py (`ensure_worker_deploy`, `push_llm_secrets`), generation-worker/src/index.ts

### J-005 Wizard deploy step: streaming logs, timeout, working directory
- **Persona:** Self-hosting operator
- **Priority:** P2
- **CORE:** yes
- **External service:** Cloudflare
- **Preconditions:** Wizard started from the repo root (it uses relative `Path('features.yaml')`, `.wizard_state.json` and `python setup.py --deploy-worker` without `cwd=`).
- **Steps:**
  1. Start wizard from the repo root, reach `/step/deploy`, POST `/step/deploy/start`.
  2. Watch `/step/deploy/stream` (SSE of subprocess lines).
  3. Repeat with the wizard started from a subdirectory (`cd setup && python ../setup.py --web`).
  4. Make the deploy hang >10 minutes (`_DEPLOY_TIMEOUT_SEC = 600`).
- **Pass check:** Step 2 streams lines and ends with a success marker; step 3 fails with a clear message rather than writing state files in the wrong place; step 4 kills the subprocess and the stream terminates (the timeout is only checked when a new output line arrives, so a silent hang is not killed: CODE-READING FINDING).
- **Code anchors:** setup/wizard/steps/deploy.py, setup/wizard/state.py, setup/wizard/steps/mode.py

### J-006 Wizard mode step and deploymentMode propagation
- **Persona:** Self-hosting operator
- **Priority:** P1
- **CORE:** yes
- **External service:** none
- **Preconditions:** Wizard running; `features.yaml` currently `deploymentMode: selfHosted` on this branch.
- **Steps:**
  1. `/step/mode`, choose `selfHosted`, submit (POST `/step/mode`, form field `mode`).
  2. Confirm `features.yaml` `deploymentMode` and `frontend/src/generated/features.ts` were regenerated (`python3 scripts/generate_features.py`).
  3. Compare with the worker: `worker/src/generated/features.ts` has FEATURE_* flags only; the worker budget gate reads `env.DEPLOYMENT_MODE ?? 'saas'` (see J-126).
- **Pass check:** `grep deploymentMode features.yaml` shows the chosen mode; `frontend/src/generated/features.ts` agrees. Unknown form values silently become `saas` (mode.py `submit`).
- **Code anchors:** setup/wizard/steps/mode.py, features.yaml, scripts/generate_features.py, frontend/src/generated/features.ts, worker/src/generated/features.ts

### J-007 Re-running setup.py is idempotent; `--skip-google` path
- **Persona:** Self-hosting operator
- **Priority:** P2
- **CORE:** yes
- **External service:** Google Sheets, Cloudflare
- **Preconditions:** A completed first run.
- **Steps:**
  1. `python setup.py --cloudflare --skip-google`.
  2. `python setup.py --cloudflare` (without `--skip-google`; the default path calls `_create_google_resources` and `ensure_google_setup_python_deps()`).
  3. Compare sheet / folder / doc created.
- **Pass check:** Step 1 prints "Google resource creation: skipped by flag" and leaves existing resources; step 2 reuses the existing LINKEDIN folder, content calendar sheet and posted doc (does not create duplicates); KV namespaces reused, D1 not recreated.
- **Code anchors:** setup.py, setup/google_resources.py, setup/python_requirements.py, setup/cloudflare.py

### J-008 Verify step and worker health probes
- **Persona:** Self-hosting operator
- **Priority:** P1
- **CORE:** yes
- **External service:** Cloudflare
- **Preconditions:** Both workers deployed.
- **Steps:**
  1. Wizard `/step/verify`.
  2. Manually: `curl {WORKER_URL}/` and `curl -H "Authorization: Bearer $WORKER_SHARED_SECRET" {GEN_URL}/v1/health` and `curl -X OPTIONS -H "Origin: https://<frontend>" -H "Access-Control-Request-Method: POST" {WORKER_URL}/`.
  3. `POST {WORKER_URL}/` with `{"action":"getTimestamp","idToken":"T","payload":{}}`.
- **Pass check:** Step 2: 200 JSON envelope; 200 health; 204 with `Access-Control-Allow-Origin` echoing the frontend origin. Step 3: `{"ok":true,"data":{"timestamp":<unix seconds>}}`.
- **Code anchors:** setup/wizard/steps/verify.py, setup/verification.py, worker/src/index.ts (`GET /`, `getTimestamp`), generation-worker/src/index.ts (`/v1/health`)

### J-009 `tsc --noEmit` gate inside setup.py
- **Persona:** Self-hosting operator
- **Priority:** P2
- **CORE:** yes
- **External service:** none
- **Preconditions:** Any Worker flag passed (`--install-worker-deps`, `--cloudflare`, `--deploy-worker`, `--sync-github-secrets`, `--all`).
- **Steps:**
  1. Run `python setup.py --install-worker-deps` on a tree with a TS type error in `frontend/` or `worker/`.
- **Pass check:** `run_typescript_dry_run()` raises `RuntimeError("<label> type check failed ...")`, aborting setup (an unrelated type error in frontend blocks a worker-only deploy). On a clean tree both print "no type errors".
- **Code anchors:** setup/cloudflare.py (`run_typescript_dry_run`), setup.py, AGENTS.md

### J-010 In-app `/setup` page in a deployed (non-local) build
- **Persona:** Tenant admin
- **Priority:** P2
- **CORE:** no
- **External service:** none
- **Preconditions:** Production frontend; signed in as admin (header shows "Setup").
- **Steps:**
  1. Click header "Setup" (route `/setup`, renders `SetupWizard embedded`).
  2. Use any step that saves config.
- **Pass check:** CODE-READING FINDING: `setupService.ts` fetches `http://localhost:3456/api/setup/write-config`, `/reset-database`, `/regenerate-features` (served only by `node frontend/server/setupWizard.js` from `npm run dev`). In production these calls fail (mixed content / connection refused); the page must show a clear "local dev only" message or be hidden.
- **Code anchors:** frontend/src/features/setup-wizard/setupService.ts, frontend/src/features/setup-wizard/SetupWizard.tsx, frontend/src/components/dashboard/index.tsx

### J-011 Local development loop
- **Persona:** Developer
- **Priority:** P2
- **CORE:** no
- **External service:** none
- **Preconditions:** `npm install` at root; `worker/.dev.vars` present (written by setup); `frontend/.env.local` with `VITE_WORKER_URL=http://localhost:8787` and `VITE_GOOGLE_CLIENT_ID`.
- **Steps:**
  1. `cd worker && npm run dev` (wrangler dev `--env local --port 8787`).
  2. `cd frontend && npm run dev` (runs vite, `server/sttServer.js`, `server/setupWizard.js` concurrently).
  3. Open the printed Vite URL (CORS: `http://localhost:5173` and `5174` are in `CORS_ALLOWED_ORIGINS`; `127.0.0.1` is not).
  4. `cd worker && npm run typecheck` and `cd frontend && npx tsc --noEmit`.
- **Pass check:** `GET http://localhost:8787/` returns the health envelope; sign-in page loads; both typechecks exit 0.
- **Code anchors:** worker/package.json, frontend/package.json, worker/wrangler.jsonc (`env.local`), README.md, AGENTS.md

### J-012 Dev auth bypass for local work and e2e
- **Persona:** Developer
- **Priority:** P2
- **CORE:** no
- **External service:** none
- **Preconditions:** `DEV_GOOGLE_AUTH_BYPASS_SECRET` in `worker/.dev.vars`; `VITE_DEV_GOOGLE_AUTH_BYPASS=true` and `VITE_DEV_GOOGLE_AUTH_BYPASS_SECRET` (or `VITE_E2E_BYPASS_SECRET`) in `frontend/.env.local`.
- **Steps:**
  1. Open the app signed out; the sign-in card shows "Continue with dev bypass".
  2. Click it.
  3. `ACTION bootstrap {}` with `idToken` = the secret.
- **Pass check:** Session returns `isAdmin:true`, `email:"dev-bypass@local.invalid"` (or `DEV_GOOGLE_AUTH_BYPASS_EMAIL`); a `users` row is upserted.
- **Code anchors:** worker/src/plugins/dev-google-auth-bypass/*, frontend/src/plugins/dev-google-auth-bypass/*, frontend/src/App.tsx

### J-013 Documented developer test commands exist
- **Persona:** Developer
- **Priority:** P3
- **CORE:** no
- **External service:** none
- **Preconditions:** Repo cloned, deps installed.
- **Steps:**
  1. Run `cd frontend && npm run test` (AGENTS.md "Testing Requirements").
  2. Run `cd worker && npm run test`.
  3. Run `npm run test:setup` at root.
- **Pass check:** (NOT IMPLEMENTED per code reading: frontend/package.json has `test:e2e*` only, worker/package.json has `dev`, `deploy`, `typecheck` only, no `test` script in either). Step 3 exists (root package.json `test:setup`). Pre-push protocol in AGENTS.md cannot be followed literally.
- **Code anchors:** AGENTS.md, frontend/package.json, worker/package.json, package.json, vitest.config.ts

### J-014 `start.sh` unified launcher
- **Persona:** Developer
- **Priority:** P3
- **CORE:** no
- **External service:** none
- **Preconditions:** Node, Python, Wrangler installed.
- **Steps:**
  1. `./start.sh` (default `local`), then `./start.sh --skip-deps --skip-wizard`, `./start.sh --reset-db`, `./start.sh production`.
- **Pass check:** Unknown flags print `Unknown option: <x>` and exit 1; missing commands are reported by `check_command`; `--reset-db` asks before destroying local D1 state (read the script before running).
- **Code anchors:** start.sh

## Sign-in and session

### J-015 Approved user signs in (self-hosted)
- **Persona:** Approved end user
- **Priority:** P0
- **CORE:** yes
- **External service:** Google OAuth
- **Preconditions:** `features.yaml` `deploymentMode: selfHosted`; worker has `GOOGLE_CLIENT_ID`, `ADMIN_EMAILS`; user's Google account.
- **Steps:**
  1. Open `{FRONTEND}/` (non-saas has no `/` route; the catch-all shows "Sign in", "Use an approved Google account to open the workspace.").
  2. Click the Google sign-in button (`GoogleLoginButton`).
  3. Frontend stores the id token in `localStorage["google_id_token"]` and calls `ACTION bootstrap {}`.
- **Pass check:** `bootstrap` returns `{email,isAdmin,config,onboardingCompleted,integrations}`; app navigates to `/topics`; a `users` row exists for the email (D1 `users`).
- **Code anchors:** frontend/src/App.tsx, frontend/src/components/GoogleLoginButton.tsx, worker/src/index.ts (`verifySession`, `bootstrap`), worker/src/db/users.ts

### J-016 SaaS landing page and redirect for signed-in users
- **Persona:** New signed-in user
- **Priority:** P2
- **CORE:** yes
- **External service:** Google OAuth
- **Preconditions:** `deploymentMode: saas` build.
- **Steps:**
  1. Signed out: open `/` (renders `Landing`); `/landing` redirects to `/`.
  2. Sign in; `/` now redirects to `/topics`.
  3. Open `/pricing`, `/about`, `/terms`, `/privacy-policy` signed out.
- **Pass check:** Landing renders with sign-in; after login `window.location.pathname === "/topics"`; the four public pages render without a token. (Landing text "Join 2,400+ content creators" is a hard-coded claim; confirm it is true or remove before launch: frontend/src/features/saas/Landing.tsx.)
- **Code anchors:** frontend/src/App.tsx, frontend/src/features/saas/Landing.tsx, frontend/src/pages/PricingPage.tsx, frontend/src/pages/AboutPage.tsx, frontend/src/pages/TermsOfServicePage.tsx

### J-017 Non-approved Google account signs in
- **Persona:** Non-approved / unauthorised user
- **Priority:** P0
- **CORE:** yes
- **External service:** Google OAuth
- **Preconditions:** A Google account whose email is in neither `ALLOWED_EMAILS` nor `ADMIN_EMAILS`, never seen before.
- **Steps:**
  1. Sign in with that account.
  2. Observe the UI: expected "Access request pending" ("Your access request is pending review...").
  3. Directly: `ACTION bootstrap {}` with that account's `T`.
  4. Then `ACTION addTopic {"topic":"x"}`.
  - CODE-READING FINDING: `verifySession` calls `upsertUser` first (inserts a row), then `checkUserAccess` reads `users.status`. Migration 0019 defines `status TEXT NOT NULL DEFAULT 'active'`, so every new Google account becomes `active` on first sign-in. `ALLOWED_EMAILS` exists only as an `Env` field (grep shows no other use in worker/src). Expected block does not happen.
- **Pass check:** Desired: Step 3 returns `{"ok":false,"error":"Access not granted. Request access at the homepage."}` and no `users` row with `status='active'` is created. (Currently expected to FAIL: bootstrap returns a session.)
- **Code anchors:** worker/src/index.ts (`verifySession`, `resolveAdminEmailAllowlist`, `Env.ALLOWED_EMAILS`), worker/src/db/users.ts (`upsertUser`, `getUserStatus`), worker/src/auth.ts (`checkUserAccess`), worker/migrations/0019_user_status_budget.sql

### J-018 Waitlist request (public endpoint)
- **Persona:** Non-approved / unauthorised user
- **Priority:** P2
- **CORE:** no
- **External service:** none
- **Preconditions:** SaaS landing.
- **Steps:**
  1. On `/` scroll to `#waitlist`, fill email (and optional name/reason), click "Join waitlist".
  2. Or `POST {WORKER_URL}/api/waitlist` body `{"email":"a@b.co","name":"A","reason":"r"}`.
  3. Repeat with `{"email":"nope"}` and with the same email twice.
- **Pass check:** Step 2: HTTP 201 `{"ok":true,"message":"Request received..."}` and a row in D1 `access_requests` (status `pending`). Invalid email: HTTP 400 `{"error":"Valid email required"}`. The table has `email UNIQUE`, so a duplicate request should return a handled response, not a 500 (verify in `createAccessRequest`). No rate limit exists on this unauthenticated endpoint (CODE-READING FINDING).
- **Code anchors:** worker/src/modes/saas/waitlist.ts, worker/src/db/users.ts (`createAccessRequest`), worker/migrations/0019_user_status_budget.sql, frontend/src/features/saas/Landing.tsx

### J-019 Admin approves a waitlist entry
- **Persona:** Tenant admin
- **Priority:** P2
- **CORE:** no
- **External service:** none
- **Preconditions:** SaaS mode; admin signed in; a pending `access_requests` row.
- **Steps:**
  1. Header "Admin" -> `/admin`.
  2. In "Waitlist" click "Approve" on the row (calls `approveUserAccess`, i.e. `ACTION __admin__ {"__path":"/api/admin/users/<email>/approve","__method":"POST"}`).
- **Pass check:** `access_requests.status='approved'`; `users.status='active'` for the email if the user row exists. If the person has never signed in there is no `users` row so `UPDATE users` changes 0 rows (harmless today because the default status is `active`, see J-017).
- **Code anchors:** frontend/src/features/saas/AdminPanel.tsx, frontend/src/services/backendApi.ts (`approveUserAccess`), worker/src/modes/saas/admin.ts, worker/src/db/users.ts (`setUserStatus`, `resolveAccessRequest`)

### J-020 Suspended user is blocked with a clear screen
- **Persona:** Non-approved / unauthorised user
- **Priority:** P1
- **CORE:** yes
- **External service:** Google OAuth
- **Preconditions:** A `users` row with `status='suspended'` (admin clicked "Suspend").
- **Steps:**
  1. Sign in as that user.
  2. Click "Sign out" on the screen.
- **Pass check:** `bootstrap` returns `Access denied: your account has been suspended. Contact support.`; UI shows "Access request pending" with the text "Your account has been suspended. Contact support for help."; "Sign out" clears `localStorage["google_id_token"]`.
- **Code anchors:** frontend/src/App.tsx (`accessPending`), worker/src/auth.ts, worker/src/index.ts (`verifySession`)

### J-021 Google ID token expires mid-session (401-equivalent)
- **Persona:** Approved end user
- **Priority:** P1
- **CORE:** yes
- **External service:** Google OAuth
- **Preconditions:** Signed in for more than the token lifetime (Google ID tokens last about one hour); the app only stores the ID token in `localStorage`, there is no refresh code in App.tsx.
- **Steps:**
  1. Open the editor on a topic, type changes, do not save.
  2. After expiry trigger any action (e.g. click a Quick Change or "Publish to LinkedIn").
- **Pass check:** Worker returns HTTP 400 `{"ok":false,"error":"Unauthorized: invalid or expired Google token."}` (not 401). `handleFailure` matches `AUTH_ERROR_PATTERN` and calls `onAuthExpired`, which signs the user out with "Your Google session expired. Sign in again to continue." Desired: unsaved editor text is preserved or the user is warned (CODE-READING FINDING: editor history is component state only; it is lost on sign-out).
- **Code anchors:** frontend/src/App.tsx (`handleAuthExpired`), frontend/src/services/backendApi.ts (`AUTH_ERROR_PATTERN`, `post`), frontend/src/components/dashboard/hooks/useDashboardQueue.ts (`handleFailure`), frontend/src/features/editor/DraftEditor.tsx

### J-022 Non-auth errors that contain "expired" or "not allowed" force a sign-out
- **Persona:** Approved end user
- **Priority:** P2
- **CORE:** yes
- **External service:** LinkedIn
- **Preconditions:** Signed in; an OAuth state older than 10 minutes, or any backend message containing the words.
- **Steps:**
  1. `ACTION completeWhatsAppConnection {"connectionId":"old","phoneNumberId":"1"}` (admin) after the 10-minute pending TTL, or trigger any error text containing "expired".
  2. Observe the UI.
- **Pass check:** Error `The WhatsApp connection session expired. Start the connection again.` is shown as a notice. CODE-READING FINDING: `AUTH_ERROR_PATTERN = /unauthorized|invalid token|expired|sign in again|not allowed/i` matches it, so paths using `handleFailure`/`isAuthErrorMessage` sign the user out.
- **Code anchors:** frontend/src/services/backendApi.ts (`AUTH_ERROR_PATTERN`), frontend/src/features/review/context/useReviewFlowActions.ts, frontend/src/features/campaign/CampaignPage.tsx

### J-023 Backend unreachable at boot
- **Persona:** New signed-in user
- **Priority:** P2
- **CORE:** yes
- **External service:** Cloudflare
- **Preconditions:** Worker URL set but worker down or blocked.
- **Steps:**
  1. Sign in.
  2. Wait.
- **Pass check:** After 10 s (`BOOTSTRAP_TIMEOUT_MS`) the screen "Unable to start the session" appears with the message "Unable to reach the backend server. Please check your connection and try again." and the backend host label.
- **Code anchors:** frontend/src/App.tsx, frontend/src/services/backendApi.ts (`formatFetchNetworkFailure`)

### J-024 Frontend built without `VITE_WORKER_URL`
- **Persona:** Self-hosting operator
- **Priority:** P2
- **CORE:** yes
- **External service:** none
- **Preconditions:** Build with empty `VITE_WORKER_URL`.
- **Steps:**
  1. Open the app signed out.
- **Pass check:** Screen "Backend URL required" with the instruction to set `VITE_WORKER_URL`; no network calls are made. A relative value (e.g. `/topics`) is rejected by `normalizeWorkerApiUrl` and shows the same screen.
- **Code anchors:** frontend/src/App.tsx, frontend/src/services/backendApi.ts (`normalizeWorkerApiUrl`, `isConfigured`)

### J-025 Deep link while signed out is restored after login
- **Persona:** Approved end user
- **Priority:** P3
- **CORE:** no
- **External service:** Google OAuth
- **Preconditions:** Signed out.
- **Steps:**
  1. Open `{FRONTEND}/topics/new` directly.
  2. Sign in.
- **Pass check:** `sessionStorage` key (POST_LOGIN_REDIRECT_KEY) holds `/topics/new` before login; after login the app lands on `/topics/new`, then the key is removed. In private mode where storage throws, the app still lands on `/topics`.
- **Code anchors:** frontend/src/App.tsx (`LoginRedirect`, `PostLoginDeepLinkRestore`), frontend/src/features/topic-navigation/utils/workspaceRoutes.ts

### J-026 Sign out
- **Persona:** Approved end user
- **Priority:** P2
- **CORE:** yes
- **External service:** Google OAuth
- **Preconditions:** Signed in.
- **Steps:**
  1. Use the account menu logout in the workspace shell.
  2. Reload.
- **Pass check:** `localStorage["google_id_token"]` removed; reload shows sign-in; `googleLogout()` called; going Back does not show private data from the previous session (rows are held in React state only).
- **Code anchors:** frontend/src/components/workspace/WorkspaceShell.tsx, frontend/src/App.tsx

### J-027 Admin-only screens and actions are enforced on both sides
- **Persona:** Approved end user
- **Priority:** P1
- **CORE:** yes
- **External service:** none
- **Preconditions:** Non-admin session `T`.
- **Steps:**
  1. Browse to `/settings`, `/admin`, `/setup`, `/enrichment`, `/automations`.
  2. `ACTION saveConfig {"generationRules":"x"}`; `ACTION saveLlmSetting {"key":"generation_worker","ref":{"provider":"gemini","model":"m"}}`; `ACTION startWhatsAppAuth {}`; `ACTION disconnectChannelAuth {"provider":"linkedin"}`; `ACTION verifyTelegramChat {"chatId":"@x"}`; `ACTION adminListTenantSettings {}`.
  3. `ACTION __admin__ {"__path":"/api/admin/users","__method":"GET"}`.
  4. `GET {WORKER_URL}/automations/rules` with `Authorization: Bearer T`; `GET {WORKER_URL}/v1/image-gen-catalog`.
- **Pass check:** Step 1 redirects to `/topics`. Step 2 each returns `Only admin users can change shared configuration.`. Step 3 returns HTTP 403 `Admin access required` (the `__admin__` branch returns a real 403). Step 4 returns 403 `Forbidden`.
- **Code anchors:** frontend/src/components/dashboard/index.tsx, worker/src/index.ts (`ensureAdmin`, `__admin__` branch, `/automations/` guard, `/v1/image-gen-catalog`)

### J-028 Worker without `GOOGLE_CLIENT_ID` accepts tokens minted for other apps
- **Persona:** Self-hosting operator
- **Priority:** P1
- **CORE:** yes
- **External service:** Google OAuth
- **Preconditions:** Worker deployed with `GOOGLE_CLIENT_ID` empty.
- **Steps:**
  1. Obtain a valid Google ID token issued for a different OAuth client (any site using Google sign-in).
  2. `ACTION bootstrap {}` with that token.
- **Pass check:** Desired: `Unauthorized: Google token audience does not match this app.` or a startup refusal. CODE-READING FINDING: the audience check is `if (env.GOOGLE_CLIENT_ID && tokenInfo.aud !== env.GOOGLE_CLIENT_ID)`, so with the variable unset the check is skipped and token verification relies on Google tokeninfo only. Combined with J-017 any Google user gets in.
- **Code anchors:** worker/src/index.ts (`verifySession`), setup/worker_config.py

## Onboarding and workspace connection

### J-029 First sign-in shows onboarding; skipping both steps
- **Persona:** New signed-in user
- **Priority:** P1
- **CORE:** yes
- **External service:** Google OAuth
- **Preconditions:** `users.onboarding_completed = 0` (default).
- **Steps:**
  1. Sign in; the `OnboardingModal` ("Connect your accounts") appears.
  2. Click "Skip for now →" (label becomes "Continue →" if an integration exists).
  3. On "Content source" click "Skip, I'll add later →".
- **Pass check:** `ACTION completeOnboarding {}` returns `{"ok":true}`; D1 `users.onboarding_completed=1`; browser navigates to `/connections` via `window.location.assign`. Next `bootstrap` returns `onboardingCompleted:true`; the modal does not reappear.
- **Code anchors:** frontend/src/features/onboarding/OnboardingModal.tsx, frontend/src/features/onboarding/ConnectAccountsGrid.tsx, frontend/src/App.tsx (`handleCompleteOnboarding`), worker/src/index.ts (`completeOnboarding`)

### J-030 Onboarding with a sheet URL (Drive consent and share)
- **Persona:** New signed-in user
- **Priority:** P1
- **CORE:** yes
- **External service:** Google Sheets, Google OAuth
- **Preconditions:** Worker has `GOOGLE_SERVICE_ACCOUNT_JSON`; user owns a Google Sheet.
- **Steps:**
  1. Step 2 "Content source": paste `https://docs.google.com/spreadsheets/d/<ID>/edit`.
  2. Click "Connect & start →"; grant the Drive scope in the Google popup.
  3. Frontend calls `ACTION connectSpreadsheet {"spreadsheetId":"<ID>","driveAccessToken":"<access token>"}` then `completeOnboarding`.
  4. Repeat with a sheet the user cannot share (not owner) and with the Drive popup denied.
- **Pass check:** Step 3 returns `{"ok":true,"title":"<sheet title>"}` and D1 `users.spreadsheet_id=<ID>`. Failure cases: CODE-READING FINDING: `handleCompleteOnboarding` catches any error, logs to console only, still calls `completeOnboarding`, and redirects to `/connections`; the user never sees why the sheet was not connected.
- **Code anchors:** frontend/src/features/onboarding/OnboardingModal.tsx, frontend/src/App.tsx, worker/src/index.ts (`connectSpreadsheet`), worker/src/google/drivePermissions.ts

### J-031 Non-admin without a connected sheet is locked out of the whole workspace
- **Persona:** New signed-in user
- **Priority:** P0
- **CORE:** yes
- **External service:** Google Sheets
- **Preconditions:** SaaS tenant, non-admin, `users.spreadsheet_id=''` (skipped sheet in J-029 or J-030 failed).
- **Steps:**
  1. After onboarding, land on `/connections` (or `/topics`).
  2. Read the screen.
  3. Try to reach the "Connect Google Sheet" card on `/connections`.
  - CODE-READING FINDING: `Dashboard` returns the "Workspace setup pending" panel (`!session.config.spreadsheetId && !session.isAdmin`) BEFORE rendering `<Routes>`, so `/connections` (which hosts `SheetConnectionCard`) and `/topics/new` are unreachable. The panel says "An admin still needs to finish setup", while onboarding told the user the sheet is optional. Server side also gates `publishContent`, `generateQuickChange`, `deleteRow`, `createDraftFromPublished` on `ensureSpreadsheetConfigured`.
- **Pass check:** Desired: A sheetless user can reach `/connections`, connect a sheet, and use the app (or the app works D1-only). Currently expected to FAIL: the user sees only "Workspace setup pending".
- **Code anchors:** frontend/src/components/dashboard/index.tsx, frontend/src/pages/connections/SheetConnectionCard.tsx, worker/src/index.ts (`ensureSpreadsheetConfigured`, `loadStoredConfig`), frontend/src/features/onboarding/OnboardingModal.tsx

### J-032 Connect a sheet from `/connections` (consent and manual-share paths)
- **Persona:** Approved end user
- **Priority:** P1
- **CORE:** yes
- **External service:** Google Sheets, Google OAuth
- **Preconditions:** Admin (to be able to reach the page, see J-031); a Google Sheet.
- **Steps:**
  1. `/connections`, `SheetConnectionCard`: paste URL, grant Drive consent.
  2. Alternative: deny consent; the card shows the service account email (`ACTION getServiceAccountEmail {}`), share the sheet manually, click "Verify access" (`ACTION getSpreadsheetStatus {}`).
- **Pass check:** `connectSpreadsheet` returns `{ok:true,title}`; or `getSpreadsheetStatus` returns `{"accessible":true,"title":"..."}`. Wrong URL: error `Sheet shared but service account still cannot access it (404)...`. Invalid `GOOGLE_SERVICE_ACCOUNT_JSON`: `GOOGLE_SERVICE_ACCOUNT_JSON is not valid JSON.`
- **Code anchors:** frontend/src/pages/connections/SheetConnectionCard.tsx, worker/src/index.ts (`connectSpreadsheet`, `getSpreadsheetStatus`, `getServiceAccountEmail`)

### J-033 Disconnect a sheet and sync from sheet
- **Persona:** Approved end user
- **Priority:** P2
- **CORE:** yes
- **External service:** Google Sheets
- **Preconditions:** Sheet connected.
- **Steps:**
  1. `ACTION syncFromSheets {}`.
  2. `ACTION disconnectSpreadsheet {}`.
  3. `ACTION getRows {}`.
- **Pass check:** Step 1 `{ok:true,count:N}`. Step 2 sets `users.spreadsheet_id=''` only; the sheet itself and the service-account share remain. Step 3 returns D1 rows only (`getRowsByUserId`). Calling `syncFromSheets` when disconnected returns `No Google Sheet is connected. Connect one from the Connections page first.`
- **Code anchors:** worker/src/index.ts (`syncFromSheets`, `disconnectSpreadsheet`, `getRows`), worker/src/persistence/pipeline-db/pipeline.ts

### J-034 Admin inherits the legacy KV spreadsheet once
- **Persona:** Tenant admin
- **Priority:** P2
- **CORE:** yes
- **External service:** Google Sheets
- **Preconditions:** `CONFIG_KV` key `shared-config` has `spreadsheetId`; admin's `users.spreadsheet_id` empty; `DEV_SPREADSHEET_ID` unset.
- **Steps:**
  1. Admin signs in, `ACTION bootstrap {}`.
  2. Non-admin signs in.
- **Pass check:** Admin's D1 row gets the KV sheet id (`setUserSpreadsheetId`) and `config.spreadsheetId` is populated; the non-admin is NOT given the KV sheet (so no Google 403 from unshared sheet). Setting `DEV_SPREADSHEET_ID` overrides for every user (dev-only; make sure not set in production).
- **Code anchors:** worker/src/index.ts (`loadStoredConfig`)

## Topic capture and scratchpad

### J-035 Add a topic from the scratchpad
- **Persona:** Approved end user
- **Priority:** P1
- **CORE:** yes
- **External service:** Google Sheets
- **Preconditions:** Signed in with a sheet connected (see J-031).
- **Steps:**
  1. Go to `/topics/new` ("Add topic details").
  2. Fill topic title, About, Message to convey, style, audience, notes.
  3. Submit.
  4. API form: `ACTION addTopic {"topic":"Why X","date":"2026-10-28","topicMeta":{"about":"...","meaning":"...","style":"Professional","audience":"...","notes":"...","pros":[],"cons":[]}}`.
- **Pass check:** Response is the new row with a UUID `topicId`, `status:"Draft"`. A row exists in D1 `pipeline_state` (written first) and, if a sheet is connected, in the sheet. Empty topic -> `topic is required.`; `topicMeta` JSON over 8000 chars -> `Topic metadata is too large.` A Sheets error is logged but does not fail the request.
- **Code anchors:** frontend/src/features/add-topic/AddTopicPage.tsx, worker/src/index.ts (`addTopic`), worker/src/persistence/pipeline-db/pipeline.ts (`addTopicToD1`)

### J-036 Generate Pro/Con insights for a topic
- **Persona:** Approved end user
- **Priority:** P2
- **CORE:** yes
- **External service:** LLM provider
- **Preconditions:** LLM key on the worker.
- **Steps:**
  1. On `/topics/new` click "Generate insights".
  2. API: `ACTION analyzeTopicInsights {"topic":"...","about":"","meaning":"","notes":""}`.
  3. Force an LLM malformed answer (or no LLM key).
- **Pass check:** Returns `{pros:[...],cons:[...]}` each at most 6 strings. Malformed JSON -> `AI returned unexpected format. Please try again.`; missing key -> provider error shown. NOTE: this action has no `checkTokenBudget` and no `ensureSpreadsheetConfigured` call (CODE-READING FINDING for budget enforcement).
- **Code anchors:** worker/src/index.ts (`analyzeTopicInsights`), frontend/src/features/add-topic/AddTopicPage.tsx

### J-037 Edit a topic's metadata
- **Persona:** Approved end user
- **Priority:** P2
- **CORE:** yes
- **External service:** none
- **Preconditions:** Existing topic.
- **Steps:**
  1. Open the topic from `/topics`, edit via the add-topic form in edit mode.
  2. API: `ACTION updateTopicMeta {"topicId":"<id>","topic":"New title","topicMeta":{...}}`.
- **Pass check:** Returns the updated row; `topic_generation_rules` JSON updated in D1; `Topic not found.` for an id of another tenant (see J-140).
- **Code anchors:** worker/src/index.ts (`updateTopicMeta`), frontend/src/components/dashboard/index.tsx (`AddTopicPageWithEdit`)

### J-038 Voice dictation in the scratchpad
- **Persona:** Approved end user
- **Priority:** P3
- **CORE:** no
- **External service:** none
- **Preconditions:** Browser with microphone permission.
- **Steps:**
  1. Click the mic button (`MicButton`) next to a text area on `/topics/new`.
  2. Speak; stop.
- **Pass check:** Text is appended to the field. The speech model is loaded in a web worker (`whisperWorker.ts`, `@huggingface/transformers`); first use downloads the model, so test on a slow network and with permission denied (a visible error, no crash).
- **Code anchors:** frontend/src/features/add-topic/MicButton.tsx, frontend/src/features/add-topic/useSpeechToText.ts, frontend/src/features/add-topic/whisperWorker.ts

### J-039 Delete a topic (and its generated images)
- **Persona:** Approved end user
- **Priority:** P1
- **CORE:** yes
- **External service:** Google Sheets
- **Preconditions:** Topic with generated images in GCS.
- **Steps:**
  1. In the queue choose delete and confirm "Confirm Delete".
  2. API: `ACTION deleteRow {"row":{<full SheetRow incl. topic,date,topicId,rowIndex>}}`.
  3. Simulate a Sheets failure after step 2 starts.
- **Pass check:** D1 `pipeline_state` row and news snapshots removed, GCS objects for the topic prefix removed, sheet row removed. Order in code is: GCS delete, then D1 delete in parallel with snapshot delete, then `sheets.deleteRow` last; a Sheets failure leaves the D1 row gone but the sheet row present, and the next merge may resurrect it (CODE-READING FINDING). No soft-delete / undo.
- **Code anchors:** worker/src/index.ts (`deleteRow`), frontend/src/components/dashboard/hooks/useDashboardQueue.ts (`handleDeleteTopic`)

### J-040 Topic list merges Sheets and D1
- **Persona:** Approved end user
- **Priority:** P1
- **CORE:** yes
- **External service:** Google Sheets
- **Preconditions:** Sheet connected with rows edited by hand in the sheet.
- **Steps:**
  1. Open `/topics` (calls `ACTION getRows {}`).
  2. Add a row manually in the sheet, reload.
  3. Filter by status chips in the queue (Draft / Pending / Approved / Published).
- **Pass check:** New sheet row appears after reload with `topicId` assigned; counts per status match; no duplicate rows for topics that exist in both stores.
- **Code anchors:** worker/src/index.ts (`getRows`), worker/src/persistence/pipeline-db/pipeline.ts (`getMergedRows`), frontend/src/components/dashboard/hooks/useDashboardQueue.ts

## Feed and clipping

### J-041 Open the feed (cache-first, auto-fetch when stale)
- **Persona:** Approved end user
- **Priority:** P2
- **CORE:** yes
- **External service:** other (news providers: RSS / NewsAPI / SerpAPI)
- **Preconditions:** Interest group with topics (J-043) or topics selected.
- **Steps:**
  1. Open `/feed`.
  2. API: `ACTION getFeedArticles {"topics":["AI agents"]}`.
- **Pass check:** Returns `{articles,fetchedAt,stale}`. Fresh (<24 h) cache returned immediately; stale/empty triggers `trendingSearch` for the first topic only and saves a snapshot. Errors in the auto-fetch are swallowed (empty list, no message): confirm the UI explains an empty feed.
- **Code anchors:** frontend/src/features/feed/FeedPage.tsx, worker/src/index.ts (`getFeedArticles`), worker/src/db/feedArticles.ts, packages/researcher

### J-042 Refresh the feed on demand
- **Persona:** Approved end user
- **Priority:** P2
- **CORE:** no
- **External service:** other (news providers)
- **Preconditions:** None.
- **Steps:**
  1. Click the refresh icon in the curated panel (`FeedCuratedPanel`).
  2. API: `ACTION refreshFeedArticles {"topic":"AI agents","region":"US","genre":"general","windowDays":3}`.
- **Pass check:** New articles saved via `saveFeedSnapshot`; provider outage returns a thrown error (400) and the UI shows a notice rather than an infinite spinner. `refreshFeedArticles` has no budget check and no rate limit.
- **Code anchors:** worker/src/index.ts (`refreshFeedArticles`), frontend/src/features/feed/components/FeedCuratedPanel.tsx

### J-043 Interest groups (create, edit, delete)
- **Persona:** Approved end user
- **Priority:** P2
- **CORE:** no
- **External service:** none
- **Preconditions:** None.
- **Steps:**
  1. `ACTION createInterestGroup {"name":"AI","topics":["agents","llm"],"domains":["techcrunch.com"],"color":"#6366f1"}`.
  2. `ACTION updateInterestGroup {"id":"<id>","name":"AI 2"}`.
  3. `ACTION listInterestGroups {}`; `ACTION deleteInterestGroup {"id":"<id>"}`.
- **Pass check:** CRUD round-trips; every call is scoped by `user_id`; missing name -> `name is required.`
- **Code anchors:** worker/src/index.ts, worker/src/db/interestGroups.ts, frontend/src/features/feed/

### J-044 Clip an article or a passage
- **Persona:** Approved end user
- **Priority:** P1
- **CORE:** yes
- **External service:** none
- **Preconditions:** Article visible in the feed.
- **Steps:**
  1. Click the clip (scissors) button on an article, or select a passage and clip.
  2. API: `ACTION createClip {"type":"article","articleTitle":"T","articleUrl":"https://example.com/a","source":"S","publishedAt":"2026-10-20","thumbnailUrl":"","passageText":""}`; also `type:"passage"`.
  3. `ACTION listClips {}`; `ACTION updateClip {"id":"<id>","passageText":"edited"}`; `ACTION deleteClip {"id":"<id>"}`.
- **Pass check:** Create returns the clip; invalid type -> `type must be "article" or "passage".`; missing title/url -> explicit errors; list shows only the caller's clips.
- **Code anchors:** worker/src/index.ts (`createClip`...), worker/src/db/clips.ts, frontend/src/features/feed/components/DebateModeView.tsx

### J-045 Attach clips to a draft and cluster them
- **Persona:** Approved end user
- **Priority:** P2
- **CORE:** yes
- **External service:** LLM provider
- **Preconditions:** At least two clips and a topic.
- **Steps:**
  1. `ACTION assignClipToPost {"clipId":"<c>","postId":"<topicId>"}`; `ACTION unassignClipFromPost {...}`.
  2. `ACTION clusterDraftClips {"draftText":"...","clips":[{"title":"A","snippet":"..."},{"title":"B","snippet":"..."}]}`.
- **Pass check:** Assign returns the link; cluster returns `{themes:[{name,indices}],support:[...],challenge:[...]}`; empty clips returns empty arrays without an LLM call. `postId` ownership is not checked against the topic table in the dispatcher (CODE-READING FINDING: verify `assignClipToPost` in db/clips.ts).
- **Code anchors:** worker/src/index.ts, worker/src/db/clips.ts

### J-046 Article analysis and insight extraction
- **Persona:** Approved end user
- **Priority:** P2
- **CORE:** yes
- **External service:** LLM provider
- **Preconditions:** LLM key.
- **Steps:**
  1. `ACTION analyzeFeedArticle {"title":"T","description":"D","source":"S"}`.
  2. `ACTION extractArticleInsights {"title":"T","description":"D","source":"S"}`.
  3. `ACTION findDraftConnections {"title":"T","description":"D","drafts":[{"topicId":"a","topic":"..."}]}` (max 50 drafts, max 4 connections).
- **Pass check:** Shapes as in code (`summary/whyItMatters/postAngles/opposingView/opinionPrompt/perspectiveFlip`; `mainTakeaway/...`; `connections[]`). Missing `title` -> `title is required.` The analysis only sees title+description+source, not the article body, so claims like "dataPoint" or "expertQuote" can only come from the snippet or be invented: check the UI labels these as snippet-derived (criterion 2: drafts are right).
- **Code anchors:** worker/src/index.ts, frontend/src/features/feed/components/

### J-047 "Debate mode" returns an invented opposing article
- **Persona:** Approved end user
- **Priority:** P1
- **CORE:** yes
- **External service:** LLM provider
- **Preconditions:** Feed article open.
- **Steps:**
  1. Switch to Debate mode (`DebateModeView`).
  2. API: `ACTION findDebateArticle {"title":"T","description":"D"}`.
  3. Click the clip button on the result.
- **Pass check:** CODE-READING FINDING: the prompt says "Generate a realistic opposing article ... Plausible publication name (e.g. Harvard Business Review)". The result is fabricated (title, source, summary) and the UI offers "Clip". Pass requires that the UI visibly labels it AI-generated / not a real article and that clipping does not save a fake URL as a source. A user quoting it on LinkedIn would publish a false citation.
- **Code anchors:** worker/src/index.ts (`findDebateArticle`), frontend/src/features/feed/components/DebateModeView.tsx

### J-048 Cross-domain and "opinion leader" angles use fictional people
- **Persona:** Approved end user
- **Priority:** P2
- **CORE:** yes
- **External service:** LLM provider
- **Preconditions:** LLM key.
- **Steps:**
  1. `ACTION crossDomainInsight {"topic":"remote work"}`.
  2. `ACTION opinionLeaderInsights {"topic":"remote work"}`.
- **Pass check:** Returns 3 insights / 4 leaders. The prompt asks for "realistic full name" and roles that are "clearly fictional composites"; verify the UI states they are fictional so names are not copied into posts as real attributions.
- **Code anchors:** worker/src/index.ts, frontend/src/features/feed/

### J-049 Thumbs up/down on an article
- **Persona:** Approved end user
- **Priority:** P3
- **CORE:** no
- **External service:** none
- **Preconditions:** Feed article.
- **Steps:**
  1. `ACTION setArticleFeedback {"articleUrl":"https://example.com/a","vote":"up"}`; `{"vote":null}` removes; `{"vote":"x"}` errors.
  2. `ACTION getArticleFeedback {}`.
- **Pass check:** `{vote:"up"}` / `{vote:null}`; `vote must be "up" or "down".`; map returned is per user.
- **Code anchors:** worker/src/index.ts, worker/migrations/0021_article_feedback.sql, frontend/src/features/feed/

### J-050 REST feed and clip endpoints require auth
- **Persona:** Non-approved / unauthorised user
- **Priority:** P1
- **CORE:** yes
- **External service:** none
- **Preconditions:** None.
- **Steps:**
  1. `GET {WORKER_URL}/api/feed` and `GET {WORKER_URL}/api/clips` with no Authorization header.
  2. Same with a valid `Authorization: Bearer T`.
  3. `POST {WORKER_URL}/api/clips` body missing fields; `POST /api/feed/items`.
- **Pass check:** Step 1 HTTP 401 `Unauthorized`; step 2 200 with only the caller's data (`interest_group_id` filtered by `user_id`); bad bodies get 4xx. Note the feed SELECT filters `news_snapshots` by `spreadsheet_id` (shared sheet = shared snapshots, see J-141).
- **Code anchors:** worker/src/index.ts (`handleFeedGet`, `handleFeedItemCreate`, `handleClipsGet`, `handleClipsCreate`)

### J-051 Trending panels (YouTube, LinkedIn, Instagram) use deployment-wide credentials
- **Persona:** Approved end user
- **Priority:** P2
- **CORE:** no
- **External service:** YouTube, LinkedIn, Instagram
- **Preconditions:** `YOUTUBE_API_KEY` / `LINKEDIN_ACCESS_TOKEN` / `INSTAGRAM_ACCESS_TOKEN` + `INSTAGRAM_USER_ID` as worker secrets (or not).
- **Steps:**
  1. `/feed` trending section, or `ACTION trendingYouTube {"query":"ai"}`, `ACTION trendingLinkedIn {"orgId":"123"}`, `ACTION trendingInstagram {"query":"ai"}`, `ACTION trendingSearch {"topic":"ai","region":"US","genre":"general","windowDays":3}`.
  2. Run with no secrets configured.
- **Pass check:** With no key, YouTube returns `{items:[]}`, LinkedIn `{elements:[]}`, Instagram `{data:[]}` (silent empty, not an error). With keys, results show. These use env-level tokens, not the per-user D1 tokens, so every tenant reads with the operator's quota/identity. USE-CASES.md says "fallback to mock data": no mock fallback exists in the worker (the frontend may; check `frontend/src/features/trending/api`).
- **Code anchors:** worker/src/index.ts (`trendingYouTube`, `trendingLinkedIn`, `trendingInstagram`, `trendingSearch`), frontend/src/features/trending/

### J-052 Topic news research and history
- **Persona:** Approved end user
- **Priority:** P2
- **CORE:** yes
- **External service:** other (news providers)
- **Preconditions:** `FEATURE_NEWS_RESEARCH` true; sheet connected (`ensureSpreadsheetConfigured`).
- **Steps:**
  1. In the topic editor open the researcher panel (`ResearcherPanel`) and search.
  2. API: `ACTION searchNewsResearch {"topicId":"<id>","topic":"...","date":"..."}`, then `ACTION listNewsResearchHistory {"topicId":"<id>","limit":20}` and `ACTION getNewsResearchSnapshot {"id":"<snapshot id>"}`.
  3. Set `features.yaml` `newsResearch: false`, regenerate, retry.
- **Pass check:** Search stores a snapshot (max `NEWS_SNAPSHOT_MAX_PER_TOPIC`, default 10; pruned by the daily cron); history lists newest first; with the flag off, each action throws `News research is disabled for this deployment.`
- **Code anchors:** worker/src/index.ts, worker/src/researcher, packages/researcher, frontend/src/features/news-research/ResearcherPanel.tsx

## Draft generation (SSE)

### J-053 Generate a draft from the queue (SSE stream)
- **Persona:** Approved end user
- **Priority:** P0
- **CORE:** yes
- **External service:** LLM provider, Cloudflare
- **Preconditions:** `GENERATION_WORKER_URL` and `GENERATION_WORKER_SECRET` set on the main worker; a Draft topic; LLM key on the generation worker.
- **Steps:**
  1. In `/topics`, open the generate dialog (`GenWorkerDraftField`: Audience chips, Tone, CTA, Constraints) and click Generate.
  2. Frontend: `POST {WORKER_URL}/api/generate/stream` with `Authorization: Bearer T`, `Accept: text/event-stream`, body `{"spreadsheetId":"<id>","topicId":"<id>","topic":"...","tone":"...","audience":"...","constraints":"...","llm":{...},"skipImages":true,...}`.
  3. Watch progress events (`event: progress` with `{step,label,ts}`), then `event: complete` with `{variants:[{text}], runId, primaryPatternId, ...}`.
  4. UI calls `ACTION saveDraftVariants {"row":{...},"variants":["v1","v2","v3","v4"]}`.
- **Pass check:** Progress steps tick in the UI, completion alert "Draft generated" with N variants; row now has `variant1..4`; D1 `node_runs` gets rows (30-day TTL) and pattern metadata saved if `topicId` + `primaryPatternId`. Draft text must match topic, tone and rules (criterion 2): spot-check one output against the supplied constraints.
- **Code anchors:** frontend/src/features/ai-draft/GenWorkerDraftField.tsx, frontend/src/components/dashboard/hooks/useDashboardQueue.ts (`draftWithGenerationWorker`), frontend/src/services/backendApi.ts (`streamCallGenerationWorker`), worker/src/index.ts (`/api/generate/stream`), generation-worker/src/index.ts (`/v1/generate`), generation-worker/src/pipeline.ts

### J-054 Network drop in the middle of the generation stream
- **Persona:** Approved end user
- **Priority:** P1
- **CORE:** yes
- **External service:** LLM provider
- **Preconditions:** Generation in progress.
- **Steps:**
  1. Start J-053.
  2. Toggle the browser offline (DevTools) after the first progress event; also try closing the laptop lid / switching Wi-Fi.
  3. Go back online.
- **Pass check:** The async generator ends (or the `reader.read()` rejects) without a `complete` event; `draftWithGenerationWorker` then throws `Generation worker returned an invalid response (missing variants).` and `handleFailure` shows an alert; progress UI clears (`finally`). No partial variants are saved. Verify the topic stays `Draft` and the user can retry; also confirm the worker keeps running the pipeline and charges LLM tokens after the client left (the server loop only stops when the writer errors).
- **Code anchors:** frontend/src/services/backendApi.ts (`streamCallGenerationWorker`), frontend/src/components/dashboard/hooks/useDashboardQueue.ts, worker/src/index.ts (stream relay)

### J-055 Generation worker down, mis-secreted, or LLM error
- **Persona:** Approved end user
- **Priority:** P1
- **CORE:** yes
- **External service:** LLM provider, Cloudflare
- **Preconditions:** (a) generation worker stopped, (b) `GENERATION_WORKER_SECRET` != `WORKER_SHARED_SECRET`, (c) invalid LLM key.
- **Steps:**
  1. Run J-053 under each condition.
- **Pass check:** (a)/(b) main worker returns HTTP 502 `{"ok":false,"error":"Generation worker error: ..."}` and the UI shows `Generation stream error 502: ...`; (c) the SSE carries `event: error` `{message}`; UI shows the message via `handleFailure`; in all cases no row is modified. Unset `GENERATION_WORKER_URL`: HTTP 400 `GENERATION_WORKER_URL is not configured.`
- **Code anchors:** worker/src/index.ts, worker/src/generation/ (callGenerationWorkerStream), generation-worker/src/index.ts (`checkAuth`)

### J-056 "Send to Generation" button on a saved Draft topic
- **Persona:** Approved end user
- **Priority:** P1
- **CORE:** yes
- **External service:** Cloudflare, LLM provider
- **Preconditions:** A topic with status `Draft` and no variants (the card shows "Saved draft" with "Send to Generation").
- **Steps:**
  1. Click "Send to Generation" (`TopicPostPreviewCard`).
  2. Frontend: `POST {WORKER_URL}/` body `{"action":"sendTopicToGeneration","idToken":"T","payload":{"topicId":"<id>"}}` with `Accept: text/event-stream`.
  3. Observe the response and the row afterwards.
  - CODE-READING FINDING 1: after a successful generation-worker response the handler runs `UPDATE pipeline_rows SET status = 'Pending' ...`; there is no table `pipeline_rows` in any migration (the table is `pipeline_state`), so D1 throws and the request ends as HTTP 400 with a D1 error while the generation worker has already started.
  - CODE-READING FINDING 2: even if that SQL worked, the SSE relay in this branch only forwards blocks; unlike `/api/generate/stream` it never calls `saveDraftVariants`, and `TopicPostPreviewCard` only checks `response.ok` and navigates without reading the body, so generated variants are never stored.
- **Pass check:** Desired: Row moves Draft -> Pending -> has 4 variants and the UI shows them on `/topics/:topicId`. Currently expected to FAIL.
- **Code anchors:** frontend/src/components/dashboard/components/TopicPostPreviewCard.tsx, frontend/src/services/backendApi.ts (`sendTopicToGeneration`), worker/src/index.ts (`sendTopicToGeneration` block), worker/migrations/0001_pipeline_init.sql, worker/migrations/0010_pipeline_user_primary.sql

### J-057 Client-supplied `spreadsheetId` overrides the server's in generation
- **Persona:** Non-approved / unauthorised user
- **Priority:** P0
- **CORE:** yes
- **External service:** Google Sheets
- **Preconditions:** Tenant A and tenant B each with a sheet; A knows B's sheet id (ids are in URLs).
- **Steps:**
  1. As A: `POST {WORKER_URL}/api/generate/stream` with body `{"spreadsheetId":"<B's sheet id>","topic":"x","topicId":"<B's topic id>"}`.
  2. As A: `ACTION callGenerationWorker {"spreadsheetId":"<B's sheet id>","topic":"x"}`.
- **Pass check:** Desired: server ignores client `spreadsheetId` and uses `storedConfig.spreadsheetId`. CODE-READING FINDING: both handlers build `{ spreadsheetId: storedConfig.spreadsheetId, ...payload }`, so the client value wins (spread order). Check which downstream reads/writes in generation-worker use `spreadsheetId` (feedback, variants/clips by session, LLM settings keyed by spreadsheet) and whether B's data can be read or polluted.
- **Code anchors:** worker/src/index.ts (`/api/generate/stream`, `callGenerationWorker`), generation-worker/src/types.ts, generation-worker/src/pipeline.ts

### J-058 Streaming generation bypasses the monthly token budget
- **Persona:** Tenant admin
- **Priority:** P1
- **CORE:** yes
- **External service:** LLM provider
- **Preconditions:** SaaS mode (`DEPLOYMENT_MODE` unset or `saas`); a user whose month usage >= `monthly_token_budget`.
- **Steps:**
  1. As that user `ACTION generateQuickChange {...}`: expect `Monthly token budget exceeded`.
  2. As that user `POST /api/generate/stream` (the main generation path).
- **Pass check:** Desired: 429-style refusal on both. CODE-READING FINDING: `/api/quickchange/stream`, `generateQuickChange`, `generateVariantsPreview` and `callGenerationWorker` call `checkTokenBudget`; `/api/generate/stream` does not. Also `analyzeTopicInsights`, `analyzeFeedArticle`, `extractArticleInsights`, `clusterDraftClips`, `findDraftConnections`, `findDebateArticle`, `crossDomainInsight`, `opinionLeaderInsights`, `generateImageFromText` have no check.
- **Code anchors:** worker/src/index.ts, worker/src/auth.ts (`checkTokenBudget`), worker/src/db/llm-usage.ts

### J-059 Pick a writing pattern/template for generation
- **Persona:** Approved end user
- **Priority:** P2
- **CORE:** yes
- **External service:** Cloudflare
- **Preconditions:** `FEATURE_CONTENT_FLOW` on.
- **Steps:**
  1. In the review workspace use `TemplateSelector` (features/content-flow).
  2. API: `ACTION listPatterns {}` (proxies `GET {GEN}/v1/patterns/full`), `ACTION assignPattern {"row":{...},"patternId":"p","patternName":"n","patternRationale":"r","generationRunId":"id"}`, `ACTION getPatternAssignment {...}`, `ACTION listPatternAssignments {}`, `ACTION savePatternMetadata {"topicId":"<id>",...}`, `ACTION getTestGroup {...}`.
- **Pass check:** Patterns list loads; assignment persists on the row (`patternId`, `patternName`); if `GENERATION_WORKER_URL` is unset `listPatterns` returns `[]` silently (no message in UI?).
- **Code anchors:** frontend/src/features/content-flow/, worker/src/index.ts, worker/src/generation/, generation-worker/src/players/patternRepository.ts

### J-060 Generation worker is open when `WORKER_SHARED_SECRET` is empty
- **Persona:** Self-hosting operator
- **Priority:** P0
- **CORE:** yes
- **External service:** Cloudflare, LLM provider
- **Preconditions:** Generation worker deployed without `WORKER_SHARED_SECRET`.
- **Steps:**
  1. From any machine: `curl -X POST -H "Content-Type: application/json" -d '{...valid GenerateRequest...}' https://<gen-worker>/v1/generate`.
  2. `curl https://<gen-worker>/v1/llm/catalog`, `curl https://<gen-worker>/v1/patterns/full`.
- **Pass check:** Desired: 401 `{"error":"Unauthorized"}`. CODE-READING FINDING: `checkAuth` returns `true` when the secret is empty, and CORS is `Access-Control-Allow-Origin: *`; anyone can run the LLM pipeline on the operator's keys. The setup path generates the secret, but a manual deploy or a skipped secret leaves it open with no warning. Also, `Authorization` is compared as `Bearer <secret>` or the bare secret (string `===`, not timing-safe).
- **Code anchors:** generation-worker/src/index.ts (`checkAuth`, `corsHeaders`), setup/worker_config.py, setup/cloudflare.py

### J-061 Custom workflows (post types)
- **Persona:** Approved end user
- **Priority:** P2
- **CORE:** no
- **External service:** none
- **Preconditions:** None.
- **Steps:**
  1. Open the workflow builder (`WorkflowBuilderModal`), create a workflow.
  2. API: `ACTION createCustomWorkflow {...}` (see `CreateCustomWorkflowPayload`), `ACTION listCustomWorkflows {}`, `ACTION updateCustomWorkflow {...}`, `ACTION deleteCustomWorkflow {"id":"<id>"}`.
  3. Generate variants with that `postType` (`cw_` prefix): `ACTION generateVariantsPreview {...,"postType":"cw_<id>"}`.
- **Pass check:** CRUD scoped per user; the custom instruction (`generationInstruction`) is included in the variants prompt; an unknown workflow id silently proceeds without instruction.
- **Code anchors:** frontend/src/features/workflows/, worker/src/features/custom-workflows/, worker/src/index.ts (`generateVariantsPreview`)

### J-062 Node runs viewer (pipeline observability)
- **Persona:** Tenant admin
- **Priority:** P3
- **CORE:** no
- **External service:** none
- **Preconditions:** A prior generation (J-053).
- **Steps:**
  1. `ACTION getNodeRuns {"topicId":"<id>"}`.
  2. Wait 30 days / set `expires_at` to the past and call again.
- **Pass check:** Returns up to 500 rows for `user_id = caller` and `topic_id`; expired rows are purged opportunistically (best effort, up to 500 per call). Input/output JSON stored in D1 include prompts and drafts: confirm retention matches the privacy policy (30 days).
- **Code anchors:** worker/src/index.ts (`getNodeRuns`), worker/migrations/0012_node_runs.sql, worker/migrations/0013_data_retention_30day.sql, frontend/src/components/dashboard/hooks/useDashboardQueue.ts

## Review, edit, variants and images

### J-063 Open generated variants and pick one
- **Persona:** Approved end user
- **Priority:** P0
- **CORE:** yes
- **External service:** Google Sheets
- **Preconditions:** Topic with 4 variants (J-053).
- **Steps:**
  1. Click the topic row in `/topics`; route `/topics/:topicId` (`TopicVariantsOrDetail`).
  2. Page through the four variants (`VariantCarousel`), choose one -> route `/topics/:topicId/editor/:variantSlot` (slot 0-3).
  3. Reload the editor URL.
- **Pass check:** Selected variant text is in the editor; URL reload re-resolves the row from `getRows` (`findRowByTopicRouteId`); an unknown `topicId` redirects/handles gracefully (no white screen). With zero variants, the page offers generation.
- **Code anchors:** frontend/src/features/review/ReviewWorkspace.tsx, frontend/src/features/variant/, frontend/src/features/topic-navigation/utils/topicRoute.ts, frontend/src/features/topic-navigation/utils/workspaceRoutes.ts

### J-064 Manual edit with undo/redo; draft survives navigation
- **Persona:** Approved end user
- **Priority:** P1
- **CORE:** yes
- **External service:** none
- **Preconditions:** Editor open.
- **Steps:**
  1. Type in the center `DraftEditor`; press Ctrl/Cmd+Z and redo.
  2. Navigate to another route without saving, then come back; also reload the tab.
  3. Click the footer approve/save action.
- **Pass check:** Undo/redo works (history entries via `pushHistoryEntry`). Unsaved text after navigation/reload is lost unless the app autosaves; there is no `beforeunload` guard in the editor (grep), so the pass check is that a visible save state exists and `ACTION updateRowStatus {"row":{...},"status":"Approved","selectedText":"...","selectedImageId":"","postTime":"","emailTo":"","emailCc":"","emailBcc":"","emailSubject":"","selectedImageUrlsJson":""}` persists the text. Verify D1 `selected_text`.
- **Code anchors:** frontend/src/features/editor/DraftEditor.tsx, frontend/src/features/review-editor/, worker/src/persistence/pipeline-db/pipeline.ts (`updateRowStatus`)

### J-065 Quick Change via SSE
- **Persona:** Approved end user
- **Priority:** P1
- **CORE:** yes
- **External service:** LLM provider
- **Preconditions:** Editor with text; sheet connected (`ensureSpreadsheetConfigured`); budget available.
- **Steps:**
  1. Select text, choose a quick action (e.g. tighten), or type an instruction; run.
  2. Wire: `POST {WORKER_URL}/api/quickchange/stream` with `Authorization: Bearer T`, body `{"row":{...},"editorText":"...","instruction":"...","scope":"selection","selection":{"start":0,"end":10}}`; events `data: {"type":"node:start"|"enrichment:node_completed"|"complete"|"error", ...}`.
  3. Click Apply.
- **Pass check:** `complete` returns `{scope,model,llmProvider,selection,replacementText,fullText}`; applying updates the textarea and pushes undo history. Empty draft -> `error` event `Draft text is required before running Quick Change.`; empty instruction -> `Quick Change needs a per-run instruction.`; budget -> HTTP 429 JSON before the stream opens; stream closing without `complete` -> UI error `Quick change stream ended without result`.
- **Code anchors:** worker/src/index.ts (`/api/quickchange/stream`), frontend/src/services/backendApi.ts (`streamGenerateQuickChange`), frontend/src/components/dashboard/hooks/useDashboardQueue.ts (`handleGenerateQuickChange`)

### J-066 Variants preview for a selection
- **Persona:** Approved end user
- **Priority:** P2
- **CORE:** yes
- **External service:** LLM provider
- **Preconditions:** Editor with a draft.
- **Steps:**
  1. Request alternative wording ("4 variants") for the selected text.
  2. API: `ACTION generateVariantsPreview {"row":{...},"editorText":"...","scope":"selection","selection":{...},"postType":"<workflow id>"}`.
  3. Apply one, then `ACTION saveDraftVariants {"row":{...},"variants":[...],"previewSelection":{"selectedText":"...","selectedImageId":"","selectedImageUrlsJson":""}}`.
- **Pass check:** Preview returns variants; saving stores them on the row and the returned row replaces the local one. Budget exhausted -> `Monthly token budget exceeded`.
- **Code anchors:** worker/src/index.ts, frontend/src/features/variant/components, frontend/src/components/dashboard/hooks/useDashboardQueue.ts

### J-067 Pick and upload images for a post
- **Persona:** Approved end user
- **Priority:** P1
- **CORE:** yes
- **External service:** other (Google Cloud Storage, SerpAPI)
- **Preconditions:** `GOOGLE_CLOUD_STORAGE_BUCKET` and service account with `objectAdmin`; `SERPAPI_KEY` for search (if used).
- **Steps:**
  1. Editor -> Media tab (`ImageAssetManager`).
  2. Search more: `ACTION fetchDraftImages {"topic":"...","searchQuery":"","count":8}`.
  3. Promote a remote image: `ACTION promoteDraftImageUrl {...}`.
  4. Upload a file: `ACTION uploadDraftImage {"topicId":"<id>","fileName":"a.png","contentType":"image/png","dataUrl":"data:image/png;base64,..."}`; try a non-image data URL and a very large file.
  5. Download: `ACTION downloadDraftImage {...}`.
- **Pass check:** Search returns at most 8 URLs; upload returns `{imageUrl}` pointing into the bucket; non-image -> `Only image uploads are supported.`; missing `topicId` -> `topicId is required to upload an image.` No explicit size cap in `uploadDraftImage` (CODE-READING FINDING: only the Worker request limit applies; check behaviour and message for a 20 MB image). Selected URLs end up in `selected_image_urls_json`.
- **Code anchors:** frontend/src/components/ImageAssetManager.tsx, worker/src/index.ts (`fetchDraftImages`, `uploadDraftImage`, `promoteDraftImageUrl`, `downloadDraftImage`), frontend/src/services/selectedImageUrls.ts

### J-068 AI image generation (text and reference)
- **Persona:** Approved end user
- **Priority:** P2
- **CORE:** no
- **External service:** other (image generation provider via generation-worker/worker image-gen)
- **Preconditions:** Image-gen provider key set in the worker; provider chosen in `/settings` (`imageGen`).
- **Steps:**
  1. Media tab -> text-to-image panel (`ImageGenTextPanel`) and reference panel (`ImageGenReferencePanel`).
  2. API: `ACTION generateImageFromText {...}`; `ACTION generateImageWithReference {...}`.
- **Pass check:** A GCS URL is returned and appears in the image list; provider failures return an error string; LLM usage is logged against `userId` (the call passes `{db, spreadsheetId, userId}`) but no budget check precedes it.
- **Code anchors:** frontend/src/components/ImageGenTextPanel.tsx, frontend/src/components/ImageGenReferencePanel.tsx, worker/src/image-gen, worker/src/index.ts

### J-069 Content review checklist before publishing
- **Persona:** Approved end user
- **Priority:** P2
- **CORE:** yes
- **External service:** LLM provider
- **Preconditions:** `FEATURE_CONTENT_REVIEW` on; editor open.
- **Steps:**
  1. Click the content review indicator (`ContentReviewIndicator`) and run the review.
  2. API: `ACTION runContentReview {"row":{...},"editorText":"...","selectedImageUrls":["https://..."],"deliveryChannel":"linkedin"}`.
  3. Change the text and re-open.
- **Pass check:** Returns a report with `fingerprint`, `reviewedAt`; stored via `updateContentReview`; after editing, the indicator shows the report is stale (fingerprint mismatch). With the flag off: `Content review is disabled for this deployment.`
- **Code anchors:** frontend/src/features/content-review/, worker/src/features/content-review, worker/src/index.ts (`runContentReview`)

### J-070 Context document upload (txt, md, pdf)
- **Persona:** Approved end user
- **Priority:** P3
- **CORE:** no
- **External service:** none
- **Preconditions:** None.
- **Steps:**
  1. `ACTION uploadContextDocument {"contentBase64":"<b64>","mimeType":"text/plain","fileName":"n.txt"}`.
  2. Repeat with a 3 MB file, an `image/png`, and a PDF with scanned (no text) pages.
- **Pass check:** Returns `{documentId,extractedText,charCount}`; over 2 MB -> `File too large (...). Maximum is 2 MB.`; wrong mime -> `Unsupported file type: ... Allowed: txt, md, pdf.` PDF extraction is a naive printable-ASCII scan, so complex PDFs yield junk text (quality, not security). The text is returned to the client; confirm it is not persisted server-side without a retention policy.
- **Code anchors:** worker/src/index.ts (`handleUploadContextDocument`)

## Rules and templates

### J-071 Personal generation rules ("My rules")
- **Persona:** Approved end user
- **Priority:** P2
- **CORE:** yes
- **External service:** none
- **Preconditions:** Signed in.
- **Steps:**
  1. `/rules` -> "My rules" -> edit -> click "Save my rules".
  2. API: `ACTION saveUserSettings {"userRules":"Never use emojis"}`.
  3. Generate a draft (J-053) and check the rule is applied.
- **Pass check:** `{ok:true}`; D1 `users.user_rules` updated; next `bootstrap` returns `config.userRules`; the generated draft respects the rule (compare `effectiveRules` precedence: topic rules > template rules > user rules > global rules).
- **Code anchors:** frontend/src/pages/GlobalRulesPage.tsx, worker/src/index.ts (`saveUserSettings`, `loadStoredConfig`), worker/migrations/0009_user_tenant_settings.sql

### J-072 Global generation rules (admin) and history
- **Persona:** Tenant admin
- **Priority:** P2
- **CORE:** yes
- **External service:** none
- **Preconditions:** Admin.
- **Steps:**
  1. `/rules` -> "Global generation rules" -> edit -> "Save global rules".
  2. API: `ACTION saveConfig {"generationRules":"..."}` then `ACTION getGenerationRulesHistory {}`.
  3. Reopen "Saved version history" and restore a version.
- **Pass check:** History keeps the previous text with `savedAt`/`savedBy` (max 50). Non-admin: `Only admin users can change shared configuration.` Note the rules and author profile live in the single KV key `shared-config` (read-modify-write, no locking), so two admins saving at once or an OAuth callback landing between read and write can clobber each other (CODE-READING FINDING).
- **Code anchors:** frontend/src/pages/GlobalRulesPage.tsx, worker/src/index.ts (`saveConfig`, `getGenerationRulesHistory`)

### J-073 Author profile ("Who am I")
- **Persona:** Approved end user
- **Priority:** P2
- **CORE:** yes
- **External service:** none
- **Preconditions:** None.
- **Steps:**
  1. `/rules` -> author profile section (`WhoAmISection`), fill and save.
  2. API: `ACTION saveUserSettings {"userWhoAmI":"..."}`.
  3. Run Quick Change and check the voice.
- **Pass check:** `users.user_who_am_i` stored; `formatAuthorProfileForPrompt` is injected into quick-change and generation prompts; per-tenant value overrides workspace `authorProfile`.
- **Code anchors:** frontend/src/features/who-am-i/WhoAmISection.tsx, worker/src/index.ts

### J-074 Post templates CRUD
- **Persona:** Tenant admin
- **Priority:** P2
- **CORE:** yes
- **External service:** Google Sheets
- **Preconditions:** Sheet connected.
- **Steps:**
  1. `/rules` -> "Post templates" -> Create / "Save changes".
  2. API: `ACTION createPostTemplate {"name":"Case study","rules":"..."}`, `ACTION listPostTemplates {}`, `ACTION updatePostTemplate {"templateId":"<id>","name":"...","rules":"..."}`, `ACTION deletePostTemplate {"templateId":"<id>"}`.
  3. Disable the sheet and call `listPostTemplates`.
- **Pass check:** Templates round-trip in the sheet's template tab. With Sheets unreachable, `listPostTemplates` returns `[]` and logs the error (UI cannot tell "none" from "failed"). Without a sheet, `listPostTemplates` returns `[]`, while create/update/delete throw the missing-spreadsheet error.
- **Code anchors:** worker/src/index.ts, worker/src/persistence/drafts.ts (`SheetsGateway`), frontend/src/pages/GlobalRulesPage.tsx

### J-075 Per-topic rules and template precedence
- **Persona:** Approved end user
- **Priority:** P2
- **CORE:** yes
- **External service:** none
- **Preconditions:** Topic; at least one template.
- **Steps:**
  1. In the editor "Topic rules" tab edit rules: `ACTION saveTopicGenerationRules {"row":{...},"topicRules":"No hashtags"}`.
  2. Choose a template: `ACTION saveGenerationTemplateId {"row":{...},"generationTemplateId":"<id>"}`.
  3. Set channel/model: `ACTION saveTopicDeliveryPreferences {"row":{...},"topicDeliveryChannel":"linkedin","topicGenerationModel":"gemini-..."}`.
  4. Run Quick Change.
- **Pass check:** If topic rules are non-empty they win and the template is skipped (code: template rules are looked up only when `topicGenerationRules` is empty); `topicGenerationRules` also stores the scratchpad metadata JSON in the same column (CODE-READING FINDING: saving "topic rules" can overwrite the scratchpad JSON `{about,meaning,...}` that `sendTopicToGeneration` parses; verify).
- **Code anchors:** worker/src/index.ts, worker/src/persistence/pipeline-db/pipeline.ts, frontend/src/features/rules/RulesPanel.tsx

## Scheduling and publishing

### J-076 Publish now to LinkedIn
- **Persona:** Approved end user
- **Priority:** P0
- **CORE:** yes
- **External service:** LinkedIn
- **Preconditions:** LinkedIn connected for this user (J-094); text approved; sheet connected.
- **Steps:**
  1. Editor footer: click "Publish to LinkedIn" (label from `CHANNEL_OPTIONS`).
  2. Wire: `ACTION updateRowStatus {"row":{...},"status":"Approved","selectedText":"<text>","selectedImageId":"","postTime":"","emailTo":"","emailCc":"","emailBcc":"","emailSubject":"","selectedImageUrlsJson":""}` then `ACTION publishContent {"row":{...},"channel":"linkedin","message":"<text>","imageUrl":"","imageUrls":[]}`.
  3. Open the LinkedIn profile feed.
- **Pass check:** `publishContent` returns `{success:true,channel:"linkedin",messageId:"<urn>",deliveryMode:"sent",mediaMode:"text"|"image"}`; the post exists on LinkedIn with the exact approved text; D1 row `status='Published'`, `post_time` set; a line is appended to the posted-log Google Doc; the UI alert says `Published "<topic>" to LinkedIn as a text post.` Empty text -> `Approved content text is empty. Approve or edit the draft before sending it.`
- **Code anchors:** frontend/src/components/dashboard/hooks/useDashboardQueue.ts (`publishFromReviewEditor`, `publishRowToSelectedChannel`), worker/src/index.ts (`publishContent`, `markPublishedForChannel`), worker/src/integrations/linkedin

### J-077 Publish to Instagram (image required)
- **Persona:** Approved end user
- **Priority:** P1
- **CORE:** yes
- **External service:** Instagram
- **Preconditions:** Instagram Business account connected (J-095); a selected image URL reachable by Meta.
- **Steps:**
  1. Select channel Instagram, choose an image in the Media tab, click "Publish to Instagram".
  2. `ACTION publishContent {"row":{...},"channel":"instagram","message":"caption","imageUrls":["https://..."]}`.
  3. Repeat with no image.
- **Pass check:** Step 2 returns `messageId` = Instagram post id and the post is live; step 3 -> `Instagram publishing requires a selected image.` Carousel: up to `MAX_IMAGES_PER_POST` images. Selected-but-private GCS URLs would make Meta reject the media; confirm bucket objects are public-readable (see J-143).
- **Code anchors:** worker/src/index.ts (`publishContent` instagram branch), worker/src/integrations/instagram

### J-078 Send via Gmail
- **Persona:** Approved end user
- **Priority:** P1
- **CORE:** yes
- **External service:** Gmail
- **Preconditions:** Gmail connected (J-096); To address.
- **Steps:**
  1. Editor -> Email tab: fill To, Cc, Bcc, Subject; the form saves via `ACTION saveEmailFields {"row":{...},"emailTo":"a@b.co","emailCc":"","emailBcc":"","emailSubject":"Hi"}`.
  2. Click "Send via Gmail": `ACTION publishContent {"row":{...},"channel":"gmail","message":"..."}`.
  3. Repeat with an empty To.
- **Pass check:** Mail arrives with subject/body; row `Published`; empty To -> UI notice "Gmail needs at least one To address..."; refresh-token revoked -> actionable error and `needs_reauth` visible in `/connections`.
- **Code anchors:** frontend/src/features/review-editor/components, worker/src/index.ts (gmail branch), worker/src/integrations/gmail

### J-079 Send via WhatsApp
- **Persona:** Approved end user
- **Priority:** P1
- **CORE:** yes
- **External service:** WhatsApp
- **Preconditions:** WhatsApp connected by an admin (J-099) with a phone number id; recipient number in the delivery panel.
- **Steps:**
  1. Delivery panel (`DashboardDelivery`): pick a recipient; click "Send via WhatsApp".
  2. `ACTION publishContent {"row":{...},"channel":"whatsapp","recipientId":"+15551234567","message":"..."}`.
  3. Use an invalid number and a recipient outside the 24-hour window.
- **Pass check:** `messageId` = wamid; invalid number -> normalizer error; the code sends non-template messages ("Send non-template WhatsApp messages through Meta Cloud API"), which Meta rejects outside the customer service window: the error text from Meta must reach the user.
- **Code anchors:** frontend/src/components/dashboard/tabs/DashboardDelivery.tsx, worker/src/index.ts (`normalizePhoneNumber`, whatsapp branch), worker/src/integrations/whatsapp

### J-080 Send via Telegram
- **Persona:** Approved end user
- **Priority:** P1
- **CORE:** yes
- **External service:** Telegram
- **Preconditions:** `TELEGRAM_BOT_TOKEN` or stored token; chat verified by an admin (J-104).
- **Steps:**
  1. Pick a verified chat in the delivery panel; click "Send via Telegram".
  2. `ACTION publishContent {"row":{...},"channel":"telegram","recipientId":"@mychannel","message":"..."}`.
- **Pass check:** Message appears in the chat; returns `messageId`; invalid chat id -> `Enter a valid Telegram chat ID or @channel username.`; bot not admin of the channel -> Telegram's error is surfaced.
- **Code anchors:** worker/src/index.ts (telegram branch, `normalizeTelegramChatId`), worker/src/integrations/telegram

### J-081 YouTube as a publish target
- **Persona:** Approved end user
- **Priority:** P2
- **CORE:** no
- **External service:** YouTube
- **Preconditions:** YouTube "connected" (J-097).
- **Steps:**
  1. Open the channel selector; `CHANNEL_OPTIONS` includes `youtube` with `publishVerb: 'YouTube Automations'`.
  2. `ACTION publishContent {"row":{...},"channel":"youtube","message":"x"}`.
- **Pass check:** (NOT IMPLEMENTED per code reading: `coerceChannelId` in worker/src/index.ts accepts only instagram, linkedin, telegram, whatsapp, gmail, and throws `Unsupported delivery channel.` for youtube; `worker/src/automations/platforms/youtube.ts` is comment-reply automation only). The README claim "publish to ... YouTube" is therefore not true for posts; confirm the UI does not offer a publish button for it.
- **Code anchors:** worker/src/index.ts (`coerceChannelId`), frontend/src/integrations/channels.ts, worker/src/automations/platforms/youtube.ts, README.md

### J-082 Schedule a future post (queued via Durable Object)
- **Persona:** Approved end user
- **Priority:** P0
- **CORE:** yes
- **External service:** LinkedIn, Cloudflare
- **Preconditions:** LinkedIn connected; DO binding `SCHEDULED_LINKEDIN_PUBLISH` present (J-133).
- **Steps:**
  1. In the editor, set a schedule time (control `aria-label="Schedule post time"`) 10 minutes ahead; click publish.
  2. Wire: `ACTION updateRowStatus {... "postTime":"2026-10-28 09:30" ...}` then `ACTION publishContent {"row":{... "postTime":"2026-10-28 09:30"},"channel":"linkedin","message":"..."}`.
  3. Observe the `ScheduledPublishBanner`; `/topics` shows the row as scheduled.
  4. Wait for the time.
- **Pass check:** Step 2 returns `deliveryMode:"queued"`, `scheduledTime:"2026-10-28 09:30"`; alert "Scheduled ... queued for LinkedIn at ...". Posted at the time (see J-083 for what actually runs). The `postTime` format must be `YYYY-MM-DD HH:mm` or `parseScheduledTimeToTimestamp` returns null and the post publishes immediately.
- **Code anchors:** worker/src/index.ts (`publishContent`, `armScheduledPublish`), worker/src/scheduled-publish/*, frontend/src/features/scheduled-publish/, frontend/src/features/content-schedule-calendar/

### J-083 Alarm fires: what the scheduled run actually executes
- **Persona:** Background / agent actor
- **Priority:** P0
- **CORE:** yes
- **External service:** LinkedIn, Cloudflare, Google Sheets
- **Preconditions:** A post queued per J-082 by a tenant (non-admin) whose sheet is in D1 `users.spreadsheet_id`, with its own LinkedIn token in D1 `social_integrations`.
- **Steps:**
  1. Let the Durable Object alarm fire (`ScheduledPublishAlarm.alarm()` -> `executeScheduledPublish(env, task)`).
  2. Read worker logs (`observability` enabled) and the row status.
  - CODE-READING FINDING A: `armScheduledPublish` is called with `userId`, but `handleArm` persists only `{topicId,topic,date,scheduledTime,intent,channel,recipientId}`; `userId` is dropped, so `task.userId` is undefined at fire time.
  - CODE-READING FINDING B: `executeScheduledPublish` calls `loadStoredConfig(env)` and `buildServices(env)` with no user, so `config.spreadsheetId` is the KV `shared-config` sheet (not the tenant's) and `pipeline` has `userId=''`; `getRowByTopicId` finds no row and the function returns silently (`if (!row) return;`).
  - CODE-READING FINDING C: every guard in `executeScheduledPublish` (`status != approved`, `postTime mismatch`, empty text) returns without logging or marking the row, so failures are invisible.
- **Pass check:** At the scheduled time the post appears on the right account, D1 row `status='Published'`. Currently expected to FAIL for multi-tenant (non-admin or non-KV-sheet) users; for the single-owner self-hosted deployment (admin sheet == KV sheet, global LinkedIn token) it likely works. A row that stays `Approved` after the time with no log line is the symptom.
- **Code anchors:** worker/src/scheduled-publish/ScheduledPublishAlarm.ts, worker/src/scheduled-publish/durablePublishScheduler.ts, worker/src/scheduled-publish/types.ts, worker/src/index.ts (`executeScheduledPublish`, `loadStoredConfig`, `buildServices`), worker/src/services.ts

### J-084 Cancel a scheduled post
- **Persona:** Approved end user
- **Priority:** P1
- **CORE:** yes
- **External service:** Cloudflare
- **Preconditions:** A queued post (J-082).
- **Steps:**
  1. Click "Cancel schedule" in the banner / delivery panel.
  2. Wire: `ACTION cancelScheduledPublish {"topicId":"<id>","scheduledTime":"2026-10-28 09:30","channel":"linkedin"}`.
  3. Repeat with a wrong `scheduledTime`, and with a `topicId` of another tenant's post.
- **Pass check:** `{success:true,cancelled:true}`; DO storage and alarm removed; the post does not fire. Wrong time -> `Scheduled time does not match the armed task. Refresh and try again.` (409 inside the DO, surfaced as an Error). CODE-READING FINDING: the dispatcher does not check that the caller owns `topicId` (DO name is `topicId::channel`, no user component); any signed-in user who knows both values can cancel. Note `channel` omitted defaults to `linkedin`, so cancelling a non-LinkedIn schedule without `channel` silently reports `cancelled:false`.
- **Code anchors:** worker/src/scheduled-publish/handleCancelDispatch.ts, worker/src/scheduled-publish/ScheduledPublishAlarm.ts, frontend/src/features/scheduled-publish/ScheduledPublishBanner.tsx, frontend/src/features/scheduled-publish/usePendingScheduledPublish.ts

### J-085 Schedule in the past
- **Persona:** Approved end user
- **Priority:** P1
- **CORE:** yes
- **External service:** LinkedIn
- **Preconditions:** Editor open.
- **Steps:**
  1. In the calendar or editor schedule control pick a time earlier than now (the UI helper `isLocalScheduleInPast` should block it).
  2. API bypass: `ACTION publishContent {"row":{... "postTime":"2020-01-01 00:00"},"channel":"linkedin","message":"x"}`.
- **Pass check:** UI blocks or warns on a past slot. API: because the arm branch requires `scheduledAt > Date.now() + 60000`, a past or near-now `postTime` is NOT queued: the call publishes immediately and returns `deliveryMode:"sent"`. The user who typed a past time must be told this will publish now before they confirm.
- **Code anchors:** frontend/src/features/content-schedule-calendar/scheduleValidation.ts, worker/src/index.ts (`publishContent`)

### J-086 Timezone semantics of a scheduled time
- **Persona:** Approved end user
- **Priority:** P1
- **CORE:** yes
- **External service:** LinkedIn, Cloudflare
- **Preconditions:** Browser timezone different from UTC (e.g. IST, UTC+5:30).
- **Steps:**
  1. Schedule a post for local 09:30 (UI sends `postTime: "2026-10-28 09:30"`, local wall time, no zone).
  2. Read the worker logic: `parseScheduledTimeToTimestamp` uses `Date.UTC(y, m-1, d, h, min)`.
  3. Compare the actual fire time to 09:30 local.
- **Pass check:** Desired: fires at 09:30 local. CODE-READING FINDING: the string is interpreted as UTC, so a UTC+5:30 user's 09:30 post fires at 15:00 local; a UTC-8 user's fires 8 h early (and a "future" local time may be already "in the past" in UTC, see J-085). The same applies to the DO check `row.postTime === task.scheduledTime`. No timezone is stored with the row.
- **Code anchors:** worker/src/scheduled-publish/time.ts, frontend/src/features/content-schedule-calendar/calendarTemporal.ts, frontend/src/features/content-schedule-calendar/scheduleValidation.ts, worker/src/index.ts

### J-087 Calendar drag-reschedule of an already queued post
- **Persona:** Approved end user
- **Priority:** P1
- **CORE:** yes
- **External service:** Cloudflare
- **Preconditions:** A queued scheduled post (J-082).
- **Steps:**
  1. Open the schedule calendar; drag the event to a later slot (`handleCalendarRescheduleCommit`).
  2. Wire: `ACTION updatePostSchedule {"row":{...},"postTime":"2026-10-29 10:00"}`.
  3. Wait past the OLD time and past the NEW time.
- **Pass check:** Desired: post fires at the new time only. CODE-READING FINDING: `updatePostSchedule` only updates the row's `postTime`; nothing re-arms a Durable Object (`armScheduledPublish` is called only from `publishContent`). At the old time the DO runs `executeScheduledPublish`, sees `row.postTime != task.scheduledTime` and silently returns; no DO exists for the new time, so the post never fires. Errors in the drag handler are swallowed (`catch {}`), so the UI shows the new slot as fine.
- **Code anchors:** frontend/src/components/dashboard/index.tsx (`handleCalendarRescheduleCommit`, `handleUpdatePostSchedule`), worker/src/index.ts (`updatePostSchedule`, `publishContent`), worker/src/scheduled-publish/ScheduledPublishAlarm.ts

### J-088 Double-click on Publish
- **Persona:** Approved end user
- **Priority:** P1
- **CORE:** yes
- **External service:** LinkedIn
- **Preconditions:** Ready-to-publish draft.
- **Steps:**
  1. Double-click (or press Enter twice) on "Publish to LinkedIn".
  2. Server-side: send the same `ACTION publishContent {...}` twice in parallel with `curl`.
- **Pass check:** Exactly one post on LinkedIn. UI guard: `if (actionLoading !== null) return;` is React state, so two clicks in one tick may both pass; server guard: `publishContent` has no idempotency key and no "already Published" check for the immediate path (only `executeScheduledPublish` checks status). Expect two posts for the parallel curl (CODE-READING FINDING). A second click after completion goes through the "Republish" confirm only in the queue, not in the editor.
- **Code anchors:** frontend/src/components/dashboard/hooks/useDashboardQueue.ts (`actionLoading`), worker/src/index.ts (`publishContent`)

### J-089 Post is live but marking it Published fails
- **Persona:** Approved end user
- **Priority:** P1
- **CORE:** yes
- **External service:** LinkedIn, Google Sheets
- **Preconditions:** Ability to fail D1/Sheets writes (e.g. revoke the service account's access to the sheet).
- **Steps:**
  1. Publish to LinkedIn (J-076) while Sheets write fails.
  2. Observe UI and LinkedIn.
  3. Click publish again.
- **Pass check:** Order in code: send to channel first, then `markRowPublished` and `appendToPostedDoc`. A failure after a successful send surfaces "Failed to send the approved message..." to the user, the row stays `Approved`, and a retry posts a duplicate (CODE-READING FINDING). Pass requires the success to be reported or the retry to detect the existing post.
- **Code anchors:** worker/src/index.ts (`publishContent`, `markPublishedForChannel`, `appendToPostedDoc`), worker/src/persistence/pipeline-db/pipeline.ts (`markRowPublished`)

### J-090 Publish fails because the channel token was revoked or expired
- **Persona:** Approved end user
- **Priority:** P1
- **CORE:** yes
- **External service:** LinkedIn
- **Preconditions:** LinkedIn token revoked from the LinkedIn side (or past the 60 days stored in `token_expires_at`).
- **Steps:**
  1. Publish to LinkedIn.
  2. Open `/connections`.
- **Pass check:** User sees the LinkedIn error text (not a blank failure), the row stays `Approved`, and `/connections` shows the account as needing reconnect (`needsReauth` flag from `listSocialIntegrations`). There is no refresh-token logic for LinkedIn (60 day token); confirm the user is warned before expiry. For a scheduled post the failure is only a console log (J-083).
- **Code anchors:** worker/src/index.ts (linkedin branch), worker/src/db/socialIntegrations.ts, frontend/src/pages/connections/ConnectionsPage.tsx, worker/src/integrations/linkedin

### J-091 Republish an already published post
- **Persona:** Approved end user
- **Priority:** P2
- **CORE:** yes
- **External service:** LinkedIn
- **Preconditions:** A `Published` row.
- **Steps:**
  1. In the queue choose "Republish"; confirm "Confirm Publish".
  2. Or in the editor edit and publish (the hook calls `createDraftFromPublished` first).
  3. API: `ACTION createDraftFromPublished {"row":{...},"selectedText":"...","selectedImageId":"","postTime":"","emailTo":"","emailCc":"","emailBcc":"","emailSubject":"","selectedImageUrlsJson":""}`.
- **Pass check:** Republish shows the confirm dialog; editor path creates a NEW draft row (original untouched, alert "Draft saved"); the new row publishes. Needs a sheet (`ensureSpreadsheetConfigured`).
- **Code anchors:** frontend/src/components/dashboard/hooks/useDashboardQueue.ts (`republishRowToSelectedChannel`, `publishFromReviewEditor`), worker/src/index.ts (`createDraftFromPublished`)

### J-092 Durable Object alarm throws and is retried
- **Persona:** Background / agent actor
- **Priority:** P2
- **CORE:** yes
- **External service:** Cloudflare, LinkedIn
- **Preconditions:** Queued post; make the publish throw (bad token).
- **Steps:**
  1. Let the alarm run; `alarm()` logs "Scheduled LinkedIn publish alarm failed" and rethrows.
  2. Observe Cloudflare retry behaviour and the row.
- **Pass check:** Failure visible somewhere a user can see (row state or banner), no more than N retries, and no duplicate post if a retry occurs after the channel call succeeded but before `markRowPublished`. Current code has no failure status written to the row (CODE-READING FINDING).
- **Code anchors:** worker/src/scheduled-publish/ScheduledPublishAlarm.ts (`alarm`), worker/src/index.ts (`executeScheduledPublish`)

## Connections and OAuth

### J-093 Connections page overview
- **Persona:** Approved end user
- **Priority:** P2
- **CORE:** yes
- **External service:** none
- **Preconditions:** Signed in (admin, see J-031).
- **Steps:**
  1. Open `/connections`.
  2. `ACTION getIntegrations {}`.
- **Pass check:** Cards for LinkedIn, Instagram, Gmail, WhatsApp, Telegram, YouTube plus the Google Sheet card; connected providers show a green "Connected" dot; list matches `{provider,internalId,displayName,profilePicture,needsReauth,connectedAt}`.
- **Code anchors:** frontend/src/pages/connections/ConnectionsPage.tsx, frontend/src/pages/connections/SocialAccountCard.tsx, worker/src/db/socialIntegrations.ts

### J-094 Connect LinkedIn (popup OAuth)
- **Persona:** Approved end user
- **Priority:** P1
- **CORE:** yes
- **External service:** LinkedIn
- **Preconditions:** Worker has `LINKEDIN_CLIENT_ID`, `LINKEDIN_CLIENT_SECRET`, `SECRET_ENCRYPTION_KEY`; redirect URI `{worker origin}/auth/linkedin/callback` registered in the LinkedIn app.
- **Steps:**
  1. `/connections` -> LinkedIn -> Connect.
  2. Wire: `ACTION startLinkedInAuth {}` -> `{authorizationUrl,callbackOrigin}`; popup opens `https://www.linkedin.com/oauth/v2/authorization?...scope=openid profile w_member_social`.
  3. Authorize; LinkedIn redirects to `GET /auth/linkedin/callback?code=...&state=...`.
  4. Popup posts `{source:"channel-bot-oauth",provider:"linkedin",ok:true}` to the opener and the UI refetches `getIntegrations`.
- **Pass check:** `social_integrations` has a row `(user_id, 'linkedin')` with encrypted token and `token_expires_at` ~60 days; card shows Connected. KV `shared-config` also gets the token (see J-103).
- **Code anchors:** worker/src/index.ts (`startLinkedInAuth`, `handleLinkedInCallback`, `consumeOAuthState`, `oauthPopupResponse`), frontend/src/App.tsx (`handleConnect`), worker/src/integrations/linkedin

### J-095 Connect Instagram
- **Persona:** Approved end user
- **Priority:** P1
- **CORE:** yes
- **External service:** Instagram
- **Preconditions:** `INSTAGRAM_APP_ID`, `INSTAGRAM_APP_SECRET`; redirect `/auth/instagram/callback` registered; account is Business/Creator.
- **Steps:**
  1. `/connections` -> Instagram -> Connect (`ACTION startInstagramAuth {}`).
  2. Authorize in popup; callback `GET /auth/instagram/callback`.
- **Pass check:** `social_integrations` row for `instagram` with username; `bootstrap.config.hasInstagramAccessToken` true; missing app id -> `Instagram OAuth is not configured in the Worker environment. Add INSTAGRAM_APP_ID and INSTAGRAM_APP_SECRET first.`
- **Code anchors:** worker/src/index.ts (`startInstagramAuth`, `handleInstagramCallback`), worker/src/integrations/instagram

### J-096 Connect Gmail
- **Persona:** Approved end user
- **Priority:** P1
- **CORE:** yes
- **External service:** Gmail, Google OAuth
- **Preconditions:** `GMAIL_CLIENT_ID`, `GMAIL_CLIENT_SECRET` on the worker; redirect `/auth/gmail/callback` registered; scopes `gmail.send` + `email`.
- **Steps:**
  1. `/connections` -> Gmail -> Connect (`ACTION startGmailAuth {}`).
  2. Authorize; callback `GET /auth/gmail/callback`.
- **Pass check:** Row for `gmail` with refresh token (access type offline must be requested, else sends fail after 1 hour; verify the authorization URL contains `access_type=offline` and `prompt=consent`); `config.gmailEmailAddress` populated.
- **Code anchors:** worker/src/index.ts (`startGmailAuth`, `handleGmailCallback`, `GMAIL_OAUTH_SCOPES`), worker/src/integrations/gmail

### J-097 Connect YouTube
- **Persona:** Approved end user
- **Priority:** P2
- **CORE:** no
- **External service:** YouTube
- **Preconditions:** Google OAuth client with YouTube scopes enabled; `/auth/youtube/callback` registered.
- **Steps:**
  1. `/connections` -> YouTube -> Connect (`ACTION startYouTubeAuth {}`).
  2. Authorize; callback `GET /auth/youtube/callback`.
- **Pass check:** Row `youtube` with channel title (`persistYouTubeConnection`, `upsertSocialIntegration`); `youtubeAuthAvailable` true in `bootstrap.config`; this only enables comment automation (J-118), not publishing (J-081).
- **Code anchors:** worker/src/index.ts (`startYouTubeAuth`, `handleYouTubeCallback`), worker/src/automations/platforms/youtube.ts

### J-098 OAuth popup closed, blocked or cancelled
- **Persona:** New signed-in user
- **Priority:** P2
- **CORE:** yes
- **External service:** LinkedIn
- **Preconditions:** None.
- **Steps:**
  1. Click Connect with the popup blocker on (`window.open` returns null).
  2. Click Connect, then close the popup without authorizing.
  3. Click Connect, then click "Cancel" on the provider page (provider returns `error=access_denied`).
- **Pass check:** Step 1: user sees guidance (CODE-READING FINDING: `handleConnect` uses `popup?.closed`, a null popup hangs the promise only until the interval sees `undefined?.closed` -> undefined, so the promise never resolves and `connecting` stays set; verify). Step 2: promise resolves, integrations refetched, no error. Step 3: popup shows the provider error text and the opener gets `ok:false` -> thrown Error only reaches `console.error` (no user-visible message).
- **Code anchors:** frontend/src/App.tsx (`handleConnect`), worker/src/index.ts (`oauthPopupResponse`)

### J-099 Connect WhatsApp (admin only, phone selection)
- **Persona:** Tenant admin
- **Priority:** P2
- **CORE:** yes
- **External service:** WhatsApp
- **Preconditions:** `META_APP_ID`, `META_APP_SECRET`; WhatsApp Business Account with at least one phone number; admin session.
- **Steps:**
  1. `/connections` -> WhatsApp -> Connect: `ACTION startWhatsAppAuth {}` (admin-guarded).
  2. Callback `GET /auth/whatsapp/callback` stores a pending record `whatsapp-pending:<connectionId>` (TTL 10 min) and posts `{connectionId, options:[{phoneNumberId,verifiedName,displayPhoneNumber}]}`.
  3. UI auto-selects `options[0]`: `ACTION completeWhatsAppConnection {"connectionId":"<id>","phoneNumberId":"<id>"}`.
  4. Non-admin presses Connect.
- **Pass check:** `bootstrap.config.whatsappPhoneNumberId` set; non-admin gets `Only admin users can change shared configuration.`; with multiple phone numbers the UI picks the first one without asking (CODE-READING FINDING: App.tsx comment "auto-select the first phone"); a connection session from a different admin is refused.
- **Code anchors:** worker/src/index.ts (`startWhatsAppAuth`, `handleWhatsAppCallback`, `completeWhatsAppConnection`), frontend/src/App.tsx

### J-100 Replayed or expired OAuth `state`
- **Persona:** Background / agent actor
- **Priority:** P2
- **CORE:** yes
- **External service:** LinkedIn
- **Preconditions:** A completed callback URL with its `state`.
- **Steps:**
  1. Open the same callback URL a second time.
  2. Open `GET /auth/linkedin/callback?code=x` without `state`.
  3. Open it with a state older than 10 minutes (`OAUTH_STATE_TTL_SECONDS = 600`).
- **Pass check:** Step 1/3 -> popup text `The OAuth session is missing or expired. Start the connection again.`; step 2 -> `Missing LinkedIn OAuth state.`; state key is deleted on first read (`consumeOAuthState`), so no replay; an attacker cannot attach their account to a victim's email because `email` is taken from the stored state, not the callback.
- **Code anchors:** worker/src/index.ts (`consumeOAuthState`, `storeOAuthState`, `handleLinkedInCallback`)

### J-101 OAuth misconfiguration: missing or wrong client id/secret, wrong redirect URI
- **Persona:** Self-hosting operator
- **Priority:** P1
- **CORE:** yes
- **External service:** LinkedIn
- **Preconditions:** (a) `LINKEDIN_CLIENT_ID` unset, (b) wrong id, (c) redirect URI not registered, (d) `OAUTH_REDIRECT_BASE_URL` wrong.
- **Steps:**
  1. `ACTION startLinkedInAuth {}` for (a).
  2. Click Connect for (b), (c), (d) in the UI.
- **Pass check:** (a) HTTP 400 `LinkedIn OAuth is not configured in the Worker environment. Add LINKEDIN_CLIENT_ID and LINKEDIN_CLIENT_SECRET first.`; the UI card should hide Connect when `linkedinAuthAvailable` is false. CODE-READING FINDING: for every failure `handleConnect` only does `console.error('OAuth connect failed:', err)`, so the user sees nothing happen. (b)-(d) fail inside the provider popup page; the operator needs a doc entry for the exact redirect URIs (`{origin}/auth/<provider>/callback`).
- **Code anchors:** frontend/src/App.tsx (`handleConnect`), worker/src/index.ts (`hasLinkedInOAuthConfig`, `buildWorkerOrigin`, `requireFrontendOrigin`), SETUP.md

### J-102 Disconnect a channel: three different "disconnect" behaviours
- **Persona:** Approved end user
- **Priority:** P1
- **CORE:** yes
- **External service:** LinkedIn
- **Preconditions:** LinkedIn connected.
- **Steps:**
  1. `/connections` -> LinkedIn -> Disconnect: UI calls `ACTION deleteIntegration {"provider":"linkedin"}` (D1 row only).
  2. Publish to LinkedIn afterwards.
  3. Admin: `ACTION disconnectChannelAuth {"provider":"linkedin"}` (KV `disconnectedAuthProviders`).
- **Pass check:** After a user disconnects, publishing must fail with a "not connected" message. CODE-READING FINDING: `publishContent` falls back to the shared KV token (J-103) when the per-user row is missing, so the post still goes out under the operator's/previous user's account. Telegram "Disconnect" (`onDisconnect('telegram')`) also only deletes a D1 integration row and leaves the KV bot token.
- **Code anchors:** frontend/src/App.tsx (`handleDisconnect`), worker/src/index.ts (`deleteIntegration`, `disconnectChannelAuth`, `publishContent`), worker/src/db/socialIntegrations.ts

### J-103 A user with no LinkedIn connection publishes through someone else's token
- **Persona:** Non-approved / unauthorised user
- **Priority:** P0
- **CORE:** yes
- **External service:** LinkedIn
- **Preconditions:** SaaS; user A connected LinkedIn earlier; user B signed up, never connected anything, has a sheet (J-031 resolved).
- **Steps:**
  1. As B: `ACTION publishContent {"row":{...},"channel":"linkedin","message":"hello"}`.
  2. Inspect which account posted.
  - CODE-READING FINDING: each OAuth callback calls `persistLinkedInConnection(env, accessToken, personUrn)` which writes the KV `shared-config` (single global slot, last writer wins) in addition to the per-user D1 row. `publishContent` tries `getSocialIntegration(userId,'linkedin')` first and falls back to `config.linkedin*` from KV when B has none, so B posts as A (or whoever connected last). Same pattern for Instagram, Gmail, WhatsApp, Telegram and the trending actions (env tokens).
- **Pass check:** Desired: B gets `LinkedIn publishing is not configured...`/"connect your account" and nothing is posted. Expected to FAIL today in multi-tenant deployments (single-owner self-hosted is fine and relies on this fallback).
- **Code anchors:** worker/src/index.ts (`publishContent`, `persistLinkedInConnection`, `handleLinkedInCallback`, `loadStoredConfig`), worker/src/db/socialIntegrations.ts

### J-104 Telegram chat verification (admin)
- **Persona:** Tenant admin
- **Priority:** P2
- **CORE:** yes
- **External service:** Telegram
- **Preconditions:** Bot token from BotFather; bot added to the target chat/channel.
- **Steps:**
  1. `/connections` -> Telegram: enter Chat ID (or `@channel`) and optional bot token; click verify.
  2. Wire: `ACTION verifyTelegramChat {"chatId":"@mychannel","botToken":"123:abc"}`.
  3. Try as a non-admin; try with a wrong chat id.
- **Pass check:** Returns `TelegramChatVerificationResult` (chat title/type); non-admin -> `Only admin users can change shared configuration.` (so ordinary tenants cannot set up Telegram even though the card is visible); invalid chat -> Telegram error text; the pasted bot token is sent to the worker over HTTPS and is not logged.
- **Code anchors:** frontend/src/pages/connections/ConnectionsPage.tsx, worker/src/index.ts (`verifyTelegramChat`), worker/src/integrations/telegram

### J-105 Stored token can no longer be decrypted (key rotated)
- **Persona:** Self-hosting operator
- **Priority:** P2
- **CORE:** yes
- **External service:** Instagram
- **Preconditions:** Tokens stored under the old `SECRET_ENCRYPTION_KEY`; key replaced.
- **Steps:**
  1. Publish to Instagram (or LinkedIn / Gmail / Telegram / WhatsApp).
- **Pass check:** Error `The stored Instagram access token can no longer be decrypted. Ask an admin to open Settings and save the token again.` (and the KV ciphertext is cleared for Instagram); per-user D1 rows fall through to the shared token silently (`catch { // Fall through }`). Settings has no obvious "save token again" field now that OAuth is the flow: confirm the message is actionable (CODE-READING FINDING: the message points to Settings; the real remedy is reconnect on `/connections`).
- **Code anchors:** worker/src/index.ts (`*_TOKEN_REAUTH_MESSAGE`, `requireSecretEncryptionKey`, `publishContent`), worker/src/db/socialIntegrations.ts

## Campaigns and bulk

### J-106 Bulk import by pasting campaign JSON
- **Persona:** Approved end user
- **Priority:** P2
- **CORE:** no
- **External service:** Google Sheets
- **Preconditions:** `FEATURE_CAMPAIGN` true; sheet connected.
- **Steps:**
  1. `/campaign` -> choose "Paste JSON" -> paste `{"version":1,"posts":[{"topicId":"t1","topic":"...","date":"2026-11-01","variants":["a","b"],"postTime":"2026-11-01 09:00"}]}`.
  2. Review in the list/calendar, click import.
  3. Wire: `ACTION bulkImportCampaign {"posts":[{...}]}`.
- **Pass check:** Returns `{success:true,imported:N}`; rows appear in `/topics` as Draft; invalid JSON is caught by `parseCampaignPaste` in the UI with a field-level message; with `campaign: false` the route redirects to `/topics` and the action throws `Campaign import is disabled for this deployment.`
- **Code anchors:** frontend/src/features/campaign/CampaignPage.tsx, frontend/src/features/campaign/validate/, worker/src/persistence/drafts.ts (`coerceBulkCampaignPostsFromPayload`), worker/src/index.ts (`bulkImportCampaign`)

### J-107 Bulk import from a file (.json, .jsonc, .csv)
- **Persona:** Approved end user
- **Priority:** P2
- **CORE:** no
- **External service:** none
- **Preconditions:** A CSV with the expected columns.
- **Steps:**
  1. `/campaign` -> "Upload file" (`accept=".json,.jsonc,.csv"`).
  2. Upload a CSV, a malformed CSV, and a 5,000-row file.
- **Pass check:** CSV rows convert to the JSON editor content (`setPasteText(JSON.stringify({version:1,posts},...))`); malformed rows give a visible error; a large file either imports or fails with a clear size message rather than a silent timeout (no server-side batch limit visible in `bulkImportCampaign`).
- **Code anchors:** frontend/src/features/campaign/CampaignPage.tsx, frontend/src/features/campaign/validate/parseCampaignDoc.ts

### J-108 Re-importing the same campaign (duplicate `topicId`)
- **Persona:** Approved end user
- **Priority:** P2
- **CORE:** no
- **External service:** Google Sheets
- **Preconditions:** A campaign already imported.
- **Steps:**
  1. Import the same JSON twice.
  2. Import posts without `topicId`.
- **Pass check:** Second import updates or skips rows with the same `topicId` (no duplicates in D1 `pipeline_state` PK `(user_id, topic_id)` or in the sheet); missing `topicId` is rejected with a message.
- **Code anchors:** worker/src/persistence/drafts.ts, worker/src/persistence/pipeline-db/pipeline.ts (`bulkImportCampaign`)

## Newsletter

### J-109 Create a newsletter and preview it
- **Persona:** Approved end user
- **Priority:** P2
- **CORE:** no
- **External service:** Gmail
- **Preconditions:** Sheet connected (the `newsletter.*` config actions use `storedConfig.spreadsheetId`).
- **Steps:**
  1. `/campaign` -> Newsletter tab -> `NewsletterWizard`.
  2. Wire: `ACTION newsletter.create {"name":"Weekly","config":{...},"autoApprove":false}`; `ACTION newsletter.list {}`; `ACTION newsletter.preview {}`; `ACTION newsletter.getConfig {}`; `ACTION newsletter.saveConfig {...}`.
- **Pass check:** Newsletter listed; preview returns rendered HTML/subject. Missing sheet -> `No spreadsheet configured.`
- **Code anchors:** frontend/src/features/campaign/components/newsletter/, worker/src/newsletter/handlers.ts, worker/migrations/0016_newsletter.sql, worker/migrations/0018_newsletters_multi.sql

### J-110 Draft, approve and send a newsletter issue manually
- **Persona:** Approved end user
- **Priority:** P2
- **CORE:** no
- **External service:** Gmail, Telegram
- **Preconditions:** A newsletter with recipients.
- **Steps:**
  1. `ACTION newsletter.createDraftByNewsletter {"newsletterId":"<id>"}` (or `newsletter.createDraftNow {}`).
  2. `ACTION newsletter.issue.update {"issueId":"<id>","subject":"...","rendered_content":"<html>"}`.
  3. `ACTION newsletter.approveIssue {"issueId":"<id>"}`, then `ACTION newsletter.sendApproved {"issueId":"<id>"}`.
  4. Try send before approve; try `newsletter.regenerateIssue` on a sent issue.
- **Pass check:** Send before approve -> `Cannot send issue with status 'draft' — must be approved first`; regenerate sent -> `Cannot regenerate an issue that has already been sent.`; recipients receive the mail; `markIssueSent` flips status.
- **Code anchors:** worker/src/newsletter/handlers.ts, worker/src/newsletter/draftCreator.ts, worker/src/newsletter/emailRenderer.ts, worker/src/newsletter/scheduler.ts

### J-111 Scheduled newsletter send vs a once-a-day cron
- **Persona:** Background / agent actor
- **Priority:** P1
- **CORE:** no
- **External service:** Cloudflare, Gmail
- **Preconditions:** Newsletter with `scheduleTimes` such as `["09:00"]` and an approved issue.
- **Steps:**
  1. Read `worker/wrangler.jsonc` `triggers.crons`: only `"0 3 * * *"`.
  2. `scheduled()` calls `runNewsletterScheduler`; `processNewsletter` sends only when `now >= next_send_at && now - next_send_at < 2h`, and creates the draft only in the 24 h preview window.
  3. Wait for the send time.
- **Pass check:** Issue is sent within minutes of its scheduled time. CODE-READING FINDING: with one run per day at 03:00 UTC, a newsletter due at any time other than 03:00-05:00 UTC is never sent (window missed, `next_send_at` not advanced). Also the legacy path says "delivery for legacy mode is handled by the Python pipeline" (`newsletter_id` null) which this repo does not contain (grep `scheduler/` only has `__init__.py`).
- **Code anchors:** worker/wrangler.jsonc, worker/src/index.ts (`scheduled`), worker/src/newsletter/scheduler.ts, worker/src/newsletter/handlers.ts

### J-112 Newsletter actions are not tenant-scoped
- **Persona:** Non-approved / unauthorised user
- **Priority:** P0
- **CORE:** yes
- **External service:** Gmail
- **Preconditions:** Tenant A has a newsletter/issue with ids; tenant B signed in.
- **Steps:**
  1. As B: `ACTION newsletter.approveIssue {"issueId":"<A's issue>"}`.
  2. As B: `ACTION newsletter.sendApproved {"issueId":"<A's issue>"}`, `ACTION newsletter.issue.update {"issueId":"<A's issue>","subject":"x"}`, `ACTION newsletter.delete {"newsletterId":"<A's newsletter>"}`, `ACTION newsletter.listIssuesByNewsletter {"newsletterId":"<A's newsletter>"}`, `ACTION newsletter.regenerateIssue {...}`.
- **Pass check:** Desired: all refused (not found / forbidden). CODE-READING FINDING: these handlers take only `issueId`/`newsletterId` and run `WHERE id = ?` with no `spreadsheet_id` or user check (`handleApproveNewsletterIssue(db, issueId)`, `handleSendApprovedNewsletterIssue`, `handleDeleteNewsletter(db, newsletterId)`). Ids are UUID-like so exploitation needs the id, but ids appear in URLs/UI/exports. Cross-tenant read/modify/send.
- **Code anchors:** worker/src/index.ts (`newsletter.*` cases), worker/src/newsletter/handlers.ts, worker/src/newsletter/persistence.ts

## Enrichment, automations and webhooks

### J-113 Enrichment page and node catalog (admin)
- **Persona:** Tenant admin
- **Priority:** P2
- **CORE:** no
- **External service:** LLM provider
- **Preconditions:** `FEATURE_ENRICHMENT` true; admin.
- **Steps:**
  1. Open `/enrichment` (`EnrichmentFlowPage`).
  2. `ACTION getNodeCatalog {}`.
  3. Run a generation and watch `EnrichmentProgressPanel`.
- **Pass check:** CODE-READING FINDING: the `getNodeCatalog` case returns `Response.json({nodes:[...]})` from inside `dispatchAction`, and the caller wraps it again with `jsonResponse({ok:true,data})`; `JSON.stringify` of a `Response` object is `{}`, so the client gets `data: {}` not the catalog. Verify the page works without it (it may use the static `builtInWorkflowCards`). Progress events `enrichment:node_completed` come from the generation stream (`lifecycleEventBus` global subscription; events from a concurrent run on the same isolate would also reach this client: check isolation).
- **Code anchors:** frontend/src/pages/EnrichmentFlowPage.tsx, frontend/src/features/generation/, worker/src/index.ts (`getNodeCatalog`, `lifecycleEventBus`), worker/src/engine

### J-114 Automation rules (admin)
- **Persona:** Tenant admin
- **Priority:** P2
- **CORE:** no
- **External service:** Instagram, LinkedIn, Telegram, Gmail
- **Preconditions:** Admin; channel connected.
- **Steps:**
  1. `/automations` -> rule editor (`RuleEditor`).
  2. Wire: `POST {WORKER_URL}/automations/rules` header `Authorization: Bearer T` body `{"platform":"instagram","channelId":"<id>","topicId":"<optional>","triggers":["comment"],"comment_reply_template":"Thanks!","enabled":true}`.
  3. `GET /automations/rules`, `GET /automations/rules/lookup?platform=instagram&channelId=<id>&topicId=<id>`, `DELETE /automations/rules` body `{platform,channelId,topicId?}`.
  4. `POST /automations/webhooks/register` body per `registerPlatformWebhook`.
- **Pass check:** Rules stored in KV (`CONFIG_KV`) and resolved topic > channel; missing `platform`/`channelId` -> 400; non-admin -> 403. Rules are global (not per tenant): all admins share them.
- **Code anchors:** frontend/src/features/automations/, worker/src/automations/routes.ts, worker/src/automations/kv.ts, worker/src/automations/engine.ts

### J-115 Instagram webhook verification handshake
- **Persona:** Background / agent actor
- **Priority:** P2
- **CORE:** no
- **External service:** Instagram
- **Preconditions:** Meta app webhook configured to `{WORKER_URL}/webhooks/instagram`.
- **Steps:**
  1. Meta sends `GET /webhooks/instagram?hub.mode=subscribe&hub.verify_token=ig_<INSTAGRAM_USER_ID>_verify&hub.challenge=123`.
  2. Send the same with a wrong token.
  3. Meta POSTs events with `X-Hub-Signature-256`.
- **Pass check:** Correct token -> body `123`, 200; wrong -> 403; POST with a bad signature is ignored (`verifyInstagramSignature` fails -> return) but still answers `OK`. CODE-READING FINDING: the verify token is derivable from the public Instagram user id (`ig_${channelId}_verify`), not a secret.
- **Code anchors:** worker/src/automations/routes.ts, worker/src/automations/platforms/instagram.ts, worker/src/automations/webhook-verify.ts

### J-116 Gmail push webhook has no sender authentication
- **Persona:** Non-approved / unauthorised user
- **Priority:** P1
- **CORE:** no
- **External service:** Gmail
- **Preconditions:** Gmail automation enabled for a channel (`emailAddress`).
- **Steps:**
  1. `POST {WORKER_URL}/webhooks/gmail` with body `{"message":{"data":"<base64 of {\"emailAddress\":\"owner@x.com\",\"historyId\":\"1\"}>"}}` and no headers.
- **Pass check:** Desired: 401/ignored without a verified Pub/Sub JWT or shared secret. CODE-READING FINDING: `handleGmailPushEvent` parses the body and proceeds to `resolveGmailAccessToken(channelId, env)` and history processing with no signature/OIDC check (Telegram and LinkedIn handlers verify; Gmail does not). The route always answers 200.
- **Code anchors:** worker/src/automations/routes.ts, worker/src/automations/platforms/gmail.ts

### J-117 Telegram and LinkedIn webhooks verify signatures
- **Persona:** Background / agent actor
- **Priority:** P2
- **CORE:** no
- **External service:** Telegram, LinkedIn
- **Preconditions:** Telegram webhook registered (secret token stored under KV `telegramSecret`).
- **Steps:**
  1. `POST /webhooks/telegram` with the right `X-Telegram-Bot-Api-Secret-Token` and a message update.
  2. Same with a wrong/missing header.
  3. `POST /webhooks/linkedin` with a bad and a good `X-LI-Signature`.
- **Pass check:** Wrong secret/signature -> event silently dropped (still HTTP 200 `OK`); valid -> automation rule evaluated and reply sent; `LINKEDIN_CLIENT_SECRET` unset -> all LinkedIn events dropped.
- **Code anchors:** worker/src/automations/platforms/telegram.ts, worker/src/automations/platforms/linkedin.ts, worker/src/automations/webhook-verify.ts

### J-118 YouTube comment polling schedule
- **Persona:** Tenant admin
- **Priority:** P2
- **CORE:** no
- **External service:** YouTube
- **Preconditions:** YouTube connected; GitHub Actions secrets `YOUTUBE_API_KEY`, `YOUTUBE_OAUTH_TOKEN`, `VITE_WORKER_URL`, `WORKER_SCHEDULER_SECRET`.
- **Steps:**
  1. `/automations` -> YouTube scheduler, enter `0 */6 * * *`, Save (`PUT /automations/youtube/schedule`; errors are swallowed: "silently ignored").
  2. Run the workflow manually (`workflow_dispatch` with `channel_id`) -> `automations/youtube_poller.py` posts to `POST /automations/internal/youtube/poll` with header `X-Scheduler-Secret`.
- **Pass check:** `GET /automations/youtube/schedule` returns the saved cron; manual dispatch records `lastPolledAt`. (NOT IMPLEMENTED per code reading: `.github/workflows/youtube-comment-poll.yml` has its `schedule:` block commented out, so the saved cron never triggers anything; the UI text "Use a GitHub Actions cron expression" is not wired to the workflow.)
- **Code anchors:** frontend/src/features/automations/YouTubeScheduler.tsx, worker/src/automations/routes.ts, .github/workflows/youtube-comment-poll.yml, automations/youtube_poller.py

### J-119 Daily cron housekeeping
- **Persona:** Background / agent actor
- **Priority:** P3
- **CORE:** no
- **External service:** Cloudflare
- **Preconditions:** Deployed worker, cron `0 3 * * *`.
- **Steps:**
  1. Trigger locally: `wrangler dev --test-scheduled` and `curl "http://localhost:8787/__scheduled"` (or wait for 03:00 UTC).
  2. Inspect logs.
- **Pass check:** `scheduled()` runs, each in `ctx.waitUntil(...catch)`: `runAutomationCleanup`, `pruneOldNewsSnapshots`, `pruneOldLlmUsageLog`, `syncImageGenCatalog`, newsletter scheduler; one failure does not stop the others. Note that `pruneOldLlmUsageLog` removes the rows the monthly budget sums over; check its retention is longer than the billing month.
- **Code anchors:** worker/src/index.ts (`scheduled`), worker/src/automations/cleanup.ts, worker/src/db/llm-usage.ts, worker/src/image-gen

## Settings, models and providers

### J-120 Admin settings: default channel, allowed models, news keys
- **Persona:** Tenant admin
- **Priority:** P2
- **CORE:** yes
- **External service:** none
- **Preconditions:** Admin.
- **Steps:**
  1. `/settings` (admin only; opens `DashboardSettingsDrawer`/settings home).
  2. Change default channel, allowed Google models, WhatsApp/Telegram recipients; save.
  3. Wire: `ACTION saveConfig {"defaultChannel":"linkedin","googleModel":"...","allowedGoogleModels":["..."],"telegramRecipients":[...],"whatsappRecipients":[...]}`.
- **Pass check:** Response is the public config (`BotConfig`) with secrets reduced to booleans (`hasLinkedInAccessToken` etc.); no ciphertext or token is returned in `bootstrap`/`saveConfig`. Non-admin gets the admin error.
- **Code anchors:** frontend/src/components/dashboard/components/DashboardSettingsDrawer.tsx, worker/src/index.ts (`saveConfig`, `toPublicConfig`)

### J-121 Pick provider and model per purpose
- **Persona:** Tenant admin
- **Priority:** P2
- **CORE:** yes
- **External service:** LLM provider
- **Preconditions:** `FEATURE_MULTI_PROVIDER_LLM` true; provider keys on the worker.
- **Steps:**
  1. `ACTION getLlmProviderCatalog {}` -> providers `gemini`, `grok`, `openrouter`, `minimax` with models.
  2. `ACTION listLlmModels {"provider":"gemini"}`.
  3. `ACTION getLlmSettings {}`; `ACTION saveLlmSetting {"key":"<LlmSettingKey>","ref":{"provider":"gemini","model":"<id>"}}`.
  4. Try an unknown provider and an unknown key.
- **Pass check:** Non-admin catalogue is filtered by `allowedGoogleModels`; unknown provider -> `Unknown LLM provider.`; unknown key -> `Unknown LLM setting key: <key>`; invalid provider in `ref` -> `Unknown provider: <p>`; with the flag off -> `Multi-provider LLM is disabled for this deployment.`
- **Code anchors:** worker/src/index.ts, worker/src/llm, worker/src/google-model-policy.ts, worker/migrations/0006_llm_settings.sql, frontend/src/components/llm

### J-122 LLM provider failure and fallback
- **Persona:** Approved end user
- **Priority:** P1
- **CORE:** yes
- **External service:** LLM provider
- **Preconditions:** Primary provider key invalid / quota exhausted; fallback configured or not.
- **Steps:**
  1. Run Quick Change (J-065), `analyzeTopicInsights` (J-036), and generation (J-053).
- **Pass check:** Where a fallback is configured (`resolveFallbackForGeneration`) the call succeeds and `llmProvider` in the result names the fallback; otherwise a readable error reaches the user (not `[object Object]`, not a raw API key in the text); usage rows recorded in `llm_usage_log` only for successful calls (check token accounting on failures).
- **Code anchors:** worker/src/llm, worker/src/index.ts (`generateTextJsonWithFallback`), worker/src/db/llm-usage.ts, packages/llm-core

## Admin, tenant and budget

### J-123 Admin panel: users, approve, suspend, budget
- **Persona:** Tenant admin
- **Priority:** P1
- **CORE:** yes
- **External service:** none
- **Preconditions:** `deploymentMode: saas` (the header link "Admin" only shows in saas; the route `/admin` itself is available to any admin in any mode).
- **Steps:**
  1. `/admin`; wire: `ACTION __admin__ {"__path":"/api/admin/users","__method":"GET"}` and `{"__path":"/api/admin/waitlist","__method":"GET"}`.
  2. Click "Budget" on a user (prompt in thousands): `ACTION __admin__ {"__path":"/api/admin/users/<email>/budget","__method":"POST","budget":1000000}`.
  3. "Suspend" / "Approve": `.../suspend` and `.../approve` (POST).
- **Pass check:** Users list includes `monthly_tokens_used`; budget update persists to `users.monthly_token_budget`; suspend -> next request by that user fails (J-128); invalid budget (0, negative, missing) -> `{"error":"budget must be a positive number"}` (HTTP 400, so an admin cannot set a zero budget as a soft block: use Suspend).
- **Code anchors:** frontend/src/features/saas/AdminPanel.tsx, frontend/src/services/backendApi.ts, worker/src/modes/saas/admin.ts, worker/src/db/users.ts

### J-124 Usage meter and usage page
- **Persona:** Approved end user
- **Priority:** P2
- **CORE:** no
- **External service:** none
- **Preconditions:** SaaS mode.
- **Steps:**
  1. Header `UsageMeter` after login (`GET {WORKER_URL}/api/usage` with `Authorization: Bearer T`).
  2. `/usage` page: `ACTION getUsageSummary {}` and `ACTION getUsageSummaryByRange {"days":7}`.
- **Pass check:** `/api/usage` returns `{used,budget,resetDate}` where `resetDate` is the 1st of next month computed in the Worker's local time (UTC); `days` clamped to 1-90; admin sees all users' usage, non-admin only their own rows. Meter and budget check use the same table (`llm_usage_log`).
- **Code anchors:** frontend/src/features/saas/UsageMeter.tsx, frontend/src/pages/UsagePage.tsx, worker/src/index.ts, worker/src/db/users.ts (`getMonthlyTokenUsage`)

### J-125 Monthly token budget exhausted
- **Persona:** Approved end user
- **Priority:** P1
- **CORE:** yes
- **External service:** LLM provider
- **Preconditions:** SaaS mode; usage >= budget.
- **Steps:**
  1. Run Quick Change from the editor (stream) and `generateVariantsPreview`.
- **Pass check:** Stream route returns HTTP 429 `{"ok":false,"error":"Monthly token budget exceeded"}`; action routes throw the same text (the `httpStatus: 429` attached to the error is ignored by the outer catch, so HTTP 400 is returned). The UI shows the message and a path to contact the admin; the editor text is not lost.
- **Code anchors:** worker/src/index.ts, worker/src/auth.ts, frontend/src/components/dashboard/hooks/useDashboardQueue.ts

### J-126 Self-hosted deployment still enforces the SaaS budget
- **Persona:** Self-hosting operator
- **Priority:** P1
- **CORE:** yes
- **External service:** LLM provider
- **Preconditions:** `features.yaml` `deploymentMode: selfHosted`; worker deployed through setup (which never sets `DEPLOYMENT_MODE`).
- **Steps:**
  1. Use the app until `llm_usage_log` sums over 500,000 tokens in the calendar month (default `monthly_token_budget`).
  2. Run Quick Change.
- **Pass check:** Desired: self-hosted has no budget (frontend hides the meter and docs say "no usage meter"). CODE-READING FINDING: the worker uses `env.DEPLOYMENT_MODE ?? 'saas'`; neither `.env.example` (commented `# DEPLOYMENT_MODE=saas`), wrangler vars nor setup set it, so a self-hosted owner is cut off at 500k tokens with `Monthly token budget exceeded` and no visible meter.
- **Code anchors:** worker/src/index.ts (`checkTokenBudget` call sites), worker/src/auth.ts, .env.example, features.yaml, worker/migrations/0019_user_status_budget.sql

### J-127 Empty `ADMIN_EMAILS` makes the repo owner an admin
- **Persona:** Self-hosting operator
- **Priority:** P0
- **CORE:** yes
- **External service:** none
- **Preconditions:** Worker deployed with `ADMIN_EMAILS` unset or empty.
- **Steps:**
  1. Sign in as `99pratyush@gmail.com` (or inspect `resolveAdminEmailAllowlist`).
  2. Sign in as the operator.
- **Pass check:** Desired: with no `ADMIN_EMAILS`, nobody is admin (or deploy refuses). CODE-READING FINDING: `resolveAdminEmailAllowlist` falls back to `DEFAULT_ADMIN_EMAIL = '99pratyush@gmail.com'`, so on any customer's deployment missing the variable, the project author gets admin (shared config, tokens, all users) and the real operator is not admin. The committed `worker/wrangler.jsonc` also lists the owner's and another person's emails in `ALLOWED_EMAILS`/`ADMIN_EMAILS`.
- **Code anchors:** worker/src/index.ts (`DEFAULT_ADMIN_EMAIL`, `resolveAdminEmailAllowlist`), worker/wrangler.jsonc, setup/worker_config.py

### J-128 Admin suspends a user while they are signed in
- **Persona:** Tenant admin
- **Priority:** P1
- **CORE:** yes
- **External service:** none
- **Preconditions:** User U with a live session; admin on `/admin`.
- **Steps:**
  1. Admin clicks "Suspend" for U.
  2. U triggers any action (e.g. `ACTION getRows {}`) and any streaming call (`POST /api/generate/stream`).
  3. U's scheduled posts (J-082) fire.
- **Pass check:** Steps 2: `Access denied: your account has been suspended. Contact support.` (action path) and HTTP 401 `Unauthorized` (stream path: `verifySession` throws, reported as 401). U's UI shows a generic notice (the sign-out/"suspended" screen only appears at bootstrap, since the mid-session message does not match `AUTH_ERROR_PATTERN`). Step 3: the DO alarm does not call `verifySession`, so a suspended user's already-queued posts still publish (CODE-READING FINDING).
- **Code anchors:** worker/src/index.ts, worker/src/auth.ts, worker/src/scheduled-publish/ScheduledPublishAlarm.ts, frontend/src/App.tsx

## Failure and recovery

### J-129 Google Sheets unavailable or unshared during topic list
- **Persona:** Approved end user
- **Priority:** P1
- **CORE:** yes
- **External service:** Google Sheets
- **Preconditions:** Revoke the service account's access to the tenant's sheet (403) or block `sheets.googleapis.com`.
- **Steps:**
  1. Reload `/topics` (`ACTION getRows {}`).
  2. Edit and approve a draft; click publish.
  3. Restore access and reload.
- **Pass check:** `getRows` falls back to D1 rows (`console.error('[getRows] Sheets merge failed, falling back to D1')`) and the UI loads; no banner tells the user the sheet is out of sync (CODE-READING FINDING). Writes: D1 updates succeed; sheet mirroring errors in `updateRowStatus`/`publishContent` must not block publishing or must be reported. After restore, rows reconcile without duplicates or lost edits.
- **Code anchors:** worker/src/index.ts (`getRows`), worker/src/persistence/pipeline-db/pipeline.ts, worker/src/persistence/drafts.ts

### J-130 Sheets down while adding a topic
- **Persona:** Approved end user
- **Priority:** P2
- **CORE:** yes
- **External service:** Google Sheets
- **Preconditions:** Same as J-129.
- **Steps:**
  1. `ACTION addTopic {"topic":"Offline topic"}`.
  2. Restore Sheets; reload and `ACTION syncFromSheets {}`.
- **Pass check:** Request returns 200 and the row (D1 first, Sheets error only logged); the sheet lacks the row; after restore the row is still present in `/topics` and is eventually mirrored or at least not duplicated/deleted by the merge.
- **Code anchors:** worker/src/index.ts (`addTopic`), worker/src/persistence/pipeline-db/pipeline.ts (`getMergedRows`)

### J-131 CORS: frontend origin not allowed, or allowlist empty
- **Persona:** Self-hosting operator
- **Priority:** P1
- **CORE:** yes
- **External service:** Cloudflare
- **Preconditions:** Frontend served from `https://app.example.com`; worker `CORS_ALLOWED_ORIGINS` lacks it.
- **Steps:**
  1. Sign in.
  2. Repeat with `CORS_ALLOWED_ORIGINS` empty.
- **Pass check:** Case 1: browser blocks the call; UI message built by `formatFetchNetworkFailure` explains the CORS variable and mixed content (if `http://` worker on an https page). Case 2: `buildCorsHeaders` returns `Access-Control-Allow-Origin: *` when the list is empty (fail-open) — acceptable only with token auth, but note `/api/waitlist` and webhooks are then callable from any site. Origins with a trailing slash or `127.0.0.1` vs `localhost` mismatches are a common failure.
- **Code anchors:** worker/src/index.ts (`buildCorsHeaders`), frontend/src/services/backendApi.ts (`formatFetchNetworkFailure`), setup/worker_config.py

### J-132 Missing `SECRET_ENCRYPTION_KEY`
- **Persona:** Self-hosting operator
- **Priority:** P1
- **CORE:** yes
- **External service:** LinkedIn
- **Preconditions:** Worker without `SECRET_ENCRYPTION_KEY`.
- **Steps:**
  1. Complete the LinkedIn authorization in the popup (J-094).
- **Pass check:** Popup shows `Missing SECRET_ENCRYPTION_KEY in the Worker environment.` CODE-READING FINDING: in `handleLinkedInCallback`, `persistLinkedInConnection` (KV) runs before `requireSecretEncryptionKey`; the per-user D1 upsert is wrapped in `.catch(() => undefined)` only for the DB call, so the error ends the flow after the shared token was already saved: the popup says failed while the shared slot changed. `startLinkedInAuth` does not pre-check the key, so the user finds out only at the end.
- **Code anchors:** worker/src/index.ts (`requireSecretEncryptionKey`, `handleLinkedInCallback`, `persistLinkedInConnection`), setup/worker_config.py

### J-133 Missing D1 binding or unapplied migrations
- **Persona:** Self-hosting operator
- **Priority:** P1
- **CORE:** yes
- **External service:** Cloudflare
- **Preconditions:** (a) `PIPELINE_DB` binding removed or id wrong; (b) database exists but migrations not applied.
- **Steps:**
  1. Sign in; `ACTION bootstrap {}`.
  2. `GET {WORKER_URL}/` (no DB needed).
- **Pass check:** Step 2 returns OK (health check does not touch D1, so setup "verify" can pass while the app is broken). Step 1 returns HTTP 400 with the raw runtime message (e.g. `Cannot read properties of undefined (reading 'prepare')` or `D1_ERROR: no such table: users`) and the frontend shows it as "Unable to start the session"/access error. Desired: a clear "database not initialised: run migrations" message and a health endpoint that checks D1.
- **Code anchors:** worker/src/index.ts (`verifySession` -> `upsertUser`, catch block), worker/wrangler.jsonc, setup/cloudflare.py (`_apply_d1_migrations`)

### J-134 Missing or invalid `GOOGLE_SERVICE_ACCOUNT_JSON`
- **Persona:** Self-hosting operator
- **Priority:** P1
- **CORE:** yes
- **External service:** Google Sheets
- **Preconditions:** Secret unset, or malformed.
- **Steps:**
  1. `ACTION getServiceAccountEmail {}`.
  2. `ACTION connectSpreadsheet {"spreadsheetId":"x","driveAccessToken":"y"}`.
  3. `ACTION getSpreadsheetStatus {}`.
- **Pass check:** Step 1 returns `{email:""}`; step 2 `Service account email not configured on this Worker.` or `GOOGLE_SERVICE_ACCOUNT_JSON is not valid JSON.`; step 3 `{accessible:false,title:""}` (errors swallowed). The SheetConnectionCard then shows no service-account email to share with: confirm the card tells the user it is a server misconfiguration, not their sheet.
- **Code anchors:** worker/src/index.ts, frontend/src/pages/connections/SheetConnectionCard.tsx

### J-135 Frontend built with the wrong Google client id
- **Persona:** Self-hosting operator
- **Priority:** P1
- **CORE:** yes
- **External service:** Google OAuth
- **Preconditions:** `VITE_GOOGLE_CLIENT_ID` differs from the worker's `GOOGLE_CLIENT_ID`; or the Pages origin missing from the OAuth client's authorized JavaScript origins.
- **Steps:**
  1. Click the Google sign-in button.
  2. Complete sign-in; observe the bootstrap error.
- **Pass check:** Google popup shows `origin_mismatch`/`invalid_client` (origins) or bootstrap fails with `Unauthorized: Google token audience does not match this app.` shown in the red error box on the sign-in card; the operator doc (SETUP.md Step 2) lists the exact origins (`http://localhost:5173` only; `5174` used by `npm run dev` is not listed: CODE-READING FINDING).
- **Code anchors:** frontend/src/components/GoogleLoginButton.tsx, frontend/src/App.tsx, worker/src/index.ts (`verifySession`), SETUP.md

### J-136 Dev auth bypass secret present in production
- **Persona:** Self-hosting operator
- **Priority:** P0
- **CORE:** yes
- **External service:** none
- **Preconditions:** `DEV_GOOGLE_AUTH_BYPASS_SECRET` set on a deployed worker (e.g. copied from `.dev.vars`).
- **Steps:**
  1. `ACTION bootstrap {}` with `idToken` = that secret.
- **Pass check:** Desired: never accepted outside local dev. CODE-READING FINDING: `verifySession` calls `tryResolveDevGoogleAuthBypassSession` before any Google call and returns `{isAdmin:true}` if the secret matches; there is no environment guard (`wrangler dev` vs deployed). The only protection is the comment "Do not set these variables in production Worker secrets". Also if `VITE_DEV_GOOGLE_AUTH_BYPASS_SECRET` is baked into a production frontend build the secret ships in the JS bundle. The deploy pipeline should assert both are absent.
- **Code anchors:** worker/src/plugins/dev-google-auth-bypass/resolve-session.ts, worker/src/index.ts (`verifySession`), frontend/src/plugins/dev-google-auth-bypass/, .github/workflows/deploy-workers.yml, .github/workflows/deploy-pages.yml

## Upgrade and migration

### J-137 Apply new D1 migrations on upgrade
- **Persona:** Self-hosting operator
- **Priority:** P1
- **CORE:** yes
- **External service:** Cloudflare
- **Preconditions:** A deployment on an older migration level; new code deployed.
- **Steps:**
  1. `cd worker && npx wrangler d1 migrations apply linkedin-pipeline-db --remote` (or `python setup.py --cloudflare`, which applies local then remote).
  2. For the generation worker: `python setup.py --cloudflare` also calls `_apply_generation_worker_d1_migrations`.
  3. Deploy workers; sign in.
- **Pass check:** Lists 0001..0021 as applied; existing users keep working and become `status='active'` with `monthly_token_budget=500000` (defaults from 0019); `pipeline_state` rows preserved by the rebuild in 0010 (verify row counts before/after on a copy). Deploying code BEFORE migrating gives runtime `no such column/table` errors (J-133): the deploy workflow/docs must order migrate-then-deploy. The 0019 file header comment says 0018 (cosmetic).
- **Code anchors:** worker/migrations/*.sql, setup/cloudflare.py (`_apply_d1_migrations`, `_apply_generation_worker_d1_migrations`), .github/workflows/deploy-workers.yml

### J-138 Legacy rows and shared-config data after upgrade
- **Persona:** Approved end user
- **Priority:** P2
- **CORE:** yes
- **External service:** Google Sheets
- **Preconditions:** Sheet rows created before `topicId` existed, or `topicGenerationRules` containing plain text instead of JSON.
- **Steps:**
  1. Open `/topics`; open such a topic (route needs `encodeTopicRouteId(row)`).
  2. Publish it (`requireTopicId(row)` in the schedule path).
  3. `sendTopicToGeneration` on a row with non-JSON `topicGenerationRules`.
- **Pass check:** Rows get a stable `topicId` on merge (no blank id); publish works; non-JSON rules are ignored (`catch { // ignore malformed JSON }`) rather than failing; scheduled publish for a row without id is refused with a clear message.
- **Code anchors:** frontend/src/features/topic-navigation/utils/topicRoute.ts, worker/src/index.ts (`requireTopicId`, `sendTopicToGeneration`), worker/migrations/0002_pipeline_topic_id_pk.sql

### J-139 Feature flags after editing `features.yaml`
- **Persona:** Developer
- **Priority:** P3
- **CORE:** no
- **External service:** none
- **Preconditions:** Edit `features.yaml` (e.g. `campaign: false`).
- **Steps:**
  1. `python3 scripts/generate_features.py` (or `python3 setup.py`; also `npm run prebuild` in frontend and `pretypecheck` in worker).
  2. Rebuild both; open `/campaign`.
- **Pass check:** `frontend/src/generated/features.ts` and `worker/src/generated/features.ts` updated; `/campaign` redirects to `/topics` and `bulkImportCampaign` throws the disabled message. Forgetting step 1 leaves the generated constants stale (no CI check seen: `tests/test_scripts_generate_features.py` covers the script only).
- **Code anchors:** features.yaml, scripts/generate_features.py, frontend/src/generated/features.ts, worker/src/generated/features.ts

## Data isolation between tenants

### J-140 Tenant A cannot read or modify tenant B's topics
- **Persona:** Approved end user
- **Priority:** P0
- **CORE:** yes
- **External service:** none
- **Preconditions:** Two non-admin accounts A and B, each with topics (D1-only or own sheets).
- **Steps:**
  1. As B, `ACTION getRows {}` -> note a `topicId` of B.
  2. As A, `ACTION getRows {}`: B's topic must not appear.
  3. As A, `ACTION updateTopicMeta {"topicId":"<B's id>","topic":"pwn","topicMeta":{}}`; `ACTION updateRowStatus {"row":{"topic":"x","date":"d","topicId":"<B's id>"},"status":"Approved","selectedText":"x",...}`; `ACTION deleteRow {"row":{... "topicId":"<B's id>"}}`; `ACTION getNodeRuns {"topicId":"<B's id>"}`; `ACTION publishContent {"row":{... "topicId":"<B's id>"},...}`.
- **Pass check:** Step 2 empty of B's rows. Step 3: every write is scoped by `user_id = A` in `pipeline_state` (PK `(user_id, topic_id)` per migration 0010), so none change B's data (A's call creates/updates only A's own row or fails with `Topic not found.`); `getNodeRuns` returns only rows with `user_id = A`. Verify by reading B's row afterwards. Note that `updateRowStatus` / `upsertFull` accept a client-supplied full row (including `status`), so A can upsert arbitrary row content for A's own account.
- **Code anchors:** worker/src/persistence/pipeline-db/pipeline.ts, worker/src/services.ts (`buildServices`), worker/migrations/0010_pipeline_user_primary.sql, worker/src/index.ts

### J-141 Two tenants connect the same Google Sheet
- **Persona:** Approved end user
- **Priority:** P2
- **CORE:** yes
- **External service:** Google Sheets
- **Preconditions:** Tenant A owns a sheet; tenant B knows its id (or is a collaborator).
- **Steps:**
  1. B runs `ACTION connectSpreadsheet {"spreadsheetId":"<A's id>","driveAccessToken":"<B's token>"}`.
  2. Both generate drafts and run news research.
- **Pass check:** Desired: B cannot connect a sheet B cannot edit (Drive token proves access, so it works only for collaborators: acceptable). Shared state keyed by `spreadsheet_id` is then shared across the two tenants: `news_snapshots`, `llm_settings` (`seedLlmSettingsIfEmpty` keyed by spreadsheet), newsletter config (`getNewsletterConfig` by spreadsheet), generation-worker records. Document that one sheet = one workspace. `completeOnboarding` accepts any `spreadsheetId` in its payload without any Drive/service-account check (CODE-READING FINDING), so B can set A's sheet id as B's workspace without proof of access; the service account then reads/writes A's sheet on B's behalf.
- **Code anchors:** worker/src/index.ts (`connectSpreadsheet`, `completeOnboarding`), worker/src/db/*, worker/src/newsletter/persistence.ts

### J-142 Per-user lists are scoped (clips, groups, feedback, integrations, personas, workflows)
- **Persona:** Approved end user
- **Priority:** P1
- **CORE:** yes
- **External service:** none
- **Preconditions:** Accounts A and B with data in each.
- **Steps:**
  1. As A: `ACTION listClips {}`, `ACTION listInterestGroups {}`, `ACTION getArticleFeedback {}`, `ACTION getIntegrations {}`, `ACTION listCustomPersonas {}`, `ACTION listCustomWorkflows {}`.
  2. As A: `ACTION deleteClip {"id":"<B's clip>"}`, `ACTION updateInterestGroup {"id":"<B's group>","name":"x"}`, `ACTION deleteCustomPersona {"personaId":"<B's>"}`, `ACTION deleteIntegration {"provider":"linkedin"}` (affects only A).
- **Pass check:** Lists contain only A's rows; mutations on B's ids change nothing / error (statements are `WHERE user_id = ?`).
- **Code anchors:** worker/src/db/clips.ts, worker/src/db/interestGroups.ts, worker/src/db/feedArticles.ts, worker/src/db/socialIntegrations.ts, worker/src/persistence/pipeline-db/pipeline.ts

### J-143 Generated and uploaded images in a shared bucket
- **Persona:** Non-approved / unauthorised user
- **Priority:** P2
- **CORE:** yes
- **External service:** other (Google Cloud Storage)
- **Preconditions:** `GOOGLE_CLOUD_STORAGE_BUCKET` shared by all tenants.
- **Steps:**
  1. Upload an image (J-067); copy its URL.
  2. Open the URL in a private window without signing in.
  3. As another tenant call `ACTION promoteDraftImageUrl {...}` / `ACTION downloadDraftImage {...}` with that URL; `ACTION deleteRow` on a topic whose `topicId` collides in prefix.
- **Pass check:** Document the intended model: URLs must be public-readable for Instagram/LinkedIn to fetch them (so anyone with the URL can view), object names must be unguessable (`gcsObjectPrefixFromTopicId`), and `deleteGcsObjectsForTopicRow` must not delete objects outside the caller's own prefix. `downloadDraftImage` fetches an arbitrary URL on behalf of the user: confirm it blocks private/internal addresses (SSRF) — `safeFetch` is used for token verification; check `downloadDraftImage`.
- **Code anchors:** worker/src/index.ts (`uploadBytesToGcs`, `gcsObjectPrefixFromTopicId`, `downloadDraftImage`, `deleteGcsObjectsForTopicRow`, `safeFetch`), worker/src/media

## Background and agent actors

### J-144 Scheduler-secret internal routes
- **Persona:** Background / agent actor
- **Priority:** P2
- **CORE:** no
- **External service:** other (GitHub Actions / external scheduler)
- **Preconditions:** `WORKER_SCHEDULER_SECRET` set (or unset for the negative test).
- **Steps:**
  1. `POST {WORKER_URL}/internal/schedule-linkedin-publish` with header `X-Scheduler-Secret: <secret>` and body `{"topicId":"<id>","scheduledTime":"2026-10-28 09:30"}`.
  2. `POST {WORKER_URL}/internal/merged-rows` and `/internal/pipeline-upsert` with and without the header.
  3. `POST {WORKER_URL}/automations/internal/youtube/poll` body `{"channelId":"UC..."}`.
  4. Same with `WORKER_SCHEDULER_SECRET` unset.
- **Pass check:** Wrong/missing header -> 401 `Unauthorized scheduler request.`; with the secret unset every request is refused (`if (!expectedSecret || ...)`). The first route publishes using the global KV LinkedIn config only (not per-tenant). Compare the secret in constant time (current code uses `!==`).
- **Code anchors:** worker/src/index.ts (`verifySchedulerSecret`, `handleScheduledLinkedInPublishRequest`, `handleInternalMergedRowsRequest`, `handleInternalPipelineUpsertRequest`), worker/src/automations/routes.ts

### J-145 Operator health check of both workers
- **Persona:** Self-hosting operator
- **Priority:** P1
- **CORE:** yes
- **External service:** Cloudflare
- **Preconditions:** Both deployed.
- **Steps:**
  1. `curl https://<main>/` -> health.
  2. `curl -H "Authorization: Bearer $SECRET" https://<gen>/v1/health`.
  3. `curl -H "Authorization: Bearer $SECRET" https://<gen>/v1/llm/catalog` (checks provider keys).
  4. `curl -H "Authorization: Bearer $SECRET" https://<gen>/v1/patterns`.
  5. From the main worker context: `ACTION listPatterns {}` (verifies `GENERATION_WORKER_SECRET` equals the generation worker's `WORKER_SHARED_SECRET`).
- **Pass check:** 200s; `patterns` non-empty; step 5 returns an array, not `Generation worker returned 401`. Neither health endpoint checks D1/KV/secret presence; document that a green health probe does not prove readiness (see J-133).
- **Code anchors:** worker/src/index.ts, generation-worker/src/index.ts, generation-worker/src/players/patternRepository.ts

### J-146 Videos page
- **Persona:** Approved end user
- **Priority:** P3
- **CORE:** no
- **External service:** Google Sheets
- **Preconditions:** `videoEpisodes: true`; sheet with an `Episodes` tab written by the local video-pipeline.
- **Steps:**
  1. Open `/videos` (`EpisodesPage`) -> `ACTION listEpisodes {}`.
  2. Set `videoEpisodes: false`, regenerate, reopen.
- **Pass check:** Episodes table renders (or a clear empty state if the tab is absent); with the flag off the route redirects to `/topics` and the action throws `Video episodes is disabled for this deployment.` The `video-pipeline/` folder is out of scope for this review.
- **Code anchors:** frontend/src/features/videos/EpisodesPage.tsx, worker/src/features/episodes, worker/src/index.ts (`listEpisodes`), features.yaml
