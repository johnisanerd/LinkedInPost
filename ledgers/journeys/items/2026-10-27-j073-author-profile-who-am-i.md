---
id: 2026-10-27-j073-author-profile-who-am-i
title: J-073 Author profile ("Who am I")
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: None.
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
core: 'yes'
external_service: none
legacy_id: J-073
---

## Purpose and scope

Author profile ("Who am I"). Priority P2, CORE yes. Imported from journey J-073 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: None.

## Steps and information flow

1. `/rules` -> author profile section (`WhoAmISection`), fill and save.
2. API: `ACTION saveUserSettings {"userWhoAmI":"..."}`.
3. Run Quick Change and check the voice.

## Modules and code map

frontend/src/features/who-am-i/WhoAmISection.tsx, worker/src/index.ts

Code anchors that exist: worker/src/index.ts

## Success and acceptance

`users.user_who_am_i` stored; `formatAuthorProfileForPrompt` is injected into quick-change and generation prompts; per-tenant value overrides workspace `authorProfile`.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
