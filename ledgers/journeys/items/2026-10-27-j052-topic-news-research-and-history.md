---
id: 2026-10-27-j052-topic-news-research-and-history
title: J-052 Topic news research and history
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: '`FEATURE_NEWS_RESEARCH` true; sheet connected (`ensureSpreadsheetConfigured`).'
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P2
core: 'yes'
external_service: other (news providers)
legacy_id: J-052
---

## Purpose and scope

Topic news research and history. Priority P2, CORE yes. Imported from journey J-052 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: `FEATURE_NEWS_RESEARCH` true; sheet connected (`ensureSpreadsheetConfigured`).

## Steps and information flow

1. In the topic editor open the researcher panel (`ResearcherPanel`) and search.
2. API: `ACTION searchNewsResearch {"topicId":"<id>","topic":"...","date":"..."}`, then `ACTION listNewsResearchHistory {"topicId":"<id>","limit":20}` and `ACTION getNewsResearchSnapshot {"id":"<snapshot id>"}`.
3. Set `features.yaml` `newsResearch: false`, regenerate, retry.

## Modules and code map

worker/src/index.ts, worker/src/researcher, packages/researcher, frontend/src/features/news-research/ResearcherPanel.tsx

Code anchors that exist: worker/src/index.ts

## Success and acceptance

Search stores a snapshot (max `NEWS_SNAPSHOT_MAX_PER_TOPIC`, default 10; pruned by the daily cron); history lists newest first; with the flag off, each action throws `News research is disabled for this deployment.`

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
