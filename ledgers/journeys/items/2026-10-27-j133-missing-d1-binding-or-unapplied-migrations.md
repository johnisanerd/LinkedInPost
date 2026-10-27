---
id: 2026-10-27-j133-missing-d1-binding-or-unapplied-migrations
title: J-133 Missing D1 binding or unapplied migrations
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: workflow
scope_type: section
scope: worker
actor: Self-hosting operator
trigger: (a) `PIPELINE_DB` binding removed or id wrong; (b) database exists but migrations not applied.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- setup/cloudflare.py
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'yes'
external_service: Cloudflare
legacy_id: J-133
---

## Purpose and scope

Missing D1 binding or unapplied migrations. Priority P1, CORE yes. Imported from journey J-133 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Self-hosting operator. Preconditions: (a) `PIPELINE_DB` binding removed or id wrong; (b) database exists but migrations not applied.

## Steps and information flow

1. Sign in; `ACTION bootstrap {}`.
2. `GET {WORKER_URL}/` (no DB needed).

## Modules and code map

worker/src/index.ts (`verifySession` -> `upsertUser`, catch block), worker/wrangler.jsonc, setup/cloudflare.py (`_apply_d1_migrations`)

Code anchors that exist: worker/src/index.ts, setup/cloudflare.py

## Success and acceptance

Step 2 returns OK (health check does not touch D1, so setup "verify" can pass while the app is broken). Step 1 returns HTTP 400 with the raw runtime message (e.g. `Cannot read properties of undefined (reading 'prepare')` or `D1_ERROR: no such table: users`) and the frontend shows it as "Unable to start the session"/access error. Desired: a clear "database not initialised: run migrations" message and a health endpoint that checks D1.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
