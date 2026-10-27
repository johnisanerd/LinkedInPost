# ARCH-AUDIT: documented architecture and config vs code

Auditor: architecture auditor, read-only pass. Branch `launch-readiness-review`. Nothing was run (no tests, builds, tsc, wrangler, scripts, network). Every item is a code-reading hypothesis until an executor reproduces it. No secret values appear here; only file:line and key names.

## Summary

- Findings: 20. By Sev: P0 = 2, P1 = 8, P2 = 5, P3 = 5.
- Checks done: 9 of 9 (results in the table; passes are listed too).
- Biggest themes:
  1. Auth gate is weaker than documented (ARCH-001, ARCH-002, ARCH-011).
  2. Setup and dev-run paths do not match the files that exist (ARCH-005, ARCH-006, ARCH-009).
  3. Config drift: `DEPLOYMENT_MODE` never reaches the worker, and cron cadence does not fit the newsletter scheduler (ARCH-007, ARCH-004).
  4. Docs describe a different stack in places (ARCH-017).

## Conformance table

| Doc claim | Source | Code status | Evidence |
|---|---|---|---|
| Main worker name `linkedin-bot-api`; generation worker `linkedin-generation-worker` | ARCHITECTURE.md:44,115 | conforms (names consistent) | worker/wrangler.jsonc:3,48; generation-worker/wrangler.jsonc:2; generation-worker/package.json:2; setup/worker_config.py:195 |
| Root `wrangler.jsonc` is "main worker also serves frontend/dist" | ARCHITECTURE.md:20, SETUP.md:14 | drift: same worker name, no `main`, assets dir is `frontend` not `frontend/dist` | wrangler.jsonc:3-10 |
| Bindings PIPELINE_DB, CONFIG_KV, SCHEDULED_LINKEDIN_PUBLISH, GENERATION_WORKER, cron `0 3 * * *` | ARCHITECTURE.md:196-204, worker/README.md:17-25 | conforms at top level | worker/wrangler.jsonc:9-50 |
| Same bindings available for `npm run dev` (`--env local`) | worker/README.md:141 | drift: `env.local` omits GENERATION_WORKER service binding and cron | worker/wrangler.jsonc:67-117 |
| DO class `ScheduledPublishAlarm` exists and is exported | ARCHITECTURE.md:199 | conforms | worker/src/scheduled-publish/ScheduledPublishAlarm.ts:7; worker/src/index.ts:125 |
| DO alarm "fires POST /internal/schedule-linkedin-publish" | ARCHITECTURE.md diagram | drift: alarm calls `executeScheduledPublish` in-process; the HTTP route is a separate entry | ScheduledPublishAlarm.ts:92; worker/src/index.ts:821 |
| Cron is "nightly maintenance / 30-day retention" only | ARCHITECTURE.md:204,276 | drift: `scheduled()` also runs the newsletter scheduler and image-catalog sync | worker/src/index.ts:1277-1296 (scheduled handler) |
| HTTP routes table (`/v1/image-gen-catalog`, `/api/usage`, `/auth/*/callback`, `/api/waitlist`, `/internal/*`, `/api/generate/stream`, `/webhooks/*`, `/automations/*`) | ARCHITECTURE.md:208-228 | conforms; undocumented extras `/api/feed`, `/api/feed/items`, `/api/clips`, `/api/quickchange/stream` | worker/src/index.ts:708-717,726-835,993 |
| `index.ts` is "~5900 lines" | ARCHITECTURE.md:194 | drift (6646 lines) | `wc -l worker/src/index.ts` |
| LLM providers gemini, grok, openrouter, minimax | ARCHITECTURE.md:244-249 | conforms | worker/src/llm/providers/ (4 files) |
| AI generation uses Anthropic Claude | AGENTS.md (Common Patterns), worker/AGENTS.md | drift: no Anthropic provider in worker/llm or llm-core | worker/src/llm/providers/ lists 4 providers, none Anthropic |
| Auth uses Firebase ID tokens in `src/auth.ts` | worker/AGENTS.md | drift: Google ID token via tokeninfo in `index.ts`; `auth.ts` is status/budget only | worker/src/index.ts:3043-3050; worker/src/auth.ts:8-28 |
| Migrations "0001 through 0020" | ARCHITECTURE.md:260, worker/README.md:83 | drift (0021 exists); sequence 0001..0021 is contiguous | worker/migrations/ (21 files) |
| GEN_DB "single migration 0001" | ARCHITECTURE.md:383 | drift (3 migrations) | generation-worker/migrations/0001..0003 |
| Gen wrangler has `usage_model: unbound` | ARCHITECTURE.md:Section 5 | missing | generation-worker/wrangler.jsonc (key absent) |
| Gen worker routes `/v1/patterns`, `/v1/patterns/full`, `/v1/llm/catalog`, `/v1/generate`, `/v1/feedback`, `/v1/suggest-pattern` | ARCHITECTURE.md:Section 5 | conforms (also `/v1/health`, undocumented) | generation-worker/src/index.ts:78-110 |
| Gen worker: "Empty secret disables the check (dev only)" | ARCHITECTURE.md:Section 5 | conforms to doc, unsafe in prod (ARCH-003) | generation-worker/src/index.ts:41-44 |
| Enrichment gated by `FEATURE_ENRICHMENT` in pipeline | ARCHITECTURE.md:Section 5 | conforms | generation-worker/src/pipeline.ts:16,114 |
| React 19 + Vite 8 + RR7 | ARCHITECTURE.md:Section 3 | conforms | frontend/package.json:36,39,69 |
| React 18, port 5173 | frontend/AGENTS.md | drift (React 19.2; Vite port 5175) | frontend/package.json:36; frontend/vite.config.ts:78 |
| Vite port 5174 strictPort | ARCHITECTURE.md, README.md:52, frontend/README.md:29, worker/README.md:137 | drift (5175) | frontend/vite.config.ts:78; playwright.config.ts:4,38 |
| `ALLOWED_EMAILS` is the allowlist; non-listed users get "Access not granted" | ARCHITECTURE.md:Section 7, SETUP.md:143,217,222, worker/README.md:Required env | drift: never read by worker code | worker/src/index.ts:136 (type only); see ARCH-002 |
| `ADMIN_EMAILS` elevated | ARCHITECTURE.md:Section 7 | conforms, with hard-coded fallback | worker/src/index.ts:3020-3027 |
| Dev bypass: `DEV_AUTH_BYPASS_SECRET`, `import.meta.env.DEV`, `plugins/dev-google-auth-bypass.ts` | ARCHITECTURE.md:Section 7 | drift: var is `DEV_GOOGLE_AUTH_BYPASS_SECRET`, plugin is a directory, and a non-DEV cloud path exists (`VITE_E2E_BYPASS_SECRET`) | frontend/src/plugins/dev-google-auth-bypass/config.ts:19-21, token.ts:13-20 |
| Frontend routes `/enrichment`, `/usage`, `/admin`, `/connections`, etc. | ARCHITECTURE.md:Section 3 | conforms | frontend/src/features/topic-navigation/utils/workspaceRoutes.ts:10-19,41-50 |
| Flag list omits `FEATURE_VIDEO_EPISODES` | ARCHITECTURE.md:Section 3 | drift | frontend/src/generated/features.ts:12 |
| `packages/researcher`: Google Trends, HN, Reddit | packages/AGENTS.md | drift: only RSS and news APIs exist | packages/researcher/src/providers/{newsApis,rss}.ts |
| `start.sh` starts frontend and worker together | AGENTS.md (Key Files) | drift: starts frontend/wizard only | start.sh:213-256 |
| `setup.py` runs `tsc --noEmit` after every invocation | AGENTS.md, setup/AGENTS.md | drift (conditional) | setup.py:98-104; ARCH-015 |
| `cli.py` does "step sequencing and user prompts" | setup/AGENTS.md | drift: argparse only | setup/cli.py:9-32 |
| Web wizard at `localhost:4242` (Python) vs `3456` (Node) | SETUP.md:35 vs ARCHITECTURE.md:Section 3 | drift (two wizards, docs mention both inconsistently) | setup/wizard/server.py:39; frontend/package.json:15 |
| `cd worker && npm test` | ARCHITECTURE.md:Section 8 | missing: no `test` script | worker/package.json:6-13 |
| features.yaml flags equal generated modules | features.yaml, scripts/generate_features.py | conforms: worker and frontend generated files are byte-identical and match yaml | worker/src/generated/features.ts:4-12; frontend/src/generated/features.ts (diff clean); features.yaml:9-24 |
| `.gitignore` covers `.env` and `.dev.vars` | check 5 | conforms | .gitignore:1,8,12-14 |
| Migration files referenced by setup exist | check 6 | conforms | setup/cloudflare.py:291-356, 371; deploy-workers.yml:38-44,74-80 |
| `DEPLOYMENT_MODE` var synced into wrangler | scripts/generate_features.py:97-107 | drift: no such var in wrangler, regex is a no-op | worker/wrangler.jsonc (key absent) |
| Worker reads every wrangler var | check 2 | conforms except `ALLOWED_EMAILS` (declared, never read) | worker/wrangler.jsonc:52; grep of `env.ALLOWED_EMAILS` in worker/src returns only the type |

## Findings

### ARCH-001
- **Sev:** P0
- **Area:** deploy/auth (setup, deploy-pages.yml, worker auth plugin)
- **Journeys:** sign-in, any authenticated journey, data safety
- **Evidence:** `.github/workflows/deploy-pages.yml:51-52` passes `secrets.E2E_BYPASS_SECRET` as `VITE_E2E_BYPASS_SECRET` into the production Pages build, so the secret is embedded in the public bundle (`frontend/src/plugins/dev-google-auth-bypass/token.ts:13-15`). `setup/cloudflare.py:156-175` and `setup/worker_config.py:224,270-282` set the same value as the worker secret `DEV_GOOGLE_AUTH_BYPASS_SECRET`. The worker accepts that exact string as `idToken` and returns an admin session (`worker/src/plugins/dev-google-auth-bypass/resolve-session.ts:20-36`; `worker/src/index.ts` verifySession, first branch ~3034-3041). Anyone who reads the bundle can call `/action` as a synthetic admin.
- **Repro (static):** read deploy-pages.yml:52, then resolve-session.ts:16-37. Executor: fetch the live bundle, grep for the secret name, send it as `idToken` to `/action`.
- **Fix hint:** do not build the bypass secret into the deployed bundle. Gate the bypass on `import.meta.env.DEV` only, drop `VITE_E2E_BYPASS_SECRET` from deploy-pages.yml, and do not set `DEV_GOOGLE_AUTH_BYPASS_SECRET` as a production worker secret (use a separate staging worker for cloud E2E).
- **Status:** open
- **Verified:** read-only: deploy-pages.yml, setup/github.py:157-188, setup/cloudflare.py:156-175, resolve-session.ts, token.ts, index.ts verifySession.

### ARCH-002
- **Sev:** P0
- **Area:** worker/auth (allowlist)
- **Journeys:** sign-in, tenant isolation, data safety
- **Evidence:** `ALLOWED_EMAILS` is declared (`worker/src/index.ts:136`) and documented as the gate (SETUP.md:217,222; worker/README.md; .env.example:3-5) but no worker code reads it. In verifySession, `upsertUser` runs first (`worker/src/index.ts` ~3068) and inserts the row with the column default `status = 'active'` (`worker/migrations/0019_user_status_budget.sql:2`; insert has no status column at `worker/src/db/users.ts:21-30`). Then `checkUserAccess` returns allowed for `'active'` (`worker/src/auth.ts:18-27`). So any verified Google account that passes the token and audience check becomes an active user.
- **Repro (static):** grep `ALLOWED_EMAILS` in worker/src (type only); read users.ts:15-31 and 0019 line 2; read index.ts verifySession end to end. Executor: sign in with a Google account not in `ALLOWED_EMAILS`; expect "Access not granted", observe success.
- **Fix hint:** either read `ALLOWED_EMAILS` in verifySession and reject before `upsertUser`, or insert new users with `status = 'pending'` in selfHosted mode and keep the access-request flow. Update SETUP.md verification line to match.
- **Status:** open
- **Verified:** read-only: worker/src/index.ts, db/users.ts, auth.ts, migrations/0019, SETUP.md, .env.example. Not confirmed: whether an earlier migration sets a different default on a fresh `users` table.

### ARCH-003
- **Sev:** P1
- **Area:** generation-worker/auth
- **Journeys:** generate drafts, data safety, cost
- **Evidence:** `checkAuth` returns true when `WORKER_SHARED_SECRET` is empty (`generation-worker/src/index.ts:41-44`), and CORS is `*` (`:18-24`). The worker is reachable on a public `workers.dev` URL (`worker/wrangler.jsonc:65`). The secret is not declared in `generation-worker/wrangler.jsonc` (`vars: {}` at :35) and is only set by setup (`setup/cloudflare.py:177-189`). A deploy via CI (`deploy-workers.yml:82-88`) or without setup leaves `/v1/generate` open to spend LLM keys. The main worker also silently sends no auth header when `GENERATION_WORKER_SECRET` is unset (`worker/src/generation/generationWorkerClient.ts:89`).
- **Repro (static):** read index.ts:41-44 and the client lines above. Executor: `curl -X POST <gen-worker>/v1/generate` with no auth against a deploy lacking the secret.
- **Fix hint:** fail closed when the secret is empty outside a local dev flag; add a startup/health check that the secret is set.
- **Status:** open
- **Verified:** read-only: generation-worker/src/index.ts, wrangler.jsonc, generationWorkerClient.ts, setup/cloudflare.py.

### ARCH-004
- **Sev:** P1
- **Area:** worker/cron + newsletter scheduler
- **Journeys:** newsletter send, scheduled work
- **Evidence:** the only cron is `0 3 * * *` (`worker/wrangler.jsonc:17-21`). `runNewsletterScheduler` only sends when `now` is within 2 hours after `next_send_at`, and only creates a preview when `now` is in the 24h before it (`worker/src/newsletter/scheduler.ts` processNewsletter, send window and preview window branches). With one run per day at 03:00 UTC, a newsletter scheduled for any time outside roughly 01:00-03:00 UTC never matches the send window; it is skipped and `next_send_at` is never advanced. Docs describe the cron as housekeeping only (ARCHITECTURE.md:204,276; worker/README.md:15).
- **Repro (static):** read wrangler.jsonc:17-21 and scheduler.ts processNewsletter. Executor: create a newsletter for 09:00 and observe that nothing sends.
- **Fix hint:** run the cron hourly (or every 15 minutes) and keep the 2h window, or send anything with `next_send_at <= now` and not yet sent.
- **Status:** open
- **Verified:** read-only: wrangler.jsonc, newsletter/scheduler.ts, index.ts scheduled handler.

### ARCH-005
- **Sev:** P1
- **Area:** start.sh / setup
- **Journeys:** first run (setup is part of the product)
- **Evidence:** `do_python_setup` checks `$PROJECT_ROOT/setup/setup.py` (start.sh:176-178) and later runs `python3 setup/setup.py` (start.sh:204). That file does not exist; the entry point is root `setup.py` (`setup/` has no `setup.py`). In production mode the function returns silently, so no Cloudflare provisioning or deploy happens while start.sh reports success. start.sh also never starts the worker (no `wrangler dev`), contrary to AGENTS.md ("start frontend dev server and worker together"), and opens `:5173` (start.sh:~246).
- **Repro (static):** `ls setup/setup.py` (absent); read start.sh:174-207.
- **Fix hint:** point to `$PROJECT_ROOT/setup.py`, fail loudly if missing, and either start the worker or correct AGENTS.md.
- **Status:** open
- **Verified:** read-only: start.sh, directory listing of setup/.

### ARCH-006
- **Sev:** P1
- **Area:** frontend dev port / CORS / Google origins
- **Journeys:** first run (local sign-in, local API calls)
- **Evidence:** Vite is on 5175 (`frontend/vite.config.ts:78`; comment at :79 says 5174). Docs say 5174 (README.md:52, frontend/README.md:29, worker/README.md:137, ARCHITECTURE.md), start.sh and SETUP.md say 5173 (SETUP.md:91), Playwright baseURL is 5175 but its webServer waits on 5174 (`frontend/playwright.config.ts:4,38`). Worker CORS allows only 5173 and 5174 (`worker/wrangler.jsonc:57` and `:91`). Result: a locally run frontend on 5175 is not in `CORS_ALLOWED_ORIGINS` and not in the documented Google "Authorized JavaScript origins", so API calls and sign-in fail on a clean machine. Playwright's `webServer` check on 5174 will time out.
- **Repro (static):** compare the five locations above. Executor: `npm run dev` in frontend and sign in.
- **Fix hint:** pick one port, set it in vite.config.ts, playwright.config.ts, CORS vars, start.sh and the docs.
- **Status:** open
- **Verified:** read-only: vite.config.ts, playwright.config.ts, wrangler.jsonc, SETUP.md, READMEs, start.sh.

### ARCH-007
- **Sev:** P1
- **Area:** worker/deployment mode
- **Journeys:** AI generation in selfHosted, usage budget
- **Evidence:** the worker reads `env.DEPLOYMENT_MODE ?? 'saas'` for token budget checks (`worker/src/index.ts:1004,1574,1586,2532`) and `checkTokenBudget` enforces budgets unless the mode is not `'saas'` (`worker/src/auth.ts:34-37`). `features.yaml:9` says `selfHosted`, but no `DEPLOYMENT_MODE` var exists in worker/wrangler.jsonc, setup does not write it (grep of setup/ finds none), and `scripts/generate_features.py:97-107` only rewrites an existing key (a no-op). The worker's generated `deploymentMode` constant is not used by index.ts (import list at :104). A selfHosted deploy therefore runs with SaaS budgets and can block generation with a per-user monthly cap.
- **Repro (static):** grep `DEPLOYMENT_MODE` across worker/wrangler.jsonc, setup/, scripts/ and worker/src. Executor: deploy selfHosted, exceed the default budget.
- **Fix hint:** use the generated `deploymentMode` in the worker instead of an env var, or have setup write `DEPLOYMENT_MODE` into wrangler vars.
- **Status:** open
- **Verified:** read-only: index.ts lines above, auth.ts, wrangler.jsonc, generate_features.py, setup grep.

### ARCH-008
- **Sev:** P1
- **Area:** frontend/automations guide, channel OAuth
- **Journeys:** connect LinkedIn
- **Evidence:** the in-app guide tells users to register `https://your-worker.workers.dev/api/auth/linkedin/callback` (`frontend/src/features/automations/LinkedInSetupGuide.tsx:33`). The worker route is `/auth/linkedin/callback` (`worker/src/index.ts:772`) and SETUP.md:171 documents `/auth/linkedin/callback`. A user following the in-app text registers a redirect URI that never matches, so the connect popup fails.
- **Repro (static):** compare the three lines.
- **Fix hint:** change the guide text to `/auth/linkedin/callback`.
- **Status:** open
- **Verified:** read-only: LinkedInSetupGuide.tsx, index.ts:772-790, SETUP.md:166-173.

### ARCH-009
- **Sev:** P1
- **Area:** root wrangler.jsonc
- **Journeys:** deploy
- **Evidence:** `wrangler.jsonc:3` names the worker `linkedin-bot-api`, same as `worker/wrangler.jsonc:3`, but it has no `main` and `assets.directory` is `frontend` (source tree, not `frontend/dist`) (`wrangler.jsonc:6-8`). Running `wrangler deploy` from the repo root would replace the API worker with an assets-only worker (and uploads the frontend source folder; no `.assetsignore` exists in the repo or frontend/, while tracked `frontend/.env.development` sits in that folder). ARCHITECTURE.md says the root file makes "deploying the main worker also serve the SPA build" at `frontend/dist`.
- **Repro (static):** read wrangler.jsonc and `ls -a . frontend | grep assetsignore` (none). Executor: `wrangler deploy --dry-run` from root and inspect the asset list.
- **Fix hint:** make the asset directory `frontend/dist`, add `.assetsignore`, and either merge into worker/wrangler.jsonc or give the root file a distinct name.
- **Status:** open
- **Verified:** read-only: root and worker wrangler configs, directory listing. Wrangler's default asset ignore list was not checked.

### ARCH-010
- **Sev:** P1
- **Area:** worker/scheduled-publish DO
- **Journeys:** schedule a post (no double posts, no lost schedules)
- **Evidence:** `alarm()` runs `executeScheduledPublish` and deletes the stored task only after success; on any error it logs and rethrows (`worker/src/scheduled-publish/ScheduledPublishAlarm.ts:85-100`). A rethrown alarm error makes the runtime retry the alarm, and the task stays stored. If publish succeeded on the channel but a later step (sheet/D1 status write) threw, the retry can publish again. Idempotency of `executeScheduledPublish` was not read in this pass.
- **Repro (static):** read ScheduledPublishAlarm.ts:85-100, then `executeScheduledPublish` in index.ts and check for a "already published" guard keyed by topic and channel.
- **Fix hint:** add an idempotency check (published flag or status read) at the start of `executeScheduledPublish`, and cap retries with a terminal failed state.
- **Status:** open
- **Verified:** read-only: ScheduledPublishAlarm.ts. Hypothesis, not confirmed.

### ARCH-011
- **Sev:** P2
- **Area:** worker/auth + CORS defaults
- **Journeys:** sign-in, data safety
- **Evidence:** the Google audience check runs only `if (env.GOOGLE_CLIENT_ID && ...)` (`worker/src/index.ts` ~3061), so an unset client id accepts tokens minted for any Google client. `buildCorsHeaders` falls back to `Access-Control-Allow-Origin: *` when `CORS_ALLOWED_ORIGINS` is empty (`worker/src/index.ts:6304-6308`). `.env.example` does not list `CORS_ALLOWED_ORIGINS` and setup only merges it when present (`setup/worker_config.py:173-181`). Prod wrangler sets it, but it lists localhost origins (`worker/wrangler.jsonc:57`).
- **Repro (static):** read the two code sites.
- **Fix hint:** reject when `GOOGLE_CLIENT_ID` is unset, and default CORS to deny.
- **Status:** open
- **Verified:** read-only: index.ts sites, wrangler.jsonc, setup/worker_config.py.

### ARCH-012
- **Sev:** P2
- **Area:** committed config / secrets
- **Journeys:** deploy by a second owner, data safety
- **Evidence:** `worker/wrangler.jsonc:100` commits a literal `DEV_GOOGLE_AUTH_BYPASS_SECRET` value under `env.local`; the same value is in tracked `frontend/.env.development` (`VITE_DEV_GOOGLE_AUTH_BYPASS_SECRET`, comment says it matches wrangler). `worker/wrangler.jsonc:52-65` also commits the owner's emails, OAuth client ids, bucket name, D1/KV ids and the owner's `workers.dev` generation URL. `worker/src/index.ts:3021` hard-codes `DEFAULT_ADMIN_EMAIL` to the owner's address, so a fork that leaves `ADMIN_EMAILS` empty makes the original owner an admin on someone else's deployment. `.gitignore` does cover `.env` and `.dev.vars` (checks pass).
- **Repro (static):** `git ls-files | grep -E '\.env'` lists `frontend/.env.development`; read the lines above.
- **Fix hint:** move local secret to untracked `.dev.vars`, replace owner data with placeholders that setup fills, remove the hard-coded admin fallback (fail closed).
- **Status:** open
- **Verified:** read-only: wrangler.jsonc, frontend/.env.development (values not copied), index.ts:3020-3027, `git ls-files`.

### ARCH-013
- **Sev:** P2
- **Area:** worker local env
- **Journeys:** local dev generation
- **Evidence:** `env.local` has no `services` entry and no triggers (`worker/wrangler.jsonc:67-117`); bindings are not inherited by a named env. `GENERATION_WORKER_URL` in `env.local.vars` is the owner's production URL (`:99`), so local dev falls back to calling production generation (`generationWorkerClient.ts:84-90,108`), with `GENERATION_WORKER_SECRET` coming from `.dev.vars`. `GENERATION_WORKER_URL` is also missing from `.dev.vars` guidance.
- **Repro (static):** read env.local and the client fallback.
- **Fix hint:** add the service binding (or a local URL) to `env.local` and document running generation-worker locally.
- **Status:** open
- **Verified:** read-only: wrangler.jsonc, generationWorkerClient.ts.

### ARCH-014
- **Sev:** P2
- **Area:** .env.example / env contract
- **Journeys:** first run, deploy
- **Evidence:** env names read in code but not in `.env.example` or any wrangler config: `YOUTUBE_CLIENT_ID`, `YOUTUBE_CLIENT_SECRET` (`worker/src/index.ts:3276,3457`), `OAUTH_REDIRECT_BASE_URL` (`worker/src/automations/routes.ts:24`; index.ts:3279), `DEV_SPREADSHEET_ID` (index.ts:3108), `NEWS_SNAPSHOT_MAX_AGE_DAYS` (index.ts:657), `DEV_GOOGLE_AUTH_BYPASS_EMAIL`, `WORKER_SHARED_SECRET` (generation-worker/src/index.ts:42; only mentioned as a comment), `VITE_E2E_BYPASS_SECRET` and `VITE_PIPELINE_LIVE_URL` (frontend). The worker reads `GOOGLE_SERVICE_ACCOUNT_JSON` while `.env.example` and SETUP.md use `GOOGLE_CREDENTIALS_JSON`; setup maps one to the other (`setup/worker_config.py:234,277`) but the wizard writes `GOOGLE_SERVICE_ACCOUNT_JSON` to `.env` (`setup/wizard/steps/google.py:72`) and `verify.py:57` checks that name. Default drift: `NEWS_SNAPSHOT_MAX_PER_TOPIC` default `10` in wrangler and setup (`worker_config.py:167`) vs. blank handling at index.ts:648.
- **Repro (static):** the comm of `env.X` refs against `.env.example` keys (see Verified).
- **Fix hint:** add the missing keys with comments; unify the credential variable name.
- **Status:** open
- **Verified:** read-only: grep of `env.<NAME>` in worker/src and generation-worker/src vs `.env.example` and wrangler var keys; frontend `import.meta.env.*` grep.

### ARCH-015
- **Sev:** P2
- **Area:** setup.py compile check
- **Journeys:** setup / release hygiene
- **Evidence:** AGENTS.md and setup/AGENTS.md:25 say `tsc --noEmit` runs after every invocation. In `setup.py:98-104` it runs only when `install_worker_deps` is true (set by `--install-worker-deps`, `--cloudflare`, `--deploy-worker`, `--sync-github-secrets`, `--all`). It is skipped for plain `python setup.py` and for `--web` (returns at :84-87, before everything). It runs in `worker/` and `frontend/` only, not generation-worker (`setup/cloudflare.py:575-586`), and failure raises before Google/Cloudflare steps.
- **Repro (static):** read setup.py:81-105.
- **Fix hint:** correct the docs, or run the check on all paths and add generation-worker.
- **Status:** open
- **Verified:** read-only: setup.py, setup/cloudflare.py:575-586, setup/cli.py.

### ARCH-016
- **Sev:** P3
- **Area:** .env.example hygiene
- **Journeys:** first run
- **Evidence:** keys with no reader in worker, generation-worker or frontend: `GOOGLE_SHEET_ID`, `GOOGLE_DOC_ID`, `GOOGLE_CLOUD_STORAGE_PREFIX` (SETUP.md:254 also lists it), `TELEGRAM_CHANNEL_ID`, `GMAIL_PUBSUB_TOPIC`, `CLOUDFLARE_API_TOKEN`, `GITHUB_REPO`, `GITHUB_PAGES_ORIGIN` (setup-only keys are fine; the others look dead). `XAI_API_KEY`, `OPENROUTER_API_KEY`, `MINIMAX_API_KEY` appear twice (`.env.example:40-45` commented, `:48-50` live). `:117` refers to "line 58 above" which no longer matches. `ALLOWED_EMAILS` is comma-separated in `.env.example:5` and space-separated in wrangler (`worker/wrangler.jsonc:52`); parser accepts both (index.ts:3013-3018). `setup/cli.py:40` says the wizard is at `localhost:4242`, matching server.py:39 but not the Node wizard on 3456.
- **Repro (static):** read `.env.example`.
- **Fix hint:** prune dead keys, dedupe, fix the stale reference.
- **Status:** open
- **Verified:** read-only: .env.example, env grep.

### ARCH-017
- **Sev:** P3
- **Area:** docs drift
- **Journeys:** developer onboarding
- **Evidence:** see the drift rows in the Conformance table: AGENTS.md and worker/AGENTS.md (Anthropic Claude, Firebase tokens, "lightweight router", KV for sessions), frontend/AGENTS.md (React 18, port 5173, `server/` as proxy config), packages/AGENTS.md (researcher providers), setup/AGENTS.md (`cli.py` role), ARCHITECTURE.md (migration counts, `usage_model`, line count, DO flow, flag list, cron scope, dev-bypass names), `cd worker && npm test` (no script), undocumented routes `/api/feed`, `/api/clips`, `/api/quickchange/stream`, `/v1/health`.
- **Repro (static):** compare rows.
- **Fix hint:** one docs pass after the P0/P1 fixes; update ARCHITECTURE.md as the spec.
- **Status:** open
- **Verified:** read-only: all listed docs vs code paths cited in the table.

### ARCH-018
- **Sev:** P3
- **Area:** features.yaml / generator
- **Journeys:** flag-gated features
- **Evidence:** `scripts/generate_features.py:23-32` defaults differ from `features.yaml` and docs: `multiProviderLlm` False (yaml true), `contentReview` False, `contentFlow` False, `videoEpisodes` False, `deploymentMode` 'saas'. A missing or unparsable yaml silently turns these off. `frontend/src/features/setup-wizard/SetupWizard.tsx:151` defaults the wizard to 'saas'. `FEATURE_ENRICHMENT` is enforced in the generation pipeline (pipeline.ts:114) and settings UI (DashboardSettingsDrawer.tsx:1172,1615) but the worker has no enrichment RPC gate, although features.yaml:3-6 says disabled features turn off Worker RPCs. Generated files match yaml values (pass). For selfHosted the shipped values are sensible; for saas, `videoEpisodes: true` in yaml contradicts the yaml comment at :22-23 ("false for saas").
- **Repro (static):** read generator DEFAULTS vs yaml.
- **Fix hint:** align defaults with yaml, set `videoEpisodes` per mode.
- **Status:** open
- **Verified:** read-only: features.yaml, generate_features.py, both generated files, flag reads in frontend, worker, gen-worker.

### ARCH-019
- **Sev:** P3
- **Area:** CI deploy
- **Journeys:** deploy
- **Evidence:** `deploy-workers.yml` runs the main worker and generation worker jobs in parallel with no `needs` (:16-88). The main worker has a service binding to `linkedin-generation-worker` (`worker/wrangler.jsonc:45-50`), so the first deploy on a new account can fail if the generation worker does not exist yet. The worker `typecheck` script runs `python3 ../scripts/generate_features.py` first (`worker/package.json:7`), which needs PyYAML on the runner; the workflow has no Python setup step. Neither Pages nor workers workflows run tests.
- **Repro (static):** read the workflow and package.json.
- **Fix hint:** add `needs`, a Python/PyYAML step, and test steps.
- **Status:** open
- **Verified:** read-only: deploy-workers.yml, deploy-pages.yml, worker/package.json.

### ARCH-020
- **Sev:** P3
- **Area:** start.sh db reset
- **Journeys:** dev
- **Evidence:** `do_db_reset` targets a D1 named `github_automation` and tables `drafts`/`posts` (start.sh:105-111); the project's DBs are `linkedin-pipeline-db` and `linkedin-gen-worker-db`. It also uses `grep -oP`, not available on macOS grep, and hides errors (`|| true`).
- **Repro (static):** read start.sh:90-118.
- **Fix hint:** remove or retarget.
- **Status:** open
- **Verified:** read-only: start.sh.

## Check results (record of passes)

1. Docs vs code: done (table). Named modules, DO class, bindings exist. No documented component is absent except `usage_model`, `npm test` in worker. Large code areas with no doc: `worker/src/newsletter`, `worker/src/automations`, `worker/src/features/episodes`, `generation-worker/src/players` (partly in gen AGENTS), `/api/feed`, `/api/clips`.
2. wrangler vs code: all wrangler vars read except `ALLOWED_EMAILS` (ARCH-002); gen-worker bindings `GEN_DB`, `VARIANTS_KV`, `CLIPS_KV` are declared (generation-worker/wrangler.jsonc:9-25) and read.
3. `.env.example` vs reads: ARCH-014, ARCH-016.
4. features: generated files in sync with yaml; ARCH-018 for defaults.
5. Security config: ARCH-001, 002, 011, 012; CORS and OAuth ids set in `worker/wrangler.jsonc:52-65`; no secret found in `frontend/src` beyond the bypass wiring; `.gitignore` OK.
6. Deploy docs: migrations 0001..0021 contiguous; setup applies them (setup/cloudflare.py:291-356); SETUP.md does not mention migrations explicitly. Start.sh issues in ARCH-005/020.
7. Naming: consistent across wrangler, setup, docs; root file collision in ARCH-009.
8. Compile-check claim: ARCH-015.
9. Scheduled work: cron wired to `scheduled()` (index.ts:1277); DO class exported and bound; ARCH-004 and ARCH-010.
