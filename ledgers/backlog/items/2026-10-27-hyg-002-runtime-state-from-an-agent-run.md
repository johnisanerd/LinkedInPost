---
id: 2026-10-27-hyg-002-runtime-state-from-an-agent-run
title: Runtime state from an agent run is tracked in git
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related: []
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: hygiene
severity: P1
area: state/exec
raw_id: HYG-002
source_file: docs/launch-readiness/findings/HYGIENE.md
---

## Problem

Runtime state from an agent run is tracked in git. these files change on every run, can contain run details and costs, and may include text from prompts. They do not belong in version control.

## Evidence and reproduction

- **Journeys:** none
- **Confidence:** confirmed-by-reading
- **Evidence:** `git ls-files state` returns 14 files: state/exec/events.jsonl, state/exec/cost_meter.jsonl, state/exec/campaign.json, state/exec/ready_queue.json, state/exec/checkpoints/<run-id>/*.json (including PRCreated.json and Committed.json), and state/exec/scratch/<run-id>.md.
- **Why it matters:** these files change on every run, can contain run details and costs, and may include text from prompts. They do not belong in version control.
- **Repro:** `git ls-files state` and read events.jsonl for anything that looks like a credential before deciding what to keep.
- **Fix hint:** `git rm -r --cached state/`, add `state/` to .gitignore. First check the files for secrets or personal data; if any are found, rotate them and record it.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

`git rm -r --cached state/`, add `state/` to .gitignore. First check the files for secrets or personal data; if any are found, rotate them and record it.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/HYGIENE.md (HYG-002). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: checked by reading the cited file and git ls-files.
