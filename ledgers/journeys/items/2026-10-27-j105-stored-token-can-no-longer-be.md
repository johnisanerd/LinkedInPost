---
id: 2026-10-27-j105-stored-token-can-no-longer-be
title: J-105 Stored token can no longer be decrypted (key rotated)
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: workflow
scope_type: section
scope: worker
actor: Self-hosting operator
trigger: Tokens stored under the old `SECRET_ENCRYPTION_KEY`; key replaced.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- worker/src/db/socialIntegrations.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P2
core: 'yes'
external_service: Instagram
legacy_id: J-105
---

## Purpose and scope

Stored token can no longer be decrypted (key rotated). Priority P2, CORE yes. Imported from journey J-105 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Self-hosting operator. Preconditions: Tokens stored under the old `SECRET_ENCRYPTION_KEY`; key replaced.

## Steps and information flow

1. Publish to Instagram (or LinkedIn / Gmail / Telegram / WhatsApp).

## Modules and code map

worker/src/index.ts (`*_TOKEN_REAUTH_MESSAGE`, `requireSecretEncryptionKey`, `publishContent`), worker/src/db/socialIntegrations.ts

Code anchors that exist: worker/src/index.ts, worker/src/db/socialIntegrations.ts

## Success and acceptance

Error `The stored Instagram access token can no longer be decrypted. Ask an admin to open Settings and save the token again.` (and the KV ciphertext is cleared for Instagram); per-user D1 rows fall through to the shared token silently (`catch { // Fall through }`). Settings has no obvious "save token again" field now that OAuth is the flow: confirm the message is actionable (CODE-READING FINDING: the message points to Settings; the real remedy is reconnect on `/connections`).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
