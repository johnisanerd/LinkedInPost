---
id: 2026-10-27-j113-enrichment-page-and-node-catalog-admin
title: J-113 Enrichment page and node catalog (admin)
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Tenant admin
trigger: '`FEATURE_ENRICHMENT` true; admin.'
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
core: 'no'
external_service: LLM provider
legacy_id: J-113
---

## Purpose and scope

Enrichment page and node catalog (admin). Priority P2, CORE no. Imported from journey J-113 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Tenant admin. Preconditions: `FEATURE_ENRICHMENT` true; admin.

## Steps and information flow

1. Open `/enrichment` (`EnrichmentFlowPage`).
2. `ACTION getNodeCatalog {}`.
3. Run a generation and watch `EnrichmentProgressPanel`.

## Modules and code map

frontend/src/pages/EnrichmentFlowPage.tsx, frontend/src/features/generation/, worker/src/index.ts (`getNodeCatalog`, `lifecycleEventBus`), worker/src/engine

Code anchors that exist: worker/src/index.ts

## Success and acceptance

CODE-READING FINDING: the `getNodeCatalog` case returns `Response.json({nodes:[...]})` from inside `dispatchAction`, and the caller wraps it again with `jsonResponse({ok:true,data})`; `JSON.stringify` of a `Response` object is `{}`, so the client gets `data: {}` not the catalog. Verify the page works without it (it may use the static `builtInWorkflowCards`). Progress events `enrichment:node_completed` come from the generation stream (`lifecycleEventBus` global subscription; events from a concurrent run on the same isolate would also reach this client: check isolation).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
