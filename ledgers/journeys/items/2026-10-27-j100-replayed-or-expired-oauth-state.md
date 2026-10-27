---
id: 2026-10-27-j100-replayed-or-expired-oauth-state
title: J-100 Replayed or expired OAuth `state`
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: worker
actor: Background / agent actor
trigger: A completed callback URL with its `state`.
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
external_service: LinkedIn
legacy_id: J-100
---

## Purpose and scope

Replayed or expired OAuth `state`. Priority P2, CORE yes. Imported from journey J-100 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Background / agent actor. Preconditions: A completed callback URL with its `state`.

## Steps and information flow

1. Open the same callback URL a second time.
2. Open `GET /auth/linkedin/callback?code=x` without `state`.
3. Open it with a state older than 10 minutes (`OAUTH_STATE_TTL_SECONDS = 600`).

## Modules and code map

worker/src/index.ts (`consumeOAuthState`, `storeOAuthState`, `handleLinkedInCallback`)

Code anchors that exist: worker/src/index.ts

## Success and acceptance

Step 1/3 -> popup text `The OAuth session is missing or expired. Start the connection again.`; step 2 -> `Missing LinkedIn OAuth state.`; state key is deleted on first read (`consumeOAuthState`), so no replay; an attacker cannot attach their account to a victim's email because `email` is taken from the stored state, not the callback.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
