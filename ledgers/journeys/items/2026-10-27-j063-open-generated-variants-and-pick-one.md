---
id: 2026-10-27-j063-open-generated-variants-and-pick-one
title: J-063 Open generated variants and pick one
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: Topic with 4 variants (J-053).
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- frontend/src/features/topic-navigation/utils/topicRoute.ts
- frontend/src/features/topic-navigation/utils/workspaceRoutes.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P0
core: 'yes'
external_service: Google Sheets
legacy_id: J-063
---

## Purpose and scope

Open generated variants and pick one. Priority P0, CORE yes. Imported from journey J-063 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: Topic with 4 variants (J-053).

## Steps and information flow

1. Click the topic row in `/topics`; route `/topics/:topicId` (`TopicVariantsOrDetail`).
2. Page through the four variants (`VariantCarousel`), choose one -> route `/topics/:topicId/editor/:variantSlot` (slot 0-3).
3. Reload the editor URL.

## Modules and code map

frontend/src/features/review/ReviewWorkspace.tsx, frontend/src/features/variant/, frontend/src/features/topic-navigation/utils/topicRoute.ts, frontend/src/features/topic-navigation/utils/workspaceRoutes.ts

Code anchors that exist: frontend/src/features/topic-navigation/utils/topicRoute.ts, frontend/src/features/topic-navigation/utils/workspaceRoutes.ts

## Success and acceptance

Selected variant text is in the editor; URL reload re-resolves the row from `getRows` (`findRowByTopicRouteId`); an unknown `topicId` redirects/handles gracefully (no white screen). With zero variants, the page offers generation.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
