---
id: 2026-10-27-j096-connect-gmail
title: J-096 Connect Gmail
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: worker
actor: Approved end user
trigger: '`GMAIL_CLIENT_ID`, `GMAIL_CLIENT_SECRET` on the worker; redirect `/auth/gmail/callback` registered; scopes `gmail.send` + `email`.'
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
external_service: Gmail, Google OAuth
legacy_id: J-096
---

## Purpose and scope

Connect Gmail. Priority P1, CORE yes. Imported from journey J-096 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: `GMAIL_CLIENT_ID`, `GMAIL_CLIENT_SECRET` on the worker; redirect `/auth/gmail/callback` registered; scopes `gmail.send` + `email`.

## Steps and information flow

1. `/connections` -> Gmail -> Connect (`ACTION startGmailAuth {}`).
2. Authorize; callback `GET /auth/gmail/callback`.

## Modules and code map

worker/src/index.ts (`startGmailAuth`, `handleGmailCallback`, `GMAIL_OAUTH_SCOPES`), worker/src/integrations/gmail

Code anchors that exist: worker/src/index.ts

## Success and acceptance

Row for `gmail` with refresh token (access type offline must be requested, else sends fail after 1 hour; verify the authorization URL contains `access_type=offline` and `prompt=consent`); `config.gmailEmailAddress` populated.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
