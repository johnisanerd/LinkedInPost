---
id: 2026-10-27-j008-verify-step-and-worker-health-probes
title: J-008 Verify step and worker health probes
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: workflow
scope_type: section
scope: worker
actor: Self-hosting operator
trigger: Both workers deployed.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- setup/wizard/steps/verify.py
- setup/verification.py
- worker/src/index.ts
- generation-worker/src/index.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'yes'
external_service: Cloudflare
legacy_id: J-008
---

## Purpose and scope

Verify step and worker health probes. Priority P1, CORE yes. Imported from journey J-008 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Self-hosting operator. Preconditions: Both workers deployed.

## Steps and information flow

1. Wizard `/step/verify`.
2. Manually: `curl {WORKER_URL}/` and `curl -H "Authorization: Bearer $WORKER_SHARED_SECRET" {GEN_URL}/v1/health` and `curl -X OPTIONS -H "Origin: https://<frontend>" -H "Access-Control-Request-Method: POST" {WORKER_URL}/`.
3. `POST {WORKER_URL}/` with `{"action":"getTimestamp","idToken":"T","payload":{}}`.

## Modules and code map

setup/wizard/steps/verify.py, setup/verification.py, worker/src/index.ts (`GET /`, `getTimestamp`), generation-worker/src/index.ts (`/v1/health`)

Code anchors that exist: setup/wizard/steps/verify.py, setup/verification.py, worker/src/index.ts, generation-worker/src/index.ts

## Success and acceptance

Step 2: 200 JSON envelope; 200 health; 204 with `Access-Control-Allow-Origin` echoing the frontend origin. Step 3: `{"ok":true,"data":{"timestamp":<unix seconds>}}`.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
