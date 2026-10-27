---
id: 2026-10-27-lr-123-dev-vars-regeneration-overwrites-the-whole
title: .dev.vars regeneration overwrites the whole file and drops earlier values, so E2E_BYPASS_SECRET regenerates and the GitHub secret goes stale.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j001-web-setup-wizard-end-to-end
- 2026-10-27-j007-re-running-setup-py-is-idempotent
- 2026-10-27-j012-dev-auth-bypass-for-local-work
related: []
docs:
- setup/cloudflare.py
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
raw_id: LR-123
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

.dev.vars regeneration overwrites the whole file and drops earlier values, so E2E_BYPASS_SECRET regenerates and the GitHub secret goes stale.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-001, J-007, J-012
- **Aliases:** SET-022
- **Evidence:** setup/cloudflare.py:504-543,659-663; setup/github.py:129-141
- **Repro:** static.
- **Fix hint:** Merge into the existing file and strip quotes when reading.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Merge into the existing file and strip quotes when reading.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-123). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of setup/cloudflare.py:504-543,659-663.
