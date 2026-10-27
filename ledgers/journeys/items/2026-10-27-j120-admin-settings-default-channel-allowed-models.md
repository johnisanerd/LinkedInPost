---
id: 2026-10-27-j120-admin-settings-default-channel-allowed-models
title: 'J-120 Admin settings: default channel, allowed models, news keys'
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Tenant admin
trigger: Admin.
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
external_service: none
legacy_id: J-120
---

## Purpose and scope

Admin settings: default channel, allowed models, news keys. Priority P2, CORE yes. Imported from journey J-120 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Tenant admin. Preconditions: Admin.

## Steps and information flow

1. `/settings` (admin only; opens `DashboardSettingsDrawer`/settings home).
2. Change default channel, allowed Google models, WhatsApp/Telegram recipients; save.
3. Wire: `ACTION saveConfig {"defaultChannel":"linkedin","googleModel":"...","allowedGoogleModels":["..."],"telegramRecipients":[...],"whatsappRecipients":[...]}`.

## Modules and code map

frontend/src/components/dashboard/components/DashboardSettingsDrawer.tsx, worker/src/index.ts (`saveConfig`, `toPublicConfig`)

Code anchors that exist: worker/src/index.ts

## Success and acceptance

Response is the public config (`BotConfig`) with secrets reduced to booleans (`hasLinkedInAccessToken` etc.); no ciphertext or token is returned in `bootstrap`/`saveConfig`. Non-admin gets the admin error.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
