---
id: 2026-10-27-lr-022-csv-campaign-import-splits-on-commas
title: CSV campaign import splits on commas and newlines, so quoted post bodies are truncated or misaligned before they are written to the sheet.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j107-bulk-import-from-a-file-json
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
area: frontend/campaign
raw_id: LR-022
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

CSV campaign import splits on commas and newlines, so quoted post bodies are truncated or misaligned before they are written to the sheet.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-107
- **Aliases:** FEB-007
- **Evidence:** frontend/src/features/campaign/CampaignPage.tsx:497-515
- **Repro:** upload a CSV whose body cell is `"Hello, world"`; preview shows `Hello` as body. Static reasoning.
- **Fix hint:** Use a real CSV parser with quoted-field support or require the JSON path.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Use a real CSV parser with quoted-field support or require the JSON path.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-022). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/features/campaign/CampaignPage.tsx:497-515.
