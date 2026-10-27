---
id: 2026-10-27-j075-per-topic-rules-and-template-precedence
title: J-075 Per-topic rules and template precedence
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: Topic; at least one template.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- worker/src/persistence/pipeline-db/pipeline.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P2
core: 'yes'
external_service: none
legacy_id: J-075
---

## Purpose and scope

Per-topic rules and template precedence. Priority P2, CORE yes. Imported from journey J-075 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: Topic; at least one template.

## Steps and information flow

1. In the editor "Topic rules" tab edit rules: `ACTION saveTopicGenerationRules {"row":{...},"topicRules":"No hashtags"}`.
2. Choose a template: `ACTION saveGenerationTemplateId {"row":{...},"generationTemplateId":"<id>"}`.
3. Set channel/model: `ACTION saveTopicDeliveryPreferences {"row":{...},"topicDeliveryChannel":"linkedin","topicGenerationModel":"gemini-..."}`.
4. Run Quick Change.

## Modules and code map

worker/src/index.ts, worker/src/persistence/pipeline-db/pipeline.ts, frontend/src/features/rules/RulesPanel.tsx

Code anchors that exist: worker/src/index.ts, worker/src/persistence/pipeline-db/pipeline.ts

## Success and acceptance

If topic rules are non-empty they win and the template is skipped (code: template rules are looked up only when `topicGenerationRules` is empty); `topicGenerationRules` also stores the scratchpad metadata JSON in the same column (CODE-READING FINDING: saving "topic rules" can overwrite the scratchpad JSON `{about,meaning,...}` that `sendTopicToGeneration` parses; verify).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
