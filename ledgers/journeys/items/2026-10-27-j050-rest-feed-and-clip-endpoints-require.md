---
id: 2026-10-27-j050-rest-feed-and-clip-endpoints-require
title: J-050 REST feed and clip endpoints require auth
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: worker
actor: Non-approved / unauthorised user
trigger: None.
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
external_service: none
legacy_id: J-050
---

## Purpose and scope

REST feed and clip endpoints require auth. Priority P1, CORE yes. Imported from journey J-050 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Non-approved / unauthorised user. Preconditions: None.

## Steps and information flow

1. `GET {WORKER_URL}/api/feed` and `GET {WORKER_URL}/api/clips` with no Authorization header.
2. Same with a valid `Authorization: Bearer T`.
3. `POST {WORKER_URL}/api/clips` body missing fields; `POST /api/feed/items`.

## Modules and code map

worker/src/index.ts (`handleFeedGet`, `handleFeedItemCreate`, `handleClipsGet`, `handleClipsCreate`)

Code anchors that exist: worker/src/index.ts

## Success and acceptance

Step 1 HTTP 401 `Unauthorized`; step 2 200 with only the caller's data (`interest_group_id` filtered by `user_id`); bad bodies get 4xx. Note the feed SELECT filters `news_snapshots` by `spreadsheet_id` (shared sheet = shared snapshots, see J-141).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
