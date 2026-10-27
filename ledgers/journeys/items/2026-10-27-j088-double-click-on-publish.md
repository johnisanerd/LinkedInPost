---
id: 2026-10-27-j088-double-click-on-publish
title: J-088 Double-click on Publish
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: Ready-to-publish draft.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- frontend/src/components/dashboard/hooks/useDashboardQueue.ts
- worker/src/index.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'yes'
external_service: LinkedIn
legacy_id: J-088
---

## Purpose and scope

Double-click on Publish. Priority P1, CORE yes. Imported from journey J-088 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: Ready-to-publish draft.

## Steps and information flow

1. Double-click (or press Enter twice) on "Publish to LinkedIn".
2. Server-side: send the same `ACTION publishContent {...}` twice in parallel with `curl`.

## Modules and code map

frontend/src/components/dashboard/hooks/useDashboardQueue.ts (`actionLoading`), worker/src/index.ts (`publishContent`)

Code anchors that exist: frontend/src/components/dashboard/hooks/useDashboardQueue.ts, worker/src/index.ts

## Success and acceptance

Exactly one post on LinkedIn. UI guard: `if (actionLoading !== null) return;` is React state, so two clicks in one tick may both pass; server guard: `publishContent` has no idempotency key and no "already Published" check for the immediate path (only `executeScheduledPublish` checks status). Expect two posts for the parallel curl (CODE-READING FINDING). A second click after completion goes through the "Republish" confirm only in the queue, not in the editor.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
