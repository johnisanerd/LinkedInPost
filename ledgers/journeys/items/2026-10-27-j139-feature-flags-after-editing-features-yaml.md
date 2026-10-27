---
id: 2026-10-27-j139-feature-flags-after-editing-features-yaml
title: J-139 Feature flags after editing `features.yaml`
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Developer
trigger: 'Edit `features.yaml` (e.g. `campaign: false`).'
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- features.yaml
- scripts/generate_features.py
- frontend/src/generated/features.ts
- worker/src/generated/features.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P3
core: 'no'
external_service: none
legacy_id: J-139
---

## Purpose and scope

Feature flags after editing `features.yaml`. Priority P3, CORE no. Imported from journey J-139 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Developer. Preconditions: Edit `features.yaml` (e.g. `campaign: false`).

## Steps and information flow

1. `python3 scripts/generate_features.py` (or `python3 setup.py`; also `npm run prebuild` in frontend and `pretypecheck` in worker).
2. Rebuild both; open `/campaign`.

## Modules and code map

features.yaml, scripts/generate_features.py, frontend/src/generated/features.ts, worker/src/generated/features.ts

Code anchors that exist: features.yaml, scripts/generate_features.py, frontend/src/generated/features.ts, worker/src/generated/features.ts

## Success and acceptance

`frontend/src/generated/features.ts` and `worker/src/generated/features.ts` updated; `/campaign` redirects to `/topics` and `bulkImportCampaign` throws the disabled message. Forgetting step 1 leaves the generated constants stale (no CI check seen: `tests/test_scripts_generate_features.py` covers the script only).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
