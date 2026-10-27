---
id: 2026-10-27-lr-120-kv-d1-provisioning-is-not-idempotent
title: KV/D1 provisioning is not idempotent and has no rollback, orphaning namespaces and hiding the real create error
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j002-headless-full-bootstrap-with-python-setup
- 2026-10-27-j007-re-running-setup-py-is-idempotent
related: []
docs:
- setup/cloudflare.py
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
raw_id: LR-120
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

KV/D1 provisioning is not idempotent and has no rollback, orphaning namespaces and hiding the real create error.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-002, J-007
- **Aliases:** SET-019
- **Evidence:** setup/cloudflare.py:226-254,305-356,386-438; setup.py:119-124
- **Repro:** static. Make step D1 fail once (bad token scope), rerun, `wrangler kv namespace list` shows duplicates.
- **Fix hint:** List before create (kv namespace list, d1 list) and write ids to config immediately after each create.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

List before create (kv namespace list, d1 list) and write ids to config immediately after each create.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-120). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of setup/cloudflare.py:226-254,305-356,386-438.
