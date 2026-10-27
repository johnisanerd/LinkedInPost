---
id: 2026-10-27-j102-disconnect-a-channel-three-different-disconnect
title: 'J-102 Disconnect a channel: three different "disconnect" behaviours'
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: LinkedIn connected.
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
priority: P1
core: 'yes'
external_service: LinkedIn
legacy_id: J-102
---

## Purpose and scope

Disconnect a channel: three different "disconnect" behaviours. Priority P1, CORE yes. Imported from journey J-102 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: LinkedIn connected.

## Steps and information flow

1. `/connections` -> LinkedIn -> Disconnect: UI calls `ACTION deleteIntegration {"provider":"linkedin"}` (D1 row only).
2. Publish to LinkedIn afterwards.
3. Admin: `ACTION disconnectChannelAuth {"provider":"linkedin"}` (KV `disconnectedAuthProviders`).

## Modules and code map

frontend/src/App.tsx (`handleDisconnect`), worker/src/index.ts (`deleteIntegration`, `disconnectChannelAuth`, `publishContent`), worker/src/db/socialIntegrations.ts

Code anchors that exist: worker/src/index.ts, worker/src/db/socialIntegrations.ts

## Success and acceptance

After a user disconnects, publishing must fail with a "not connected" message. CODE-READING FINDING: `publishContent` falls back to the shared KV token (J-103) when the per-user row is missing, so the post still goes out under the operator's/previous user's account. Telegram "Disconnect" (`onDisconnect('telegram')`) also only deletes a D1 integration row and leaves the KV bot token.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
