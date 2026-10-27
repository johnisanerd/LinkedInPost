---
id: 2026-10-27-j098-oauth-popup-closed-blocked-or-cancelled
title: J-098 OAuth popup closed, blocked or cancelled
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: New signed-in user
trigger: None.
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
external_service: LinkedIn
legacy_id: J-098
---

## Purpose and scope

OAuth popup closed, blocked or cancelled. Priority P2, CORE yes. Imported from journey J-098 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: New signed-in user. Preconditions: None.

## Steps and information flow

1. Click Connect with the popup blocker on (`window.open` returns null).
2. Click Connect, then close the popup without authorizing.
3. Click Connect, then click "Cancel" on the provider page (provider returns `error=access_denied`).

## Modules and code map

frontend/src/App.tsx (`handleConnect`), worker/src/index.ts (`oauthPopupResponse`)

Code anchors that exist: worker/src/index.ts

## Success and acceptance

Step 1: user sees guidance (CODE-READING FINDING: `handleConnect` uses `popup?.closed`, a null popup hangs the promise only until the interval sees `undefined?.closed` -> undefined, so the promise never resolves and `connecting` stays set; verify). Step 2: promise resolves, integrations refetched, no error. Step 3: popup shows the provider error text and the opener gets `ok:false` -> thrown Error only reaches `console.error` (no user-visible message).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
