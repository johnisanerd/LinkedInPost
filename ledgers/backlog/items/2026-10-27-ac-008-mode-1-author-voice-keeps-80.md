---
id: 2026-10-27-ac-008-mode-1-author-voice-keeps-80
title: Mode 1 author-voice keeps >=80% of words
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related: []
docs:
- worker/src/engine/nodes/definitions/draft-generator.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: investigation
severity: P2
area: worker/generation
raw_id: AC-008
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
---

## Problem

Mode 1 author-voice keeps >=80% of words.

## Evidence and reproduction

- **Source:** launch-release/findings/raw/existing-reviews.md section 5, row D2-1
- **Alias:** D2-1
- **Original tag:** AC1 (no severity given, defaulted to P2)
- **Current status:** unverified
- **Evidence:** worker/src/engine/nodes/definitions/draft-generator.ts (no test seen for 80%)
- **Covered by:** none

## Acceptance criteria

- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (AC-008). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: reconciler could not confirm in code (no test seen for 80%); needs a check.
