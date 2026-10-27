# Rejected or already-fixed claims

### REJ-001 P3 frontend/feed - FEA-027 claim that the main worker does not route /api/clips
- **Reason:** Partly wrong: ARCH-AUDIT lists /api/clips and /api/feed routes in worker/src/index.ts:714-717,804-807. The real defect (unset globalThis.VITE_WORKER_URL) is covered by FEB-002 and kept as an alias there; the dead /v1/variants/save part stays valid.

### REJ-002 P3 deploy/auth - FEB-026 duplicate of the bypass secret item
- **Reason:** Not wrong, but obsolete once the bypass secret is removed; folded into LR-001 as an alias.

### REJ-003 P3 existing-review/c02 - C02-2 Favicon next to source
- **Reason:** Existing review marked this fixed; code evidence: FeedArticleCard.tsx:76-83.

### REJ-004 P3 existing-review/c02 - C02-4 2-line summary default
- **Reason:** Existing review marked this fixed; code evidence: FeedArticleCard.tsx:~69 `line-clamp-2` + content fallback.

### REJ-005 P3 existing-review/c02 - C02-7 j/k/o/c keyboard nav
- **Reason:** Existing review marked this fixed; code evidence: features/feed/hooks/useFeedKeyboard.ts:38; FeedPage.tsx:586-596.

### REJ-006 P3 existing-review/c02 - C02-12 Detail as side-sheet not full-screen
- **Reason:** Existing review marked this fixed; code evidence: FeedPage.tsx:1375-1405 (480px sheet, `asSheet`). overlay darkens feed (modal)

### REJ-007 P3 existing-review/c03 - C03-3 "Compose post from clips" CTA
- **Reason:** Existing review marked this fixed; code evidence: ClipsDock.tsx:133-145.

### REJ-008 P3 existing-review/c04 - C04-1 Queue row primary CTA always visible
- **Reason:** Existing review marked this fixed; code evidence: components/dashboard/tabs/DashboardQueue.tsx:~852,896,925. only delete column is dimmed (`opacity-40`, :942)

### REJ-009 P3 existing-review/c04 - C04-3 Unified status pill
- **Reason:** Existing review marked this fixed; code evidence: components/ui/StatusPill.tsx; DashboardQueue.tsx:20,768. adoption elsewhere (calendar, newsletter) unchecked

### REJ-010 P3 existing-review/c04 - C04-4 Empty state starter templates + tour
- **Reason:** Existing review marked this fixed; code evidence: DashboardQueue.tsx:431-435,585-588.

### REJ-011 P3 existing-review/c04 - C04-12 AI-Draft modal not nested in drawer
- **Reason:** Existing review marked this fixed; code evidence: DashboardQueue.tsx:161,187-220 (dialog owned by queue). TopicDetailPanel is a separate overlay (:55)

### REJ-012 P3 existing-review/c05 - C05-2 TopicDetailPanel uses ScheduleEditor
- **Reason:** Existing review marked this fixed; code evidence: components/dashboard/components/TopicDetailPanel.tsx:369.

### REJ-013 P3 existing-review/c05 - C05-3 Calendar uses ScheduleEditor
- **Reason:** Existing review marked this fixed; code evidence: content-schedule-calendar/ContentScheduleCalendar.tsx:367. so 2 of 3 entry points unified; editor remains

### REJ-014 P3 existing-review/c05 - C05-9 Single ChannelPicker component
- **Reason:** Existing review marked this fixed; code evidence: components/channels (imported DashboardDelivery.tsx:7, TopicsRightRail.tsx:6,258,390). bulk modal still separate (DashboardQueue.tsx:1017)

### REJ-015 P3 existing-review/c06 - C06-4 Passive autosave restore
- **Reason:** Existing review marked this fixed; code evidence: ReviewDialogs.tsx:43 "Restore previous draft?"; useReviewFlowState.ts:645 autoSaveTrigger.

### REJ-016 P3 existing-review/c08 - C08-1 Newsletter live preview (desktop/mobile)
- **Reason:** Existing review marked this fixed; code evidence: campaign/components/newsletter/NewsletterConfigDrawer.tsx:44-51,97-101,192-200. `[x]` in doc is correct

### REJ-017 P3 existing-review/c08 - C08-6 Send test to me
- **Reason:** Existing review marked this fixed; code evidence: NewsletterConfigDrawer.tsx:187,304-308.

### REJ-018 P3 existing-review/c09 - C09-3 Cmd-K settings search
- **Reason:** Existing review marked this fixed; code evidence: DashboardSettingsDrawer.tsx:1225-1228,1305. scoped to settings only

### REJ-019 P3 existing-review/c09 - C09-8 Sticky ToC
- **Reason:** Existing review marked this fixed; code evidence: DashboardSettingsDrawer.tsx ~L1317-1390.

### REJ-020 P3 existing-review/c09 - C09-9 Setup wizard progress "Step N of M"
- **Reason:** Existing review marked this fixed; code evidence: features/setup-wizard/SetupWizard.tsx:91-105.

### REJ-021 P3 existing-review/c09 - C09-10 Wizard label rename
- **Reason:** Existing review marked this fixed; code evidence: SetupWizard.tsx:77-89 ("Trending Sources","Image Generation","Voice Transcription").

### REJ-022 P3 existing-review/c09 - C09-11 Wizard Back buttons
- **Reason:** Existing review marked this fixed; code evidence: SetupWizard.tsx:538-636; EnvVarsStep.tsx:438.

### REJ-023 P3 existing-review/c09 - C09-12 EnvVars grouped w/ docs links
- **Reason:** Existing review marked this fixed; code evidence: EnvVarsStep.tsx:456-532 (groups + links). example values not verified

### REJ-024 P3 existing-review/c10 - C10-1 Progress to non-admins in editor
- **Reason:** Existing review marked this fixed; code evidence: EditorSidebar.tsx:417; GenerationPanel.tsx:312 (EnrichmentProgressPanel).

### REJ-025 P3 existing-review/c11 - C11-2 Feed 👍/👎 persisted
- **Reason:** Existing review marked this fixed; code evidence: worker index.ts:1812 `setArticleFeedback`, :1823 get; FeedPage.tsx:1280.

### REJ-026 P3 existing-review/c13 - C13-9 Global shortcuts g+t/g+f/?
- **Reason:** Existing review marked this fixed; code evidence: App.tsx:126; components/HelpOverlay.tsx:4-9; hooks/useGlobalShortcuts.ts.

### REJ-027 P3 existing-review/c05b - C05b Bulk campaign: 3-mode import, file upload
- **Reason:** Existing review marked this fixed; code evidence: campaign/CampaignPage.tsx:70,591-603 (Prompt/File/Paste). audits/05

### REJ-028 P3 existing-review/c05d - C05d Bulk: draft persistence, undo delete
- **Reason:** Existing review marked this fixed; code evidence: CampaignPage.tsx:247-251 localStorage; :469 undo text. audits/05

### REJ-029 P3 existing-review/u - U-052/041 WhatsApp card on /connections
- **Reason:** Existing review marked this fixed; code evidence: pages/connections/ConnectionsPage.tsx:22,60.

### REJ-030 P3 existing-review/u - U-053 Telegram verification on /connections
- **Reason:** Existing review marked this fixed; code evidence: ConnectionsPage.tsx:7,15,23 `verifyTelegramChat`. worker index.ts:2388

### REJ-031 P3 existing-review/u - U-057/060 listRules/lookupEffectiveRule use checkedFetch
- **Reason:** Existing review marked this fixed; code evidence: features/automations/api.ts:16,30,67.

### REJ-032 P3 existing-review/u - U-062 YouTube: no webhook form
- **Reason:** Existing review marked this fixed; code evidence: features/automations/AutomationsTab.tsx:120.

### REJ-033 P3 existing-review/u - U-J1.5 analyzeTopicInsights
- **Reason:** Existing review marked this fixed; code evidence: worker index.ts:1878; backendApi.ts:1077.

### REJ-034 P3 existing-review/u - U-J1.8 generateQuickChange
- **Reason:** Existing review marked this fixed; code evidence: worker index.ts:1572; backendApi.ts:649.

### REJ-035 P3 existing-review/u - U-J12 6 enrichment actions in worker
- **Reason:** Existing review marked this fixed; code evidence: worker index.ts:1919,2024,2070,2118,2159,2201. all present, all have backendApi methods (:1086,1726-1745)

### REJ-036 P3 existing-review/p1 - P1-T1 AppSidebar active-state / automations nav fix
- **Reason:** Existing review marked this fixed; code evidence: AppSidebar.tsx:116-148 (`PAGE_TO_PATH` incl. automations; `useEnd` only topics). checkboxes never ticked; code landed

### REJ-037 P3 existing-review/p1 - P1-T2 TrendingSidebar refresh button + refetch, remove AddTopic debounce
- **Reason:** Existing review marked this fixed; code evidence: add-topic/TrendingSidebar.tsx:8-31; TopicRightPanel.tsx:87,96; useTrending.ts:295-300.

### REJ-038 P3 existing-review/p1 - P1-T3 ContentReview provider revert guard
- **Reason:** Existing review marked this fixed; code evidence: features/content-review/ContentReviewSettings.tsx:58-62 (empty-catalog guard); services/configService.ts:293-308 normalize.

### REJ-039 P3 existing-review/p1 - P1-T4 TopicsRightRail provider/model validation
- **Reason:** Existing review marked this fixed; code evidence: components/dashboard/components/TopicsRightRail.tsx:111-125.

### REJ-040 P3 existing-review/p2 - P2-T1..3 Feed L/M/Q/R types, 4 worker cases, 4 API methods
- **Reason:** Existing review marked this fixed; code evidence: worker index.ts:2070,2118,2159,2201; backendApi.ts:1730-1745.

### REJ-041 P3 existing-review/p2 - P2-T4 Tab L connection finder + Debate button
- **Reason:** Existing review marked this fixed; code evidence: ArticleDetailView.tsx:189,571; FeedPage.tsx onDebate.

### REJ-042 P3 existing-review/p2 - P2-T5/6 DebateModeView + wiring
- **Reason:** Existing review marked this fixed; code evidence: features/feed/components/DebateModeView.tsx; FeedPage.tsx debateMode.

### REJ-043 P3 existing-review/p2 - P2-T7 DraftContextView Q/R tabs
- **Reason:** Existing review marked this fixed; code evidence: DraftContextView.tsx:143,159.

### REJ-044 P3 existing-review/d3 - D3-1 /feed split layout, group switcher, filters
- **Reason:** Existing review marked this fixed; code evidence: FeedPage.tsx; /trending redirects dashboard/index.tsx:899-900.

### REJ-045 P3 existing-review/d3 - D3-3 Clips CRUD (/api/clips) + persistence
- **Reason:** Existing review marked this fixed; code evidence: worker index.ts:714-717,804-807. assign/unassign by action not verified

### REJ-046 P3 existing-review/d3 - D3-5 Dock magnification, expand, drag to draft
- **Reason:** Existing review marked this fixed; code evidence: ClipsDock.tsx:158,332-367.

### REJ-047 P3 existing-review/d2 - D2-4 4 variants w/ variant_rationale + badges
- **Reason:** Existing review marked this fixed; code evidence: worker engine/types.ts, draft-generator.ts; frontend VariantCarousel.tsx.

### REJ-048 P3 existing-review/de - DE-2 Compare never replaces without confirmation
- **Reason:** Existing review marked this fixed; code evidence: useReviewFlowActions.ts:~357-372 (compare onConfirm sets editor text).
