---
id: 2026-10-27-j145-operator-health-check-of-both-workers
title: J-145 Operator health check of both workers
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: workflow
scope_type: section
scope: worker
actor: Self-hosting operator
trigger: Both deployed.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- generation-worker/src/index.ts
- generation-worker/src/players/patternRepository.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'yes'
external_service: Cloudflare
legacy_id: J-145
---

## Purpose and scope

Operator health check of both workers. Priority P1, CORE yes. Imported from journey J-145 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Self-hosting operator. Preconditions: Both deployed.

## Steps and information flow

1. `curl https://<main>/` -> health.
2. `curl -H "Authorization: Bearer $SECRET" https://<gen>/v1/health`.
3. `curl -H "Authorization: Bearer $SECRET" https://<gen>/v1/llm/catalog` (checks provider keys).
4. `curl -H "Authorization: Bearer $SECRET" https://<gen>/v1/patterns`.
5. From the main worker context: `ACTION listPatterns {}` (verifies `GENERATION_WORKER_SECRET` equals the generation worker's `WORKER_SHARED_SECRET`).

## Modules and code map

worker/src/index.ts, generation-worker/src/index.ts, generation-worker/src/players/patternRepository.ts

Code anchors that exist: worker/src/index.ts, generation-worker/src/index.ts, generation-worker/src/players/patternRepository.ts

## Success and acceptance

200s; `patterns` non-empty; step 5 returns an array, not `Generation worker returned 401`. Neither health endpoint checks D1/KV/secret presence; document that a green health probe does not prove readiness (see J-133).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
