---
id: 2026-10-27-j094-connect-linkedin-popup-oauth
title: J-094 Connect LinkedIn (popup OAuth)
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: Worker has `LINKEDIN_CLIENT_ID`, `LINKEDIN_CLIENT_SECRET`, `SECRET_ENCRYPTION_KEY`; redirect URI `{worker origin}/auth/linkedin/callback` registered in the LinkedIn app.
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
external_service: LinkedIn
legacy_id: J-094
---

## Purpose and scope

Connect LinkedIn (popup OAuth). Priority P1, CORE yes. Imported from journey J-094 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: Worker has `LINKEDIN_CLIENT_ID`, `LINKEDIN_CLIENT_SECRET`, `SECRET_ENCRYPTION_KEY`; redirect URI `{worker origin}/auth/linkedin/callback` registered in the LinkedIn app.

## Steps and information flow

1. `/connections` -> LinkedIn -> Connect.
2. Wire: `ACTION startLinkedInAuth {}` -> `{authorizationUrl,callbackOrigin}`; popup opens `https://www.linkedin.com/oauth/v2/authorization?...scope=openid profile w_member_social`.
3. Authorize; LinkedIn redirects to `GET /auth/linkedin/callback?code=...&state=...`.
4. Popup posts `{source:"channel-bot-oauth",provider:"linkedin",ok:true}` to the opener and the UI refetches `getIntegrations`.

## Modules and code map

worker/src/index.ts (`startLinkedInAuth`, `handleLinkedInCallback`, `consumeOAuthState`, `oauthPopupResponse`), frontend/src/App.tsx (`handleConnect`), worker/src/integrations/linkedin

Code anchors that exist: worker/src/index.ts

## Success and acceptance

`social_integrations` has a row `(user_id, 'linkedin')` with encrypted token and `token_expires_at` ~60 days; card shows Connected. KV `shared-config` also gets the token (see J-103).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
