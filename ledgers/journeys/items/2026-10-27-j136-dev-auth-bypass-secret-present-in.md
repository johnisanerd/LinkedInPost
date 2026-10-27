---
id: 2026-10-27-j136-dev-auth-bypass-secret-present-in
title: J-136 Dev auth bypass secret present in production
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: workflow
scope_type: section
scope: frontend
actor: Self-hosting operator
trigger: '`DEV_GOOGLE_AUTH_BYPASS_SECRET` set on a deployed worker (e.g. copied from `.dev.vars`).'
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/plugins/dev-google-auth-bypass/resolve-session.ts
- worker/src/index.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P0
core: 'yes'
external_service: none
legacy_id: J-136
---

## Purpose and scope

Dev auth bypass secret present in production. Priority P0, CORE yes. Imported from journey J-136 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Self-hosting operator. Preconditions: `DEV_GOOGLE_AUTH_BYPASS_SECRET` set on a deployed worker (e.g. copied from `.dev.vars`).

## Steps and information flow

1. `ACTION bootstrap {}` with `idToken` = that secret.

## Modules and code map

worker/src/plugins/dev-google-auth-bypass/resolve-session.ts, worker/src/index.ts (`verifySession`), frontend/src/plugins/dev-google-auth-bypass/, .github/workflows/deploy-workers.yml, .github/workflows/deploy-pages.yml

Code anchors that exist: worker/src/plugins/dev-google-auth-bypass/resolve-session.ts, worker/src/index.ts

## Success and acceptance

Desired: never accepted outside local dev. CODE-READING FINDING: `verifySession` calls `tryResolveDevGoogleAuthBypassSession` before any Google call and returns `{isAdmin:true}` if the secret matches; there is no environment guard (`wrangler dev` vs deployed). The only protection is the comment "Do not set these variables in production Worker secrets". Also if `VITE_DEV_GOOGLE_AUTH_BYPASS_SECRET` is baked into a production frontend build the secret ships in the JS bundle. The deploy pipeline should assert both are absent.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
