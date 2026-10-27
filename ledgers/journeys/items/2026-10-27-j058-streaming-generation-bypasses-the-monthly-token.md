---
id: 2026-10-27-j058-streaming-generation-bypasses-the-monthly-token
title: J-058 Streaming generation bypasses the monthly token budget
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: worker
actor: Tenant admin
trigger: SaaS mode (`DEPLOYMENT_MODE` unset or `saas`); a user whose month usage >= `monthly_token_budget`.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- worker/src/auth.ts
- worker/src/db/llm-usage.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'yes'
external_service: LLM provider
legacy_id: J-058
---

## Purpose and scope

Streaming generation bypasses the monthly token budget. Priority P1, CORE yes. Imported from journey J-058 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Tenant admin. Preconditions: SaaS mode (`DEPLOYMENT_MODE` unset or `saas`); a user whose month usage >= `monthly_token_budget`.

## Steps and information flow

1. As that user `ACTION generateQuickChange {...}`: expect `Monthly token budget exceeded`.
2. As that user `POST /api/generate/stream` (the main generation path).

## Modules and code map

worker/src/index.ts, worker/src/auth.ts (`checkTokenBudget`), worker/src/db/llm-usage.ts

Code anchors that exist: worker/src/index.ts, worker/src/auth.ts, worker/src/db/llm-usage.ts

## Success and acceptance

Desired: 429-style refusal on both. CODE-READING FINDING: `/api/quickchange/stream`, `generateQuickChange`, `generateVariantsPreview` and `callGenerationWorker` call `checkTokenBudget`; `/api/generate/stream` does not. Also `analyzeTopicInsights`, `analyzeFeedArticle`, `extractArticleInsights`, `clusterDraftClips`, `findDraftConnections`, `findDebateArticle`, `crossDomainInsight`, `opinionLeaderInsights`, `generateImageFromText` have no check.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
