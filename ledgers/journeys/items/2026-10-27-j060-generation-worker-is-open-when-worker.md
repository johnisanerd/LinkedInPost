---
id: 2026-10-27-j060-generation-worker-is-open-when-worker
title: J-060 Generation worker is open when `WORKER_SHARED_SECRET` is empty
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: workflow
scope_type: section
scope: worker
actor: Self-hosting operator
trigger: Generation worker deployed without `WORKER_SHARED_SECRET`.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- generation-worker/src/index.ts
- setup/worker_config.py
- setup/cloudflare.py
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P0
core: 'yes'
external_service: Cloudflare, LLM provider
legacy_id: J-060
---

## Purpose and scope

Generation worker is open when `WORKER_SHARED_SECRET` is empty. Priority P0, CORE yes. Imported from journey J-060 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Self-hosting operator. Preconditions: Generation worker deployed without `WORKER_SHARED_SECRET`.

## Steps and information flow

1. From any machine: `curl -X POST -H "Content-Type: application/json" -d '{...valid GenerateRequest...}' https://<gen-worker>/v1/generate`.
2. `curl https://<gen-worker>/v1/llm/catalog`, `curl https://<gen-worker>/v1/patterns/full`.

## Modules and code map

generation-worker/src/index.ts (`checkAuth`, `corsHeaders`), setup/worker_config.py, setup/cloudflare.py

Code anchors that exist: generation-worker/src/index.ts, setup/worker_config.py, setup/cloudflare.py

## Success and acceptance

Desired: 401 `{"error":"Unauthorized"}`. CODE-READING FINDING: `checkAuth` returns `true` when the secret is empty, and CORS is `Access-Control-Allow-Origin: *`; anyone can run the LLM pipeline on the operator's keys. The setup path generates the secret, but a manual deploy or a skipped secret leaves it open with no warning. Also, `Authorization` is compared as `Bearer <secret>` or the bare secret (string `===`, not timing-safe).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
