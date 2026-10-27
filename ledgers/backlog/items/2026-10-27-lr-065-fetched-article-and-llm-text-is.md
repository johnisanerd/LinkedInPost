---
id: 2026-10-27-lr-065-fetched-article-and-llm-text-is
title: Fetched article and LLM text is inserted into newsletter HTML unescaped, allowing attribute and HTML injection and possible stored XSS.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j052-topic-news-research-and-history
- 2026-10-27-j109-create-a-newsletter-and-preview-it
- 2026-10-27-j110-draft-approve-and-send-a-newsletter
related: []
docs:
- worker/src/newsletter/emailRenderer.ts
- worker/src/researcher/providers/rss.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: worker/newsletter
raw_id: LR-065
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Fetched article and LLM text is inserted into newsletter HTML unescaped, allowing attribute and HTML injection and possible stored XSS.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-052, J-109, J-110
- **Aliases:** WKB-015
- **Evidence:** worker/src/newsletter/emailRenderer.ts:202,206,261-262; worker/src/researcher/providers/rss.ts:7-12
- **Repro:** static. Executor: add a custom RSS feed whose item title contains `<img src=x onerror=alert(1)>` in CDATA and whose link contains `"`; open preview.
- **Fix hint:** HTML-escape all interpolated strings, allow only http(s) URLs, sanitise LLM HTML with an allow-list.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

HTML-escape all interpolated strings, allow only http(s) URLs, sanitise LLM HTML with an allow-list.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-065). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/newsletter/emailRenderer.ts:202,206,261-262.
