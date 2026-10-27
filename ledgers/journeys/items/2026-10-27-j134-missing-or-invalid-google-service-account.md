---
id: 2026-10-27-j134-missing-or-invalid-google-service-account
title: J-134 Missing or invalid `GOOGLE_SERVICE_ACCOUNT_JSON`
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: workflow
scope_type: section
scope: frontend
actor: Self-hosting operator
trigger: Secret unset, or malformed.
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
external_service: Google Sheets
legacy_id: J-134
---

## Purpose and scope

Missing or invalid `GOOGLE_SERVICE_ACCOUNT_JSON`. Priority P1, CORE yes. Imported from journey J-134 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Self-hosting operator. Preconditions: Secret unset, or malformed.

## Steps and information flow

1. `ACTION getServiceAccountEmail {}`.
2. `ACTION connectSpreadsheet {"spreadsheetId":"x","driveAccessToken":"y"}`.
3. `ACTION getSpreadsheetStatus {}`.

## Modules and code map

worker/src/index.ts, frontend/src/pages/connections/SheetConnectionCard.tsx

Code anchors that exist: worker/src/index.ts

## Success and acceptance

Step 1 returns `{email:""}`; step 2 `Service account email not configured on this Worker.` or `GOOGLE_SERVICE_ACCOUNT_JSON is not valid JSON.`; step 3 `{accessible:false,title:""}` (errors swallowed). The SheetConnectionCard then shows no service-account email to share with: confirm the card tells the user it is a server misconfiguration, not their sheet.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
