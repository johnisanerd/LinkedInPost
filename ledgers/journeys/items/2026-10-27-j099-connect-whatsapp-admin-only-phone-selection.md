---
id: 2026-10-27-j099-connect-whatsapp-admin-only-phone-selection
title: J-099 Connect WhatsApp (admin only, phone selection)
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Tenant admin
trigger: '`META_APP_ID`, `META_APP_SECRET`; WhatsApp Business Account with at least one phone number; admin session.'
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
external_service: WhatsApp
legacy_id: J-099
---

## Purpose and scope

Connect WhatsApp (admin only, phone selection). Priority P2, CORE yes. Imported from journey J-099 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Tenant admin. Preconditions: `META_APP_ID`, `META_APP_SECRET`; WhatsApp Business Account with at least one phone number; admin session.

## Steps and information flow

1. `/connections` -> WhatsApp -> Connect: `ACTION startWhatsAppAuth {}` (admin-guarded).
2. Callback `GET /auth/whatsapp/callback` stores a pending record `whatsapp-pending:<connectionId>` (TTL 10 min) and posts `{connectionId, options:[{phoneNumberId,verifiedName,displayPhoneNumber}]}`.
3. UI auto-selects `options[0]`: `ACTION completeWhatsAppConnection {"connectionId":"<id>","phoneNumberId":"<id>"}`.
4. Non-admin presses Connect.

## Modules and code map

worker/src/index.ts (`startWhatsAppAuth`, `handleWhatsAppCallback`, `completeWhatsAppConnection`), frontend/src/App.tsx

Code anchors that exist: worker/src/index.ts

## Success and acceptance

`bootstrap.config.whatsappPhoneNumberId` set; non-admin gets `Only admin users can change shared configuration.`; with multiple phone numbers the UI picks the first one without asking (CODE-READING FINDING: App.tsx comment "auto-select the first phone"); a connection session from a different admin is refused.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
