---
id: 2026-10-27-j129-google-sheets-unavailable-or-unshared-during
title: J-129 Google Sheets unavailable or unshared during topic list
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: worker
actor: Approved end user
trigger: Revoke the service account's access to the tenant's sheet (403) or block `sheets.googleapis.com`.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- worker/src/persistence/pipeline-db/pipeline.ts
- worker/src/persistence/drafts.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'yes'
external_service: Google Sheets
legacy_id: J-129
---

## Purpose and scope

Google Sheets unavailable or unshared during topic list. Priority P1, CORE yes. Imported from journey J-129 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: Revoke the service account's access to the tenant's sheet (403) or block `sheets.googleapis.com`.

## Steps and information flow

1. Reload `/topics` (`ACTION getRows {}`).
2. Edit and approve a draft; click publish.
3. Restore access and reload.

## Modules and code map

worker/src/index.ts (`getRows`), worker/src/persistence/pipeline-db/pipeline.ts, worker/src/persistence/drafts.ts

Code anchors that exist: worker/src/index.ts, worker/src/persistence/pipeline-db/pipeline.ts, worker/src/persistence/drafts.ts

## Success and acceptance

`getRows` falls back to D1 rows (`console.error('[getRows] Sheets merge failed, falling back to D1')`) and the UI loads; no banner tells the user the sheet is out of sync (CODE-READING FINDING). Writes: D1 updates succeed; sheet mirroring errors in `updateRowStatus`/`publishContent` must not block publishing or must be reported. After restore, rows reconcile without duplicates or lost edits.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
