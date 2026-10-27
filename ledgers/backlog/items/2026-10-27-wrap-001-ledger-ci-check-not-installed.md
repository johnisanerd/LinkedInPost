---
id: 2026-10-27-wrap-001-ledger-ci-check-not-installed
title: The ledger CI check from the setup scaffold is not installed, so ledger validity is only checked by hand
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
type: process
raw_id: WRAP-001
source_file: docs/launch-readiness/findings/GAPS.md (wrap-up)
---

## Problem

The setup scaffold ships .github/workflows/ledgers.yml (install with --with-ci). This repository installed the scaffold without it, so nothing runs `manage.py check` on pull requests or pushes to main.

## Evidence and reproduction

`python3 /Users/pratyush.mishra/setup/tools/install.py <repo>` (preview) lists the workflow only with `--with-ci`. `ls .github/workflows` shows no ledgers.yml.

## Acceptance criteria

- The workflow runs `python3 tools/ledgers/manage.py check` on push and pull request, and it passes on main.

## Plan

Owner decision: install the workflow (`--with-ci --apply`) and check it passes on a branch before relying on it.

## Attempts

- 2026-10-27 — Filed during wrap-up. Not installed in this session; a workflow file is an owner-visible change.

## Verification

Pending. Not performed.

