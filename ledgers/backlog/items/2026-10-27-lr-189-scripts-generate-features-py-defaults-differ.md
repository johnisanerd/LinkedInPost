---
id: 2026-10-27-lr-189-scripts-generate-features-py-defaults-differ
title: scripts/generate_features.py defaults differ from features.yaml, so a missing yaml silently turns flags off, and videoEpisodes contradicts it.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j139-feature-flags-after-editing-features-yaml
related: []
docs:
- scripts/generate_features.py
- features.yaml
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P3
area: worker/config
raw_id: LR-189
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

scripts/generate_features.py defaults differ from features.yaml, so a missing yaml silently turns flags off, and videoEpisodes contradicts it.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-139
- **Aliases:** ARCH-018
- **Evidence:** scripts/generate_features.py:23-32; features.yaml:9-24
- **Repro:** (static check) Open scripts/generate_features.py:23-32 and confirm the behaviour described in the summary; then exercise the matching journey (J-139) to observe it.
- **Fix hint:** Align defaults with the yaml and set videoEpisodes per mode.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Align defaults with the yaml and set videoEpisodes per mode.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-189). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of scripts/generate_features.py:23-32.
