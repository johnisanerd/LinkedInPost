---
id: 2026-10-27-lr-156-gemini-and-news-api-keys-are
title: Gemini and news API keys are sent in the URL query string, exposed to logs and proxies
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j053-generate-a-draft-from-the-queue
related: []
docs:
- packages/researcher/src/providers/newsApis.ts
- worker/src/llm/providers/gemini.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: worker/llm
raw_id: LR-156
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Gemini and news API keys are sent in the URL query string, exposed to logs and proxies.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-053
- **Aliases:** GWP-016
- **Evidence:** packages/researcher/src/providers/newsApis.ts:20-29; worker/src/llm/providers/gemini.ts:52,85,158
- **Repro:** static.
- **Fix hint:** Use x-goog-api-key for Gemini and headers where the vendor supports them; keep error text free of the URL.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Use x-goog-api-key for Gemini and headers where the vendor supports them; keep error text free of the URL.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-156). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of packages/researcher/src/providers/newsApis.ts:20-29.
