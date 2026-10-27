---
id: 2026-10-27-lr-064-newsletter-bodies-are-generated-in-gemini
title: Newsletter bodies are generated in Gemini JSON mode, so the stored email body is an escaped JSON string rather than HTML.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j109-create-a-newsletter-and-preview-it
- 2026-10-27-j110-draft-approve-and-send-a-newsletter
- 2026-10-27-j111-scheduled-newsletter-send-vs-a-once
related: []
docs:
- worker/src/newsletter/emailRenderer.ts
- worker/src/llm/providers/gemini.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: worker/newsletter
raw_id: LR-064
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Newsletter bodies are generated in Gemini JSON mode, so the stored email body is an escaped JSON string rather than HTML.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-109..J-111
- **Aliases:** WKB-014
- **Evidence:** worker/src/newsletter/emailRenderer.ts:80-103,117-130; worker/src/llm/providers/gemini.ts:145
- **Repro:** static. Executor: `newsletter.createDraftByNewsletter`, read `rendered_content`.
- **Fix hint:** Add a plain-text/HTML generation path or request {html} and parse it.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Add a plain-text/HTML generation path or request {html} and parse it.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-064). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/newsletter/emailRenderer.ts:80-103,117-130.
