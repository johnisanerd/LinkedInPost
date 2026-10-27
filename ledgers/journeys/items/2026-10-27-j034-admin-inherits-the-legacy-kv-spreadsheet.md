---
id: 2026-10-27-j034-admin-inherits-the-legacy-kv-spreadsheet
title: J-034 Admin inherits the legacy KV spreadsheet once
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: worker
actor: Tenant admin
trigger: '`CONFIG_KV` key `shared-config` has `spreadsheetId`; admin''s `users.spreadsheet_id` empty; `DEV_SPREADSHEET_ID` unset.'
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P2
core: 'yes'
external_service: Google Sheets
legacy_id: J-034
---

## Purpose and scope

Admin inherits the legacy KV spreadsheet once. Priority P2, CORE yes. Imported from journey J-034 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Tenant admin. Preconditions: `CONFIG_KV` key `shared-config` has `spreadsheetId`; admin's `users.spreadsheet_id` empty; `DEV_SPREADSHEET_ID` unset.

## Steps and information flow

1. Admin signs in, `ACTION bootstrap {}`.
2. Non-admin signs in.

## Modules and code map

worker/src/index.ts (`loadStoredConfig`)

Code anchors that exist: worker/src/index.ts

## Success and acceptance

Admin's D1 row gets the KV sheet id (`setUserSpreadsheetId`) and `config.spreadsheetId` is populated; the non-admin is NOT given the KV sheet (so no Google 403 from unshared sheet). Setting `DEV_SPREADSHEET_ID` overrides for every user (dev-only; make sure not set in production).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
