---
id: 2026-10-27-j001-web-setup-wizard-end-to-end
title: J-001 Web setup wizard, end to end
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: workflow
scope_type: section
scope: setup
actor: Self-hosting operator
trigger: Clean machine with Python 3, Node, Git; repo cloned; `pip install -r requirements.txt` done; Cloudflare API token and Google service account key to hand.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- setup.py
- setup/cli.py
- setup/wizard/server.py
- setup/wizard/state.py
- SETUP.md
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'yes'
external_service: Cloudflare
legacy_id: J-001
---

## Purpose and scope

Web setup wizard, end to end. Priority P1, CORE yes. Imported from journey J-001 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Self-hosting operator. Preconditions: Clean machine with Python 3, Node, Git; repo cloned; `pip install -r requirements.txt` done; Cloudflare API token and Google service account key to hand.

## Steps and information flow

1. `python setup.py --web` (setup.py `main()` calls `run_wizard()`; Flask binds 127.0.0.1:4242 and opens the browser).
2. `/` redirects to `/step/mode`; pick a mode and submit (POST `/step/mode`).
3. `/step/prereqs` then POST `/step/prereqs/complete`.
4. `/step/google` (service account JSON, OAuth client id) POST.
5. `/step/cloudflare` (API token) POST: D1 and KV provisioned.
6. `/step/apikeys` POST (Gemini required).
7. `/step/deploy`, press start (POST `/step/deploy/start`), watch `/step/deploy/stream`.
8. `/step/verify`, then `/complete`.
- Note: SETUP.md says "6-step wizard"; the code has 7 steps (`mode` is the extra one, `STEPS` in setup/wizard/state.py).

## Modules and code map

setup.py, setup/cli.py, setup/wizard/server.py, setup/wizard/state.py, setup/wizard/steps/*.py, SETUP.md

Code anchors that exist: setup.py, setup/cli.py, setup/wizard/server.py, setup/wizard/state.py, SETUP.md

## Success and acceptance

Each step redirects to the next; `.wizard_state.json` in the repo root has all seven keys `true`; `/complete` renders; both workers respond (see J-008).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
