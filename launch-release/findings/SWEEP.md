# Sweep: doubt statements not individually tracked

Method: grep for hypothesis, not confirmed, unverified, not checked, not tested, not run, might, may be, could be, unclear, suspect, appears, looks like, todo, fixme over the raw reviewer files, ARCH-AUDIT, JOURNEY-DELTA, TEST-COVERAGE and AUTOMATIONS (CODE-REVIEW.md does not exist). 100 marker lines were found; 4 added doubts without a marker word were also checked. Status lives in status.json, not here.

### SWP-001 P3 setup/deps - requirements.txt pins google-generativeai==0.8.2, a deprecated package that nothing in the repo imports.
- **Source:** launch-release/findings/raw/setup.md SET-033 (the "hypothesis on protobuf conflicts" clause, setup.md:333)
- **Journeys:** J-001, J-011
- **Confidence:** confirmed-by-reading
- **Evidence:** requirements.txt:6; grep for generativeai over automations/, scripts/, setup/, setup.py, frontend/server finds only requirements.txt
- **Why it matters:** An unused pinned package can make pip fail or downgrade protobuf against google-api-python-client>=2.157, breaking the first-run install for no benefit.
- **Repro or check:** `grep -rn generativeai --include=*.py .` (expect no hit outside node_modules), then in a clean venv `pip install -r requirements.txt && pip check`.
- **Fix hint:** Delete the google-generativeai line; if pip check passes without it nothing else is needed.

### SWP-002 P3 setup/wizard - The wizard prerequisite check marks Wrangler as found when only npx exists, then tells the user to install it globally.
- **Source:** launch-release/findings/raw/setup.md SET-033 (setup.md:333, "prereq check passes if only npx exists")
- **Journeys:** J-001, J-002
- **Confidence:** confirmed-by-reading
- **Evidence:** setup/wizard/steps/prereqs.py:40-41 (`shutil.which('wrangler') or shutil.which('npx')`)
- **Why it matters:** The check reports Wrangler present on any machine with Node, so a missing or wrong-major wrangler is only found later during deploy (see LR-125).
- **Repro or check:** On a machine with npx and no wrangler on PATH, open the wizard prerequisites step and see Wrangler CLI marked ok with found set to the npx path.
- **Fix hint:** Report the real version via `npx --no-install wrangler --version` run from worker/, and require major 4.

### INV-021 P2 setup/wizard - Does the wizard Node 18 floor accept a Node version that the pinned wrangler 4 cannot run on?
- **Source:** launch-release/findings/raw/setup.md SET-033 (setup.md:333, "Node 18 is below what wrangler 4 / CI (Node 24) assume (hypothesis)")
- **Journeys:** J-001, J-002
- **Confidence:** hypothesis
- **Evidence:** setup/wizard/steps/prereqs.py:22-29 (Node 18+); .github/workflows/deploy-workers.yml:26,63 and deploy-pages.yml:33 (Node 24); worker/package.json wrangler ^4.92.0
- **Why it matters:** If wrangler 4.92 needs Node 20 or newer, a user on Node 18 passes the prerequisite step and then fails at deploy.
- **Repro or check:** `npm view wrangler@^4.92.0 engines.node` and `npm view wrangler@^4.78.0 engines.node`; compare with the floor in prereqs.py:22-29.
- **Fix hint:** decide: raise the floor in prereqs.py (and SETUP.md) to the engines value, or confirm 18 is enough and drop the question.

### INV-022 P3 worker/image-gen - Is the Veo :generateVideo URL a real Gemini endpoint, or does every Veo video request fail?
- **Source:** launch-release/findings/raw/worker-b.md WKB-027 (worker-b.md:270, "Veo uses a :generateVideo path that is not a documented Gemini endpoint (hypothesis, low impact)")
- **Journeys:** J-068
- **Confidence:** hypothesis
- **Evidence:** worker/src/image-gen/providers/veo.ts:11 and generation-worker/src/image-gen/providers/veo.ts:11
- **Why it matters:** If the path is invalid, video generation always returns 404 after the user selects it, in two copies of the provider.
- **Repro or check:** Compare the path with the current Gemini API Veo docs (the documented call is a long-running predict on the model), or run one request with a real key and read the HTTP status; also grep the UI for a path that offers video (`grep -rn veo frontend/src worker/src`).
- **Fix hint:** decide: fix the path in both copies, or remove Veo from the model catalog if video is out of scope for launch.

### INV-023 P3 setup/wizard - Is gemini-2.0-flash, the model the wizard uses to validate the Gemini key, still served for new keys?
- **Source:** launch-release/findings/raw/setup.md SET-026 (setup.md:263, "Model name validity is a hypothesis")
- **Journeys:** J-001, J-004
- **Confidence:** hypothesis
- **Evidence:** setup/wizard/steps/apikeys.py:51
- **Why it matters:** Any non-200 blocks the whole wizard (LR-130); a retired model name would block every new user with a valid key.
- **Repro or check:** `curl -s -o /dev/null -w '%{http_code}' -H 'x-goog-api-key: $KEY' -H 'content-type: application/json' -d '{"contents":[{"parts":[{"text":"hi"}]}]}' https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent` with a fresh key; also run ListModels and look for the id. Related: LR-193.
- **Fix hint:** decide: switch validation to the ListModels call (no model name), or update the id to a current model.

### INV-024 P2 worker/automations - Does a standard LinkedIn app get access to /v2/webhookSubscriptions and MEMBER_TO_MEMBER messages, or is LinkedIn automation dead for everyone?
- **Source:** launch-release/findings/raw/worker-b.md WKB-031 (worker-b.md:310, "not available to standard LinkedIn apps (hypothesis)")
- **Journeys:** J-114, J-116
- **Confidence:** hypothesis
- **Evidence:** worker/src/automations/platforms/linkedin.ts:13 and :127
- **Why it matters:** If the products need a LinkedIn partner program, the LinkedIn automation toggle can never work and should be hidden at launch (LR-137 only covers Gmail and credentials).
- **Repro or check:** Read the current LinkedIn developer docs for the Webhooks and Messaging products and the app's Products tab; or call `POST https://api.linkedin.com/v2/webhookSubscriptions` with the owner token and read the 403 or 404 body.
- **Fix hint:** decide: hide LinkedIn from the automations UI, or document the required LinkedIn product.

## Coverage table

Verdicts: tracked as ID, new (SWP or INV), or rejected with the reason. The existing-reviews.md rows are tracked individually as CONS, UC, SP and AC items.

| Marker source (file:line) | Verdict | Reason |
|---|---|---|
| launch-release/findings/raw/existing-reviews.md:4 | rejected | status-key legend text, not a finding |
| launch-release/findings/raw/existing-reviews.md:18 | tracked as CONS-007 | Row C01-7 marked "unverified"; ledger status investigate. |
| launch-release/findings/raw/existing-reviews.md:19 | tracked as CONS-008 | Row C01-8 marked "unverified"; ledger status investigate. |
| launch-release/findings/raw/existing-reviews.md:31 | rejected | "disappears" contains the marker; row is tracked as CONS-020 (open, covered by LR-095) |
| launch-release/findings/raw/existing-reviews.md:50 | tracked as CONS-039 | Row C03-11 marked "not checked"; ledger status investigate. |
| launch-release/findings/raw/existing-reviews.md:57 | tracked as CONS-046 | Row C04-7 marked "unverified"; ledger status investigate. |
| launch-release/findings/raw/existing-reviews.md:63 | tracked as CONS-052 | Row C04-13 marked "unverified"; ledger status investigate. |
| launch-release/findings/raw/existing-reviews.md:65 | tracked as CONS-054 | Row C04-15 marked "unverified"; ledger status investigate. |
| launch-release/findings/raw/existing-reviews.md:68 | tracked as CONS-057 | Row C04-18 marked "unverified"; ledger status investigate. |
| launch-release/findings/raw/existing-reviews.md:73 | tracked as CONS-062 | Row C05-5 marked "unverified"; ledger status investigate. |
| launch-release/findings/raw/existing-reviews.md:74 | tracked as CONS-063 | Row C05-6 marked "unverified"; ledger status investigate. |
| launch-release/findings/raw/existing-reviews.md:76 | tracked as CONS-065 | Row C05-8 marked "unverified"; ledger status investigate. |
| launch-release/findings/raw/existing-reviews.md:80 | tracked as CONS-069 | Row C05-12 marked "unverified"; ledger status investigate. |
| launch-release/findings/raw/existing-reviews.md:87 | tracked as CONS-076 | Row C06-6 marked "unverified"; ledger status investigate. |
| launch-release/findings/raw/existing-reviews.md:88 | tracked as CONS-077 | Row C06-7 marked "unverified"; ledger status investigate. |
| launch-release/findings/raw/existing-reviews.md:103 | tracked as CONS-092 | Row C08-3 marked "not confirmed"; ledger status investigate. |
| launch-release/findings/raw/existing-reviews.md:104 | tracked as CONS-093 | Row C08-4 marked "not confirmed"; ledger status investigate. |
| launch-release/findings/raw/existing-reviews.md:111 | tracked as CONS-100 | Row C08-11 marked "unverified"; ledger status investigate. |
| launch-release/findings/raw/existing-reviews.md:128 | tracked as CONS-117 | Row C09-16 marked "unverified"; ledger status investigate. |
| launch-release/findings/raw/existing-reviews.md:132 | tracked as CONS-121 | Row C10-3 marked "unverified"; ledger status investigate. |
| launch-release/findings/raw/existing-reviews.md:136 | tracked as CONS-125 | Row C10-7 marked "unverified"; ledger status investigate. |
| launch-release/findings/raw/existing-reviews.md:169 | tracked as UC-005 | Row U-J1.1 marked "unverified"; ledger status investigate. |
| launch-release/findings/raw/existing-reviews.md:170 | tracked as UC-006 | Row U-J1.2 marked "unverified"; ledger status investigate. |
| launch-release/findings/raw/existing-reviews.md:171 | tracked as UC-007 | Row U-J1.3 marked "unverified"; ledger status investigate. |
| launch-release/findings/raw/existing-reviews.md:172 | tracked as UC-008 | Row U-J1.4 marked "not confirmed"; ledger status investigate. |
| launch-release/findings/raw/existing-reviews.md:178 | tracked as UC-014 | Row U-J1.10 marked "unverified"; ledger status investigate. |
| launch-release/findings/raw/existing-reviews.md:179 | tracked as UC-015 | Row U-J2-5 marked "unverified"; ledger status investigate. |
| launch-release/findings/raw/existing-reviews.md:181 | tracked as UC-017 | Row U-J7 marked "unverified"; ledger status investigate. |
| launch-release/findings/raw/existing-reviews.md:183 | tracked as UC-019 | Row U-J10 marked "unverified"; ledger status investigate. |
| launch-release/findings/raw/existing-reviews.md:187 | tracked as UC-023 | Row U-E2E marked "not run"; ledger status open. |
| launch-release/findings/raw/existing-reviews.md:209 | tracked as SP-009 | Row P2-T8 marked "not run"; ledger status investigate. |
| launch-release/findings/raw/existing-reviews.md:221 | tracked as AC-007 | Row D3-7 marked "unverified"; ledger status investigate. |
| launch-release/findings/raw/existing-reviews.md:222 | tracked as AC-008 | Row D2-1 marked "unverified"; ledger status investigate. |
| launch-release/findings/raw/existing-reviews.md:224 | tracked as AC-010 | Row D2-3 marked "unverified"; ledger status investigate. |
| launch-release/findings/raw/existing-reviews.md:226 | tracked as AC-012 | Row D2-5 marked "not run"; ledger status investigate. |
| launch-release/findings/raw/existing-reviews.md:229 | tracked as AC-015 | Row DE-3 marked "unverified"; ledger status investigate. |
| launch-release/findings/raw/existing-reviews.md:230 | tracked as AC-016 | Row DE-4 marked "unverified"; ledger status investigate. |
| launch-release/findings/raw/existing-reviews.md:246 | rejected | count-table column header, not a finding |
| launch-release/findings/raw/fe-a.md:3 | rejected | convention note defining the word hypothesis, not a finding |
| launch-release/findings/raw/fe-a.md:36 | tracked as LR-056 | Worker-side cancellation hypothesis is carried by LR-056 fix hint (persist under ctx.waitUntil). |
| launch-release/findings/raw/fe-a.md:39 | tracked as LR-056 | Same as fe-a:36; relay may be cancelled when the client drops, covered by the waitUntil fix hint. |
| launch-release/findings/raw/fe-a.md:99 | rejected | Marker is an ordinary word (appears, looks like); the enclosing defect is tracked as LR-028. |
| launch-release/findings/raw/fe-a.md:135 | tracked as LR-083 | Heading FEA-014 (hypothesis); ledger status open. |
| launch-release/findings/raw/fe-a.md:160 | rejected | Marker is an ordinary word (appears); the enclosing defect is tracked as LR-085. |
| launch-release/findings/raw/fe-a.md:169 | rejected | Marker is an ordinary word (appears); the enclosing defect is tracked as LR-086. |
| launch-release/findings/raw/fe-a.md:189 | rejected | Marker is an ordinary word (looks like); the enclosing defect is tracked as LR-091. |
| launch-release/findings/raw/fe-a.md:209 | rejected | Marker is an ordinary word (may be); the enclosing defect is tracked as LR-093. |
| launch-release/findings/raw/fe-a.md:245 | tracked as LR-159 | Heading FEA-025 (hypothesis); ledger status investigate. |
| launch-release/findings/raw/fe-a.md:249 | tracked as LR-159 | Heading FEA-025 (not checked); ledger status investigate. |
| launch-release/findings/raw/fe-a.md:269 | rejected | Marker is an ordinary word (not run); the enclosing defect is tracked as LR-027. |
| launch-release/findings/raw/fe-a.md:285 | tracked as LR-168 | Heading FEA-029 (hypothesis); ledger status investigate. |
| launch-release/findings/raw/fe-a.md:290 | rejected | Marker is an ordinary word (appears); the enclosing defect is tracked as LR-168. |
| launch-release/findings/raw/fe-b.md:27 | tracked as LR-072 | Heading FEB-003 (hypothesis); ledger status open. |
| launch-release/findings/raw/fe-b.md:31 | rejected | Marker is an ordinary word (hypothesis); the enclosing defect is tracked as LR-072. |
| launch-release/findings/raw/fe-b.md:41 | rejected | Marker is an ordinary word (appears); the enclosing defect is tracked as LR-030. |
| launch-release/findings/raw/fe-b.md:152 | rejected | Marker is an ordinary word (appears); the enclosing defect is tracked as LR-098. |
| launch-release/findings/raw/fe-b.md:167 | tracked as LR-101 | Doubt (users.id vs email, db/users.ts not read) is LR-101, investigate. |
| launch-release/findings/raw/fe-b.md:197 | tracked as LR-094 | Doubt (no sample label) is LR-094, investigate. |
| launch-release/findings/raw/gen-pkg.md:71 | tracked as LR-037 | Legacy 100-char cap activation is in the LR-037 title and fix hint. |
| launch-release/findings/raw/gen-pkg.md:141 | tracked as LR-117 | Entity decoding is LR-117. The "frontend innerHTML not checked" doubt is settled: grep of frontend/src finds no dangerouslySetInnerHTML; only NewsCard.tsx:52 clears a node with innerHTML = empty string. |
| launch-release/findings/raw/gen-pkg.md:191 | rejected | Marker is an ordinary word (appears); the enclosing defect is tracked as LR-154. |
| launch-release/findings/raw/gen-pkg.md:231 | tracked as LR-115 | Dead-code hypothesis is in the LR-115 title ("appear to be unused") and fix hint. |
| launch-release/findings/raw/setup.md:143 | tracked as LR-047 | "python" may be a different interpreter: the defect (bare python) is LR-047. |
| launch-release/findings/raw/setup.md:153 | tracked as LR-048 | The "/health route may 404" doubt is settled: grep of worker/src finds no /health route; LR-048 fix hint already says to probe the endpoint setup/verification.py uses. |
| launch-release/findings/raw/setup.md:223 | tracked as LR-123 | Quote case is in the LR-123 fix hint (strip quotes when reading). |
| launch-release/findings/raw/setup.md:263 | new: INV-023 (also LR-130 for the live-call requirement) | Whether gemini-2.0-flash (the wizard validation model) is still served was never tracked; LR-130 covers only the hard requirement and the key in the URL. |
| launch-release/findings/raw/setup.md:273 | tracked as LR-125 | Exact wrangler version hypothesis; LR-125 fix hint aligns versions. |
| launch-release/findings/raw/setup.md:293 | tracked as LR-127 | Mangled JSON hypothesis is in LR-127 title. |
| launch-release/findings/raw/setup.md:333 | new: SWP-001, SWP-002, INV-021 (also LR-162 for the doc drift) | Sub-hypotheses not in LR-162: unused google-generativeai pin and protobuf conflict, npx-only wrangler prereq pass, Node 18 floor vs wrangler 4 and CI Node 24. |
| launch-release/findings/raw/setup.md:339 | tracked as LR-051 | Alias SET-034; LR-051 repro is to check how worker/src reads deployment mode. |
| launch-release/findings/raw/worker-a.md:3 | rejected | report preamble saying everything is static reading; each item carries its own confidence |
| launch-release/findings/raw/worker-a.md:47 | rejected | Marker is an ordinary word (unverified); the enclosing defect is tracked as LR-015. |
| launch-release/findings/raw/worker-a.md:247 | rejected | Marker is an ordinary word (appears); the enclosing defect is tracked as LR-055. |
| launch-release/findings/raw/worker-a.md:267 | tracked as LR-147 | Heading WKA-027 (hypothesis); ledger status investigate. |
| launch-release/findings/raw/worker-a.md:275 | tracked as LR-147 | LR-147 is investigate and says to apply 0010 to a copy of production data; that check settles whether pre-0010 rows existed. |
| launch-release/findings/raw/worker-a.md:361 | tracked as LR-187 | Serialization is certain; UI impact hypothesis is LR-187, investigate. |
| launch-release/findings/raw/worker-b.md:21 | rejected | Marker is an ordinary word (appears); the enclosing defect is tracked as LR-012. |
| launch-release/findings/raw/worker-b.md:90 | rejected | Marker is an ordinary word (appears); the enclosing defect is tracked as LR-058. |
| launch-release/findings/raw/worker-b.md:130 | tracked as LR-061 | LR-061 is investigate (live call to confirm). |
| launch-release/findings/raw/worker-b.md:150 | tracked as LR-065 | Stored-XSS doubt on the UI side is settled: the three newsletter preview iframes use sandbox="allow-same-origin" without allow-scripts (NewsletterDashboard.tsx:478, NewsletterConfigDrawer.tsx:802,930). Email phishing and attribute injection remain in LR-065. |
| launch-release/findings/raw/worker-b.md:170 | tracked as LR-056 | Alias WKB-017; relay with no catch and no abort signal is in LR-056 fix hint. |
| launch-release/findings/raw/worker-b.md:200 | rejected | Marker is an ordinary word (appears); the enclosing defect is tracked as LR-060. |
| launch-release/findings/raw/worker-b.md:216 | tracked as LR-152 | Heading marks the item as hypothesis; LR-152 is investigate. |
| launch-release/findings/raw/worker-b.md:224 | tracked as LR-152 | LinkedIn little-text behaviour is untested; LR-152 is investigate. |
| launch-release/findings/raw/worker-b.md:270 | new: INV-022 (also LR-149 for the OpenAI/Stability formats) | Veo :generateVideo endpoint hypothesis is not in LR-149 (which covers dall-e and Stability only). |
| launch-release/findings/raw/worker-b.md:310 | new: INV-024 (also LR-137 for the Gmail key and auth) | Availability of the LinkedIn webhookSubscriptions and MEMBER_TO_MEMBER endpoints to a standard app is not in LR-137. |
| launch-release/findings/raw/worker-b.md:320 | rejected | Marker is an ordinary word (appears); the enclosing defect is tracked as LR-138. |
| launch-release/findings/raw/worker-b.md:436 | rejected | Marker is an ordinary word (not run); the enclosing defect is tracked as LR-190. |
| launch-release/findings/raw/worker-b.md:446 | tracked as LR-193 | LR-193 is investigate. |
| launch-release/findings/ARCH-AUDIT.md:3 | rejected | report preamble saying everything is static reading; each item carries its own confidence |
| launch-release/findings/ARCH-AUDIT.md:77 | tracked as LR-009 | Settled: worker/migrations/0007_multi_tenant.sql creates users with no status column; the only status column is added by 0019 with DEFAULT active, so no earlier migration changes the default. |
| launch-release/findings/ARCH-AUDIT.md:147 | tracked as LR-018 | Default asset ignore list unchecked: LR-018 fix hint adds .assetsignore, and its repro is wrangler deploy --dry-run. |
| launch-release/findings/ARCH-AUDIT.md:157 | tracked as LR-070 | Idempotency of executeScheduledPublish: LR-070 is the no-idempotency finding. |
| launch-release/findings/JOURNEY-DELTA.md:40 | tracked as JRN-005 | Item hypothesis; ledger status investigate. |
| launch-release/findings/TEST-COVERAGE.md:147 | rejected | Marker is an ordinary word (appears); the enclosing defect is tracked as TST-008. |
| launch-release/findings/TEST-COVERAGE.md:219 | rejected | Marker is an ordinary word (appears); the enclosing defect is tracked as TST-017. |
| launch-release/findings/TEST-COVERAGE.md:235 | tracked as TST-019 | Timezone and past-time doubt is the subject of TST-019 and J-085. |
| launch-release/findings/TEST-COVERAGE.md:356 | rejected | Marker is an ordinary word (not run); the enclosing defect is tracked as TST-034. |
| launch-release/findings/AUTOMATIONS.md:35 | tracked as AUT-005 | Item hypothesis; ledger status investigate. |
| launch-release/findings/AUTOMATIONS.md:37 | tracked as AUT-005 | Item hypothesis; ledger status investigate. |
| launch-release/findings/raw/fe-b.md:175 (extra, non-marker) | tracked as LR-101 | Non-marker doubt: db/users.ts not read. LR-101 is investigate. |
| launch-release/findings/raw/fe-b.md:201 (extra, non-marker) | tracked as LR-094 | Non-marker doubt: dashboard label not read. LR-094 is investigate. |
| launch-release/findings/raw/gen-pkg.md:161 (extra, non-marker) | tracked as LR-156 | Non-marker doubt: URL not seen logged; exposure surface only. |
| launch-release/findings/raw/gen-pkg.md:241 (extra, non-marker) | tracked as LR-148 | Non-marker doubt: frontend rendering not verified; settled for innerHTML as at gen-pkg:141, prompt-injection part stays in LR-148. |
