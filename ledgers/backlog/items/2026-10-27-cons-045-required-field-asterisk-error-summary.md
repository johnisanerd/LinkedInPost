---
id: 2026-10-27-cons-045-required-field-asterisk-error-summary
title: Required-field asterisk + error summary
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-178-queue-and-addtopic-polish-no-required
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: ux-gap
severity: P2
area: frontend/queue
raw_id: CONS-045
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
---

## Problem

Required-field asterisk + error summary.

## Evidence and reproduction

- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C04-6
- **Alias:** C04-6
- **Original tag:** MED (mapped to P2)
- **Current status:** partial
- **Evidence:** AddTopicPage.tsx:275 inline title error (no asterisk on title)
- **Covered by:** LR-178

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (CONS-045). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: partial; still open in code (no asterisk on title); covered by LR-178.
