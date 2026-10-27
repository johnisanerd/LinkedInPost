---
id: 2026-10-27-j101-oauth-misconfiguration-missing-or-wrong-client
title: 'J-101 OAuth misconfiguration: missing or wrong client id/secret, wrong redirect URI'
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: workflow
scope_type: section
scope: frontend
actor: Self-hosting operator
trigger: (a) `LINKEDIN_CLIENT_ID` unset, (b) wrong id, (c) redirect URI not registered, (d) `OAUTH_REDIRECT_BASE_URL` wrong.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- SETUP.md
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'yes'
external_service: LinkedIn
legacy_id: J-101
---

## Purpose and scope

OAuth misconfiguration: missing or wrong client id/secret, wrong redirect URI. Priority P1, CORE yes. Imported from journey J-101 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Self-hosting operator. Preconditions: (a) `LINKEDIN_CLIENT_ID` unset, (b) wrong id, (c) redirect URI not registered, (d) `OAUTH_REDIRECT_BASE_URL` wrong.

## Steps and information flow

1. `ACTION startLinkedInAuth {}` for (a).
2. Click Connect for (b), (c), (d) in the UI.

## Modules and code map

frontend/src/App.tsx (`handleConnect`), worker/src/index.ts (`hasLinkedInOAuthConfig`, `buildWorkerOrigin`, `requireFrontendOrigin`), SETUP.md

Code anchors that exist: worker/src/index.ts, SETUP.md

## Success and acceptance

(a) HTTP 400 `LinkedIn OAuth is not configured in the Worker environment. Add LINKEDIN_CLIENT_ID and LINKEDIN_CLIENT_SECRET first.`; the UI card should hide Connect when `linkedinAuthAvailable` is false. CODE-READING FINDING: for every failure `handleConnect` only does `console.error('OAuth connect failed:', err)`, so the user sees nothing happen. (b)-(d) fail inside the provider popup page; the operator needs a doc entry for the exact redirect URIs (`{origin}/auth/<provider>/callback`).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
