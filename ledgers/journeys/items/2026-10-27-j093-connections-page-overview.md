---
id: 2026-10-27-j093-connections-page-overview
title: J-093 Connections page overview
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: Signed in (admin, see J-031).
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/db/socialIntegrations.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P2
core: 'yes'
external_service: none
legacy_id: J-093
---

## Purpose and scope

Connections page overview. Priority P2, CORE yes. Imported from journey J-093 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: Signed in (admin, see J-031).

## Steps and information flow

1. Open `/connections`.
2. `ACTION getIntegrations {}`.

## Modules and code map

frontend/src/pages/connections/ConnectionsPage.tsx, frontend/src/pages/connections/SocialAccountCard.tsx, worker/src/db/socialIntegrations.ts

Code anchors that exist: worker/src/db/socialIntegrations.ts

## Success and acceptance

Cards for LinkedIn, Instagram, Gmail, WhatsApp, Telegram, YouTube plus the Google Sheet card; connected providers show a green "Connected" dot; list matches `{provider,internalId,displayName,profilePicture,needsReauth,connectedAt}`.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
