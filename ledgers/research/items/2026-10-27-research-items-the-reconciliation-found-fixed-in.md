---
id: 2026-10-27-research-items-the-reconciliation-found-fixed-in
title: Items the reconciliation found fixed in the current code (read-only)
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related: []
docs:
- docs/launch-readiness/findings/EXISTING-REVIEWS.md
status: complete
source_revision: a65b712
---

## Question

Which previously reported items does the current code already fix?

## Sources and method

Reading of the cited code for each existing-review row marked fixed. Not executed.

## Findings

- AC-001: read-only: fixed per reconciliation, evidence FeedPage.tsx; /trending redirects dashboard/index.tsx:899-900
- AC-003: read-only: fixed per reconciliation, evidence worker index.ts:714-717,804-807
- AC-005: read-only: fixed per reconciliation, evidence ClipsDock.tsx:158,332-367
- AC-011: read-only: fixed per reconciliation, evidence worker engine/types.ts, draft-generator.ts; frontend VariantCarousel.tsx
- AC-014: read-only: fixed per reconciliation, evidence useReviewFlowActions.ts:~357-372 (compare onConfirm sets editor text)
- CONS-012: read-only: fixed per reconciliation, evidence FeedArticleCard.tsx:76-83
- CONS-014: read-only: fixed per reconciliation, evidence FeedArticleCard.tsx:~69 line-clamp-2 + content fallback
- CONS-017: read-only: fixed per reconciliation, evidence features/feed/hooks/useFeedKeyboard.ts:38; FeedPage.tsx:586-596
- CONS-022: read-only: fixed per reconciliation, evidence FeedPage.tsx:1375-1405 (480px sheet, asSheet)
- CONS-031: read-only: fixed per reconciliation, evidence ClipsDock.tsx:133-145
- CONS-040: read-only: fixed per reconciliation, evidence components/dashboard/tabs/DashboardQueue.tsx:~852,896,925
- CONS-042: read-only: fixed per reconciliation, evidence components/ui/StatusPill.tsx; DashboardQueue.tsx:20,768
- CONS-043: read-only: fixed per reconciliation, evidence DashboardQueue.tsx:431-435,585-588
- CONS-051: read-only: fixed per reconciliation, evidence DashboardQueue.tsx:161,187-220 (dialog owned by queue)
- CONS-059: read-only: fixed per reconciliation, evidence components/dashboard/components/TopicDetailPanel.tsx:369
- CONS-060: read-only: fixed per reconciliation, evidence content-schedule-calendar/ContentScheduleCalendar.tsx:367
- CONS-066: read-only: fixed per reconciliation, evidence components/channels (imported DashboardDelivery.tsx:7, TopicsRightRail.tsx:6,258,390)
- CONS-074: read-only: fixed per reconciliation, evidence ReviewDialogs.tsx:43 "Restore previous draft?"; useReviewFlowState.ts:645 autoSaveTrigger
- CONS-090: read-only: fixed per reconciliation, evidence campaign/components/newsletter/NewsletterConfigDrawer.tsx:44-51,97-101,192-200
- CONS-095: read-only: fixed per reconciliation, evidence NewsletterConfigDrawer.tsx:187,304-308
- CONS-104: read-only: fixed per reconciliation, evidence DashboardSettingsDrawer.tsx:1225-1228,1305
- CONS-109: read-only: fixed per reconciliation, evidence DashboardSettingsDrawer.tsx ~L1317-1390
- CONS-110: read-only: fixed per reconciliation, evidence features/setup-wizard/SetupWizard.tsx:91-105
- CONS-111: read-only: fixed per reconciliation, evidence SetupWizard.tsx:77-89 ("Trending Sources","Image Generation","Voice Transcription")
- CONS-112: read-only: fixed per reconciliation, evidence SetupWizard.tsx:538-636; EnvVarsStep.tsx:438
- CONS-113: read-only: fixed per reconciliation, evidence EnvVarsStep.tsx:456-532 (groups + links)
- CONS-119: read-only: fixed per reconciliation, evidence EditorSidebar.tsx:417; GenerationPanel.tsx:312 (EnrichmentProgressPanel)
- CONS-127: read-only: fixed per reconciliation, evidence worker index.ts:1812 setArticleFeedback, :1823 get; FeedPage.tsx:1280
- CONS-141: read-only: fixed per reconciliation, evidence App.tsx:126; components/HelpOverlay.tsx:4-9; hooks/useGlobalShortcuts.ts
- CONS-144: read-only: fixed per reconciliation, evidence campaign/CampaignPage.tsx:70,591-603 (Prompt/File/Paste)
- CONS-146: read-only: fixed per reconciliation, evidence CampaignPage.tsx:247-251 localStorage; :469 undo text
- GAP-002: read-only: generation-worker/src reviewed by gen-pkg (GWP-*); reconciler grep timeout no longer blocks coverage
- GAP-003: read-only: covered by launch-release/findings/TEST-COVERAGE.md, AUTOMATIONS.md and JOURNEY-DELTA.md
- GAP-005: read-only: covered by launch-release/findings/TEST-COVERAGE.md, AUTOMATIONS.md and JOURNEY-DELTA.md
- REJ-003: read-only: existing-reviews.md recorded evidence FeedArticleCard.tsx:76-83
- REJ-004: read-only: existing-reviews.md recorded evidence FeedArticleCard.tsx:~69 `line-clamp-2` + content fallback
- REJ-005: read-only: existing-reviews.md recorded evidence features/feed/hooks/useFeedKeyboard.ts:38; FeedPage.tsx:586-596
- REJ-006: read-only: existing-reviews.md recorded evidence FeedPage.tsx:1375-1405 (480px sheet, `asSheet`)
- REJ-007: read-only: existing-reviews.md recorded evidence ClipsDock.tsx:133-145
- REJ-008: read-only: existing-reviews.md recorded evidence components/dashboard/tabs/DashboardQueue.tsx:~852,896,925
- REJ-009: read-only: existing-reviews.md recorded evidence components/ui/StatusPill.tsx; DashboardQueue.tsx:20,768
- REJ-010: read-only: existing-reviews.md recorded evidence DashboardQueue.tsx:431-435,585-588
- REJ-011: read-only: existing-reviews.md recorded evidence DashboardQueue.tsx:161,187-220 (dialog owned by queue)
- REJ-012: read-only: existing-reviews.md recorded evidence components/dashboard/components/TopicDetailPanel.tsx:369
- REJ-013: read-only: existing-reviews.md recorded evidence content-schedule-calendar/ContentScheduleCalendar.tsx:367
- REJ-014: read-only: existing-reviews.md recorded evidence components/channels (imported DashboardDelivery.tsx:7, TopicsRightRail.tsx:6,258,390)
- REJ-015: read-only: existing-reviews.md recorded evidence ReviewDialogs.tsx:43 "Restore previous draft?"; useReviewFlowState.ts:645 autoSaveTrigger
- REJ-016: read-only: existing-reviews.md recorded evidence campaign/components/newsletter/NewsletterConfigDrawer.tsx:44-51,97-101,192-200
- REJ-017: read-only: existing-reviews.md recorded evidence NewsletterConfigDrawer.tsx:187,304-308
- REJ-018: read-only: existing-reviews.md recorded evidence DashboardSettingsDrawer.tsx:1225-1228,1305
- REJ-019: read-only: existing-reviews.md recorded evidence DashboardSettingsDrawer.tsx ~L1317-1390
- REJ-020: read-only: existing-reviews.md recorded evidence features/setup-wizard/SetupWizard.tsx:91-105
- REJ-021: read-only: existing-reviews.md recorded evidence SetupWizard.tsx:77-89 ("Trending Sources","Image Generation","Voice Transcription")
- REJ-022: read-only: existing-reviews.md recorded evidence SetupWizard.tsx:538-636; EnvVarsStep.tsx:438
- REJ-023: read-only: existing-reviews.md recorded evidence EnvVarsStep.tsx:456-532 (groups + links)
- REJ-024: read-only: existing-reviews.md recorded evidence EditorSidebar.tsx:417; GenerationPanel.tsx:312 (EnrichmentProgressPanel)
- REJ-025: read-only: existing-reviews.md recorded evidence worker index.ts:1812 `setArticleFeedback`, :1823 get; FeedPage.tsx:1280
- REJ-026: read-only: existing-reviews.md recorded evidence App.tsx:126; components/HelpOverlay.tsx:4-9; hooks/useGlobalShortcuts.ts
- REJ-027: read-only: existing-reviews.md recorded evidence campaign/CampaignPage.tsx:70,591-603 (Prompt/File/Paste)
- REJ-028: read-only: existing-reviews.md recorded evidence CampaignPage.tsx:247-251 localStorage; :469 undo text
- REJ-029: read-only: existing-reviews.md recorded evidence pages/connections/ConnectionsPage.tsx:22,60
- REJ-030: read-only: existing-reviews.md recorded evidence ConnectionsPage.tsx:7,15,23 `verifyTelegramChat`
- REJ-031: read-only: existing-reviews.md recorded evidence features/automations/api.ts:16,30,67
- REJ-032: read-only: existing-reviews.md recorded evidence features/automations/AutomationsTab.tsx:120
- REJ-033: read-only: existing-reviews.md recorded evidence worker index.ts:1878; backendApi.ts:1077
- REJ-034: read-only: existing-reviews.md recorded evidence worker index.ts:1572; backendApi.ts:649
- REJ-035: read-only: existing-reviews.md recorded evidence worker index.ts:1919,2024,2070,2118,2159,2201
- REJ-036: read-only: existing-reviews.md recorded evidence AppSidebar.tsx:116-148 (`PAGE_TO_PATH` incl. automations; `useEnd` only topics)
- REJ-037: read-only: existing-reviews.md recorded evidence add-topic/TrendingSidebar.tsx:8-31; TopicRightPanel.tsx:87,96; useTrending.ts:295-300
- REJ-038: read-only: existing-reviews.md recorded evidence features/content-review/ContentReviewSettings.tsx:58-62 (empty-catalog guard); services/configServic
- REJ-039: read-only: existing-reviews.md recorded evidence components/dashboard/components/TopicsRightRail.tsx:111-125
- REJ-040: read-only: existing-reviews.md recorded evidence worker index.ts:2070,2118,2159,2201; backendApi.ts:1730-1745
- REJ-041: read-only: existing-reviews.md recorded evidence ArticleDetailView.tsx:189,571; FeedPage.tsx onDebate
- REJ-042: read-only: existing-reviews.md recorded evidence features/feed/components/DebateModeView.tsx; FeedPage.tsx debateMode
- REJ-043: read-only: existing-reviews.md recorded evidence DraftContextView.tsx:143,159
- REJ-044: read-only: existing-reviews.md recorded evidence FeedPage.tsx; /trending redirects dashboard/index.tsx:899-900
- REJ-045: read-only: existing-reviews.md recorded evidence worker index.ts:714-717,804-807
- REJ-046: read-only: existing-reviews.md recorded evidence ClipsDock.tsx:158,332-367
- REJ-047: read-only: existing-reviews.md recorded evidence worker engine/types.ts, draft-generator.ts; frontend VariantCarousel.tsx
- REJ-048: read-only: existing-reviews.md recorded evidence useReviewFlowActions.ts:~357-372 (compare onConfirm sets editor text)
- SP-001: read-only: fixed per reconciliation, evidence AppSidebar.tsx:116-148 (PAGE_TO_PATH incl. automations; useEnd only topics)
- SP-002: read-only: fixed per reconciliation, evidence add-topic/TrendingSidebar.tsx:8-31; TopicRightPanel.tsx:87,96; useTrending.ts:295-300
- SP-003: read-only: fixed per reconciliation, evidence features/content-review/ContentReviewSettings.tsx:58-62 (empty-catalog guard); services/configService.ts:293-308 normalize
- SP-004: read-only: fixed per reconciliation, evidence components/dashboard/components/TopicsRightRail.tsx:111-125
- SP-005: read-only: fixed per reconciliation, evidence worker index.ts:2070,2118,2159,2201; backendApi.ts:1730-1745
- SP-006: read-only: fixed per reconciliation, evidence ArticleDetailView.tsx:189,571; FeedPage.tsx onDebate
- SP-007: read-only: fixed per reconciliation, evidence features/feed/components/DebateModeView.tsx; FeedPage.tsx debateMode
- SP-008: read-only: fixed per reconciliation, evidence DraftContextView.tsx:143,159
- UC-001: read-only: fixed per reconciliation, evidence pages/connections/ConnectionsPage.tsx:22,60
- UC-002: read-only: fixed per reconciliation, evidence ConnectionsPage.tsx:7,15,23 verifyTelegramChat
- UC-003: read-only: fixed per reconciliation, evidence features/automations/api.ts:16,30,67
- UC-004: read-only: fixed per reconciliation, evidence features/automations/AutomationsTab.tsx:120
- UC-009: read-only: fixed per reconciliation, evidence worker index.ts:1878; backendApi.ts:1077
- UC-012: read-only: fixed per reconciliation, evidence worker index.ts:1572; backendApi.ts:649
- UC-021: read-only: fixed per reconciliation, evidence worker index.ts:1919,2024,2070,2118,2159,2201

## Limits

These are read-only: the fix is visible in the code, not proven by a run. Verification requires an executor (GAP-001).

## Recommendations and follow-up

Run the cited journey before closing any of these as verified.
