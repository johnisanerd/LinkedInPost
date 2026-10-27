---
id: 2026-10-27-j038-voice-dictation-in-the-scratchpad
title: J-038 Voice dictation in the scratchpad
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: Browser with microphone permission.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- frontend/src/features/add-topic/useSpeechToText.ts
- frontend/src/features/add-topic/whisperWorker.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P3
core: 'no'
external_service: none
legacy_id: J-038
---

## Purpose and scope

Voice dictation in the scratchpad. Priority P3, CORE no. Imported from journey J-038 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: Browser with microphone permission.

## Steps and information flow

1. Click the mic button (`MicButton`) next to a text area on `/topics/new`.
2. Speak; stop.

## Modules and code map

frontend/src/features/add-topic/MicButton.tsx, frontend/src/features/add-topic/useSpeechToText.ts, frontend/src/features/add-topic/whisperWorker.ts

Code anchors that exist: frontend/src/features/add-topic/useSpeechToText.ts, frontend/src/features/add-topic/whisperWorker.ts

## Success and acceptance

Text is appended to the field. The speech model is loaded in a web worker (`whisperWorker.ts`, `@huggingface/transformers`); first use downloads the model, so test on a slow network and with permission denied (a visible error, no crash).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
