---
id: 2026-10-27-j107-bulk-import-from-a-file-json
title: J-107 Bulk import from a file (.json, .jsonc, .csv)
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: A CSV with the expected columns.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- frontend/src/features/campaign/validate/parseCampaignDoc.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P2
core: 'no'
external_service: none
legacy_id: J-107
---

## Purpose and scope

Bulk import from a file (.json, .jsonc, .csv). Priority P2, CORE no. Imported from journey J-107 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: A CSV with the expected columns.

## Steps and information flow

1. `/campaign` -> "Upload file" (`accept=".json,.jsonc,.csv"`).
2. Upload a CSV, a malformed CSV, and a 5,000-row file.

## Modules and code map

frontend/src/features/campaign/CampaignPage.tsx, frontend/src/features/campaign/validate/parseCampaignDoc.ts

Code anchors that exist: frontend/src/features/campaign/validate/parseCampaignDoc.ts

## Success and acceptance

CSV rows convert to the JSON editor content (`setPasteText(JSON.stringify({version:1,posts},...))`); malformed rows give a visible error; a large file either imports or fails with a clear size message rather than a silent timeout (no server-side batch limit visible in `bulkImportCampaign`).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
