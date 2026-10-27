---
id: 2026-10-27-j022-non-auth-errors-that-contain-expired
title: J-022 Non-auth errors that contain "expired" or "not allowed" force a sign-out
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: Signed in; an OAuth state older than 10 minutes, or any backend message containing the words.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- frontend/src/services/backendApi.ts
- frontend/src/features/review/context/useReviewFlowActions.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P2
core: 'yes'
external_service: LinkedIn
legacy_id: J-022
---

## Purpose and scope

Non-auth errors that contain "expired" or "not allowed" force a sign-out. Priority P2, CORE yes. Imported from journey J-022 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: Signed in; an OAuth state older than 10 minutes, or any backend message containing the words.

## Steps and information flow

1. `ACTION completeWhatsAppConnection {"connectionId":"old","phoneNumberId":"1"}` (admin) after the 10-minute pending TTL, or trigger any error text containing "expired".
2. Observe the UI.

## Modules and code map

frontend/src/services/backendApi.ts (`AUTH_ERROR_PATTERN`), frontend/src/features/review/context/useReviewFlowActions.ts, frontend/src/features/campaign/CampaignPage.tsx

Code anchors that exist: frontend/src/services/backendApi.ts, frontend/src/features/review/context/useReviewFlowActions.ts

## Success and acceptance

Error `The WhatsApp connection session expired. Start the connection again.` is shown as a notice. CODE-READING FINDING: `AUTH_ERROR_PATTERN = /unauthorized|invalid token|expired|sign in again|not allowed/i` matches it, so paths using `handleFailure`/`isAuthErrorMessage` sign the user out.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
