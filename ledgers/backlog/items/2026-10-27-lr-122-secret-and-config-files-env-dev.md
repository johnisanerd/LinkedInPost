---
id: 2026-10-27-lr-122-secret-and-config-files-env-dev
title: Secret and config files (.env, .dev.vars) are written with default permissions rather than 0600
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j001-web-setup-wizard-end-to-end
- 2026-10-27-j002-headless-full-bootstrap-with-python-setup
related: []
docs:
- setup/cloudflare.py
- setup/github.py
- setup.py
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: setup/cli
raw_id: LR-122
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Secret and config files (.env, .dev.vars) are written with default permissions rather than 0600.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-001, J-002
- **Aliases:** SET-021
- **Evidence:** setup/cloudflare.py:511,543,663; setup/github.py:141
- **Repro:** static. `python setup.py --cloudflare; ls -l worker/.dev.vars`.
- **Fix hint:** Shared write_secret_file helper using os.open with 0o600 and chmod existing files.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Shared write_secret_file helper using os.open with 0o600 and chmod existing files.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-122). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of setup/cloudflare.py:511,543,663.
