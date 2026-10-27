---
id: 2026-10-27-j125-monthly-token-budget-exhausted
title: J-125 Monthly token budget exhausted
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: SaaS mode; usage >= budget.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- worker/src/auth.ts
- frontend/src/components/dashboard/hooks/useDashboardQueue.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'yes'
external_service: LLM provider
legacy_id: J-125
---

## Purpose and scope

Monthly token budget exhausted. Priority P1, CORE yes. Imported from journey J-125 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: SaaS mode; usage >= budget.

## Steps and information flow

1. Run Quick Change from the editor (stream) and `generateVariantsPreview`.

## Modules and code map

worker/src/index.ts, worker/src/auth.ts, frontend/src/components/dashboard/hooks/useDashboardQueue.ts

Code anchors that exist: worker/src/index.ts, worker/src/auth.ts, frontend/src/components/dashboard/hooks/useDashboardQueue.ts

## Success and acceptance

Stream route returns HTTP 429 `{"ok":false,"error":"Monthly token budget exceeded"}`; action routes throw the same text (the `httpStatus: 429` attached to the error is ignored by the outer catch, so HTTP 400 is returned). The UI shows the message and a path to contact the admin; the editor text is not lost.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
