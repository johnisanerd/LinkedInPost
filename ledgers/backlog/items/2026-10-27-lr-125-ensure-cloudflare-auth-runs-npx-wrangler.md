---
id: 2026-10-27-lr-125-ensure-cloudflare-auth-runs-npx-wrangler
title: ensure_cloudflare_auth runs npx wrangler before dependencies are installed, and the root pins wrangler 3.x while the workers need 4.x.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j001-web-setup-wizard-end-to-end
- 2026-10-27-j002-headless-full-bootstrap-with-python-setup
related: []
docs:
- setup.py
- setup/cloudflare.py
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: setup/cli
raw_id: LR-125
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

ensure_cloudflare_auth runs npx wrangler before dependencies are installed, and the root pins wrangler 3.x while the workers need 4.x.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-001, J-002
- **Aliases:** SET-027
- **Evidence:** setup.py:100-103; setup/cloudflare.py:43-49
- **Repro:** static.
- **Fix hint:** Install deps first, use npx --no-install wrangler from worker/, align the root devDependency.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Install deps first, use npx --no-install wrangler from worker/, align the root devDependency.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-125). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of setup.py:100-103.
