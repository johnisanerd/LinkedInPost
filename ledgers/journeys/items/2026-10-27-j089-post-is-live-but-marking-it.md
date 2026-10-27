---
id: 2026-10-27-j089-post-is-live-but-marking-it
title: J-089 Post is live but marking it Published fails
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: worker
actor: Approved end user
trigger: Ability to fail D1/Sheets writes (e.g. revoke the service account's access to the sheet).
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- worker/src/persistence/pipeline-db/pipeline.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'yes'
external_service: LinkedIn, Google Sheets
legacy_id: J-089
---

## Purpose and scope

Post is live but marking it Published fails. Priority P1, CORE yes. Imported from journey J-089 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: Ability to fail D1/Sheets writes (e.g. revoke the service account's access to the sheet).

## Steps and information flow

1. Publish to LinkedIn (J-076) while Sheets write fails.
2. Observe UI and LinkedIn.
3. Click publish again.

## Modules and code map

worker/src/index.ts (`publishContent`, `markPublishedForChannel`, `appendToPostedDoc`), worker/src/persistence/pipeline-db/pipeline.ts (`markRowPublished`)

Code anchors that exist: worker/src/index.ts, worker/src/persistence/pipeline-db/pipeline.ts

## Success and acceptance

Order in code: send to channel first, then `markRowPublished` and `appendToPostedDoc`. A failure after a successful send surfaces "Failed to send the approved message..." to the user, the row stays `Approved`, and a retry posts a duplicate (CODE-READING FINDING). Pass requires the success to be reported or the retry to detect the existing post.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
