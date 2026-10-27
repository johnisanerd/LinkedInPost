---
id: 2026-10-27-j012-dev-auth-bypass-for-local-work
title: J-012 Dev auth bypass for local work and e2e
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Developer
trigger: '`DEV_GOOGLE_AUTH_BYPASS_SECRET` in `worker/.dev.vars`; `VITE_DEV_GOOGLE_AUTH_BYPASS=true` and `VITE_DEV_GOOGLE_AUTH_BYPASS_SECRET` (or `VITE_E2E_BYPASS_SECRET`) in `frontend/.env.local`.'
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001 []
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P2
core: 'no'
external_service: none
legacy_id: J-012
---

## Purpose and scope

Dev auth bypass for local work and e2e. Priority P2, CORE no. Imported from journey J-012 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Developer. Preconditions: `DEV_GOOGLE_AUTH_BYPASS_SECRET` in `worker/.dev.vars`; `VITE_DEV_GOOGLE_AUTH_BYPASS=true` and `VITE_DEV_GOOGLE_AUTH_BYPASS_SECRET` (or `VITE_E2E_BYPASS_SECRET`) in `frontend/.env.local`.

## Steps and information flow

1. Open the app signed out; the sign-in card shows "Continue with dev bypass".
2. Click it.
3. `ACTION bootstrap {}` with `idToken` = the secret.

## Modules and code map

worker/src/plugins/dev-google-auth-bypass/*, frontend/src/plugins/dev-google-auth-bypass/*, frontend/src/App.tsx

## Success and acceptance

Session returns `isAdmin:true`, `email:"dev-bypass@local.invalid"` (or `DEV_GOOGLE_AUTH_BYPASS_EMAIL`); a `users` row is upserted.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
