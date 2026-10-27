---
id: 2026-10-27-j121-pick-provider-and-model-per-purpose
title: J-121 Pick provider and model per purpose
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Tenant admin
trigger: '`FEATURE_MULTI_PROVIDER_LLM` true; provider keys on the worker.'
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- worker/src/google-model-policy.ts
- worker/migrations/0006_llm_settings.sql
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P2
core: 'yes'
external_service: LLM provider
legacy_id: J-121
---

## Purpose and scope

Pick provider and model per purpose. Priority P2, CORE yes. Imported from journey J-121 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Tenant admin. Preconditions: `FEATURE_MULTI_PROVIDER_LLM` true; provider keys on the worker.

## Steps and information flow

1. `ACTION getLlmProviderCatalog {}` -> providers `gemini`, `grok`, `openrouter`, `minimax` with models.
2. `ACTION listLlmModels {"provider":"gemini"}`.
3. `ACTION getLlmSettings {}`; `ACTION saveLlmSetting {"key":"<LlmSettingKey>","ref":{"provider":"gemini","model":"<id>"}}`.
4. Try an unknown provider and an unknown key.

## Modules and code map

worker/src/index.ts, worker/src/llm, worker/src/google-model-policy.ts, worker/migrations/0006_llm_settings.sql, frontend/src/components/llm

Code anchors that exist: worker/src/index.ts, worker/src/google-model-policy.ts, worker/migrations/0006_llm_settings.sql

## Success and acceptance

Non-admin catalogue is filtered by `allowedGoogleModels`; unknown provider -> `Unknown LLM provider.`; unknown key -> `Unknown LLM setting key: <key>`; invalid provider in `ref` -> `Unknown provider: <p>`; with the flag off -> `Multi-provider LLM is disabled for this deployment.`

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
