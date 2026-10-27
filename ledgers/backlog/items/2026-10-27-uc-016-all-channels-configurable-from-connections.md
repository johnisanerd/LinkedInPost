---
id: 2026-10-27-uc-016-all-channels-configurable-from-connections
title: All channels configurable from /connections
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-163-use-cases-md-and-related-docs
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: wiring-gap
severity: P2
area: frontend/channels
raw_id: UC-016
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
---

## Problem

All channels configurable from /connections.

## Evidence and reproduction

- **Source:** launch-release/findings/raw/existing-reviews.md section 2, row U-J6
- **Alias:** U-J6
- **Original tag:** ✅ (no severity given, defaulted to P2)
- **Current status:** partial
- **Evidence:** ConnectionsPage.tsx; Telegram/WhatsApp *recipient* config still in Settings drawer (DashboardSettingsDrawer.tsx:1788,1939)
- **Covered by:** LR-163

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (UC-016). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: partial; still open in code (ConnectionsPage.tsx; Telegram/WhatsApp *recipient* config still in Settings drawer (DashboardSettingsDrawer.tsx:1788,1939)); covered by LR-163.
