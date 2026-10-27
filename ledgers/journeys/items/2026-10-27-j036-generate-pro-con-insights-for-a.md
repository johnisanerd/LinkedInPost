---
id: 2026-10-27-j036-generate-pro-con-insights-for-a
title: J-036 Generate Pro/Con insights for a topic
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: LLM key on the worker.
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
legacy_id: J-036
---

## Purpose and scope

Generate Pro/Con insights for a topic. Priority P2, CORE yes. Imported from journey J-036 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: LLM key on the worker.

## Steps and information flow

1. On `/topics/new` click "Generate insights".
2. API: `ACTION analyzeTopicInsights {"topic":"...","about":"","meaning":"","notes":""}`.
3. Force an LLM malformed answer (or no LLM key).

## Modules and code map

worker/src/index.ts (`analyzeTopicInsights`), frontend/src/features/add-topic/AddTopicPage.tsx

Code anchors that exist: worker/src/index.ts

## Success and acceptance

Returns `{pros:[...],cons:[...]}` each at most 6 strings. Malformed JSON -> `AI returned unexpected format. Please try again.`; missing key -> provider error shown. NOTE: this action has no `checkTokenBudget` and no `ensureSpreadsheetConfigured` call (CODE-READING FINDING for budget enforcement).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
