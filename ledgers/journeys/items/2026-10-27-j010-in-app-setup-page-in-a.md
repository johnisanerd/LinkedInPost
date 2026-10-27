---
id: 2026-10-27-j010-in-app-setup-page-in-a
title: J-010 In-app `/setup` page in a deployed (non-local) build
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Tenant admin
trigger: Production frontend; signed in as admin (header shows "Setup").
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- frontend/src/features/setup-wizard/setupService.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P2
core: 'no'
external_service: none
legacy_id: J-010
---

## Purpose and scope

In-app `/setup` page in a deployed (non-local) build. Priority P2, CORE no. Imported from journey J-010 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Tenant admin. Preconditions: Production frontend; signed in as admin (header shows "Setup").

## Steps and information flow

1. Click header "Setup" (route `/setup`, renders `SetupWizard embedded`).
2. Use any step that saves config.

## Modules and code map

frontend/src/features/setup-wizard/setupService.ts, frontend/src/features/setup-wizard/SetupWizard.tsx, frontend/src/components/dashboard/index.tsx

Code anchors that exist: frontend/src/features/setup-wizard/setupService.ts

## Success and acceptance

CODE-READING FINDING: `setupService.ts` fetches `http://localhost:3456/api/setup/write-config`, `/reset-database`, `/regenerate-features` (served only by `node frontend/server/setupWizard.js` from `npm run dev`). In production these calls fail (mixed content / connection refused); the page must show a clear "local dev only" message or be hidden.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
