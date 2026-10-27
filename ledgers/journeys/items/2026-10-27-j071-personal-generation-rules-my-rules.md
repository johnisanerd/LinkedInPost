---
id: 2026-10-27-j071-personal-generation-rules-my-rules
title: J-071 Personal generation rules ("My rules")
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: Signed in.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- worker/migrations/0009_user_tenant_settings.sql
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P2
core: 'yes'
external_service: none
legacy_id: J-071
---

## Purpose and scope

Personal generation rules ("My rules"). Priority P2, CORE yes. Imported from journey J-071 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: Signed in.

## Steps and information flow

1. `/rules` -> "My rules" -> edit -> click "Save my rules".
2. API: `ACTION saveUserSettings {"userRules":"Never use emojis"}`.
3. Generate a draft (J-053) and check the rule is applied.

## Modules and code map

frontend/src/pages/GlobalRulesPage.tsx, worker/src/index.ts (`saveUserSettings`, `loadStoredConfig`), worker/migrations/0009_user_tenant_settings.sql

Code anchors that exist: worker/src/index.ts, worker/migrations/0009_user_tenant_settings.sql

## Success and acceptance

`{ok:true}`; D1 `users.user_rules` updated; next `bootstrap` returns `config.userRules`; the generated draft respects the rule (compare `effectiveRules` precedence: topic rules > template rules > user rules > global rules).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
