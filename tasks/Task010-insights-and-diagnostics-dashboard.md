## Task010: Insights Generation and Diagnostics Dashboard

**Related TRs**: TR011, TR012, TR022

### Objective
- Generate 3–5 pre-computed insights per call using metrics & adherence results.
- Build a Streamlit diagnostics dashboard to display insights, metrics, and drill-down transcript spans.
- Enable export of insights and reports.

### Deliverables
- Insights generator: LLM via LangChain that consumes structured results from Task009 (not raw transcript).
- Pre-computed insights storage in MongoDB:
```
{ "insight_id": "uuid", "type": "string", "text": "string", "linked_metrics": ["metric_id"], "evidence": [{"start": "00:05:10", "end": "00:05:45"}] }
```
- Streamlit dashboard:
  - Insights panel
  - Metrics visualization (charts: talk ratio, empathy, adherence %)
  - Drill-down to transcript snippets
  - Export options (CSV/PDF)

### Steps
- Insights Computation
  - Define insight categories (e.g., objections raised, script adherence gaps, missed CTAs, empathy presence, rep talk dominance)
  - Implement LangChain LLM chain to generate short, structured insights based on stored metrics/adherence results
  - Store pre-computed insights along with evidence references
- Dashboard UI (Streamlit)
  - Layout:
    - Top: Key insights (3–5 bullets with evidence)
    - Middle: Charts (Plotly/Altair) for per-call metrics
    - Bottom: Transcript drill-down (click → jump to evidence span)
  - Highlight adherence % coverage and missing steps
- Drill-down Linking
  - Ensure insights and metrics reference transcript spans from Task009
  - Provide clickable evidence that shows snippet + timestamp
- Export Options
  - Export per-call insights + metrics as CSV (tabular) or PDF (report-style)
  - Support lightweight template formatting (logo, header, date, call ID)

### Acceptance Criteria
- 3–5 insights per call generated and stored at job completion.
- Dashboard shows insights, charts, and transcript drill-downs without recomputation (pre-computed results only).
- Charts render without errors; drill-down opens correct transcript snippet.
- CSV/PDF export generates a readable file with insights + metrics.

### Dependencies
- Task009 → Metric + adherence results.
- Task004 → Job tracking & frontend polling.
- Task005 → Script linkage for adherence insights.