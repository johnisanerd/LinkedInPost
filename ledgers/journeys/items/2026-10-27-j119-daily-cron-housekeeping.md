---
id: 2026-10-27-j119-daily-cron-housekeeping
title: J-119 Daily cron housekeeping
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: worker
actor: Background / agent actor
trigger: Deployed worker, cron `0 3 * * *`.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- worker/src/automations/cleanup.ts
- worker/src/db/llm-usage.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P3
core: 'no'
external_service: Cloudflare
legacy_id: J-119
---

## Purpose and scope

Daily cron housekeeping. Priority P3, CORE no. Imported from journey J-119 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Background / agent actor. Preconditions: Deployed worker, cron `0 3 * * *`.

## Steps and information flow

1. Trigger locally: `wrangler dev --test-scheduled` and `curl "http://localhost:8787/__scheduled"` (or wait for 03:00 UTC).
2. Inspect logs.

## Modules and code map

worker/src/index.ts (`scheduled`), worker/src/automations/cleanup.ts, worker/src/db/llm-usage.ts, worker/src/image-gen

Code anchors that exist: worker/src/index.ts, worker/src/automations/cleanup.ts, worker/src/db/llm-usage.ts

## Success and acceptance

`scheduled()` runs, each in `ctx.waitUntil(...catch)`: `runAutomationCleanup`, `pruneOldNewsSnapshots`, `pruneOldLlmUsageLog`, `syncImageGenCatalog`, newsletter scheduler; one failure does not stop the others. Note that `pruneOldLlmUsageLog` removes the rows the monthly budget sums over; check its retention is longer than the billing month.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
