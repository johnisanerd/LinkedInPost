---
id: 2026-10-27-j124-usage-meter-and-usage-page
title: J-124 Usage meter and usage page
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: SaaS mode.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- worker/src/db/users.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P2
core: 'no'
external_service: none
legacy_id: J-124
---

## Purpose and scope

Usage meter and usage page. Priority P2, CORE no. Imported from journey J-124 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: SaaS mode.

## Steps and information flow

1. Header `UsageMeter` after login (`GET {WORKER_URL}/api/usage` with `Authorization: Bearer T`).
2. `/usage` page: `ACTION getUsageSummary {}` and `ACTION getUsageSummaryByRange {"days":7}`.

## Modules and code map

frontend/src/features/saas/UsageMeter.tsx, frontend/src/pages/UsagePage.tsx, worker/src/index.ts, worker/src/db/users.ts (`getMonthlyTokenUsage`)

Code anchors that exist: worker/src/index.ts, worker/src/db/users.ts

## Success and acceptance

`/api/usage` returns `{used,budget,resetDate}` where `resetDate` is the 1st of next month computed in the Worker's local time (UTC); `days` clamped to 1-90; admin sees all users' usage, non-admin only their own rows. Meter and budget check use the same table (`llm_usage_log`).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
