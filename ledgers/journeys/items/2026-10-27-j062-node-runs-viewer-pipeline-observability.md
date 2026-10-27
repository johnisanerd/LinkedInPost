---
id: 2026-10-27-j062-node-runs-viewer-pipeline-observability
title: J-062 Node runs viewer (pipeline observability)
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Tenant admin
trigger: A prior generation (J-053).
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- worker/migrations/0012_node_runs.sql
- worker/migrations/0013_data_retention_30day.sql
- frontend/src/components/dashboard/hooks/useDashboardQueue.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P3
core: 'no'
external_service: none
legacy_id: J-062
---

## Purpose and scope

Node runs viewer (pipeline observability). Priority P3, CORE no. Imported from journey J-062 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Tenant admin. Preconditions: A prior generation (J-053).

## Steps and information flow

1. `ACTION getNodeRuns {"topicId":"<id>"}`.
2. Wait 30 days / set `expires_at` to the past and call again.

## Modules and code map

worker/src/index.ts (`getNodeRuns`), worker/migrations/0012_node_runs.sql, worker/migrations/0013_data_retention_30day.sql, frontend/src/components/dashboard/hooks/useDashboardQueue.ts

Code anchors that exist: worker/src/index.ts, worker/migrations/0012_node_runs.sql, worker/migrations/0013_data_retention_30day.sql, frontend/src/components/dashboard/hooks/useDashboardQueue.ts

## Success and acceptance

Returns up to 500 rows for `user_id = caller` and `topic_id`; expired rows are purged opportunistically (best effort, up to 500 per call). Input/output JSON stored in D1 include prompts and drafts: confirm retention matches the privacy policy (30 days).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
