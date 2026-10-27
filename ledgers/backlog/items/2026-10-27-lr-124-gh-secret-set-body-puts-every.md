---
id: 2026-10-27-lr-124-gh-secret-set-body-puts-every
title: gh secret set --body puts every secret on the process command line and is not scoped with --repo
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j002-headless-full-bootstrap-with-python-setup
related: []
docs:
- setup/github.py
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: setup/cli
raw_id: LR-124
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

gh secret set --body puts every secret on the process command line and is not scoped with --repo.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-002
- **Aliases:** SET-023
- **Evidence:** setup/github.py:203
- **Repro:** static.
- **Fix hint:** Pass the value via stdin and add --repo owner/repo.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Pass the value via stdin and add --repo owner/repo.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-124). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of setup/github.py:203.
