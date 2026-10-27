---
id: 2026-10-27-lr-018-the-root-wrangler-jsonc-reuses-the
title: The root wrangler.jsonc reuses the API worker name, has no main, and uploads frontend source as assets, so a root deploy overwrites the API.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j002-headless-full-bootstrap-with-python-setup
- 2026-10-27-j003-fresh-cloudflare-account-against-the-committed
related: []
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: deploy/config
raw_id: LR-018
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The root wrangler.jsonc reuses the API worker name, has no main, and uploads frontend source as assets, so a root deploy overwrites the API.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-002, J-003
- **Aliases:** ARCH-009
- **Evidence:** wrangler.jsonc:3-10
- **Repro:** (static check) Open wrangler.jsonc:3-10 and confirm the behaviour described in the summary; then exercise the matching journey (J-002, J-003) to observe it.
- **Fix hint:** Point assets at frontend/dist, add .assetsignore, and merge into worker/wrangler.jsonc or give the root file a distinct name.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Point assets at frontend/dist, add .assetsignore, and merge into worker/wrangler.jsonc or give the root file a distinct name.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-018). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of wrangler.jsonc:3-10.
