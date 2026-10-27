---
id: 2026-10-27-j005-wizard-deploy-step-streaming-logs-timeout
title: 'J-005 Wizard deploy step: streaming logs, timeout, working directory'
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: workflow
scope_type: section
scope: setup
actor: Self-hosting operator
trigger: Wizard started from the repo root (it uses relative `Path('features.yaml')`, `.wizard_state.json` and `python setup.py --deploy-worker` without `cwd=`).
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- setup/wizard/steps/deploy.py
- setup/wizard/state.py
- setup/wizard/steps/mode.py
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P2
core: 'yes'
external_service: Cloudflare
legacy_id: J-005
---

## Purpose and scope

Wizard deploy step: streaming logs, timeout, working directory. Priority P2, CORE yes. Imported from journey J-005 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Self-hosting operator. Preconditions: Wizard started from the repo root (it uses relative `Path('features.yaml')`, `.wizard_state.json` and `python setup.py --deploy-worker` without `cwd=`).

## Steps and information flow

1. Start wizard from the repo root, reach `/step/deploy`, POST `/step/deploy/start`.
2. Watch `/step/deploy/stream` (SSE of subprocess lines).
3. Repeat with the wizard started from a subdirectory (`cd setup && python ../setup.py --web`).
4. Make the deploy hang >10 minutes (`_DEPLOY_TIMEOUT_SEC = 600`).

## Modules and code map

setup/wizard/steps/deploy.py, setup/wizard/state.py, setup/wizard/steps/mode.py

Code anchors that exist: setup/wizard/steps/deploy.py, setup/wizard/state.py, setup/wizard/steps/mode.py

## Success and acceptance

Step 2 streams lines and ends with a success marker; step 3 fails with a clear message rather than writing state files in the wrong place; step 4 kills the subprocess and the stream terminates (the timeout is only checked when a new output line arrives, so a silent hang is not killed: CODE-READING FINDING).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
