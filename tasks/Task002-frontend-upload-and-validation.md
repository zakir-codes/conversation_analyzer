## Task002: Frontend Upload UI and File Validation

**Related TRs**: TR001, TR002, TR019, TR030

### Objective
- Provide a Streamlit upload interface for audio, video, transcripts, and scripts.
- Enforce file validation (type, size) with clear feedback.
- Offer a simple preview for uploaded files to improve user confidence before analysis.

### Deliverables
- Streamlit Upload Page (under `frontend/pages/upload.py`).
- Upload box supporting drag & drop + button.
- Config-driven validation: allowed extensions & max file size.
- Preview panel showing filename, size, type, and basic metadata (e.g., duration for audio/video, snippet for transcript).
- Progress/success/failure messaging in the UI.

### Steps
- UI Setup
  - Add Upload page in Streamlit app navigation.
  - Use `st.file_uploader()` with support for multiple file types.
- Validation
  - Read allowed extensions and size limit from `.env` / config (Task001 baseline).
  - Reject invalid uploads with red error message.
  - Show friendly error (e.g., “File too large. Max size = 100MB”).
- Preview
  - Display uploaded file’s name, size, type.
  - For transcripts (.txt / .md): show first 200 characters as snippet.
  - For audio/video: show file duration (if metadata available) or a placeholder note.
- Status Handling
  - On upload: show progress indicator (Uploading…).
  - On success: show green confirmation message.
  - On failure: show red error message.
- Integration Prep
  - Store metadata in frontend state to be passed later to backend APIs (Task003 onward).

### Acceptance Criteria
- Users can upload supported files (.wav, .mp3, .mp4, .txt, .md).
- Invalid uploads (wrong format/too large) → clear error message shown immediately.
- Successful uploads → preview displays filename, size, type, and basic metadata.
- Progress, success, and error messages visible and styled consistently.

### Dependencies
- Task001 (project setup, folder structure, and orchestration).
- Local config (`.env`) defines validation parameters (allowed extensions, max file size).