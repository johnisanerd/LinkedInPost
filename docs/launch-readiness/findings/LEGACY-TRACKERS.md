# Items still live in the legacy trackers

Items from launch-release/ledgers-legacy/*.md that are not already in EXISTING-REVIEWS.md. MCP-PROGRESS.md has nothing pending (all 24 items done). Read-only; nothing executed.

### IDEA-001 P3 setup/cli - setup/cli.py is an inert scaffold: parse_args() runs but nothing executes
- **Source:** launch-release/ledgers-legacy/MCP-TEST-IDEAS.md (bootstrap idempotency test note)
- **Detail:** setup/cli.py is 40 lines: parse_args() and a __main__ call, no main action. Flags (including --web) are accepted and do nothing. The real entry is setup.py.
- **Action:** Delete the dead CLI or make it fail with a pointer to setup.py, so nobody thinks it configures anything.

### IDEA-002 P2 setup/tests - Wizard deploy tests mock subprocess and kill 0% of mutants
- **Source:** launch-release/ledgers-legacy/MCP-TEST-IDEAS.md (mutation_tester on setup/wizard/steps/deploy.py)
- **Detail:** The mutation run reported a 0% kill rate: the tests are decorative.
- **Action:** Add assertions on the deploy step's real outputs, or treat setup tests as non-evidence for the setup P0 items.

### IDEA-003 P3 setup/tests - setup/wizard/tests fixtures leak Flask state when run with tests/
- **Source:** launch-release/ledgers-legacy/MCP-TEST-IDEAS.md (infrastructure bugs)
- **Detail:** Run together with tests/, 10+ tests fail in a cascade; run alone, all 18 pass. The note records only a workaround.
- **Action:** Isolate the Flask client fixture, or document running the suites separately.

### IDEA-004 P3 tooling - mutation_tester.py blocks for 300s+ (project-root detection, full-repo copy)
- **Source:** launch-release/ledgers-legacy/MCP-TEST-IDEAS.md (mutation_tester systemic issues)
- **Detail:** Run on setup/wizard/steps/mode.py it copied the whole repo to a temp dir and timed out.
- **Action:** Developer tooling; not shipped to users.

### IDEA-005 P3 setup/google - parse_service_account_json exits the process via fail()/sys.exit(1)
- **Source:** launch-release/ledgers-legacy/MCP-TEST-IDEAS.md (DESIGN ISSUE note)
- **Detail:** The function cannot be unit-tested without mocking sys.exit, and a library helper kills the wizard process on bad input.
- **Action:** Raise an exception from the helper and let the caller decide.

### IDEA-006 P2 worker/tests - Worker auth, D1 bad-parameter and missing-LLM-credential tests were never run
- **Source:** launch-release/ledgers-legacy/MCP-TEST-IDEAS.md (New ideas - worker/backend coverage)
- **Detail:** Three ideas are ticked [x] but their own text says they were blocked by a gateway 403 (marked with a cross). They have no result.
- **Action:** Write them as real tests: worker auth middleware, D1 queries with invalid parameters, llm client with missing credentials.

### IDEA-007 P2 generation-worker/tests - Image pipeline tests with empty and over-2000-character text were never run
- **Source:** launch-release/ledgers-legacy/MCP-TEST-IDEAS.md (New ideas - worker/backend coverage)
- **Detail:** Ticked [x] but blocked by a gateway 403; no result.
- **Action:** Test the generation-worker image pipeline with empty variant text and text over 2000 characters.

### IDEA-008 P2 frontend/tests - Frontend bootstrap, network-timeout and empty-feed tests were never run
- **Source:** launch-release/ledgers-legacy/MCP-TEST-IDEAS.md (New ideas - frontend coverage)
- **Detail:** Ticked [x] but blocked by a gateway 403. They cover App.tsx with a missing backend URL, backendApi.ts on network timeout and the feed with an empty response. The first relates to INV-001.
- **Action:** Write the three tests.

### IDEA-009 P2 packages/tests - llm-core missing model key and researcher rate-limit tests were never run
- **Source:** launch-release/ledgers-legacy/MCP-TEST-IDEAS.md (New ideas - packages coverage)
- **Detail:** Ticked [x] but blocked by a gateway 403; no result.
- **Action:** Test packages/llm-core provider config with a missing model key and packages/researcher with a rate-limited response.

### IDEA-010 P3 setup/cli - Expired-token credentials file and empty-argument tests bounced
- **Source:** launch-release/ledgers-legacy/MCP-TEST-IDEAS.md (Bounced section)
- **Detail:** Both marked [!] as infrastructure unavailable. setup/cli.py does nothing (IDEA-001), so the tests have no target.
- **Action:** No action.

### IDEA-011 P2 deploy/tooling - bin/journey-health did not complete and is not portable
- **Source:** launch-release/ledgers-legacy/MCP-TEST-IDEAS.md (bin/journey-health runs bounced: J1 ran 5/6 before timeout; kill-test not done)
- **Detail:** The script hard-codes LP_ROOT=/home/openclaw/workspaces/linkedin-post and checks ports through /proc/net/tcp, so it is Linux-only and cannot run on a Mac checkout as written. Neither the healthy-stack run nor the dead-stack run finished.
- **Action:** Make LP_ROOT relative to the script and use a portable port check; then use it as part of GAP-001's executor pass.

### IDEA-012 P3 worker/audit - No audit trail of template, variant and image per published post
- **Source:** launch-release/ledgers-legacy/ideas.md (Stage 8: keep an audit trail)
- **Detail:** ideas.md asks for an audit trail of which template, variant and image were used. A grep for audit trail / auditLog in worker/src found nothing.
- **Action:** Decide if the owner wants this at launch; if yes record post type and variant index at publish.

### IDEA-013 P3 docs/ideas - ideas.md content-pipeline operating model (8 stages, few-shot library, router rubric)
- **Source:** launch-release/ledgers-legacy/ideas.md
- **Detail:** A pasted design spec, not a tracker: intake brief, optional research, post-type routing, draft, variants, automated review, human approval, visuals, publish. The engine already routes post types and returns variants with rationale (see AC-004 in EXISTING-REVIEWS.md).
- **Action:** Design guidance for later quality work.

### IDEA-014 P3 docs/feed-report - FEED report suggestion: let ClipsDock assign a clip to several posts
- **Source:** launch-release/ledgers-legacy/FEED_EXPLORATION_REPORT.md (Next Steps for Implementation, item 6)
- **Detail:** The report says ClipsDock assigns a single post id and could expand to multiple posts. The rest of the report is a descriptive snapshot (see FR-001 and FR-002 in EXISTING-REVIEWS.md).
- **Action:** Post-launch feature.
