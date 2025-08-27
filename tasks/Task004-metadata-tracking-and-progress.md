## Task004: Metadata Tracking and Progress Updates

**Related TRs**: TR004, TR020, TR026

### Objective
- Implement metadata tracking for files and processing jobs in MongoDB.
- Allow the frontend to poll and display real-time job progress through defined stages.
- Provide clear job visibility from upload → processing → completion/failure.

### Deliverables
- MongoDB collections:
  - `files` → Stores metadata of each uploaded file: `file_id`, `original_name`, `stored_path`, `type`, `size`, `upload_time`, `status`.
  - `jobs` → Tracks progress of processing pipelines: `job_id`, `related_file_ids`, `current_stage`, `stages_history`, `created_at`, `updated_at`.
- Backend API endpoints (FastAPI):
  - `POST /jobs/` → create new job record when file upload starts
  - `PATCH /jobs/{job_id}` → update job stage/status
  - `GET /jobs/{job_id}` → fetch latest job status
  - `GET /jobs/{job_id}/timeline` → (optional) return full status history
- Frontend (Streamlit) integration:
  - Polls `/jobs/{job_id}` every X seconds (configurable)
  - Displays progress (Uploading → Transcribing → Analyzing → Completed/Failed)

### Steps
- Schema Definition
  - `jobs` collection schema:
```
{
  "job_id": "uuid",
  "related_file_ids": ["file_uuid1", "file_uuid2"],
  "current_stage": "Transcribing",
  "stages_history": [
    {"stage": "Uploading", "timestamp": "2025-08-27T12:00:00Z"},
    {"stage": "Transcribing", "timestamp": "2025-08-27T12:05:00Z"}
  ],
  "status": "InProgress",
  "created_at": "...",
  "updated_at": "..."
}
```
- Backend Implementation (FastAPI)
  - Service layer for job lifecycle (`create_job`, `update_stage`, `get_job`)
  - Ensure idempotency (repeated updates don’t corrupt state)
  - Auto-update `updated_at` timestamp on stage change
- Integration with Task003 (Storage)
  - When file is saved → `files` collection updated
  - When processing starts → `jobs` entry created
  - Each pipeline step (ASR, analysis, report generation) triggers `update_stage`
- Frontend Polling (Streamlit)
  - Use polling interval (default 5s, configurable)
  - Show status bar / progress indicator
  - Handle errors gracefully (e.g., Failed state with error message)

### Acceptance Criteria
- Every uploaded file has metadata stored in `files` collection.
- Each job has a unique `job_id` and reflects correct processing stage.
- Stage transitions are timestamped and visible in MongoDB.
- Frontend shows updated status within polling interval.
- Failed jobs clearly display error reason.

### Dependencies
- Task001 → Local dev & MongoDB setup.
- Task003 → Storage adapter for uploaded files.
- Task002 → Frontend upload flow.