---
id: 2026-10-27-j019-admin-approves-a-waitlist-entry
title: J-019 Admin approves a waitlist entry
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Tenant admin
trigger: SaaS mode; admin signed in; a pending `access_requests` row.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- frontend/src/services/backendApi.ts
- worker/src/modes/saas/admin.ts
- worker/src/db/users.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P2
core: 'no'
external_service: none
legacy_id: J-019
---

## Purpose and scope

Admin approves a waitlist entry. Priority P2, CORE no. Imported from journey J-019 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Tenant admin. Preconditions: SaaS mode; admin signed in; a pending `access_requests` row.

## Steps and information flow

1. Header "Admin" -> `/admin`.
2. In "Waitlist" click "Approve" on the row (calls `approveUserAccess`, i.e. `ACTION __admin__ {"__path":"/api/admin/users/<email>/approve","__method":"POST"}`).

## Modules and code map

frontend/src/features/saas/AdminPanel.tsx, frontend/src/services/backendApi.ts (`approveUserAccess`), worker/src/modes/saas/admin.ts, worker/src/db/users.ts (`setUserStatus`, `resolveAccessRequest`)

Code anchors that exist: frontend/src/services/backendApi.ts, worker/src/modes/saas/admin.ts, worker/src/db/users.ts

## Success and acceptance

`access_requests.status='approved'`; `users.status='active'` for the email if the user row exists. If the person has never signed in there is no `users` row so `UPDATE users` changes 0 rows (harmless today because the default status is `active`, see J-017).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
