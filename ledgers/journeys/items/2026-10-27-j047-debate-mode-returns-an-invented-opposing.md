---
id: 2026-10-27-j047-debate-mode-returns-an-invented-opposing
title: J-047 "Debate mode" returns an invented opposing article
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: Feed article open.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'yes'
external_service: LLM provider
legacy_id: J-047
---

## Purpose and scope

"Debate mode" returns an invented opposing article. Priority P1, CORE yes. Imported from journey J-047 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: Feed article open.

## Steps and information flow

1. Switch to Debate mode (`DebateModeView`).
2. API: `ACTION findDebateArticle {"title":"T","description":"D"}`.
3. Click the clip button on the result.

## Modules and code map

worker/src/index.ts (`findDebateArticle`), frontend/src/features/feed/components/DebateModeView.tsx

Code anchors that exist: worker/src/index.ts

## Success and acceptance

CODE-READING FINDING: the prompt says "Generate a realistic opposing article ... Plausible publication name (e.g. Harvard Business Review)". The result is fabricated (title, source, summary) and the UI offers "Clip". Pass requires that the UI visibly labels it AI-generated / not a real article and that clipping does not save a fake URL as a source. A user quoting it on LinkedIn would publish a false citation.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
