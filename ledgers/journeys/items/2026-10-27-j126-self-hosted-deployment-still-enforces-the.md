---
id: 2026-10-27-j126-self-hosted-deployment-still-enforces-the
title: J-126 Self-hosted deployment still enforces the SaaS budget
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: workflow
scope_type: section
scope: worker
actor: Self-hosting operator
trigger: '`features.yaml` `deploymentMode: selfHosted`; worker deployed through setup (which never sets `DEPLOYMENT_MODE`).'
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- worker/src/auth.ts
- features.yaml
- worker/migrations/0019_user_status_budget.sql
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'yes'
external_service: LLM provider
legacy_id: J-126
---

## Purpose and scope

Self-hosted deployment still enforces the SaaS budget. Priority P1, CORE yes. Imported from journey J-126 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Self-hosting operator. Preconditions: `features.yaml` `deploymentMode: selfHosted`; worker deployed through setup (which never sets `DEPLOYMENT_MODE`).

## Steps and information flow

1. Use the app until `llm_usage_log` sums over 500,000 tokens in the calendar month (default `monthly_token_budget`).
2. Run Quick Change.

## Modules and code map

worker/src/index.ts (`checkTokenBudget` call sites), worker/src/auth.ts, .env.example, features.yaml, worker/migrations/0019_user_status_budget.sql

Code anchors that exist: worker/src/index.ts, worker/src/auth.ts, features.yaml, worker/migrations/0019_user_status_budget.sql

## Success and acceptance

Desired: self-hosted has no budget (frontend hides the meter and docs say "no usage meter"). CODE-READING FINDING: the worker uses `env.DEPLOYMENT_MODE ?? 'saas'`; neither `.env.example` (commented `# DEPLOYMENT_MODE=saas`), wrangler vars nor setup set it, so a self-hosted owner is cut off at 500k tokens with `Monthly token budget exceeded` and no visible meter.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
