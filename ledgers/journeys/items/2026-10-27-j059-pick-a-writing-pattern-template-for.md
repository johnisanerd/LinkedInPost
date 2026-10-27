---
id: 2026-10-27-j059-pick-a-writing-pattern-template-for
title: J-059 Pick a writing pattern/template for generation
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: '`FEATURE_CONTENT_FLOW` on.'
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- generation-worker/src/players/patternRepository.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P2
core: 'yes'
external_service: Cloudflare
legacy_id: J-059
---

## Purpose and scope

Pick a writing pattern/template for generation. Priority P2, CORE yes. Imported from journey J-059 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: `FEATURE_CONTENT_FLOW` on.

## Steps and information flow

1. In the review workspace use `TemplateSelector` (features/content-flow).
2. API: `ACTION listPatterns {}` (proxies `GET {GEN}/v1/patterns/full`), `ACTION assignPattern {"row":{...},"patternId":"p","patternName":"n","patternRationale":"r","generationRunId":"id"}`, `ACTION getPatternAssignment {...}`, `ACTION listPatternAssignments {}`, `ACTION savePatternMetadata {"topicId":"<id>",...}`, `ACTION getTestGroup {...}`.

## Modules and code map

frontend/src/features/content-flow/, worker/src/index.ts, worker/src/generation/, generation-worker/src/players/patternRepository.ts

Code anchors that exist: worker/src/index.ts, generation-worker/src/players/patternRepository.ts

## Success and acceptance

Patterns list loads; assignment persists on the row (`patternId`, `patternName`); if `GENERATION_WORKER_URL` is unset `listPatterns` returns `[]` silently (no message in UI?).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
