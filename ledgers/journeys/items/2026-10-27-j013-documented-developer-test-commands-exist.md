---
id: 2026-10-27-j013-documented-developer-test-commands-exist
title: J-013 Documented developer test commands exist
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Developer
trigger: Repo cloned, deps installed.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- AGENTS.md
- vitest.config.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P3
core: 'no'
external_service: none
legacy_id: J-013
---

## Purpose and scope

Documented developer test commands exist. Priority P3, CORE no. Imported from journey J-013 in docs/launch-readiness/journeys/JOURNEYS.md. The journey designer marked part of this journey NOT IMPLEMENTED per code reading.

## Actor, trigger and prerequisites

Persona: Developer. Preconditions: Repo cloned, deps installed.

## Steps and information flow

1. Run `cd frontend && npm run test` (AGENTS.md "Testing Requirements").
2. Run `cd worker && npm run test`.
3. Run `npm run test:setup` at root.

## Modules and code map

AGENTS.md, frontend/package.json, worker/package.json, package.json, vitest.config.ts

Code anchors that exist: AGENTS.md, vitest.config.ts

## Success and acceptance

(NOT IMPLEMENTED per code reading: frontend/package.json has `test:e2e*` only, worker/package.json has `dev`, `deploy`, `typecheck` only, no `test` script in either). Step 3 exists (root package.json `test:setup`). Pre-push protocol in AGENTS.md cannot be followed literally.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record. Not implemented per the journey designer: see the NOT IMPLEMENTED text in the steps.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
