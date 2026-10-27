---
id: 2026-10-27-j004-generation-worker-deploy-requires-an-llm
title: J-004 Generation worker deploy requires an LLM key
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: workflow
scope_type: section
scope: worker
actor: Self-hosting operator
trigger: '`.env` without GEMINI_API_KEY and XAI_API_KEY.'
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- setup.py
- setup/cloudflare.py
- generation-worker/src/index.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P2
core: 'yes'
external_service: Cloudflare, LLM provider
legacy_id: J-004
---

## Purpose and scope

Generation worker deploy requires an LLM key. Priority P2, CORE yes. Imported from journey J-004 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Self-hosting operator. Preconditions: `.env` without GEMINI_API_KEY and XAI_API_KEY.

## Steps and information flow

1. `python setup.py --deploy-worker`.
2. Read the error.
3. Add `GEMINI_API_KEY`, rerun.

## Modules and code map

setup.py, setup/cloudflare.py (`ensure_worker_deploy`, `push_llm_secrets`), generation-worker/src/index.ts

Code anchors that exist: setup.py, setup/cloudflare.py, generation-worker/src/index.ts

## Success and acceptance

Step 2 fails fast with an explicit "at least one LLM key" message before any deploy (per SETUP.md); step 3 succeeds and `GET {GEN_WORKER_URL}/v1/health` with `Authorization: Bearer $WORKER_SHARED_SECRET` returns `{"status":"ok","service":"generation-worker",...}`.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
