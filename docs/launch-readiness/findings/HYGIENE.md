# Hygiene and not-implemented items

Checked by reading the files and running git ls-files and grep. Nothing was executed. These were not in the reviewer output; the second completeness pass found them.

### NI-001 P2 worker/youtube - YouTube is offered as a publish channel, but publishing rejects it with "Unsupported delivery channel"
- **Journeys:** J-081
- **Confidence:** confirmed-by-reading
- **Evidence:** worker/src/index.ts:129 (ChannelId includes youtube); worker/src/index.ts:5365-5375 (coerceChannelId accepts only instagram, linkedin, telegram, whatsapp, gmail and throws otherwise); worker/src/index.ts:4841 (publish calls coerceChannelId).
- **Repro:** POST /action with channel "youtube" to a publish action; expect the error "Unsupported delivery channel."
- **Fix hint:** decide: either implement YouTube publish or remove YouTube from the publish channel choices in the UI. The choice is a product decision, so it is an owner question first.

### NI-002 P2 ci/youtube - The YouTube comment poll is saved in the UI but its schedule is commented out in the workflow
- **Journeys:** J-118
- **Confidence:** confirmed-by-reading
- **Evidence:** .github/workflows/youtube-comment-poll.yml:9-11 (the schedule block, including the cron line, is commented out with "Disabled by default").
- **Repro:** save a YouTube poll cron in the UI, then check the Actions tab: no scheduled run appears.
- **Fix hint:** either enable the schedule in the workflow when the UI saves a cron, or show the user that polling is manual-only. Decide which; do not hide the setting.

### NI-003 P2 worker,frontend/test - No `test` script exists in frontend or worker, although AGENTS.md tells agents to run one
- **Journeys:** J-013
- **Confidence:** confirmed-by-reading
- **Evidence:** frontend/package.json scripts: prebuild, dev, build, lint, preview, setup-wizard, test:e2e, test:e2e:ui, test:e2e:headed, test:e2e:setup (no `test`). worker/package.json scripts: pretypecheck, dev, dev:default, dev:remote, deploy, typecheck (no `test`). AGENTS.md says `cd frontend && npm run test` and `cd worker && npm run test`.
- **Repro:** `npm run test` in frontend/ or worker/ fails with "Missing script".
- **Fix hint:** add a `test` script that runs the unit tests (or change AGENTS.md to the scripts that exist). Do not add a script that only runs e2e and calls it unit testing.

### HYG-001 P2 repo/hygiene - 10 .DS_Store files are tracked by git
- **Journeys:** none
- **Confidence:** confirmed-by-reading
- **Evidence:** `git ls-files | grep .DS_Store` returns 10 paths, including .DS_Store, cons/.DS_Store, docs/.DS_Store, generation-worker/.DS_Store, packages/.DS_Store, setup/.DS_Store. The commit fec687f "chore: update .DS_Store" shows this was committed on purpose or by accident.
- **Repro:** `git ls-files | grep -c '\.DS_Store$'` returns 10.
- **Fix hint:** `git rm --cached` each file and add `.DS_Store` to .gitignore.

### HYG-002 P1 state/exec - Runtime state from an agent run is tracked in git
- **Journeys:** none
- **Confidence:** confirmed-by-reading
- **Evidence:** `git ls-files state` returns 14 files: state/exec/events.jsonl, state/exec/cost_meter.jsonl, state/exec/campaign.json, state/exec/ready_queue.json, state/exec/checkpoints/<run-id>/*.json (including PRCreated.json and Committed.json), and state/exec/scratch/<run-id>.md.
- **Why it matters:** these files change on every run, can contain run details and costs, and may include text from prompts. They do not belong in version control.
- **Repro:** `git ls-files state` and read events.jsonl for anything that looks like a credential before deciding what to keep.
- **Fix hint:** `git rm -r --cached state/`, add `state/` to .gitignore. First check the files for secrets or personal data; if any are found, rotate them and record it.

### HYG-003 P1 frontend/.env.development - A tracked dev env file holds an auth-bypass secret key
- **Journeys:** J-136
- **Confidence:** confirmed-by-reading
- **Evidence:** frontend/.env.development is tracked (`git ls-files | grep env.development` lists it). Its keys include VITE_DEV_GOOGLE_AUTH_BYPASS_SECRET and VITE_DEV_GOOGLE_AUTH_BYPASS. The value is not recorded in this file. ARCH-AUDIT.md said .gitignore covers .env; it does not cover .env.development, so this file was missed.
- **Repro:** `git ls-files frontend/.env.development` shows the file; `sed 's/=.*/=<redacted>/' frontend/.env.development` shows the keys.
- **Fix hint:** untrack the file (`git rm --cached`) and ignore `.env.*` except `.env.example`. Check whether the committed value equals any production worker secret; if it does, rotate both. Also see LR-001, which covers the production bypass secret.
