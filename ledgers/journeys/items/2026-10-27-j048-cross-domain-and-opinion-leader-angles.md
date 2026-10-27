---
id: 2026-10-27-j048-cross-domain-and-opinion-leader-angles
title: J-048 Cross-domain and "opinion leader" angles use fictional people
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: LLM key.
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
external_service: LLM provider
legacy_id: J-048
---

## Purpose and scope

Cross-domain and "opinion leader" angles use fictional people. Priority P2, CORE yes. Imported from journey J-048 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: LLM key.

## Steps and information flow

1. `ACTION crossDomainInsight {"topic":"remote work"}`.
2. `ACTION opinionLeaderInsights {"topic":"remote work"}`.

## Modules and code map

worker/src/index.ts, frontend/src/features/feed/

Code anchors that exist: worker/src/index.ts

## Success and acceptance

Returns 3 insights / 4 leaders. The prompt asks for "realistic full name" and roles that are "clearly fictional composites"; verify the UI states they are fictional so names are not copied into posts as real attributions.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
