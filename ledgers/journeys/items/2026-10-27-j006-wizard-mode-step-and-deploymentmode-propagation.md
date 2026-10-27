---
id: 2026-10-27-j006-wizard-mode-step-and-deploymentmode-propagation
title: J-006 Wizard mode step and deploymentMode propagation
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: workflow
scope_type: section
scope: frontend
actor: Self-hosting operator
trigger: 'Wizard running; `features.yaml` currently `deploymentMode: selfHosted` on this branch.'
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- setup/wizard/steps/mode.py
- features.yaml
- scripts/generate_features.py
- frontend/src/generated/features.ts
- worker/src/generated/features.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'yes'
external_service: none
legacy_id: J-006
---

## Purpose and scope

Wizard mode step and deploymentMode propagation. Priority P1, CORE yes. Imported from journey J-006 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Self-hosting operator. Preconditions: Wizard running; `features.yaml` currently `deploymentMode: selfHosted` on this branch.

## Steps and information flow

1. `/step/mode`, choose `selfHosted`, submit (POST `/step/mode`, form field `mode`).
2. Confirm `features.yaml` `deploymentMode` and `frontend/src/generated/features.ts` were regenerated (`python3 scripts/generate_features.py`).
3. Compare with the worker: `worker/src/generated/features.ts` has FEATURE_* flags only; the worker budget gate reads `env.DEPLOYMENT_MODE ?? 'saas'` (see J-126).

## Modules and code map

setup/wizard/steps/mode.py, features.yaml, scripts/generate_features.py, frontend/src/generated/features.ts, worker/src/generated/features.ts

Code anchors that exist: setup/wizard/steps/mode.py, features.yaml, scripts/generate_features.py, frontend/src/generated/features.ts, worker/src/generated/features.ts

## Success and acceptance

`grep deploymentMode features.yaml` shows the chosen mode; `frontend/src/generated/features.ts` agrees. Unknown form values silently become `saas` (mode.py `submit`).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
