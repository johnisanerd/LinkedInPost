---
id: 2026-10-27-j065-quick-change-via-sse
title: J-065 Quick Change via SSE
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: Editor with text; sheet connected (`ensureSpreadsheetConfigured`); budget available.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- frontend/src/services/backendApi.ts
- frontend/src/components/dashboard/hooks/useDashboardQueue.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'yes'
external_service: LLM provider
legacy_id: J-065
---

## Purpose and scope

Quick Change via SSE. Priority P1, CORE yes. Imported from journey J-065 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: Editor with text; sheet connected (`ensureSpreadsheetConfigured`); budget available.

## Steps and information flow

1. Select text, choose a quick action (e.g. tighten), or type an instruction; run.
2. Wire: `POST {WORKER_URL}/api/quickchange/stream` with `Authorization: Bearer T`, body `{"row":{...},"editorText":"...","instruction":"...","scope":"selection","selection":{"start":0,"end":10}}`; events `data: {"type":"node:start"|"enrichment:node_completed"|"complete"|"error", ...}`.
3. Click Apply.

## Modules and code map

worker/src/index.ts (`/api/quickchange/stream`), frontend/src/services/backendApi.ts (`streamGenerateQuickChange`), frontend/src/components/dashboard/hooks/useDashboardQueue.ts (`handleGenerateQuickChange`)

Code anchors that exist: worker/src/index.ts, frontend/src/services/backendApi.ts, frontend/src/components/dashboard/hooks/useDashboardQueue.ts

## Success and acceptance

`complete` returns `{scope,model,llmProvider,selection,replacementText,fullText}`; applying updates the textarea and pushes undo history. Empty draft -> `error` event `Draft text is required before running Quick Change.`; empty instruction -> `Quick Change needs a per-run instruction.`; budget -> HTTP 429 JSON before the stream opens; stream closing without `complete` -> UI error `Quick change stream ended without result`.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
