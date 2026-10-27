---
id: 2026-10-27-j122-llm-provider-failure-and-fallback
title: J-122 LLM provider failure and fallback
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: worker
actor: Approved end user
trigger: Primary provider key invalid / quota exhausted; fallback configured or not.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- worker/src/db/llm-usage.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'yes'
external_service: LLM provider
legacy_id: J-122
---

## Purpose and scope

LLM provider failure and fallback. Priority P1, CORE yes. Imported from journey J-122 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: Primary provider key invalid / quota exhausted; fallback configured or not.

## Steps and information flow

1. Run Quick Change (J-065), `analyzeTopicInsights` (J-036), and generation (J-053).

## Modules and code map

worker/src/llm, worker/src/index.ts (`generateTextJsonWithFallback`), worker/src/db/llm-usage.ts, packages/llm-core

Code anchors that exist: worker/src/index.ts, worker/src/db/llm-usage.ts

## Success and acceptance

Where a fallback is configured (`resolveFallbackForGeneration`) the call succeeds and `llmProvider` in the result names the fallback; otherwise a readable error reaches the user (not `[object Object]`, not a raw API key in the text); usage rows recorded in `llm_usage_log` only for successful calls (check token accounting on failures).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
