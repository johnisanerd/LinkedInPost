---
id: 2026-10-27-j080-send-via-telegram
title: J-080 Send via Telegram
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: worker
actor: Approved end user
trigger: '`TELEGRAM_BOT_TOKEN` or stored token; chat verified by an admin (J-104).'
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'yes'
external_service: Telegram
legacy_id: J-080
---

## Purpose and scope

Send via Telegram. Priority P1, CORE yes. Imported from journey J-080 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: `TELEGRAM_BOT_TOKEN` or stored token; chat verified by an admin (J-104).

## Steps and information flow

1. Pick a verified chat in the delivery panel; click "Send via Telegram".
2. `ACTION publishContent {"row":{...},"channel":"telegram","recipientId":"@mychannel","message":"..."}`.

## Modules and code map

worker/src/index.ts (telegram branch, `normalizeTelegramChatId`), worker/src/integrations/telegram

Code anchors that exist: worker/src/index.ts

## Success and acceptance

Message appears in the chat; returns `messageId`; invalid chat id -> `Enter a valid Telegram chat ID or @channel username.`; bot not admin of the channel -> Telegram's error is surfaced.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
