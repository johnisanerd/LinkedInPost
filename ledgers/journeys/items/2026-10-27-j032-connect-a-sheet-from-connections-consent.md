---
id: 2026-10-27-j032-connect-a-sheet-from-connections-consent
title: J-032 Connect a sheet from `/connections` (consent and manual-share paths)
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: Admin (to be able to reach the page, see J-031); a Google Sheet.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'yes'
external_service: Google Sheets, Google OAuth
legacy_id: J-032
---

## Purpose and scope

Connect a sheet from `/connections` (consent and manual-share paths). Priority P1, CORE yes. Imported from journey J-032 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: Admin (to be able to reach the page, see J-031); a Google Sheet.

## Steps and information flow

1. `/connections`, `SheetConnectionCard`: paste URL, grant Drive consent.
2. Alternative: deny consent; the card shows the service account email (`ACTION getServiceAccountEmail {}`), share the sheet manually, click "Verify access" (`ACTION getSpreadsheetStatus {}`).

## Modules and code map

frontend/src/pages/connections/SheetConnectionCard.tsx, worker/src/index.ts (`connectSpreadsheet`, `getSpreadsheetStatus`, `getServiceAccountEmail`)

Code anchors that exist: worker/src/index.ts

## Success and acceptance

`connectSpreadsheet` returns `{ok:true,title}`; or `getSpreadsheetStatus` returns `{"accessible":true,"title":"..."}`. Wrong URL: error `Sheet shared but service account still cannot access it (404)...`. Invalid `GOOGLE_SERVICE_ACCOUNT_JSON`: `GOOGLE_SERVICE_ACCOUNT_JSON is not valid JSON.`

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
