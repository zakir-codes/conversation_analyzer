## Task006: Metric Selection and Defaults

**Related TRs**: TR006, TR021

### Objective
- Allow users to choose which metrics to calculate during analysis.
- Ensure a default metric set is applied when no selection is made.
- Prepare backend to support aggregation hooks for rep/team analytics.

### Deliverables
- Frontend (Streamlit):
  - Multi-select UI with available metrics (e.g., Talk-Listen Ratio, Script Adherence, Sentiment, Silence %)
  - Short descriptions/help text for each metric
  - Default preset applied automatically when no selection is made
- Backend (FastAPI):
  - Endpoint parameter in `POST /jobs/` to accept `metrics` array
  - Validation: only recognized metrics accepted
  - Store selected (or default) metrics in `jobs` collection
  - Stubs for metric aggregation (rep-level averages, team trends)
- Storage / Schema:
  - Extend `jobs` collection with:
```
{
  "job_id": "uuid",
  "metrics": ["talk_listen_ratio", "script_adherence", "sentiment"]
}
```

### Steps
- Define Available Metrics
  - Create a static config file (e.g., `metrics_config.json`) listing all metrics, IDs, and descriptions.
  - Mark subset as `default: true`.
- Frontend
  - Implement multi-select dropdown bound to metrics config.
  - Show tooltips or inline text with metric definitions.
  - If user skips selection → apply defaults automatically.
- Backend
  - Extend job creation to accept metrics list.
  - Validate against metrics config (reject invalid entries).
  - Save validated metrics in job metadata.
- Aggregation Hooks (stubs)
  - Define interfaces for rep-level/team-level aggregations (to be filled in later).
  - Example:
```
def aggregate_metrics(jobs: List[Dict], level="rep"):
    # placeholder for future leaderboard/trend calculations
    return {}
```

### Acceptance Criteria
- User can select one or more metrics via UI; defaults applied if none selected.
- Selected metrics appear in job config in MongoDB.
- Backend rejects unknown/invalid metrics gracefully.
- Aggregation stub functions exist for future analytics expansion.

### Dependencies
- Task002 → Frontend upload & UI.
- Task004 → Job metadata tracking.