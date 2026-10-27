<!-- Generated: 2026-04-28 | Updated: 2026-04-28 -->

# LinkedInPost

## Purpose
A full-stack content creation and publishing platform for LinkedIn posts. Users browse curated news feeds, clip articles, generate AI-powered post drafts, schedule publishing, and track performance. The system has a React/Vite frontend, a Cloudflare Worker backend, a separate generation worker, and a Python setup wizard.

## Key Files

| File | Description |
|------|-------------|
| `package.json` | Root workspace — orchestrates frontend, worker, and generation-worker |
| `setup.py` | Python CLI setup wizard entry point; runs tsc --noEmit dry-run build after every invocation |
| `start.sh` | Convenience script to start frontend dev server and worker together |
| `wrangler.jsonc` | Cloudflare Worker deployment configuration |
| `.env.example` | Template for all required environment variables |
| `features.yaml` | Feature flags configuration |
| `SETUP.md` | Developer onboarding guide |
| `README.md` | Project overview and architecture summary |

## Subdirectories

| Directory | Purpose |
|-----------|---------|
| `frontend/` | React 18 + Vite + Tailwind frontend application (see `frontend/AGENTS.md`) |
| `worker/` | Cloudflare Worker backend — API routes, AI generation, persistence (see `worker/AGENTS.md`) |
| `generation-worker/` | Separate Cloudflare Worker for heavy AI content generation (see `generation-worker/AGENTS.md`) |
| `packages/` | Shared TypeScript packages: llm-core, researcher (see `packages/AGENTS.md`) |
| `setup/` | Python setup wizard for first-run configuration (see `setup/AGENTS.md`) |
| `docs/` | Architecture plans, feature specs, design documents |
| `scripts/` | Build and deployment helper scripts |
| `automations/` | Automation workflows (social, scheduling) |

## For AI Agents

### Working In This Directory
- This is a pnpm/npm workspace; run `npm install` at root to install all packages
- Frontend lives in `frontend/`, backend in `worker/`, shared code in `packages/`
- Always run `tsc --noEmit` in **both** `frontend/` and `worker/` before committing or pushing
- Never use git worktrees; work directly on `main` branch
- Never skip the pre-push protocol: pull → compile check → fix → push

### Testing Requirements
- Frontend: `cd frontend && npm run test`
- E2E: `cd frontend && npx playwright test`
- Worker: `cd worker && npm run test` (if applicable)
- Always run compile checks before merging

### Common Patterns
- Environment variables are loaded via `.env` (copy from `.env.example`)
- Cloudflare KV and D1 are the persistence layers in the worker
- AI generation uses Anthropic Claude models via the `packages/llm-core` abstraction

## Dependencies

### External
- React 18 — UI framework
- Vite — frontend build tool
- Tailwind CSS — utility-first styling
- Framer Motion — animations
- Cloudflare Workers — serverless backend runtime
- Anthropic Claude — AI content generation
- Google Sheets API — post tracking/CMS layer

<!-- MANUAL: -->


<!-- setup-ledgers:begin -->
## Orient and choose the authoritative sources

1. Read [ledgers/README.md](ledgers/README.md) and [the protocol](ledgers/PROTOCOL.md).
2. Search active and archived records before filing or working a task. Read the
   relevant document registry entries and their linked design sources. Do not
   treat old plans, progress labels, or wiki/package mirrors as current evidence.
3. Read the project's registered core/module designs and any existing engineering
   invariants before changing governed boundaries. Preserve project-specific rules.

## File, claim, implement, verify

- Every concrete gap, issue, inefficiency, boundary bypass, or investigation gets
  a backlog item immediately. Include call path, reproduction, source revision,
  measured/suspected impact, and acceptance criteria. Search and reuse first.
- Before investigating or editing an item, claim it: `status: in-progress`, agent
  identity in `owner`, exact Git branch in `branch`, isolated `worktree`, and an
  ISO `claimed_at` with timezone. Record the claim in Attempts. Publish the claim
  safely by normal merge to the agreed integration branch before dependent work;
  inspect competing claims. No blind takeover or overwriting another agent.
- Keep dated Attempts, including failed approaches, evidence, blockers, and
  handoff details. Close only with resolution and actual verification evidence.
- Feature changes update the owning design/usage docs, feature acceptance checks,
  backlog record, and any settled decision in the same change. Link instead of
  duplicating prose. If documentation needs no change, explain why in Verification.
- For journey work, read the journey and every linked active/archive ticket and
  supporting record. Link affected items with `journeys: [journey-id]`; maintain
  its actor/flow, module/file map, gaps and revision-bound acceptance evidence.
  Resolve the complete required ticket set across handoffs, respecting existing
  claims; do not fix one symptom and declare the journey complete. Unresolved
  linked tickets keep it partial/blocked/failing. Re-run whole-journey success and
  failure checks before verified; ticket closure alone is not verification, and
  related feature/review/design updates must reflect only the tested scope.
- Before work, read the latest relevant completed review in `ledgers/reviews/`
  and check its source revision. After requested reviews or meaningful work,
  append an overall/section/feature snapshot for the scope actually examined.
  Capture capabilities, architectural conflicts, priorities, and evidence limits;
  link actionable findings to backlog items and retain previous review history.
- Ideas and research use their own ledgers; promotion creates explicit links to
  features/work. A recommendation is not automatically a binding decision.
- Run `python3 tools/ledgers/manage.py index` and `check` before committing, plus
  relevant behavior checks for code changes. These checks validate structure;
  agents remain responsible for truthful evidence and performing the workflow.

## Git and collaboration

- Always edit in a dedicated branch in an isolated worktree. Reuse a suitable
  owned worktree when available. Never disturb another session's changes.
- Never run destructive Git commands or any `git stash` operation.
- Stage selected files/hunks explicitly. Commit only this session's changes.
- Integrate only by a normal merge preserving concurrent work. If unsafe or
  conflicted, retain the validated commits/worktree and report the blocker.
- Do not push or create a pull request unless the user asks. Historical docs
  requesting automatic pushes or shared-checkout edits are superseded here.
- Keep coherent changes together and unrelated changes separate. Amend small
  follow-ups into unpublished commits when appropriate; ask before rewriting
  pushed, reviewed, shared, or ambiguous history.

## No idle waiting (owner rule 2026-10-27)

Never wait for the sake of waiting. Do not run `sleep`, fixed-delay loops or "wait N
minutes" commands to pass time, and do not end a turn just to wait. Instead:
run long commands in the background and use their completion notification; meanwhile do
other useful work (claim and start the next item, review a diff, read output files, check
`git status`, `ps`, logs and test results yourself); when you must poll something the
harness cannot notify you about (CI, a deploy), poll with a concrete status command that
shows expected progress and act on what it returns. If there is truly nothing to do, say
so and finish the turn instead of sleeping. A tool that "is taking long" is a reason to
look at what it is doing, not to wait.

## Session wrap-up (autonomous or long sessions)

Before ending a session, in this order, and report each step truthfully:

1. **File every finding.** Each gap, bug, risk, doubtful claim, unfinished
   investigation, review observation and "found while doing X" becomes a backlog
   item now (search first; extend or reopen instead of duplicating), with call
   path/evidence, source revision, impact and acceptance criteria, unclaimed. A
   finding mentioned only in chat or a report is lost. Correct records you ticked
   or closed too early (untick, add a dated correction); never leave an overstated
   tick standing.
2. **Settle your claims.** Close items you finished with real verification evidence;
   release (reopen with an Attempts note) anything you claimed but did not work.
   Record owner-only decisions in the item with options and a recommendation.
3. **Merge and publish.** Merge all finished branches into the integration branch
   with normal merges, resolve generated-index conflicts by regenerating
   (`manage.py index`, then `check`), run the relevant tests, and push only when the user has
   authorized it (project instructions may grant standing authority). Verify with `git status -sb` that the branch matches its remote.
4. **Clean up what you created.** For each session-owned worktree and branch, remove
   it only after confirming its tip is an ancestor of the integration branch
   (`git merge-base --is-ancestor`) and its tree is clean; use `git worktree remove`
   and `git branch -d` (never force). Keep and list anything unmerged, dirty,
   shared, or owned by another session or still running a test; stop background
   jobs you started.
5. **Hand over.** If work remains, write a short prompt (about 25 lines) the owner can
   paste into the next agent. It must contain: (a) the repo path and the files to read
   first; (b) the user's original instructions, quoted as given (trimmed, not
   paraphrased), each marked done / partly done / not done, with whatever is left listed
   first as the next work, so nothing the user asked for is dropped; (c) the skills and
   slash commands the user invoked in the session or that are relevant to the remaining
   work (for example /boss, /finish-the-job, /loop, project skills), each with one line
   on why, so the next agent invokes them instead of missing them; (d) the working rules
   that mattered (claim on the integration branch before work or delegation, no idling
   while claimable work exists, test commands with absolute paths, merge-only git,
   index+check before pushing, honest ticks); (e) the open owner decisions; (f) the exact
   next items in priority order. Keep a current command log or handover note in the
   repo's scratch area so the next agent starts from facts, not memory.
6. **Report.** End with what is merged and verified, what is not, and what is waiting
   on the owner. Do not end on caveats that you could still resolve.

## Document upkeep

`ledgers/documents/` identifies one authoritative design per scope. Design is
intent; delivery status is in features/backlog, and dated findings are in
research. Preserve provenance, mark superseded sources with successor pointers,
and record unresolved contradictions as work. Existing project instructions
remain binding; reconcile policy conflicts explicitly. Product runtime ledgers are separate:
this workflow does not create another ticket scheduler or runtime state writer.
<!-- setup-ledgers:end -->
