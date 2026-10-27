---
id: 2026-10-27-j123-admin-panel-users-approve-suspend-budget
title: 'J-123 Admin panel: users, approve, suspend, budget'
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Tenant admin
trigger: '`deploymentMode: saas` (the header link "Admin" only shows in saas; the route `/admin` itself is available to any admin in any mode).'
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
priority: P1
core: 'yes'
external_service: none
legacy_id: J-123
---

## Purpose and scope

Admin panel: users, approve, suspend, budget. Priority P1, CORE yes. Imported from journey J-123 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Tenant admin. Preconditions: `deploymentMode: saas` (the header link "Admin" only shows in saas; the route `/admin` itself is available to any admin in any mode).

## Steps and information flow

1. `/admin`; wire: `ACTION __admin__ {"__path":"/api/admin/users","__method":"GET"}` and `{"__path":"/api/admin/waitlist","__method":"GET"}`.
2. Click "Budget" on a user (prompt in thousands): `ACTION __admin__ {"__path":"/api/admin/users/<email>/budget","__method":"POST","budget":1000000}`.
3. "Suspend" / "Approve": `.../suspend` and `.../approve` (POST).

## Modules and code map

frontend/src/features/saas/AdminPanel.tsx, frontend/src/services/backendApi.ts, worker/src/modes/saas/admin.ts, worker/src/db/users.ts

Code anchors that exist: frontend/src/services/backendApi.ts, worker/src/modes/saas/admin.ts, worker/src/db/users.ts

## Success and acceptance

Users list includes `monthly_tokens_used`; budget update persists to `users.monthly_token_budget`; suspend -> next request by that user fails (J-128); invalid budget (0, negative, missing) -> `{"error":"budget must be a positive number"}` (HTTP 400, so an admin cannot set a zero budget as a soft block: use Suspend).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
