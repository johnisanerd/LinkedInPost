# Raw findings: setup / install / CI (SET)

Counts: P0 = 7, P1 = 10, P2 = 15, P3 = 2 (total 34)
Scope read: setup.py, start.sh, setup/*.py, setup/wizard/{server,state}.py + steps/*.py + templates (grep), scripts/*, .env.example, SETUP.md, .github/workflows/*, plus frontend/server/setupWizard.js (the wizard that start.sh and scripts/*.sh actually launch).
All findings are static code reading (nothing run). Existing IDs referenced, not duplicated: ARCH-005 (start.sh wrong setup path), ARCH-006 (ports), ARCH-009 (root wrangler), ARCH-015 (tsc gate), ARCH-020 (start.sh db reset).

---

### SET-001 Node setup wizard listens on all interfaces, no auth, and returns secret values
- **Sev:** P0
- **Area:** frontend/server/setupWizard.js (launched by start.sh, scripts/setup-local.sh, scripts/setup-launcher.sh via `npm run setup-wizard`)
- **Journeys:** J-001, J-011
- **Evidence:** `server.listen(PORT, ...)` (setupWizard.js:595) passes no host, so Node binds `::`/0.0.0.0, reachable from the LAN (the Flask wizard correctly uses 127.0.0.1, setup/wizard/server.py:44). No auth, no Host check. `GET /api/setup/state?projectDir=` (setupWizard.js:64-160) parses `frontend/.env` and `worker/.dev.vars` and returns each required var's raw `value` (GEMINI_API_KEY, GOOGLE_CREDENTIALS_JSON, ...) in the `envVars` array (setupWizard.js:131-141). Anyone on the same network can read the operator's keys while the wizard runs.
- **Repro:** static. Run `./start.sh`, then from another host `curl 'http://<lan-ip>:3456/api/setup/state?projectDir=/abs/path/to/repo'`.
- **Fix hint:** `server.listen(PORT, '127.0.0.1')`; drop the raw `value` from the state response (return only `isSet`); reject non-localhost Host headers.
- **Status:** open
- **Verified:** read-only: frontend/server/setupWizard.js, start.sh, scripts/setup-local.sh

### SET-002 Wizard `run-setup-py` takes args, env vars and project dir from the request body (remote code execution)
- **Sev:** P0
- **Area:** frontend/server/setupWizard.js:270-310
- **Journeys:** J-001, J-002
- **Evidence:** `const env = { ...process.env, ...envVars }` and `spawn('python3', ['setup.py', ...args], { cwd: projectDir, env })`. A caller can set `PYTHONPATH`, `PATH`, `NODE_OPTIONS`, `PYTHONSTARTUP` etc. and any `projectDir` that holds a `setup.py` (the only check is `path.resolve` plus `.includes('..')`, which is a no-op after resolve). Combined with SET-001 this is unauthenticated remote code execution for anything that can reach port 3456.
- **Repro:** static. POST `{"projectDir":"/tmp/x","args":[],"envVars":{"PYTHONPATH":"/tmp/evil"}}` to `/api/setup/run-setup-py`.
- **Fix hint:** fix `projectDir` to the server's own repo root, allow-list args (`--cloudflare`, `--deploy-worker`, ...) and env keys, bind to loopback.
- **Status:** open
- **Verified:** read-only: frontend/server/setupWizard.js

### SET-003 `reset-database` builds a `bash -c` string from the request's `projectDir` (command injection)
- **Sev:** P0
- **Area:** frontend/server/setupWizard.js:355-370
- **Journeys:** J-001, J-011
- **Evidence:** ``spawn('bash', ['-c', `cd "${workerDir}" && npx wrangler d1 execute ...`])`` where `workerDir = join(projectDir, 'worker')`. A `projectDir` containing `"; <cmd>; "` breaks out of the quotes. Also deletes rows with no confirmation and targets tables `sheet_rows` / `generation_runs` (the shell script start.sh uses different names, see ARCH-020).
- **Repro:** static. POST `{"projectDir":"/x\"; touch /tmp/pwned; \""}`.
- **Fix hint:** use `spawn('npx', [...], { cwd })` with an argument array and a fixed repo root; require an explicit confirm token.
- **Status:** open
- **Verified:** read-only: frontend/server/setupWizard.js

### SET-004 Wizard `write-config` writes arbitrary dirs, allows `.dev.vars` line injection, truncates existing files
- **Sev:** P0
- **Area:** frontend/server/setupWizard.js:178-225
- **Journeys:** J-001, J-003
- **Evidence:** Keys and values come from the body and are written verbatim (`${key}=${trimmed}`); a value containing `\n` injects extra variables (e.g. `DEV_GOOGLE_AUTH_BYPASS_SECRET=...`, `ADMIN_EMAILS=...`), a key can contain anything. `writeFileSync` replaces `frontend/.env` and `worker/.dev.vars` entirely (drops all keys not in the payload, including setup.py-generated `SECRET_ENCRYPTION_KEY`, see SET-007) with default permissions (0644). `mkdir(..., recursive)` on an arbitrary `projectDir`.
- **Repro:** static. POST envVars `{"X":"a\nDEV_GOOGLE_AUTH_BYPASS_SECRET=pwn"}`, then run the worker.
- **Fix hint:** validate key names against `^[A-Z][A-Z0-9_]*$`, reject control chars in values, merge instead of truncate, `mode: 0o600`, fix project root server-side.
- **Status:** open
- **Verified:** read-only: frontend/server/setupWizard.js

### SET-005 `SECRET_ENCRYPTION_KEY` printed in plain text in the bootstrap summary (and streamed to the wizard browser)
- **Sev:** P0
- **Area:** setup/worker_config.py:439; setup/wizard/steps/deploy.py:35-36,90
- **Journeys:** J-002, J-001, J-005
- **Evidence:** `print(f'SECRET_ENCRYPTION_KEY = {worker_bootstrap.encryption_key}')`. Other secrets in the same function are masked (`<configured>`, line 434/438), so this one is an oversight. The key encrypts stored channel tokens. It lands in terminal scrollback, CI logs if setup.py runs there, and the wizard's SSE log at `/step/deploy/stream`.
- **Repro:** static. Run `python setup.py --cloudflare`, read the summary.
- **Fix hint:** print `<set, see worker/.dev.vars>` like the others.
- **Status:** open
- **Verified:** read-only: setup/worker_config.py, setup/wizard/steps/deploy.py

### SET-006 Auth-bypass secret is pushed to the production Worker and an E2E secret is baked into the public Pages bundle
- **Sev:** P0
- **Area:** setup/worker_config.py:270-283; setup/cloudflare.py:156-175; setup/github.py:157-195; .github/workflows/deploy-pages.yml:51-52
- **Journeys:** J-012, J-015, J-002
- **Evidence:** `build_worker_secret_values` always includes `DEV_GOOGLE_AUTH_BYPASS_SECRET` in the prod `--secrets-file`, and `set_worker_secrets` also does `wrangler secret put` for it. The Worker treats any request whose `idToken` equals that string as an admin session (worker/src/plugins/dev-google-auth-bypass/resolve-session.ts:20-38, doc comment: "Do not set these variables in production"). `sync_github_secrets` generates `E2E_BYPASS_SECRET`, and deploy-pages.yml injects it as `VITE_E2E_BYPASS_SECRET` into the public JS bundle; the code comments (worker_config.py:270, github.py:160) say the two values must be the same. So the documented design places a prod admin password into a public bundle. (The generated value differs from the dev value unless the operator makes them equal; either way the E2E feature cannot work without exposing it.)
- **Repro:** static. Set both secrets equal as the comments direct, build Pages, grep `dist/assets/*.js` for the value, send it as `idToken` to the prod Worker.
- **Fix hint:** never deploy the bypass secret to prod; remove `VITE_E2E_BYPASS_SECRET` from the Pages build (run E2E against a separate staging Worker).
- **Status:** open
- **Verified:** read-only: setup/worker_config.py, setup/cloudflare.py, setup/github.py, .github/workflows/deploy-pages.yml, worker/src/plugins/dev-google-auth-bypass/resolve-session.ts

### SET-007 Re-running setup on a machine without `worker/.dev.vars` rotates `SECRET_ENCRYPTION_KEY` and pushes it to production (stored tokens become undecryptable)
- **Sev:** P0
- **Area:** setup/worker_config.py:115-122; setup/github.py:53; setup/cloudflare.py:635-642
- **Journeys:** J-007, J-002, J-027-class channel connection flows
- **Evidence:** `load_worker_encryption_key` returns env, else `.dev.vars` (gitignored, local only), else a NEW random key. `ensure_worker_deploy` ships it as a Worker secret. On a new machine, after `rm worker/.dev.vars`, or after SET-004 truncates it, a redeploy replaces the production key; previously encrypted tokens in D1/KV can no longer be read. Same for `WORKER_SCHEDULER_SECRET` (less severe) and `GENERATION_WORKER_SECRET`. No warning or confirmation, no check against the deployed Worker.
- **Repro:** static. Deploy once; delete `worker/.dev.vars` and unset `SECRET_ENCRYPTION_KEY`; run `python setup.py --deploy-worker`; observe a different key in the secrets file.
- **Fix hint:** persist generated keys to `.env` (0600) at creation; refuse to deploy a freshly generated key if the Worker already has the secret (`wrangler secret list`) unless `--rotate-keys`.
- **Status:** open
- **Verified:** read-only: setup/worker_config.py, setup/github.py, setup/cloudflare.py

### SET-008 `--deploy-worker` aborts on a clean `.env` because the secrets-file builder rejects the empty bypass secret
- **Sev:** P1
- **Area:** setup/worker_config.py:282; setup/cloudflare.py:600-604
- **Journeys:** J-002, J-001, J-005
- **Evidence:** `build_worker_secret_values` puts `'DEV_GOOGLE_AUTH_BYPASS_SECRET': os.environ.get(..., '')` into the required dict (not the `optional` dict that is filtered). `build_wrangler_secrets_file` raises `Missing required Worker secrets ... DEV_GOOGLE_AUTH_BYPASS_SECRET` for any empty value. `.env.example` leaves it commented out (line 131). So the documented happy path (SETUP.md "python setup.py --all") fails at the main Worker deploy, after the generation worker has already been deployed. The only "fix" is to create a production bypass secret (SET-006).
- **Repro:** static. Clean `.env` without `DEV_GOOGLE_AUTH_BYPASS_SECRET`, `python setup.py --deploy-worker`.
- **Fix hint:** move that key to the `optional` dict (and delete the prod push per SET-006).
- **Status:** open
- **Verified:** read-only: setup/worker_config.py, setup/cloudflare.py, .env.example

### SET-009 `setup.py` imports `dotenv` at module top, before the dependency installer can run; `--skip-google` and `--web` never install anything
- **Sev:** P1
- **Area:** setup.py:55; setup/python_requirements.py:11-16
- **Journeys:** J-001, J-002, J-007
- **Evidence:** `from dotenv import load_dotenv` (setup.py:55) executes before `main()`; on a clean interpreter it raises `ModuleNotFoundError` so `ensure_google_setup_python_deps` (line 107-109) is unreachable. SETUP.md:54 promises auto-install. The installer also only probes `google.cloud.storage` (python_requirements.py:13), so missing `flask`, `requests`, `PyYAML`, `json5` are never detected, and it is skipped entirely with `--skip-google`. `--web` returns at setup.py:84 before it.
- **Repro:** static / fresh venv: `python setup.py --web` without `pip install -r requirements.txt`.
- **Fix hint:** wrap the dotenv import in try/except and run the ensure-deps step first; probe all of requirements.txt.
- **Status:** open
- **Verified:** read-only: setup.py, setup/python_requirements.py, requirements.txt, SETUP.md

### SET-010 `run_typescript_dry_run` calls `npx tsc` in `frontend/` that setup never installs; setup aborts on a clean clone
- **Sev:** P1
- **Area:** setup/cloudflare.py:575-586; setup.py:102-104
- **Journeys:** J-009, J-002, J-001
- **Evidence:** `install_worker_dependencies` installs only `worker/` and `generation-worker/` (cloudflare.py:196-223). `frontend/` is not a root workspace (package.json workspaces: packages/*, generation-worker, worker). With no `frontend/node_modules`, `npx tsc` tries to fetch the unrelated `tsc` package (or prompts) and `run_command` raises, which setup.py:165-169 turns into a hard stop before any Google/Cloudflare work. Related to ARCH-015 (gate coverage); this is the clean-machine failure.
- **Repro:** static. Fresh clone, `python setup.py --cloudflare`.
- **Fix hint:** `npm ci` in `frontend/` first, or run `tsc` via the installed local binary and skip when absent.
- **Status:** open
- **Verified:** read-only: setup/cloudflare.py, setup.py, package.json

### SET-011 Committed owner ids make `--cloudflare` skip creation and migrate the owner's D1 (non-owner accounts fail); see J-003
- **Sev:** P1
- **Area:** worker/wrangler.jsonc:10-20; setup/cloudflare.py:315-323; setup/worker_config.py:133-137
- **Journeys:** J-003, J-002, J-001
- **Evidence:** the tracked config has `database_id 4dee8b3f-...`, KV ids `3d0846f3...` / `66555d70...`, owner emails, Google client id, bucket and `GENERATION_WORKER_URL ...99pratyush.workers.dev`. `provision_d1_database` treats it as provisioned, runs `migrations apply --remote` against the owner's id (auth error on any other account), and `create_cloudflare_kv_namespaces` reuses the ids. Only `REPLACE_WITH_*` is recognised. Wrangler's first-deploy `--secrets-file` then targets the owner's resources. In the same account it would silently share the owner's data.
- **Repro:** static. Fresh Cloudflare account, `python setup.py --cloudflare`.
- **Fix hint:** commit a template (`wrangler.template.jsonc` with placeholders) and generate `wrangler.jsonc`; or verify ids via `wrangler d1 info` before trusting them.
- **Status:** open
- **Verified:** read-only: worker/wrangler.jsonc, setup/cloudflare.py, setup/worker_config.py

### SET-012 Generation worker KV namespaces are never provisioned; committed ids are the owner's
- **Sev:** P1
- **Area:** generation-worker/wrangler.jsonc:14-21; setup/cloudflare.py (no gen KV code)
- **Journeys:** J-004, J-003, J-002
- **Evidence:** `VARIANTS_KV` and `CLIPS_KV` have fixed ids; grep of setup/ shows KV creation only for `CONFIG_KV` in the main worker (`create_kv_namespace`, cloudflare.py:226). `provision_generation_worker_d1` handles D1 only (386-438), and also treats the owner's D1 id as provisioned. `wrangler deploy` of the generation worker fails on any other account (unknown namespace ids).
- **Repro:** static. Fresh account, `python setup.py --all`, watch `deploy_generation_worker`.
- **Fix hint:** create and patch both KV namespaces in `provision_generation_worker_d1`; use placeholders in the tracked config.
- **Status:** open
- **Verified:** read-only: generation-worker/wrangler.jsonc, setup/cloudflare.py

### SET-013 Web wizard dead-ends at the Cloudflare step: env var name mismatch and a required bucket the wizard never collects
- **Sev:** P1
- **Area:** setup/wizard/steps/google.py:72; setup/wizard/steps/cloudflare.py:75-84; setup/google_resources.py:133-143
- **Journeys:** J-001
- **Evidence:** the Google step writes `GOOGLE_SERVICE_ACCOUNT_JSON` to `.env`. The Cloudflare step shells out to `setup.py --cloudflare` (no `--skip-google`), which requires `GOOGLE_CREDENTIALS_JSON` (google_resources.py:133, cloudflare.py:507,623) and `GOOGLE_CLOUD_STORAGE_BUCKET` (google_resources.py:141-143); both `sys.exit(1)`. The wizard has no bucket field. Result: error text is shown and the step can never complete. `setup/wizard/steps/apikeys.py:19` even lists `GOOGLE_CREDENTIALS_JSON` as a root key, which no step writes. (The Node wizard has the same name confusion, setupWizard.js:75.)
- **Repro:** static. Walk the wizard with valid inputs; at step 4 observe `[fail] GOOGLE_CREDENTIALS_JSON: not set`.
- **Fix hint:** write the canonical name (`GOOGLE_CREDENTIALS_JSON`), add a bucket field, or pass `--skip-google` when the wizard has no Drive bootstrap.
- **Status:** open
- **Verified:** read-only: setup/wizard/steps/{google,cloudflare,apikeys,verify}.py, setup/google_resources.py, setup/cloudflare.py

### SET-014 Wizard shells out to `python` (not `sys.executable`) and to cwd-relative `setup.py`
- **Sev:** P1
- **Area:** setup/wizard/steps/cloudflare.py:75-78; setup/wizard/steps/deploy.py:25; setup/wizard/state.py:6; mode.py:14,26
- **Journeys:** J-001, J-005
- **Evidence:** cloudflare.py uses `['python', 'setup.py', ...]`; macOS and many Debian/Ubuntu installs have no `python` binary, and a venv-less `python` may be a different interpreter without the deps. deploy.py correctly uses `sys.executable` but both use `'setup.py'` relative to cwd, as do `.env`, `.wizard_state.json`, `features.yaml`, `scripts/generate_features.py`. Starting the wizard as `python /path/to/setup.py --web` from another directory writes state/.env in the wrong place and the subprocess cannot find `setup.py`.
- **Repro:** static. `cd ~ && python3 ~/LinkedInPost/setup.py --web`.
- **Fix hint:** use `[sys.executable, str(ROOT/'setup.py'), ...]` and `ROOT`-anchored paths everywhere.
- **Status:** open
- **Verified:** read-only: setup/wizard/steps/*.py, setup/wizard/state.py

### SET-015 Wizard verify step cannot pass: worker URL depends on `CLOUDFLARE_SUBDOMAIN` which nothing sets
- **Sev:** P1
- **Area:** setup/wizard/steps/verify.py:15-32
- **Journeys:** J-008, J-001, J-145
- **Evidence:** `get_worker_url` returns `None` unless the env var `CLOUDFLARE_SUBDOMAIN` is set; grep shows it appears only in tests (setup/wizard/tests/test_verify.py). setup.py parses the real URL (`extract_worker_url`) but never persists it. So "Worker responds" is always `Worker URL unknown`, `all_ok` stays false, `mark_complete('verify')` is never reached, and `/complete` is unreachable by the intended flow. The probe also hits `/health` while setup/verification.py checks `GET /` with a `backend` marker (I could not find a `/health` route in worker/src; hypothesis that this probe 404s even with a URL).
- **Repro:** static. Finish deploy, open `/step/verify`.
- **Fix hint:** persist `VITE_WORKER_URL` from the deploy output into `.env` and read it here; probe the same endpoint setup/verification.py uses.
- **Status:** open
- **Verified:** read-only: setup/wizard/steps/verify.py, setup/verification.py, setup/wizard/tests/test_verify.py (grep), worker/src (grep /health)

### SET-016 Wizard verify reads stale `os.environ`, and its JSONC "comment strip" corrupts URLs
- **Sev:** P2
- **Area:** setup/wizard/steps/verify.py:20-24,46-47,56-58
- **Journeys:** J-008, J-001
- **Evidence:** keys the wizard saved with `set_key` go to files, not `os.environ` (only `CLOUDFLARE_API_TOKEN` is copied, cloudflare.py:72), so "Gemini API key set" and "Google service account set" read the environment from when `python setup.py --web` started, i.e. false for a first run. Separately `re.sub(r'//.*', '', text)` deletes everything after `//` on a line, including `"GENERATION_WORKER_URL": "https://..."` in wrangler.jsonc, making the JSON invalid (returns None). The "Cloudflare token set" check also fails for operators who use `wrangler login` (which `ensure_cloudflare_auth` explicitly supports).
- **Repro:** static.
- **Fix hint:** re-read `.env` via `dotenv_values`, use json5 (already a dependency) for wrangler.jsonc.
- **Status:** open
- **Verified:** read-only: setup/wizard/steps/verify.py, setup/wizard/steps/{google,apikeys}.py, worker/wrangler.jsonc

### SET-017 Copying `.env.example` yields a deployed Worker with a public constant encryption key and placeholder API keys
- **Sev:** P1
- **Area:** .env.example:9-10,22-23,32-33,36,39; setup/worker_config.py:115-122
- **Journeys:** J-002, J-007
- **Evidence:** `.env.example` sets live-looking placeholders: `SECRET_ENCRYPTION_KEY=REPLACE_WITH_BASE64_32_BYTE_KEY`, `GEMINI_API_KEY=your_gemini_api_key_here`, `TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here`, `CLOUDFLARE_API_TOKEN=your_cloudflare_api_token_here`, `GOOGLE_SHARE_EMAIL=your_email@gmail.com`. `load_worker_encryption_key` takes any non-empty env value, so a user who does `cp .env.example .env` and fills only some fields deploys with the string `REPLACE_WITH_BASE64_32_BYTE_KEY` as the key that encrypts channel tokens (known to everyone who reads the repo). Other placeholders are pushed as real secrets too (the secrets-file filter only drops empty values), and the Drive folder is "shared" with a fake address.
- **Repro:** static. `cp .env.example .env`, set required fields, `python setup.py --all`.
- **Fix hint:** comment out all placeholder lines in `.env.example`; in setup.py reject values matching `REPLACE_WITH_|your_.*_here` and require base64 32 bytes for the key.
- **Status:** open
- **Verified:** read-only: .env.example, setup/worker_config.py, setup/cloudflare.py

### SET-018 Re-running `--cloudflare` rewrites wrangler.jsonc vars from env only: blank allow-list reopens sign-up, and migrations/env sections are overwritten
- **Sev:** P1
- **Area:** setup/worker_config.py:144-207; setup/github.py:50-51
- **Journeys:** J-007, J-015, J-003
- **Evidence:** `update_wrangler_config` replaces `config['vars']` wholesale from `WorkerBootstrap` (only CORS and `NEWS_SNAPSHOT_MAX_PER_TOPIC` / `GENERATION_WORKER_URL` are preserved). `ALLOWED_EMAILS`/`ADMIN_EMAILS` come from `--allowed-emails` or env; if the operator set them directly in wrangler.jsonc, the rerun writes `""` (the code warns only: "any verified Google account can sign up"), and `ensure_worker_deploy` deploys that. It also replaces `durable_objects`, `migrations` (single tag `v1`; a later DO migration tag is dropped, which makes the next deploy fail or delete a class), `services`, and the entire `env` object, and `json.dumps` strips all comments. `INSTAGRAM_APP_ID` etc. are blanked the same way.
- **Repro:** static. Hand-edit `ALLOWED_EMAILS` in wrangler.jsonc, then `python setup.py --cloudflare` with an empty env.
- **Fix hint:** merge: only overwrite a var when the new value is non-empty; keep unknown keys and migrations; fail closed (refuse empty ALLOWED_EMAILS in selfHosted mode).
- **Status:** open
- **Verified:** read-only: setup/worker_config.py, setup/github.py, worker/wrangler.jsonc

### SET-019 KV/D1 provisioning is not idempotent and has no rollback
- **Sev:** P2
- **Area:** setup/cloudflare.py:226-254,305-356,386-438; setup.py:119-124
- **Journeys:** J-007, J-002
- **Evidence:** (a) `create_cloudflare_kv_namespaces` returns early only if BOTH ids are real; with one set it creates two new namespaces (orphaning one). New ids are held in memory and written only in `update_worker_wrangler_config` (setup.py:123) after the D1 steps; if `provision_d1_database` or `provision_generation_worker_d1` raises, the new KV ids are lost and the next run creates more. (b) `wrangler d1 create` for a name that already exists (previous run died before patching the id) fails; the `--json` attempt's error is swallowed by `except RuntimeError` and the retry without `--json` raises a generic message, hiding the real cause; no `d1 list` lookup to adopt the existing database. (c) `_patch_d1_database_id` regex replaces every `database_id` in the file.
- **Repro:** static. Make step D1 fail once (bad token scope), rerun, `wrangler kv namespace list` shows duplicates.
- **Fix hint:** list-before-create (`kv namespace list`, `d1 list`), write ids to config immediately after each create.
- **Status:** open
- **Verified:** read-only: setup/cloudflare.py, setup.py

### SET-020 Deploy steps report success when sub-steps failed or the URL was not found
- **Sev:** P2
- **Area:** setup/cloudflare.py:141-193,547-572,644-650; setup/wizard/steps/deploy.py:46-51
- **Journeys:** J-002, J-005, J-008
- **Evidence:** `set_worker_secrets` and `push_llm_secrets` catch `RuntimeError` and only `warn`; a failed `secret put` does not change the exit code. When `extract_worker_url` finds nothing, setup warns and exits 0 (also `verify_worker_endpoint` is skipped), and the wizard marks `deploy` complete on return code 0. Conversely when `verify_worker_endpoint` fails it raises after the Worker is already live and skips GitHub sync/summary, with no rollback or next-step message. `'Success' in stdout` checks depend on wrangler's output wording.
- **Repro:** static.
- **Fix hint:** collect failures and exit non-zero; require a resolved URL before reporting success.
- **Status:** open
- **Verified:** read-only: setup/cloudflare.py, setup/verification.py, setup/wizard/steps/deploy.py

### SET-021 Secret/config files are written with default permissions, not 0600
- **Sev:** P2
- **Area:** setup/cloudflare.py:511,543,663; setup/github.py:141; setup/wizard/steps/{apikeys,google,cloudflare}.py (`dotenv.set_key`); frontend/server/setupWizard.js:216,220
- **Journeys:** J-001, J-002
- **Evidence:** `.env` (service-account private key, Cloudflare token), `worker/.dev.vars`, `generation-worker/.dev.vars` are created with `write_text` / `set_key` / `writeFileSync` under the umask (usually 0644, world-readable on shared hosts). No `chmod` or `os.open(..., 0o600)` anywhere in setup/. (The temp secrets file from `NamedTemporaryFile` is 0600 and is unlinked, which is fine.)
- **Repro:** static. `python setup.py --cloudflare; ls -l worker/.dev.vars`.
- **Fix hint:** shared `write_secret_file()` helper using `os.open(..., 0o600)`; `os.chmod` existing files.
- **Status:** open
- **Verified:** read-only: setup/*.py, setup/wizard/steps/*.py

### SET-022 `.dev.vars` regeneration overwrites the whole file and drops values from earlier steps
- **Sev:** P2
- **Area:** setup/cloudflare.py:504-543,659-663; setup/github.py:129-141
- **Journeys:** J-007, J-001, J-012
- **Evidence:** `write_worker_dev_vars` / `write_generation_worker_dev_vars` rebuild the file from `os.environ` + bootstrap. Anything only present in the file (the `E2E_BYPASS_SECRET` that `_write_dev_var` appended, `DEV_GOOGLE_AUTH_BYPASS_EMAIL`, keys the Python wizard wrote to `worker/.dev.vars` for fields not in `build_worker_dev_values`, e.g. `FAL_API_KEY` for the generation worker) is lost on the next run, so `E2E_BYPASS_SECRET` regenerates each time and the already-synced GitHub secret goes stale. `ensure_worker_deploy` rewrites the file a second time (cloudflare.py:659-663) after deploy. The `set_key` quoting from the wizard (`KEY='v'`) is returned with quotes by `read_worker_dev_var` (worker_config.py:103-112), used as a fallback for the encryption/scheduler/generation secrets (hypothesis for the quote case).
- **Repro:** static.
- **Fix hint:** merge into the existing file; strip quotes when reading.
- **Status:** open
- **Verified:** read-only: setup/cloudflare.py, setup/github.py, setup/worker_config.py, setup/wizard/steps/apikeys.py

### SET-023 `gh secret set --body <value>` puts every secret on the process command line
- **Sev:** P2
- **Area:** setup/github.py:203
- **Journeys:** J-002
- **Evidence:** `['gh','secret','set',name,'--body',value]` exposes `CLOUDFLARE_API_TOKEN`, `WORKER_SCHEDULER_SECRET`, `YOUTUBE_OAUTH_TOKEN` to other local users via `ps`, and into shell-history-like process audit logs. It is also not scoped with `--repo` although `github_repo` is computed (github.py:48), so on a clone with a fork/upstream mismatch the secrets go to whatever repo `gh` resolves.
- **Repro:** static.
- **Fix hint:** pass the value via stdin (`gh secret set NAME` reads stdin) and add `--repo owner/repo`.
- **Status:** open
- **Verified:** read-only: setup/github.py

### SET-024 Python wizard has no CSRF/Host protection; a visited web page can trigger deploys and overwrite config
- **Sev:** P2
- **Area:** setup/wizard/server.py:14,44; setup/wizard/steps/*.py (POST routes)
- **Journeys:** J-001, J-005
- **Evidence:** every POST (`/step/mode`, `/step/google`, `/step/cloudflare`, `/step/apikeys`, `/step/deploy/start`) accepts form-encoded bodies with no token, Origin or Host check; cross-site `<form method=post action=http://localhost:4242/step/deploy/start>` works from any page the operator has open (and DNS rebinding bypasses the 127.0.0.1 bind). `/step/deploy/start` runs `wrangler deploy` with the operator's credentials; `/step/cloudflare` replaces the stored token. `app.secret_key` is the hard-coded string `'linkedin-setup-wizard-local'` (unused today, but trivially forgeable if sessions are added).
- **Repro:** static.
- **Fix hint:** per-run random CSRF token in a hidden field, validate `Host`/`Origin`, random `secret_key`.
- **Status:** open
- **Verified:** read-only: setup/wizard/server.py, steps/deploy.py, steps/cloudflare.py

### SET-025 Wizard deploy step: timeout cannot fire on a silent hang, concurrent starts race, stream blocks forever
- **Sev:** P2
- **Area:** setup/wizard/steps/deploy.py:20-91
- **Journeys:** J-005
- **Evidence:** the 600 s check runs inside `for line in proc.stdout`, i.e. only after a line arrives; a hung wrangler prints nothing, so the deadline never triggers. `/step/deploy/start` has no "already running" guard: two clicks start two `setup.py --deploy-worker` processes sharing one queue/events (`_deploy_done.clear()` of the second wipes state of the first). `generate()` calls `_log_queue.get()` with no timeout; a browser refresh mid-run leaves a consumer thread stuck, and log lines are consumed by whichever listener wins. After a timeout the stream reports `__FAILED__` but no message says why.
- **Repro:** static.
- **Fix hint:** `threading.Timer`/`communicate(timeout)`, lock around start, per-run queue.
- **Status:** open
- **Verified:** read-only: setup/wizard/steps/deploy.py

### SET-026 Wizard API-key step requires a live Gemini call, sends the key in the URL, and fails closed on any network error
- **Sev:** P2
- **Area:** setup/wizard/steps/apikeys.py:46-57,111-117
- **Journeys:** J-001, J-004
- **Evidence:** `validate_gemini_key` POSTs to `.../models/gemini-2.0-flash:generateContent?key={key}`; any non-200 (quota, a retired model name, regional block, offline) blocks the whole wizard with "validation failed" and there is no skip. The key is in the query string (logged by proxies; Google supports the `x-goog-api-key` header). A generation-worker-only deployment with `XAI_API_KEY` (which setup.py explicitly accepts, cloudflare.py:441,461) cannot pass this step. Model name validity is a hypothesis.
- **Repro:** static.
- **Fix hint:** header auth, allow any one LLM key, downgrade validation failure to a warning with a "continue anyway" button.
- **Status:** open
- **Verified:** read-only: setup/wizard/steps/apikeys.py, setup/cloudflare.py

### SET-027 `ensure_cloudflare_auth` runs `npx wrangler` at repo root before deps are installed; root pins wrangler 3.x while workers need 4.x
- **Sev:** P2
- **Area:** setup.py:100-103; setup/cloudflare.py:43-49; package.json devDependencies
- **Journeys:** J-002, J-001
- **Evidence:** auth check precedes `install_worker_dependencies`. In ROOT, `npx wrangler` resolves to the root devDependency `^3.114.17` if installed, otherwise downloads latest and may prompt "Ok to proceed?" on stdin (stdin is inherited, only stdout/stderr captured, so it can hang). worker needs `^4.92.0`, generation-worker `^4.78.0`; the `wrangler deploy --secrets-file` path used by setup is a v4-era feature (hypothesis on exact version). Auth probing with a different major than the one that later deploys can give a false pass/fail.
- **Repro:** static.
- **Fix hint:** install deps first, run `npx --no-install wrangler` from `worker/`, align the root devDependency.
- **Status:** open
- **Verified:** read-only: setup.py, setup/cloudflare.py, package.json, worker/package.json, generation-worker/package.json

### SET-028 `setup-production.sh` swallows setup.py failure and prints "Setup Complete!"; launcher scripts need frontend deps they never install
- **Sev:** P2
- **Area:** scripts/setup-production.sh:83,98,103-106; scripts/setup-local.sh:55-56; scripts/setup-launcher.sh:39-40; start.sh:204
- **Journeys:** J-002, J-001, J-011
- **Evidence:** `python3 setup.py $PYTHON_ARGS 2>&1 || true` and the same for generate_features, then the banner "Setup Complete!" runs unconditionally (and start.sh:204 downgrades failure to a warning, see ARCH-005 for the wrong path). `setup-production.sh` installs frontend deps AFTER setup.py. `setup-local.sh` / `setup-launcher.sh` run `npm run setup-wizard` (express, in frontend/package.json) without `npm install`; on a fresh clone the background process dies, `sleep 3` passes, the browser opens a dead port, and `wait` returns non-zero. The "next steps" text references `frontend/.env.example` and `worker/.dev.vars.example` (the latter does not exist; generation-worker has one).
- **Repro:** static. Fresh clone, `./scripts/setup-local.sh`.
- **Fix hint:** remove `|| true`, propagate exit codes, install deps first, poll the port instead of `sleep 3`.
- **Status:** open
- **Verified:** read-only: scripts/setup-production.sh, scripts/setup-local.sh, scripts/setup-launcher.sh, start.sh

### SET-029 `start.sh` sources `.env` as shell code (mangles JSON values and executes content); no cleanup on Ctrl+C
- **Sev:** P2
- **Area:** start.sh:80-85,221-240,255-273
- **Journeys:** J-011, J-001
- **Evidence:** `set -a; source .env` treats `.env` as bash. `.env.example:23` stores `GOOGLE_CREDENTIALS_JSON={"type":"service_account",...}` unquoted; bash strips the double quotes, exporting invalid JSON. python-dotenv does not override existing env vars, so a later `setup.py` run (via the production path) sees the mangled value (hypothesis; blocked today by ARCH-005 path bug). Any `$(...)`, backtick or `;` in a value runs. There is no `trap`, so Ctrl+C kills the foreground `wait` but leaves the backgrounded wizard/Vite process running. The wizard `wait` blocks, so `do_launch_app` only starts after the wizard exits; the two wizards (Node :3456 here vs Flask :4242 documented in SETUP.md) are never reconciled (J-001).
- **Repro:** static.
- **Fix hint:** parse `.env` with python-dotenv or `grep`, do not `source`; add `trap 'kill 0' INT TERM EXIT`.
- **Status:** open
- **Verified:** read-only: start.sh, .env.example, setup.py

### SET-030 Deploy workflow applies remote D1 migrations on every push to main, cancels in flight, and uses unpinned third-party action with Cloudflare credentials
- **Sev:** P2
- **Area:** .github/workflows/deploy-workers.yml:12-14,38-52,74-88
- **Journeys:** J-002, J-145
- **Evidence:** `cloudflare/wrangler-action@v3` (movable tag, third-party) receives `CLOUDFLARE_API_TOKEN`; no SHA pin. Migrations apply against production before deploy and before any test (the job runs `typecheck` only), with `cancel-in-progress: true` keyed on ref, so a second push can kill a run between "migrations applied" and "deploy" (schema ahead of code) or mid-migration. The `deploy-generation-worker` job `npm ci` at repo root (workspace install) but its `cache-dependency-path` is the root lock while `deploy-worker` uses `worker/package-lock.json`; two lockfiles for one workspace can drift. No `permissions:` block (defaults apply). On a fork/clone without the secrets the job fails on every push. No `pull_request_target`, no secret echo found.
- **Repro:** static; push two commits touching worker/ in quick succession.
- **Fix hint:** pin to a commit SHA, `cancel-in-progress: false` for the deploy concurrency group, add `permissions: contents: read`, guard with `if: ${{ secrets.CLOUDFLARE_API_TOKEN != '' }}` (via env) for forks.
- **Status:** open
- **Verified:** read-only: .github/workflows/deploy-workers.yml, package.json, worker/package.json

### SET-031 No CI runs tests or type checks on pull requests; Pages build always uses committed-secret names without a guard
- **Sev:** P2
- **Area:** .github/workflows/ (all three)
- **Journeys:** J-013, J-002
- **Evidence:** the three workflows trigger only on `push: main` or `workflow_dispatch`. AGENTS.md requires `tsc --noEmit` and tests before merge, but nothing enforces it: `deploy-workers.yml` deploys to production straight after `typecheck` of worker/ and generation-worker/ only (frontend `tsc`, frontend vitest, playwright, setup pytest never run). `deploy-pages.yml` builds even when `VITE_WORKER_URL` / `VITE_GOOGLE_CLIENT_ID` repo secrets are unset, publishing a site that points nowhere.
- **Repro:** static.
- **Fix hint:** add a `pull_request` workflow running tsc (all three packages), `npm run test`, `pytest setup/wizard/tests`; fail Pages build when secrets are empty.
- **Status:** open
- **Verified:** read-only: .github/workflows/*.yml, AGENTS.md

### SET-032 YouTube poller workflow loses its "already replied" state on every run (duplicate replies)
- **Sev:** P2
- **Area:** .github/workflows/youtube-comment-poll.yml:13-31; automations/youtube_poller.py:19,140-159
- **Journeys:** J-051-class automation, J-099-class publish safety
- **Evidence:** the poller dedupes via a local file `.youtube_replied_ids` in the runner's working directory. The workflow has no `actions/cache`, artifact or commit step, and GitHub-hosted runners are ephemeral, so each run re-replies to the same comments. The schedule is commented out (workflow_dispatch only), which limits exposure to manual runs.
- **Repro:** static; dispatch twice with the same channel.
- **Fix hint:** persist replied ids in the Worker (KV/D1) or restore/save the file via `actions/cache`.
- **Status:** open
- **Verified:** read-only: .github/workflows/youtube-comment-poll.yml, automations/youtube_poller.py (lines 1-30, 140-260 by grep)

### SET-033 Compile-check and Python version claims are inconsistent across docs, wizard and code
- **Sev:** P3
- **Area:** setup/AGENTS.md ("Python 3.9+"); setup/wizard/steps/prereqs.py:17-37; SETUP.md:35-42; requirements.txt
- **Journeys:** J-001, J-013
- **Evidence:** the wizard hard-requires Python 3.11 and Node 18; setup/AGENTS.md says 3.9+; SETUP.md says "6-step wizard" while the code has 7 (J-001 note) and describes the order "Prerequisites, Google, ..." omitting the mode step. The code itself only needs `from __future__ import annotations` (3.7+). Node 18 is below what wrangler 4 / CI (Node 24) assume (hypothesis). `requirements.txt` pins `google-generativeai==0.8.2` (deprecated package, not imported by setup/ or the wizard; hypothesis on protobuf conflicts with `google-api-python-client>=2.157`), `flask>=3.0` has no upper bound, and the prereq check passes if only `npx` exists (`shutil.which('wrangler') or shutil.which('npx')`).
- **Repro:** static.
- **Fix hint:** pick one floor, update docs; drop unused pins.
- **Status:** open
- **Verified:** read-only: setup/wizard/steps/prereqs.py, setup/AGENTS.md, SETUP.md, requirements.txt, setup/python_requirements.py

### SET-034 Wizard "mode" step: `DEPLOYMENT_MODE` sync target does not exist in wrangler.jsonc (hypothesis)
- **Sev:** P3
- **Area:** scripts/generate_features.py:97-107; setup/wizard/steps/mode.py:17-26; setup/worker_config.py:175-190
- **Journeys:** J-006
- **Evidence:** `update_wrangler_deployment_mode` regex-replaces `"DEPLOYMENT_MODE": "..."` in worker/wrangler.jsonc, but that key is absent from the tracked vars and `update_wrangler_config` never writes it. If the Worker reads `DEPLOYMENT_MODE` from env rather than the generated `features.ts`, choosing the mode in the wizard has no effect on the deployed Worker. Also `set_deployment_mode` raises (HTTP 500) when `features.yaml` is missing or the generator fails (`check=True`), and `.wizard_state.json` is not in .gitignore (only booleans, but it is written into the repo root).
- **Repro:** static; check how worker/src reads deployment mode.
- **Fix hint:** confirm the single source of truth and delete the dead regex or emit the var.
- **Status:** open
- **Verified:** read-only: scripts/generate_features.py, setup/wizard/steps/mode.py, setup/worker_config.py, worker/wrangler.jsonc, .gitignore
