---
id: 2026-10-27-lr-176-newsletter-subject-template-variables-are-not
title: Newsletter subject template variables are not verified end to end and validation lacks character counts
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j109-create-a-newsletter-and-preview-it
related: []
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P3
area: frontend/newsletter
raw_id: LR-176
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Newsletter subject template variables are not verified end to end and validation lacks character counts.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-109
- **Aliases:** C08-7, C08-2
- **Evidence:** frontend/src/features/campaign/components/newsletter/NewsletterConfigDrawer.tsx:125-137
- **Repro:** (static check) Open frontend/src/features/campaign/components/newsletter/NewsletterConfigDrawer.tsx:125-137 and confirm the behaviour described in the summary; then exercise the matching journey (J-109) to observe it.
- **Fix hint:** Verify variables end to end or remove the claim.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Verify variables end to end or remove the claim.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-176). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/features/campaign/components/newsletter/NewsletterConfigDrawer.tsx:125-137.
