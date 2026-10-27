---
id: 2026-10-27-lr-154-no-llm-provider-call-has-a
title: No LLM provider call has a timeout, so a stalled provider holds the request and the fallback model is never tried
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j053-generate-a-draft-from-the-queue
- 2026-10-27-j055-generation-worker-down-mis-secreted-or
- 2026-10-27-j065-quick-change-via-sse
- 2026-10-27-j122-llm-provider-failure-and-fallback
related: []
docs:
- worker/src/llm/providers/gemini.ts
- generation-worker/src/players/retryUtils.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: worker/llm
raw_id: LR-154
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

No LLM provider call has a timeout, so a stalled provider holds the request and the fallback model is never tried.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-053, J-055, J-065, J-122
- **Aliases:** WKB-025, GWP-019
- **Evidence:** worker/src/llm/providers/gemini.ts:84,157; generation-worker/src/players/retryUtils.ts
- **Repro:** static; executor: point a provider at a blackhole URL.
- **Fix hint:** Wrap provider fetches with a 60-90 s AbortSignal.timeout mapped to a retryable error and an overall pipeline deadline; cache the model catalog.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Wrap provider fetches with a 60-90 s AbortSignal.timeout mapped to a retryable error and an overall pipeline deadline; cache the model catalog.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-154). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/llm/providers/gemini.ts:84,157.
