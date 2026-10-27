---
id: 2026-10-27-j114-automation-rules-admin
title: J-114 Automation rules (admin)
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Tenant admin
trigger: Admin; channel connected.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/automations/routes.ts
- worker/src/automations/kv.ts
- worker/src/automations/engine.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P2
core: 'no'
external_service: Instagram, LinkedIn, Telegram, Gmail
legacy_id: J-114
---

## Purpose and scope

Automation rules (admin). Priority P2, CORE no. Imported from journey J-114 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Tenant admin. Preconditions: Admin; channel connected.

## Steps and information flow

1. `/automations` -> rule editor (`RuleEditor`).
2. Wire: `POST {WORKER_URL}/automations/rules` header `Authorization: Bearer T` body `{"platform":"instagram","channelId":"<id>","topicId":"<optional>","triggers":["comment"],"comment_reply_template":"Thanks!","enabled":true}`.
3. `GET /automations/rules`, `GET /automations/rules/lookup?platform=instagram&channelId=<id>&topicId=<id>`, `DELETE /automations/rules` body `{platform,channelId,topicId?}`.
4. `POST /automations/webhooks/register` body per `registerPlatformWebhook`.

## Modules and code map

frontend/src/features/automations/, worker/src/automations/routes.ts, worker/src/automations/kv.ts, worker/src/automations/engine.ts

Code anchors that exist: worker/src/automations/routes.ts, worker/src/automations/kv.ts, worker/src/automations/engine.ts

## Success and acceptance

Rules stored in KV (`CONFIG_KV`) and resolved topic > channel; missing `platform`/`channelId` -> 400; non-admin -> 403. Rules are global (not per tenant): all admins share them.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
