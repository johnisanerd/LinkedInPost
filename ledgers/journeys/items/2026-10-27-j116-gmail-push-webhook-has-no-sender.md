---
id: 2026-10-27-j116-gmail-push-webhook-has-no-sender
title: J-116 Gmail push webhook has no sender authentication
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: worker
actor: Non-approved / unauthorised user
trigger: Gmail automation enabled for a channel (`emailAddress`).
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/automations/routes.ts
- worker/src/automations/platforms/gmail.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'no'
external_service: Gmail
legacy_id: J-116
---

## Purpose and scope

Gmail push webhook has no sender authentication. Priority P1, CORE no. Imported from journey J-116 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Non-approved / unauthorised user. Preconditions: Gmail automation enabled for a channel (`emailAddress`).

## Steps and information flow

1. `POST {WORKER_URL}/webhooks/gmail` with body `{"message":{"data":"<base64 of {\"emailAddress\":\"owner@x.com\",\"historyId\":\"1\"}>"}}` and no headers.

## Modules and code map

worker/src/automations/routes.ts, worker/src/automations/platforms/gmail.ts

Code anchors that exist: worker/src/automations/routes.ts, worker/src/automations/platforms/gmail.ts

## Success and acceptance

Desired: 401/ignored without a verified Pub/Sub JWT or shared secret. CODE-READING FINDING: `handleGmailPushEvent` parses the body and proceeds to `resolveGmailAccessToken(channelId, env)` and history processing with no signature/OIDC check (Telegram and LinkedIn handlers verify; Gmail does not). The route always answers 200.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
