---
id: 2026-10-27-j072-global-generation-rules-admin-and-history
title: J-072 Global generation rules (admin) and history
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Tenant admin
trigger: Admin.
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
legacy_id: J-072
---

## Purpose and scope

Global generation rules (admin) and history. Priority P2, CORE yes. Imported from journey J-072 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Tenant admin. Preconditions: Admin.

## Steps and information flow

1. `/rules` -> "Global generation rules" -> edit -> "Save global rules".
2. API: `ACTION saveConfig {"generationRules":"..."}` then `ACTION getGenerationRulesHistory {}`.
3. Reopen "Saved version history" and restore a version.

## Modules and code map

frontend/src/pages/GlobalRulesPage.tsx, worker/src/index.ts (`saveConfig`, `getGenerationRulesHistory`)

Code anchors that exist: worker/src/index.ts

## Success and acceptance

History keeps the previous text with `savedAt`/`savedBy` (max 50). Non-admin: `Only admin users can change shared configuration.` Note the rules and author profile live in the single KV key `shared-config` (read-modify-write, no locking), so two admins saving at once or an OAuth callback landing between read and write can clobber each other (CODE-READING FINDING).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
