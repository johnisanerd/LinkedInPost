---
id: 2026-10-27-j027-admin-only-screens-and-actions-are
title: J-027 Admin-only screens and actions are enforced on both sides
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: Non-admin session `T`.
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
external_service: none
legacy_id: J-027
---

## Purpose and scope

Admin-only screens and actions are enforced on both sides. Priority P1, CORE yes. Imported from journey J-027 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: Non-admin session `T`.

## Steps and information flow

1. Browse to `/settings`, `/admin`, `/setup`, `/enrichment`, `/automations`.
2. `ACTION saveConfig {"generationRules":"x"}`; `ACTION saveLlmSetting {"key":"generation_worker","ref":{"provider":"gemini","model":"m"}}`; `ACTION startWhatsAppAuth {}`; `ACTION disconnectChannelAuth {"provider":"linkedin"}`; `ACTION verifyTelegramChat {"chatId":"@x"}`; `ACTION adminListTenantSettings {}`.
3. `ACTION __admin__ {"__path":"/api/admin/users","__method":"GET"}`.
4. `GET {WORKER_URL}/automations/rules` with `Authorization: Bearer T`; `GET {WORKER_URL}/v1/image-gen-catalog`.

## Modules and code map

frontend/src/components/dashboard/index.tsx, worker/src/index.ts (`ensureAdmin`, `__admin__` branch, `/automations/` guard, `/v1/image-gen-catalog`)

Code anchors that exist: worker/src/index.ts

## Success and acceptance

Step 1 redirects to `/topics`. Step 2 each returns `Only admin users can change shared configuration.`. Step 3 returns HTTP 403 `Admin access required` (the `__admin__` branch returns a real 403). Step 4 returns 403 `Forbidden`.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
