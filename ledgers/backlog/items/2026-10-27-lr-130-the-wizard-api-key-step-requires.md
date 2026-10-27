---
id: 2026-10-27-lr-130-the-wizard-api-key-step-requires
title: The wizard API-key step requires a live Gemini call, sends the key in the URL, and fails on any network error with no skip option.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j001-web-setup-wizard-end-to-end
- 2026-10-27-j004-generation-worker-deploy-requires-an-llm
related: []
docs:
- setup/wizard/steps/apikeys.py
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: setup/wizard
raw_id: LR-130
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The wizard API-key step requires a live Gemini call, sends the key in the URL, and fails on any network error with no skip option.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-001, J-004
- **Aliases:** SET-026
- **Evidence:** setup/wizard/steps/apikeys.py:46-57,111-117
- **Repro:** static.
- **Fix hint:** Header auth, accept any one LLM key, downgrade validation failure to a warning with Continue anyway.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Header auth, accept any one LLM key, downgrade validation failure to a warning with Continue anyway.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-130). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of setup/wizard/steps/apikeys.py:46-57,111-117.
