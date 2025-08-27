## Task005: Script Upload and Job Linking

**Related TRs**: TR005, TR010

### Objective
- Enable uploading of reference scripts/playbooks (e.g., `.txt`, `.md`) to be used in adherence analysis.
- Provide a mechanism to link a script to a processing job so the analysis stage knows which rules or playbook to check against.

### Deliverables
- Frontend (Streamlit):
  - Upload widget for `.txt`/`.md` scripts
  - Script selection dropdown when starting a job
- Backend (FastAPI):
  - Endpoint to upload and persist script files
  - Store metadata in MongoDB (`scripts` collection)
  - Support linking a script to a job at job creation
- Storage:
  - Scripts saved to `master_script/` folder with unique filenames

### Steps
- Frontend
  - Extend upload UI with a new “Upload Script” option
  - Validate scripts for type/size
  - Show uploaded scripts in a list of available scripts
  - Add dropdown to select a script when creating an analysis job
- Backend
  - Implement `POST /scripts/` → upload a script
  - Implement `GET /scripts/` → list all available scripts with metadata
  - Extend `POST /jobs/` to accept `script_id` (optional) to link a job with a chosen script

### MongoDB Schema
- `scripts` collection:
```
{
  "script_id": "uuid",
  "name": "onboarding_playbook.md",
  "path": "master_script/onboarding_playbook_<uuid>.md",
  "upload_time": "2025-08-27T10:00:00Z",
  "version": 1,
  "status": "active"
}
```
- `jobs` collection extended with:
```
{
  "job_id": "uuid",
  "script_id": "uuid (nullable)"
}
```

### Integration
- When analysis starts, pipeline retrieves the linked script from MongoDB + storage.
- Future-ready for script versioning (e.g., multiple revisions of the same playbook).

### Acceptance Criteria
- Scripts upload successfully into `master_script/` and metadata stored in `scripts` collection.
- Scripts are visible in frontend selection list.
- A selected script is linked to the job config (`script_id` stored in job metadata).
- Jobs without script selection proceed without adherence analysis.

### Dependencies
- Task002 → Frontend upload UI.
- Task003 → Storage adapter for saving files.
- Task004 → Job metadata tracking.