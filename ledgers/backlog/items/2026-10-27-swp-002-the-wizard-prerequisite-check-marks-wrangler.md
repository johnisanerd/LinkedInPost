---
id: 2026-10-27-swp-002-the-wizard-prerequisite-check-marks-wrangler
title: The wizard prerequisite check marks Wrangler as found when only npx exists, then tells the user to install it globally.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j001-web-setup-wizard-end-to-end
- 2026-10-27-j002-headless-full-bootstrap-with-python-setup
related:
- 2026-10-27-lr-125-ensure-cloudflare-auth-runs-npx-wrangler
docs:
- setup.md
- setup/wizard/steps/prereqs.py
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: investigation
severity: P3
area: setup/wizard
raw_id: SWP-002
source_file: docs/launch-readiness/findings/SWEEP.md
---

## Problem

The wizard prerequisite check marks Wrangler as found when only npx exists, then tells the user to install it globally. The check reports Wrangler present on any machine with Node, so a missing or wrong-major wrangler is only found later during deploy (see LR-125).

## Evidence and reproduction

- **Source:** docs/launch-readiness/findings/raw/setup.md SET-033 (setup.md:333, "prereq check passes if only npx exists")
- **Journeys:** J-001, J-002
- **Confidence:** confirmed-by-reading
- **Evidence:** setup/wizard/steps/prereqs.py:40-41 (`shutil.which('wrangler') or shutil.which('npx')`)
- **Why it matters:** The check reports Wrangler present on any machine with Node, so a missing or wrong-major wrangler is only found later during deploy (see LR-125).
- **Repro or check:** On a machine with npx and no wrangler on PATH, open the wizard prerequisites step and see Wrangler CLI marked ok with found set to the npx path.
- **Fix hint:** Report the real version via `npx --no-install wrangler --version` run from worker/, and require major 4.

## Acceptance criteria

- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Report the real version via `npx --no-install wrangler --version` run from worker/, and require major 4.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/SWEEP.md (SWP-002). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: setup/wizard/steps/prereqs.py:40-41.
