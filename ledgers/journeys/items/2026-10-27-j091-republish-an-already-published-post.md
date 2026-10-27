---
id: 2026-10-27-j091-republish-an-already-published-post
title: J-091 Republish an already published post
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: A `Published` row.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- frontend/src/components/dashboard/hooks/useDashboardQueue.ts
- worker/src/index.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P2
core: 'yes'
external_service: LinkedIn
legacy_id: J-091
---

## Purpose and scope

Republish an already published post. Priority P2, CORE yes. Imported from journey J-091 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: A `Published` row.

## Steps and information flow

1. In the queue choose "Republish"; confirm "Confirm Publish".
2. Or in the editor edit and publish (the hook calls `createDraftFromPublished` first).
3. API: `ACTION createDraftFromPublished {"row":{...},"selectedText":"...","selectedImageId":"","postTime":"","emailTo":"","emailCc":"","emailBcc":"","emailSubject":"","selectedImageUrlsJson":""}`.

## Modules and code map

frontend/src/components/dashboard/hooks/useDashboardQueue.ts (`republishRowToSelectedChannel`, `publishFromReviewEditor`), worker/src/index.ts (`createDraftFromPublished`)

Code anchors that exist: frontend/src/components/dashboard/hooks/useDashboardQueue.ts, worker/src/index.ts

## Success and acceptance

Republish shows the confirm dialog; editor path creates a NEW draft row (original untouched, alert "Draft saved"); the new row publishes. Needs a sheet (`ensureSpreadsheetConfigured`).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
