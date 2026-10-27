---
id: 2026-10-27-j031-non-admin-without-a-connected-sheet
title: J-031 Non-admin without a connected sheet is locked out of the whole workspace
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: New signed-in user
trigger: SaaS tenant, non-admin, `users.spreadsheet_id=''` (skipped sheet in J-029 or J-030 failed).
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P0
core: 'yes'
external_service: Google Sheets
legacy_id: J-031
---

## Purpose and scope

Non-admin without a connected sheet is locked out of the whole workspace. Priority P0, CORE yes. Imported from journey J-031 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: New signed-in user. Preconditions: SaaS tenant, non-admin, `users.spreadsheet_id=''` (skipped sheet in J-029 or J-030 failed).

## Steps and information flow

1. After onboarding, land on `/connections` (or `/topics`).
2. Read the screen.
3. Try to reach the "Connect Google Sheet" card on `/connections`.
- CODE-READING FINDING: `Dashboard` returns the "Workspace setup pending" panel (`!session.config.spreadsheetId && !session.isAdmin`) BEFORE rendering `<Routes>`, so `/connections` (which hosts `SheetConnectionCard`) and `/topics/new` are unreachable. The panel says "An admin still needs to finish setup", while onboarding told the user the sheet is optional. Server side also gates `publishContent`, `generateQuickChange`, `deleteRow`, `createDraftFromPublished` on `ensureSpreadsheetConfigured`.

## Modules and code map

frontend/src/components/dashboard/index.tsx, frontend/src/pages/connections/SheetConnectionCard.tsx, worker/src/index.ts (`ensureSpreadsheetConfigured`, `loadStoredConfig`), frontend/src/features/onboarding/OnboardingModal.tsx

Code anchors that exist: worker/src/index.ts

## Success and acceptance

Desired: A sheetless user can reach `/connections`, connect a sheet, and use the app (or the app works D1-only). Currently expected to FAIL: the user sees only "Workspace setup pending".

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
