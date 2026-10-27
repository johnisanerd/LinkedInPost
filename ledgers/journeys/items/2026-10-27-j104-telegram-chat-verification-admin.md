---
id: 2026-10-27-j104-telegram-chat-verification-admin
title: J-104 Telegram chat verification (admin)
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Tenant admin
trigger: Bot token from BotFather; bot added to the target chat/channel.
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
external_service: Telegram
legacy_id: J-104
---

## Purpose and scope

Telegram chat verification (admin). Priority P2, CORE yes. Imported from journey J-104 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Tenant admin. Preconditions: Bot token from BotFather; bot added to the target chat/channel.

## Steps and information flow

1. `/connections` -> Telegram: enter Chat ID (or `@channel`) and optional bot token; click verify.
2. Wire: `ACTION verifyTelegramChat {"chatId":"@mychannel","botToken":"123:abc"}`.
3. Try as a non-admin; try with a wrong chat id.

## Modules and code map

frontend/src/pages/connections/ConnectionsPage.tsx, worker/src/index.ts (`verifyTelegramChat`), worker/src/integrations/telegram

Code anchors that exist: worker/src/index.ts

## Success and acceptance

Returns `TelegramChatVerificationResult` (chat title/type); non-admin -> `Only admin users can change shared configuration.` (so ordinary tenants cannot set up Telegram even though the card is visible); invalid chat -> Telegram error text; the pasted bot token is sent to the worker over HTTPS and is not logged.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
