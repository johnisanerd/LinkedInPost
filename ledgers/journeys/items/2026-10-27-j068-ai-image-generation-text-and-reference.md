---
id: 2026-10-27-j068-ai-image-generation-text-and-reference
title: J-068 AI image generation (text and reference)
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: Image-gen provider key set in the worker; provider chosen in `/settings` (`imageGen`).
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
external_service: other (image generation provider via generation-worker/worker image-gen)
legacy_id: J-068
---

## Purpose and scope

AI image generation (text and reference). Priority P2, CORE no. Imported from journey J-068 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: Image-gen provider key set in the worker; provider chosen in `/settings` (`imageGen`).

## Steps and information flow

1. Media tab -> text-to-image panel (`ImageGenTextPanel`) and reference panel (`ImageGenReferencePanel`).
2. API: `ACTION generateImageFromText {...}`; `ACTION generateImageWithReference {...}`.

## Modules and code map

frontend/src/components/ImageGenTextPanel.tsx, frontend/src/components/ImageGenReferencePanel.tsx, worker/src/image-gen, worker/src/index.ts

Code anchors that exist: worker/src/index.ts

## Success and acceptance

A GCS URL is returned and appears in the image list; provider failures return an error string; LLM usage is logged against `userId` (the call passes `{db, spreadsheetId, userId}`) but no budget check precedes it.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
