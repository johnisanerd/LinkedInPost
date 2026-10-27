---
id: 2026-10-27-j066-variants-preview-for-a-selection
title: J-066 Variants preview for a selection
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: Editor with a draft.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- frontend/src/components/dashboard/hooks/useDashboardQueue.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P2
core: 'yes'
external_service: LLM provider
legacy_id: J-066
---

## Purpose and scope

Variants preview for a selection. Priority P2, CORE yes. Imported from journey J-066 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: Editor with a draft.

## Steps and information flow

1. Request alternative wording ("4 variants") for the selected text.
2. API: `ACTION generateVariantsPreview {"row":{...},"editorText":"...","scope":"selection","selection":{...},"postType":"<workflow id>"}`.
3. Apply one, then `ACTION saveDraftVariants {"row":{...},"variants":[...],"previewSelection":{"selectedText":"...","selectedImageId":"","selectedImageUrlsJson":""}}`.

## Modules and code map

worker/src/index.ts, frontend/src/features/variant/components, frontend/src/components/dashboard/hooks/useDashboardQueue.ts

Code anchors that exist: worker/src/index.ts, frontend/src/components/dashboard/hooks/useDashboardQueue.ts

## Success and acceptance

Preview returns variants; saving stores them on the row and the returned row replaces the local one. Budget exhausted -> `Monthly token budget exceeded`.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
