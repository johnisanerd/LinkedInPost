---
id: 2026-10-27-j064-manual-edit-with-undo-redo-draft
title: J-064 Manual edit with undo/redo; draft survives navigation
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: Editor open.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/persistence/pipeline-db/pipeline.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'yes'
external_service: none
legacy_id: J-064
---

## Purpose and scope

Manual edit with undo/redo; draft survives navigation. Priority P1, CORE yes. Imported from journey J-064 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: Editor open.

## Steps and information flow

1. Type in the center `DraftEditor`; press Ctrl/Cmd+Z and redo.
2. Navigate to another route without saving, then come back; also reload the tab.
3. Click the footer approve/save action.

## Modules and code map

frontend/src/features/editor/DraftEditor.tsx, frontend/src/features/review-editor/, worker/src/persistence/pipeline-db/pipeline.ts (`updateRowStatus`)

Code anchors that exist: worker/src/persistence/pipeline-db/pipeline.ts

## Success and acceptance

Undo/redo works (history entries via `pushHistoryEntry`). Unsaved text after navigation/reload is lost unless the app autosaves; there is no `beforeunload` guard in the editor (grep), so the pass check is that a visible save state exists and `ACTION updateRowStatus {"row":{...},"status":"Approved","selectedText":"...","selectedImageId":"","postTime":"","emailTo":"","emailCc":"","emailBcc":"","emailSubject":"","selectedImageUrlsJson":""}` persists the text. Verify D1 `selected_text`.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
