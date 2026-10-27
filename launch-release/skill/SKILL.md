---
name: release-readiness
description: Get an existing product ready to hand to end customers under a feature freeze — build a launch-release/ folder (plan, journeys, findings, ledger, handover), run journey-designer / architecture-auditor / code-reviewer / executor / fixer agents, fix and live-verify until the ledger is clean. Project-agnostic, product-owner lens. Use when the owner says "get this ready to ship", "release checklist", "find all bugs before users see it", "feature freeze", "release development idea", "don't shame me in front of users".
---

# Release readiness (feature freeze → verified delivery)

Runs inside `finish-the-job` company mode (CEO + max 5 employees, run loop, QA gate, git discipline, 70% context handover, learning ledger, closing sequence). This skill adds the release-specific method. Project-agnostic; docs-manager (`docs-manager/launch-release/`) is the worked example.

## Product-owner lens (first step, always)
Look at the workspace as the business user / paying customer, not the maintainer. Write the **core promise in one sentence** and 3-5 **core value criteria** (e.g. for a code-context tool: fast, efficient, right context to the coding agent, context injected as work progresses, works in a large codebase, steers the agent to the right next target until the pieces connect). Anything not serving the promise is out of scope. Customers must never hit a broken first run, a wrong/stale answer, or a slow call.

## Rules
- **Feature freeze.** No new capability, no expansion. Make what exists work: wire it, fix it, verify it. A needed new capability goes to the ledger's *Frozen* section with the smallest in-scope alternative.
- **Reuse, don't refactor, don't delete.** Integrate into one unified flow along the existing plan; extend existing paths; one way per thing (D306 where it applies); no mass deletions or big refactors. Use as much existing code as possible.
- **Ground in docs and research.** Read the architecture docs / ADD / decision log first and audit conformance against them; use web research for external behavior, standards, and known failure modes (cite). Confusion → read docs, then research, then decide and record. Do not ask the owner what the docs answer.
- **One folder, one ledger.** All in `launch-release/` inside the product repo so a future agent resumes from the handover alone. The owner should never have to repeat these instructions: the handover names this skill.

## Folder (create first)
`launch-release/README.md` (handover: goal, core promise, freeze, skills to use, how to continue, layout, current state/next step) · `PLAN.md` (acceptance A1..An, roles, finding format, rules) · `LEDGER.md` (the **final release delivery checklist**: every issue, gap, mis-implementation, bad design, improvement-before-ship, each with Sev/Area/Evidence/Repro/Status/Verified, plus the verification steps that prove delivery; Frozen; Verification log) · `journeys/JOURNEYS.md` · `findings/{ARCH-AUDIT,CODE-REVIEW,EXEC-RESULTS}.md` · `fixes/` · `skill/` (copy of this skill and finish-the-job).
Finding format: `ID` · `Sev` P0 data loss/crash/wrong context served, P1 core flow broken or too slow, P2 degraded with workaround, P3 polish · `Area` · `Evidence` file:line or command+output · `Repro` · `Fix hint` · `Status` open/in-progress/fixed/accepted/frozen · `Verified` command→result.

## Employees (max 5 at once; each in its own git worktree; each commits and pushes its own verified work)
1. **Journey designer** (read-only) → every customer/agent journey: happy + bad flows, first-run/setup/install, upgrade, misconfiguration, large-project use, recovery. Each: ID, persona, preconditions, copy-pasteable steps, objective pass/fail check, priority, `CORE` tag, external-service flag. 60+ for a CLI/service product. Written to `journeys/JOURNEYS.md`.
2. **Architecture auditor** (read-only) → for each journey and each architecture doc section: is it implemented as documented? conformance table + findings; classify FIX-NOW / ACCEPT / FROZEN; check response shapes against the design examples, security, concurrency, performance budgets, packaging, setup/config correctness.
3. **Code reviewer** (read-only, small experiments in temp repos) → correctness, data loss, security, perf at scale, races, error handling, platform issues. Runs `/code-review` style passes; skips what is already fixed.
(1-3 in parallel.)
4. **Executor** (after 1) → actually runs every journey for real: each tool/command one by one, bad flows included, destructive ones in temp repos. Always includes **a fresh toy project** (e.g. a Tic-Tac-Toe app built from scratch with the product installed exactly as a customer would) to test setup/onboarding and the guidance loop end to end: does the product give the right context, inject it as work proceeds, and steer the coding agent to the right next target until the pieces connect and the app works? Also measures the core promise on the real large project (latency p50/p95, response size, top-result quality on 10 real queries). Records pass/fail + output in EXEC-RESULTS and files every failure into the ledger.
5. **Fixer** (continuous, after 2-4; split into disjoint file ownership if more than one) → fixes ledger items by root cause, with a test each, targeted tests only; notes in `fixes/`; re-runs the failing journey to close the item.
CEO: merges findings into LEDGER (dedupe, assign Sev), assigns batches, reads short reports, spot-verifies, runs the full suite once at the end. Handover at 70% context as defined in `finish-the-job`.

## Loop (run until done, same-day deadline mindset)
journeys → audit/review → execute → ledger → fix batch → re-execute failed journeys → repeat until: no open P0/P1; P2 fixed or accepted with a reason; core-promise measurements meet budget; README quickstart run verbatim on a clean machine/repo passes; toy-project journey passes end to end; independent QA gate passes; full suite green; everything merged and pushed; consumer pointer bumped; worktrees/branches cleaned; docs updated after the retro.

## Watch-outs (learned)
- Slow machine = a bug: check `uptime`, duplicate background loops, per-call git spawn counts before blaming the product.
- Never run a full slow suite repeatedly; targeted tests while iterating, full once at the end.
- Verify every claim by running it; a finding without a repro is a hypothesis, label it so.
- Don't touch the live consumer's data (wiki project, release tier) except read-only checks, unless the owner said so.
- Setup is part of the product: a correct code path behind a broken install/config/first run still ships a broken product.
