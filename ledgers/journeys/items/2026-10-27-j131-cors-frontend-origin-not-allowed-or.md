---
id: 2026-10-27-j131-cors-frontend-origin-not-allowed-or
title: 'J-131 CORS: frontend origin not allowed, or allowlist empty'
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: workflow
scope_type: section
scope: frontend
actor: Self-hosting operator
trigger: Frontend served from `https://app.example.com`; worker `CORS_ALLOWED_ORIGINS` lacks it.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- frontend/src/services/backendApi.ts
- setup/worker_config.py
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'yes'
external_service: Cloudflare
legacy_id: J-131
---

## Purpose and scope

CORS: frontend origin not allowed, or allowlist empty. Priority P1, CORE yes. Imported from journey J-131 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Self-hosting operator. Preconditions: Frontend served from `https://app.example.com`; worker `CORS_ALLOWED_ORIGINS` lacks it.

## Steps and information flow

1. Sign in.
2. Repeat with `CORS_ALLOWED_ORIGINS` empty.

## Modules and code map

worker/src/index.ts (`buildCorsHeaders`), frontend/src/services/backendApi.ts (`formatFetchNetworkFailure`), setup/worker_config.py

Code anchors that exist: worker/src/index.ts, frontend/src/services/backendApi.ts, setup/worker_config.py

## Success and acceptance

Case 1: browser blocks the call; UI message built by `formatFetchNetworkFailure` explains the CORS variable and mixed content (if `http://` worker on an https page). Case 2: `buildCorsHeaders` returns `Access-Control-Allow-Origin: *` when the list is empty (fail-open) — acceptable only with token auth, but note `/api/waitlist` and webhooks are then callable from any site. Origins with a trailing slash or `127.0.0.1` vs `localhost` mismatches are a common failure.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
