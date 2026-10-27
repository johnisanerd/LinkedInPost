---
id: 2026-10-27-j057-client-supplied-spreadsheetid-overrides-the-server
title: J-057 Client-supplied `spreadsheetId` overrides the server's in generation
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: worker
actor: Non-approved / unauthorised user
trigger: Tenant A and tenant B each with a sheet; A knows B's sheet id (ids are in URLs).
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- generation-worker/src/types.ts
- generation-worker/src/pipeline.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P0
core: 'yes'
external_service: Google Sheets
legacy_id: J-057
---

## Purpose and scope

Client-supplied `spreadsheetId` overrides the server's in generation. Priority P0, CORE yes. Imported from journey J-057 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Non-approved / unauthorised user. Preconditions: Tenant A and tenant B each with a sheet; A knows B's sheet id (ids are in URLs).

## Steps and information flow

1. As A: `POST {WORKER_URL}/api/generate/stream` with body `{"spreadsheetId":"<B's sheet id>","topic":"x","topicId":"<B's topic id>"}`.
2. As A: `ACTION callGenerationWorker {"spreadsheetId":"<B's sheet id>","topic":"x"}`.

## Modules and code map

worker/src/index.ts (`/api/generate/stream`, `callGenerationWorker`), generation-worker/src/types.ts, generation-worker/src/pipeline.ts

Code anchors that exist: worker/src/index.ts, generation-worker/src/types.ts, generation-worker/src/pipeline.ts

## Success and acceptance

Desired: server ignores client `spreadsheetId` and uses `storedConfig.spreadsheetId`. CODE-READING FINDING: both handlers build `{ spreadsheetId: storedConfig.spreadsheetId, ...payload }`, so the client value wins (spread order). Check which downstream reads/writes in generation-worker use `spreadsheetId` (feedback, variants/clips by session, LLM settings keyed by spreadsheet) and whether B's data can be read or polluted.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
