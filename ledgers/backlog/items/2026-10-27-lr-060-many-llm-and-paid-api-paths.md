---
id: 2026-10-27-lr-060-many-llm-and-paid-api-paths
title: Many LLM and paid-API paths (stream generation, insights, trending, images, newsletter drafts) skip the usage budget check, so spend is uncapped.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j036-generate-pro-con-insights-for-a
- 2026-10-27-j045-attach-clips-to-a-draft-and
- 2026-10-27-j046-article-analysis-and-insight-extraction
- 2026-10-27-j047-debate-mode-returns-an-invented-opposing
- 2026-10-27-j048-cross-domain-and-opinion-leader-angles
- 2026-10-27-j052-topic-news-research-and-history
- 2026-10-27-j053-generate-a-draft-from-the-queue
- 2026-10-27-j058-streaming-generation-bypasses-the-monthly-token
- 2026-10-27-j068-ai-image-generation-text-and-reference
- 2026-10-27-j069-content-review-checklist-before-publishing
- 2026-10-27-j109-create-a-newsletter-and-preview-it
- 2026-10-27-j125-monthly-token-budget-exhausted
- 2026-10-27-j126-self-hosted-deployment-still-enforces-the
related: []
docs:
- worker/src/index.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: worker/llm
raw_id: LR-060
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Many LLM and paid-API paths (stream generation, insights, trending, images, newsletter drafts) skip the usage budget check, so spend is uncapped.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-036, J-045..J-048, J-052, J-053, J-058, J-068, J-069, J-109, J-125, J-126
- **Aliases:** WKA-012, WKB-016, WKB-020, GWP-010
- **Evidence:** worker/src/index.ts:835-1010 (no checkTokenBudget); budget checked only at worker/src/index.ts:1004,1574,1586,2532
- **Repro:** static. Executor: set a user's budget to 1 token, run a generation via the queue stream.
- **Fix hint:** Check the budget once in the dispatcher or stream entry for an LLM-spending action set, filter client llm through an allow-list, pass userId into the usage context, add per-user rate limits for paid search and image actions.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Check the budget once in the dispatcher or stream entry for an LLM-spending action set, filter client llm through an allow-list, pass userId into the usage context, add per-user rate limits for paid search and image actions.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-060). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/index.ts:835-1010 (no checkTokenBudget).
