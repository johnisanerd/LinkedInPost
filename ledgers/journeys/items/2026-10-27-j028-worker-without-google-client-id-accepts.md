---
id: 2026-10-27-j028-worker-without-google-client-id-accepts
title: J-028 Worker without `GOOGLE_CLIENT_ID` accepts tokens minted for other apps
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: workflow
scope_type: section
scope: worker
actor: Self-hosting operator
trigger: Worker deployed with `GOOGLE_CLIENT_ID` empty.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- setup/worker_config.py
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'yes'
external_service: Google OAuth
legacy_id: J-028
---

## Purpose and scope

Worker without `GOOGLE_CLIENT_ID` accepts tokens minted for other apps. Priority P1, CORE yes. Imported from journey J-028 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Self-hosting operator. Preconditions: Worker deployed with `GOOGLE_CLIENT_ID` empty.

## Steps and information flow

1. Obtain a valid Google ID token issued for a different OAuth client (any site using Google sign-in).
2. `ACTION bootstrap {}` with that token.

## Modules and code map

worker/src/index.ts (`verifySession`), setup/worker_config.py

Code anchors that exist: worker/src/index.ts, setup/worker_config.py

## Success and acceptance

Desired: `Unauthorized: Google token audience does not match this app.` or a startup refusal. CODE-READING FINDING: the audience check is `if (env.GOOGLE_CLIENT_ID && tokenInfo.aud !== env.GOOGLE_CLIENT_ID)`, so with the variable unset the check is skipped and token verification relies on Google tokeninfo only. Combined with J-017 any Google user gets in.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
