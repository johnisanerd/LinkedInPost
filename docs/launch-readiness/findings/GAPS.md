# Review gaps and process issues

Things this review did not do, or decisions it left open. Read-only; nothing executed.

### GAP-001 P1 process/review - No executor pass: nothing was run
- **Gap:** Nothing was run. launch-release/findings/EXEC-RESULTS.md does not exist yet, and every LR item is read-only (confirmed-by-reading or hypothesis).
- **Action:** Run the P0 and P1 journeys on a fresh clone and record the results in the Verification log in LEDGER.md.
- **Owner:** 

### GAP-002 P1 process/review - generation-worker/src missed by the existing-review reconciler
- **Gap:** generation-worker/src was not covered by the existing-review reconciler (its grep timed out). It was covered only by the gen-pkg reviewer (findings/raw/gen-pkg.md).
- **Action:** Do a second review pass over generation-worker/src.
- **Owner:** 

### GAP-003 P2 process/review - Test coverage was not mapped
- **Gap:** Tests under frontend/src, the worker/src *.test.ts files, tests/ and tests-e2e/ were not read for what they claim to cover.
- **Action:** Map each journey's pass check to an existing test or mark it untested.
- **Owner:** 

### GAP-004 P3 process/review - video-pipeline/ is out of scope
- **Gap:** video-pipeline/ is a separate product with vendored submodules (.gitmodules lists ViMax, MoneyPrinterTurbo, youtube-automation-agent, remotion) and its own ledger (video-pipeline/direction/skills/LEDGER.yaml) and backlog (docs/plans/video-pipeline/BACKLOG.md). It was not reviewed.
- **Action:** The owner decides whether it gets its own launch-release.
- **Owner:** 

### GAP-005 P3 process/review - automations/, docs/research and .copilot-tracking not reviewed
- **Gap:** automations/ (youtube_poller.py only), docs/research/ and .copilot-tracking/ were only glanced at or not reviewed.
- **Action:** Owner decides whether any of them ships to users; review if so.
- **Owner:** 

### GAP-006 P2 process/review - Pre-push compile check not run
- **Gap:** The AGENTS.md pre-push check (tsc --noEmit in frontend/ and worker/) was not run. This merge is docs-only: no TypeScript changed except a comment-path edit in worker/src/engine/workflows/definitions/__tests__/postTypesPlaybook.test.ts.
- **Action:** Run tsc --noEmit in frontend/ and worker/ before the next code change is pushed.
- **Owner:** 

### GAP-007 P3 process/review - Repo rule conflict: work on main, no worktrees
- **Gap:** AGENTS.md says to work directly on main and never use git worktrees. This review used the branch launch-readiness-review at the owner's request, and it is being merged into main.
- **Action:** Decision needed: keep or update that rule.
- **Owner:** 

### GAP-008 P3 process/review - Template source repo named 'setup' not found
- **Gap:** The owner named a repository 'setup'. No local repo of that name exists in ~/Documents/GitHub. The ledger template was taken from trade/docs-manager/launch-release and Developer-Tools/skills/release-readiness.
- **Action:** Owner confirms the source repo.
- **Owner:** 

### GAP-009 P3 process/review - GitHub connectivity unreliable
- **Gap:** GitHub connectivity was unreliable during this session (git fetch and gh timed out). Whether the branch matches origin is unknown.
- **Action:** Re-check origin sync before any push.
- **Owner:** 

### GAP-010 P2 process/review - Existing-review rows marked unverified were never checked
- **Gap:** Rows marked unverified in the cons/ audits, USE-CASES.md and the acceptance criteria were never checked in code. See the investigate rows in EXISTING-REVIEWS.md.
- **Action:** Check them after execution, or accept the unverified claims as stale documentation.
- **Owner:** 

### GAP-011 P2 process/review - Journey pass checks are derived by reading
- **Gap:** Journey pass checks were derived by reading the code, not executed. See GAP-001.
- **Action:** Execute the P0 and P1 journeys; see GAP-001.
- **Owner:** 

### GAP-012 P3 process/review - Raw IDs aliased by script; cross-references may be incomplete
- **Gap:** The 224 raw IDs are aliased into LR items by a coordinator script; cross-references between raw reviewers may still be incomplete.
- **Action:** Spot-check duplicates after execution.
- **Owner:** 
