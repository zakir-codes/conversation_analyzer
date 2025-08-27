## Task009: NLP Metrics and Script Adherence

**Related TRs**: TR009, TR010

### Objective
- Compute selected conversation metrics and script adherence coverage against uploaded scripts.
- Store structured outputs with transcript evidence to support downstream insights (Task010).

### Deliverables
- Metrics computation module (LLM via LangChain + NLP utilities).
- Script adherence checker with coverage %, missing steps, and deviations.
- MongoDB storage schema: `{ metric_name, value, evidence_spans, confidence }`.

### Steps
- Metric Computation
  - Implement functions for core metrics (e.g., talk ratio, interruptions, empathy markers, silence, filler words).
  - Use transcript + speaker diarization for calculation.
  - Where applicable, run LLM via LangChain to extract higher-order signals (e.g., empathy detection, objection handling).
- Script Adherence Check
  - Index uploaded script (Task005) with embeddings (LangChain).
  - Compare transcript chunks to script steps via retrieval/semantic similarity.
  - Output:
    - Adherence % coverage
    - Missing script items
    - Extra/unexpected topics
- Evidence Capture
  - For each metric/adherence item, store supporting transcript spans (timestamp + text + speaker).
  - Ensure these are linkable for dashboard drill-down (Task010).
- Database Integration
  - Store results in `job_results.metrics[]` and `job_results.adherence`.
  - Each entry includes structured data, e.g.:
```
{
  "metric_name": "Talk Ratio",
  "value": 0.72,
  "target": 0.55,
  "evidence_spans": [
    {"start": "00:05:10", "end": "00:10:00", "speaker": "Rep"}
  ]
}
```

### Acceptance Criteria
- All selected metrics (from Task006) computed and stored per call.
- Script adherence % and gaps (missing/extra) reported.
- Each result links to transcript evidence spans.
- Stored data structured to allow pre-computed insights (Task010).

### Dependencies
- Task006 → Metric selection.
- Task008 → Transcript availability.
- Task005 → Script upload.