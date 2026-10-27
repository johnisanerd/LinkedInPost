---
id: 2026-10-27-j061-custom-workflows-post-types
title: J-061 Custom workflows (post types)
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: None.
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
external_service: none
legacy_id: J-061
---

## Purpose and scope

Custom workflows (post types). Priority P2, CORE no. Imported from journey J-061 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: None.

## Steps and information flow

1. Open the workflow builder (`WorkflowBuilderModal`), create a workflow.
2. API: `ACTION createCustomWorkflow {...}` (see `CreateCustomWorkflowPayload`), `ACTION listCustomWorkflows {}`, `ACTION updateCustomWorkflow {...}`, `ACTION deleteCustomWorkflow {"id":"<id>"}`.
3. Generate variants with that `postType` (`cw_` prefix): `ACTION generateVariantsPreview {...,"postType":"cw_<id>"}`.

## Modules and code map

frontend/src/features/workflows/, worker/src/features/custom-workflows/, worker/src/index.ts (`generateVariantsPreview`)

Code anchors that exist: worker/src/index.ts

## Success and acceptance

CRUD scoped per user; the custom instruction (`generationInstruction`) is included in the variants prompt; an unknown workflow id silently proceeds without instruction.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
