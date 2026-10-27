---
id: 2026-10-27-lr-155-provider-and-model-are-silently-substituted
title: Provider and model are silently substituted (unknown provider, vision to Gemini, newsletter fixed model) without telling the user.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j069-content-review-checklist-before-publishing
- 2026-10-27-j121-pick-provider-and-model-per-purpose
- 2026-10-27-j122-llm-provider-failure-and-fallback
related: []
docs:
- worker/src/llm/genWorkerDefaults.ts
- worker/src/llm/gateway.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: worker/llm
raw_id: LR-155
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Provider and model are silently substituted (unknown provider, vision to Gemini, newsletter fixed model) without telling the user.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-069, J-121, J-122
- **Aliases:** WKB-024
- **Evidence:** worker/src/llm/genWorkerDefaults.ts:23-38; worker/src/llm/gateway.ts:105-129
- **Repro:** static; executor: set the vision setting to grok and run content review; check which vendor logs the call.
- **Fix hint:** Return {requested, used, reason} and show it in the UI; honour workspace refs in the newsletter.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Return {requested, used, reason} and show it in the UI; honour workspace refs in the newsletter.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-155). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/llm/genWorkerDefaults.ts:23-38.
