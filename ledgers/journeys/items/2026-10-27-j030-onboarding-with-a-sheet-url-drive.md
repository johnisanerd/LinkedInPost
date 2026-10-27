---
id: 2026-10-27-j030-onboarding-with-a-sheet-url-drive
title: J-030 Onboarding with a sheet URL (Drive consent and share)
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: New signed-in user
trigger: Worker has `GOOGLE_SERVICE_ACCOUNT_JSON`; user owns a Google Sheet.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- worker/src/google/drivePermissions.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'yes'
external_service: Google Sheets, Google OAuth
legacy_id: J-030
---

## Purpose and scope

Onboarding with a sheet URL (Drive consent and share). Priority P1, CORE yes. Imported from journey J-030 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: New signed-in user. Preconditions: Worker has `GOOGLE_SERVICE_ACCOUNT_JSON`; user owns a Google Sheet.

## Steps and information flow

1. Step 2 "Content source": paste `https://docs.google.com/spreadsheets/d/<ID>/edit`.
2. Click "Connect & start →"; grant the Drive scope in the Google popup.
3. Frontend calls `ACTION connectSpreadsheet {"spreadsheetId":"<ID>","driveAccessToken":"<access token>"}` then `completeOnboarding`.
4. Repeat with a sheet the user cannot share (not owner) and with the Drive popup denied.

## Modules and code map

frontend/src/features/onboarding/OnboardingModal.tsx, frontend/src/App.tsx, worker/src/index.ts (`connectSpreadsheet`), worker/src/google/drivePermissions.ts

Code anchors that exist: worker/src/index.ts, worker/src/google/drivePermissions.ts

## Success and acceptance

Step 3 returns `{"ok":true,"title":"<sheet title>"}` and D1 `users.spreadsheet_id=<ID>`. Failure cases: CODE-READING FINDING: `handleCompleteOnboarding` catches any error, logs to console only, still calls `completeOnboarding`, and redirects to `/connections`; the user never sees why the sheet was not connected.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
