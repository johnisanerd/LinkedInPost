---
id: 2026-10-27-j011-local-development-loop
title: J-011 Local development loop
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Developer
trigger: '`npm install` at root; `worker/.dev.vars` present (written by setup); `frontend/.env.local` with `VITE_WORKER_URL=http://localhost:8787` and `VITE_GOOGLE_CLIENT_ID`.'
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- README.md
- AGENTS.md
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P2
core: 'no'
external_service: none
legacy_id: J-011
---

## Purpose and scope

Local development loop. Priority P2, CORE no. Imported from journey J-011 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Developer. Preconditions: `npm install` at root; `worker/.dev.vars` present (written by setup); `frontend/.env.local` with `VITE_WORKER_URL=http://localhost:8787` and `VITE_GOOGLE_CLIENT_ID`.

## Steps and information flow

1. `cd worker && npm run dev` (wrangler dev `--env local --port 8787`).
2. `cd frontend && npm run dev` (runs vite, `server/sttServer.js`, `server/setupWizard.js` concurrently).
3. Open the printed Vite URL (CORS: `http://localhost:5173` and `5174` are in `CORS_ALLOWED_ORIGINS`; `127.0.0.1` is not).
4. `cd worker && npm run typecheck` and `cd frontend && npx tsc --noEmit`.

## Modules and code map

worker/package.json, frontend/package.json, worker/wrangler.jsonc (`env.local`), README.md, AGENTS.md

Code anchors that exist: README.md, AGENTS.md

## Success and acceptance

`GET http://localhost:8787/` returns the health envelope; sign-in page loads; both typechecks exit 0.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
