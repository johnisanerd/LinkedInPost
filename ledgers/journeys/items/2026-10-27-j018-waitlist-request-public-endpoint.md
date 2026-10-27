---
id: 2026-10-27-j018-waitlist-request-public-endpoint
title: J-018 Waitlist request (public endpoint)
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Non-approved / unauthorised user
trigger: SaaS landing.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/modes/saas/waitlist.ts
- worker/src/db/users.ts
- worker/migrations/0019_user_status_budget.sql
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P2
core: 'no'
external_service: none
legacy_id: J-018
---

## Purpose and scope

Waitlist request (public endpoint). Priority P2, CORE no. Imported from journey J-018 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Non-approved / unauthorised user. Preconditions: SaaS landing.

## Steps and information flow

1. On `/` scroll to `#waitlist`, fill email (and optional name/reason), click "Join waitlist".
2. Or `POST {WORKER_URL}/api/waitlist` body `{"email":"a@b.co","name":"A","reason":"r"}`.
3. Repeat with `{"email":"nope"}` and with the same email twice.

## Modules and code map

worker/src/modes/saas/waitlist.ts, worker/src/db/users.ts (`createAccessRequest`), worker/migrations/0019_user_status_budget.sql, frontend/src/features/saas/Landing.tsx

Code anchors that exist: worker/src/modes/saas/waitlist.ts, worker/src/db/users.ts, worker/migrations/0019_user_status_budget.sql

## Success and acceptance

Step 2: HTTP 201 `{"ok":true,"message":"Request received..."}` and a row in D1 `access_requests` (status `pending`). Invalid email: HTTP 400 `{"error":"Valid email required"}`. The table has `email UNIQUE`, so a duplicate request should return a handled response, not a 500 (verify in `createAccessRequest`). No rate limit exists on this unauthenticated endpoint (CODE-READING FINDING).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
