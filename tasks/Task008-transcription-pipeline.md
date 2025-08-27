## Task008: Transcription Pipeline (Whisper via LangChain)

**Related TRs**: TR008, TR023, TR024

### Objective
- Convert audio/video into text using OpenAI Whisper API orchestrated via LangChain.
- Meet baseline WER (Word Error Rate) and acceptable latency for POC.
- Provide an extensible pipeline that can later plug in alternatives (WhisperX, local models).

### Deliverables
- Transcription module integrated with job worker.
- LangChain wrapper to call OpenAI Whisper API with configurable parameters (model, temperature, chunk size).
- Preprocessing:
  - Extract audio from video (`ffmpeg`).
  - Normalize audio format (mono, sample rate).
- Storage: save transcript text and metadata (timestamps, model used, latency).
- Link transcript path + metadata to job record in MongoDB.

### Steps
- Audio Extraction & Preprocessing
  - Detect if uploaded file is audio or video.
  - If video → extract audio using `ffmpeg`.
  - Convert audio to Whisper-compatible format (WAV, 16kHz mono).
- LangChain Whisper Integration
  - Use `langchain-openai` (e.g., ChatOpenAI or Whisper wrapper).
  - Configure model via env vars (e.g., `WHISPER_MODEL=whisper-1`).
  - Support chunking for long audio files (LangChain document loaders).
- Transcription Call
  - Call OpenAI Whisper API via LangChain pipeline.
  - Collect transcript + optional metadata (confidence, tokens, segments).
- Storage & Linking
  - Save transcript as `.txt`/`.json` under `processed_voice/`.
  - Insert transcript metadata (job_id, file path, duration, latency, model version) in MongoDB.
- Metrics & Logging
  - Record processing latency (start_time, end_time).
  - Capture quality metrics if available (confidence, segment breakdown).
  - Stub for later WER comparison against ground truth (for eval).

### Acceptance Criteria
- A 30-minute audio/video file is transcribed via Whisper API in ≤ target latency (T).
- Transcript stored under `processed_voice/` and linked to correct job in DB.
- Job record updated with transcript metadata.
- Errors (e.g., API timeout, audio too long) are captured and reflected in job status.

### Dependencies
- Task003 → Storage directories (`processed_voice/` + transcripts).
- Task007 → Background job orchestration.