---
id: 2026-10-27-j079-send-via-whatsapp
title: J-079 Send via WhatsApp
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: WhatsApp connected by an admin (J-099) with a phone number id; recipient number in the delivery panel.
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
external_service: WhatsApp
legacy_id: J-079
---

## Purpose and scope

Send via WhatsApp. Priority P1, CORE yes. Imported from journey J-079 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: WhatsApp connected by an admin (J-099) with a phone number id; recipient number in the delivery panel.

## Steps and information flow

1. Delivery panel (`DashboardDelivery`): pick a recipient; click "Send via WhatsApp".
2. `ACTION publishContent {"row":{...},"channel":"whatsapp","recipientId":"+15551234567","message":"..."}`.
3. Use an invalid number and a recipient outside the 24-hour window.

## Modules and code map

frontend/src/components/dashboard/tabs/DashboardDelivery.tsx, worker/src/index.ts (`normalizePhoneNumber`, whatsapp branch), worker/src/integrations/whatsapp

Code anchors that exist: worker/src/index.ts

## Success and acceptance

`messageId` = wamid; invalid number -> normalizer error; the code sends non-template messages ("Send non-template WhatsApp messages through Meta Cloud API"), which Meta rejects outside the customer service window: the error text from Meta must reach the user.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
