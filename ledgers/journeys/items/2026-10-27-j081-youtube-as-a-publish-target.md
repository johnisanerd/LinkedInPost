---
id: 2026-10-27-j081-youtube-as-a-publish-target
title: J-081 YouTube as a publish target
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: YouTube "connected" (J-097).
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- frontend/src/integrations/channels.ts
- worker/src/automations/platforms/youtube.ts
- README.md
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P2
core: 'no'
external_service: YouTube
legacy_id: J-081
---

## Purpose and scope

YouTube as a publish target. Priority P2, CORE no. Imported from journey J-081 in docs/launch-readiness/journeys/JOURNEYS.md. The journey designer marked part of this journey NOT IMPLEMENTED per code reading.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: YouTube "connected" (J-097).

## Steps and information flow

1. Open the channel selector; `CHANNEL_OPTIONS` includes `youtube` with `publishVerb: 'YouTube Automations'`.
2. `ACTION publishContent {"row":{...},"channel":"youtube","message":"x"}`.

## Modules and code map

worker/src/index.ts (`coerceChannelId`), frontend/src/integrations/channels.ts, worker/src/automations/platforms/youtube.ts, README.md

Code anchors that exist: worker/src/index.ts, frontend/src/integrations/channels.ts, worker/src/automations/platforms/youtube.ts, README.md

## Success and acceptance

(NOT IMPLEMENTED per code reading: `coerceChannelId` in worker/src/index.ts accepts only instagram, linkedin, telegram, whatsapp, gmail, and throws `Unsupported delivery channel.` for youtube; `worker/src/automations/platforms/youtube.ts` is comment-reply automation only). The README claim "publish to ... YouTube" is therefore not true for posts; confirm the UI does not offer a publish button for it.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record. Not implemented per the journey designer: see the NOT IMPLEMENTED text in the steps.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
