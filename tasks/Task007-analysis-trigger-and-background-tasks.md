## Task007: Analysis Trigger and Background Processing

**Related TRs**: TR007, TR017

### Objective
- Kick off the analysis pipeline once all required inputs are ready.
- Ensure processing runs asynchronously so the UI is never blocked.
- Track failures and progress via job status updates.

### Deliverables
- Frontend (Streamlit):
  - “Analyze” button enabled only when all required inputs (file + script + metrics) are valid
  - Button click calls backend to create job and trigger analysis
  - Display returned `job_id` immediately for status polling
- Backend (FastAPI):
  - `POST /jobs/analyze` endpoint to create a new job with config (files, script, metrics)
  - Enqueue background task (FastAPI BackgroundTasks; Celery/RQ stub for future scaling)
  - Worker updates status timeline in MongoDB
- Database (MongoDB):
  - Store `job_id`, config, timestamps, and job status progression (Uploading → Validating → Processing → Completed/Failed)

### Steps
- Frontend
  - Add “Analyze” button to UI
  - Keep button disabled until file(s), script, and metrics are selected
  - On click: `POST` job request → receive `job_id`
  - Pass `job_id` to polling mechanism (Task004)
- Backend Endpoint
  - Accept job creation request with config (files, script, metrics)
  - Validate required inputs exist
  - Insert initial job record in MongoDB (status = `QUEUED`)
  - Trigger background task with `job_id`
- Background Worker
  - Process job asynchronously
  - Validate files exist in storage
  - Run stubbed pipeline steps (transcription, metric calculation)
  - Update status at each stage
  - On success → set status = `COMPLETED`
  - On error → set status = `FAILED` with error details
- Error Handling
  - Capture exceptions in background job
  - Store `error_message` in job record for frontend display

### Acceptance Criteria
- “Analyze” button activates only when all required inputs are valid.
- Clicking button triggers backend job creation and returns `job_id`.
- Job runs in background without blocking frontend.
- MongoDB shows job progressing through statuses.
- Errors/failures are captured and shown in job status.

### Dependencies
- Task004 → Job tracking schema and status updates.
- Task006 → Metrics selection in job config.