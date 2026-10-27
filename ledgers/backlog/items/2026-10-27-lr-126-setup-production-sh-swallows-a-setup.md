---
id: 2026-10-27-lr-126-setup-production-sh-swallows-a-setup
title: setup-production.sh swallows a setup.py failure and prints Setup Complete, and the local launchers need frontend dependencies they never install.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j001-web-setup-wizard-end-to-end
- 2026-10-27-j002-headless-full-bootstrap-with-python-setup
- 2026-10-27-j011-local-development-loop
related: []
docs:
- scripts/setup-production.sh
- scripts/setup-local.sh
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: setup/cli
raw_id: LR-126
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

setup-production.sh swallows a setup.py failure and prints Setup Complete, and the local launchers need frontend dependencies they never install.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-001, J-002, J-011
- **Aliases:** SET-028
- **Evidence:** scripts/setup-production.sh:83,98,103-106; scripts/setup-local.sh:55-56
- **Repro:** static. Fresh clone, `./scripts/setup-local.sh`.
- **Fix hint:** Remove || true, propagate exit codes, install deps first, poll the port instead of sleep 3.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Remove || true, propagate exit codes, install deps first, poll the port instead of sleep 3.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-126). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of scripts/setup-production.sh:83,98,103-106.
