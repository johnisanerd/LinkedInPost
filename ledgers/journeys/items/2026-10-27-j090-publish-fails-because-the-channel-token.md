---
id: 2026-10-27-j090-publish-fails-because-the-channel-token
title: J-090 Publish fails because the channel token was revoked or expired
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: LinkedIn token revoked from the LinkedIn side (or past the 60 days stored in `token_expires_at`).
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
legacy_id: J-090
---

## Purpose and scope

Publish fails because the channel token was revoked or expired. Priority P1, CORE yes. Imported from journey J-090 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: LinkedIn token revoked from the LinkedIn side (or past the 60 days stored in `token_expires_at`).

## Steps and information flow

1. Publish to LinkedIn.
2. Open `/connections`.

## Modules and code map

worker/src/index.ts (linkedin branch), worker/src/db/socialIntegrations.ts, frontend/src/pages/connections/ConnectionsPage.tsx, worker/src/integrations/linkedin

Code anchors that exist: worker/src/index.ts, worker/src/db/socialIntegrations.ts

## Success and acceptance

User sees the LinkedIn error text (not a blank failure), the row stays `Approved`, and `/connections` shows the account as needing reconnect (`needsReauth` flag from `listSocialIntegrations`). There is no refresh-token logic for LinkedIn (60 day token); confirm the user is warned before expiry. For a scheduled post the failure is only a console log (J-083).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
