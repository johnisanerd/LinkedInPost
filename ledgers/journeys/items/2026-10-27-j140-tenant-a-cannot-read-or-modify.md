---
id: 2026-10-27-j140-tenant-a-cannot-read-or-modify
title: J-140 Tenant A cannot read or modify tenant B's topics
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: worker
actor: Approved end user
trigger: Two non-admin accounts A and B, each with topics (D1-only or own sheets).
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/persistence/pipeline-db/pipeline.ts
- worker/src/services.ts
- worker/migrations/0010_pipeline_user_primary.sql
- worker/src/index.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P0
core: 'yes'
external_service: none
legacy_id: J-140
---

## Purpose and scope

Tenant A cannot read or modify tenant B's topics. Priority P0, CORE yes. Imported from journey J-140 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: Two non-admin accounts A and B, each with topics (D1-only or own sheets).

## Steps and information flow

1. As B, `ACTION getRows {}` -> note a `topicId` of B.
2. As A, `ACTION getRows {}`: B's topic must not appear.
3. As A, `ACTION updateTopicMeta {"topicId":"<B's id>","topic":"pwn","topicMeta":{}}`; `ACTION updateRowStatus {"row":{"topic":"x","date":"d","topicId":"<B's id>"},"status":"Approved","selectedText":"x",...}`; `ACTION deleteRow {"row":{... "topicId":"<B's id>"}}`; `ACTION getNodeRuns {"topicId":"<B's id>"}`; `ACTION publishContent {"row":{... "topicId":"<B's id>"},...}`.

## Modules and code map

worker/src/persistence/pipeline-db/pipeline.ts, worker/src/services.ts (`buildServices`), worker/migrations/0010_pipeline_user_primary.sql, worker/src/index.ts

Code anchors that exist: worker/src/persistence/pipeline-db/pipeline.ts, worker/src/services.ts, worker/migrations/0010_pipeline_user_primary.sql, worker/src/index.ts

## Success and acceptance

Step 2 empty of B's rows. Step 3: every write is scoped by `user_id = A` in `pipeline_state` (PK `(user_id, topic_id)` per migration 0010), so none change B's data (A's call creates/updates only A's own row or fails with `Topic not found.`); `getNodeRuns` returns only rows with `user_id = A`. Verify by reading B's row afterwards. Note that `updateRowStatus` / `upsertFull` accept a client-supplied full row (including `status`), so A can upsert arbitrary row content for A's own account.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
