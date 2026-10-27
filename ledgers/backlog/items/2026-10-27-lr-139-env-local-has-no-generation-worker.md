---
id: 2026-10-27-lr-139-env-local-has-no-generation-worker
title: env.local has no generation-worker service binding or cron and points GENERATION_WORKER_URL at the owner's production worker.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j011-local-development-loop
related: []
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: worker/config
raw_id: LR-139
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

env.local has no generation-worker service binding or cron and points GENERATION_WORKER_URL at the owner's production worker.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-011
- **Aliases:** ARCH-013
- **Evidence:** worker/wrangler.jsonc:67-117,99
- **Repro:** (static check) Open worker/wrangler.jsonc:67-117,99 and confirm the behaviour described in the summary; then exercise the matching journey (J-011) to observe it.
- **Fix hint:** Add the service binding or a local URL to env.local and document running the generation worker locally.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Add the service binding or a local URL to env.local and document running the generation worker locally.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-139). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/wrangler.jsonc:67-117,99.
