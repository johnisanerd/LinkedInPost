---
id: 2026-10-27-j002-headless-full-bootstrap-with-python-setup
title: J-002 Headless full bootstrap with `python setup.py --all`
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: workflow
scope_type: section
scope: setup
actor: Self-hosting operator
trigger: '`.env` populated (GEMINI_API_KEY or XAI_API_KEY, GOOGLE_CLIENT_ID / VITE_GOOGLE_CLIENT_ID, service account JSON, bucket name); `npx wrangler login` done; `gh` authenticated if GitHub secrets sync is w'
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- setup.py
- setup/cloudflare.py
- setup/worker_config.py
- setup/google_resources.py
- setup/github.py
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'yes'
external_service: Cloudflare
legacy_id: J-002
---

## Purpose and scope

Headless full bootstrap with `python setup.py --all`. Priority P1, CORE yes. Imported from journey J-002 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Self-hosting operator. Preconditions: `.env` populated (GEMINI_API_KEY or XAI_API_KEY, GOOGLE_CLIENT_ID / VITE_GOOGLE_CLIENT_ID, service account JSON, bucket name); `npx wrangler login` done; `gh` authenticated if GitHub secrets sync is wanted.

## Steps and information flow

1. `python setup.py --all` (sets install-worker-deps, cloudflare, deploy-worker, sync-github-secrets).
2. Observe in order: features regeneration, worker deps install, `tsc --noEmit` in worker and frontend, Google resources, KV namespaces, D1 create and migrations, generation worker D1, `worker/.dev.vars` written, generation worker deployed first then main worker, LLM secrets pushed, GitHub secrets synced, summary printed.

## Modules and code map

setup.py `main()`, setup/cloudflare.py, setup/worker_config.py, setup/google_resources.py, setup/github.py

Code anchors that exist: setup.py, setup/cloudflare.py, setup/worker_config.py, setup/google_resources.py, setup/github.py

## Success and acceptance

Exit code 0; `GET {WORKER_URL}/` returns `{"ok":true,"data":{"status":"ok","backend":"cloudflare-worker"}}`; the main worker `GENERATION_WORKER_URL` var points at the generation worker URL.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
