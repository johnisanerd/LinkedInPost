---
id: 2026-10-27-j115-instagram-webhook-verification-handshake
title: J-115 Instagram webhook verification handshake
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: worker
actor: Background / agent actor
trigger: Meta app webhook configured to `{WORKER_URL}/webhooks/instagram`.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/automations/routes.ts
- worker/src/automations/platforms/instagram.ts
- worker/src/automations/webhook-verify.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P2
core: 'no'
external_service: Instagram
legacy_id: J-115
---

## Purpose and scope

Instagram webhook verification handshake. Priority P2, CORE no. Imported from journey J-115 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Background / agent actor. Preconditions: Meta app webhook configured to `{WORKER_URL}/webhooks/instagram`.

## Steps and information flow

1. Meta sends `GET /webhooks/instagram?hub.mode=subscribe&hub.verify_token=ig_<INSTAGRAM_USER_ID>_verify&hub.challenge=123`.
2. Send the same with a wrong token.
3. Meta POSTs events with `X-Hub-Signature-256`.

## Modules and code map

worker/src/automations/routes.ts, worker/src/automations/platforms/instagram.ts, worker/src/automations/webhook-verify.ts

Code anchors that exist: worker/src/automations/routes.ts, worker/src/automations/platforms/instagram.ts, worker/src/automations/webhook-verify.ts

## Success and acceptance

Correct token -> body `123`, 200; wrong -> 403; POST with a bad signature is ignored (`verifyInstagramSignature` fails -> return) but still answers `OK`. CODE-READING FINDING: the verify token is derivable from the public Instagram user id (`ig_${channelId}_verify`), not a secret.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
