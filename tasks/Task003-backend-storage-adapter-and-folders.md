## Task003: Backend Storage Adapter and Folder Mapping

**Related TRs**: TR003, TR025, TR030

### Objective
- Implement a backend storage adapter that saves uploaded files into structured folders by type.
- Support additional folders for diagnostic reports and processed audio transcripts.
- Ensure safe writes with unique filenames and consistent directory mapping.

### Deliverables
- `backend/app/storage/adapter.py` → storage adapter implementation.
- Updated folder mapping rules:
  - Audio (raw uploads) → `storage/preprocess_voice/`
  - Transcript (raw text uploads) → `storage/preprocess_chat/`
  - Scripts (reference/expected scripts) → `storage/master_script/`
  - Processed audio (transcribed outputs) → `storage/processed_voice/`
  - Diagnostic reports & analysis outputs → `storage/postprocess_files/`
- Unique filename generator with timestamp + UUID.
- Config-driven limits (file size, allowed types).

### Steps
- Module Setup
  - Create `backend/app/storage/adapter.py`.
  - Define `save_file(file, category)` that:
    - Validates type & size
    - Maps file to correct directory
    - Generates safe, unique filename
    - Writes file to disk safely
- Config Integration
  - Load allowed file types and size limits from `.env` / config.
  - Ensure values align with frontend validation (Task002).
- Unique Naming
  - Use filename pattern: `<category>_<timestamp>_<uuid>.<ext>`.
  - Check for collisions before saving.
- Safe Write & Error Handling
  - Ensure folders exist (auto-create if missing).
  - Return structured JSON response:
```
{
  "path": "storage/preprocess_voice/audio_20250827_abc123.wav",
  "filename": "audio_20250827_abc123.wav",
  "status": "success"
}
```
  - Log errors with request ID/job ID for traceability.
- Integration Prep
  - Expose adapter functions via backend service layer.
  - Return metadata for MongoDB insert (Task004).

### Acceptance Criteria
- Uploaded files are stored in correct mapped folders.
- Filenames are unique (no overwrites, no collisions).
- Size/type validation is enforced at backend.
- Processed audio transcripts are stored under `processed_voice/`.
- Diagnostic reports & results are stored under `postprocess_files/`.

### Dependencies
- Task001 → Project setup & folder creation.
- Task002 → Upload UI passes files to backend API.