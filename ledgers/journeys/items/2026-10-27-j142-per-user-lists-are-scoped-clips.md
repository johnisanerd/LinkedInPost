---
id: 2026-10-27-j142-per-user-lists-are-scoped-clips
title: J-142 Per-user lists are scoped (clips, groups, feedback, integrations, personas, workflows)
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: worker
actor: Approved end user
trigger: Accounts A and B with data in each.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/db/clips.ts
- worker/src/db/interestGroups.ts
- worker/src/db/feedArticles.ts
- worker/src/db/socialIntegrations.ts
- worker/src/persistence/pipeline-db/pipeline.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'yes'
external_service: none
legacy_id: J-142
---

## Purpose and scope

Per-user lists are scoped (clips, groups, feedback, integrations, personas, workflows). Priority P1, CORE yes. Imported from journey J-142 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: Accounts A and B with data in each.

## Steps and information flow

1. As A: `ACTION listClips {}`, `ACTION listInterestGroups {}`, `ACTION getArticleFeedback {}`, `ACTION getIntegrations {}`, `ACTION listCustomPersonas {}`, `ACTION listCustomWorkflows {}`.
2. As A: `ACTION deleteClip {"id":"<B's clip>"}`, `ACTION updateInterestGroup {"id":"<B's group>","name":"x"}`, `ACTION deleteCustomPersona {"personaId":"<B's>"}`, `ACTION deleteIntegration {"provider":"linkedin"}` (affects only A).

## Modules and code map

worker/src/db/clips.ts, worker/src/db/interestGroups.ts, worker/src/db/feedArticles.ts, worker/src/db/socialIntegrations.ts, worker/src/persistence/pipeline-db/pipeline.ts

Code anchors that exist: worker/src/db/clips.ts, worker/src/db/interestGroups.ts, worker/src/db/feedArticles.ts, worker/src/db/socialIntegrations.ts, worker/src/persistence/pipeline-db/pipeline.ts

## Success and acceptance

Lists contain only A's rows; mutations on B's ids change nothing / error (statements are `WHERE user_id = ?`).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
