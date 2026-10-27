---
id: 2026-10-27-j141-two-tenants-connect-the-same-google
title: J-141 Two tenants connect the same Google Sheet
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: worker
actor: Approved end user
trigger: Tenant A owns a sheet; tenant B knows its id (or is a collaborator).
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- worker/src/newsletter/persistence.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P2
core: 'yes'
external_service: Google Sheets
legacy_id: J-141
---

## Purpose and scope

Two tenants connect the same Google Sheet. Priority P2, CORE yes. Imported from journey J-141 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: Tenant A owns a sheet; tenant B knows its id (or is a collaborator).

## Steps and information flow

1. B runs `ACTION connectSpreadsheet {"spreadsheetId":"<A's id>","driveAccessToken":"<B's token>"}`.
2. Both generate drafts and run news research.

## Modules and code map

worker/src/index.ts (`connectSpreadsheet`, `completeOnboarding`), worker/src/db/*, worker/src/newsletter/persistence.ts

Code anchors that exist: worker/src/index.ts, worker/src/newsletter/persistence.ts

## Success and acceptance

Desired: B cannot connect a sheet B cannot edit (Drive token proves access, so it works only for collaborators: acceptable). Shared state keyed by `spreadsheet_id` is then shared across the two tenants: `news_snapshots`, `llm_settings` (`seedLlmSettingsIfEmpty` keyed by spreadsheet), newsletter config (`getNewsletterConfig` by spreadsheet), generation-worker records. Document that one sheet = one workspace. `completeOnboarding` accepts any `spreadsheetId` in its payload without any Drive/service-account check (CODE-READING FINDING), so B can set A's sheet id as B's workspace without proof of access; the service account then reads/writes A's sheet on B's behalf.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
