## Technical PRD: Multi-Modal Sales Conversation Analytics (POC)

| ID | Technical Requirement | Description | Acceptance Criteria | Notes |
| --- | --- | --- | --- | --- |
| TR001 | File Upload UI | Streamlit upload box for audio, video, transcript, and script files | User can upload via drag & drop / button; progress & error messages visible | Supported formats: .wav, .mp3, .mp4, .txt, .md |
| TR002 | File Validation | Validate file type and size before saving | Invalid uploads are rejected with clear error messages | Configurable limits (default: 100MB) |
| TR003 | Storage Adapter | Save files locally in structured folders by type | Files stored with unique names; directories consistent | Future extension to cloud storage |
| TR004 | Metadata Tracking | Track files, jobs, and progress in MongoDB | Job status visible (Uploading → Transcribing → Analyzing → Complete/Failed) | MongoDB local instance |
| TR005 | Script Upload | Allow uploading of sales scripts / playbooks | .txt and .md accepted; linked to analysis jobs | Multiple scripts allowed |
| TR006 | Metric Selection | Let users select analysis metrics before processing | Metrics shown in list; multi-select works; defaults applied | Example metrics: talk ratio, adherence, empathy |
| TR007 | Analysis Trigger | Start backend pipeline only when inputs valid | “Analyze” button enabled only if valid uploads & selections | Job ID generated |
| TR008 | Transcription | Convert audio/video to text | STT baseline (Whisper) works with acceptable WER | Runs within target latency for 30-min file |
| TR009 | NLP Metrics | Run text against selected metrics | Metrics computed and stored in MongoDB | Uses LangChain + OpenAI/Vertex LLMs |
| TR010 | Script Adherence | Compare transcript vs. uploaded scripts | Coverage % and missing/extra parts flagged | Evidence spans shown |
| TR011 | Insights Generation | Summarize 3–5 key insights per call | Insights stored in Mongo and shown on dashboard | Focus: objections, CTAs, next steps |
| TR012 | Dashboard | Display per-call diagnostics | Charts render correctly; export option available | Built with Plotly/Altair in Streamlit |
| TR013 | History & Filters | Allow browsing/filtering past analyses | User can view history list and filter by date/rep | Pagination required |
| TR014 | Exports | Support CSV and PDF downloads | Files generated and downloadable per report | Configurable export options |
| TR015 | Error Handling | Transparent error handling in frontend/backend | User-friendly messages; Job ID provided | Logs retained |
| TR016 | Observability | Logging and tracing for analysis jobs | Structured logs + spans in Langfuse | End-to-end traceability |
| TR017 | Background Tasks | Run transcription & analysis asynchronously | Backend processes jobs without blocking | FastAPI background tasks |
| TR018 | Orchestration | Start all services with one command | make up runs backend (8000), frontend (3000), and MongoDB local | Python 3.12 baseline environment 
| TR019 | File Preview          | Provide basic preview/summary of uploaded transcript/audio metadata | User can see filename, size, and type before analysis        | Audio length or transcript snippet |
| TR020 | Progress Polling      | Frontend polls MongoDB for job status                               | Status updates visible in near real-time                     | Uses Mongo metadata store          |
| TR021 | Leaderboard & Trends  | Display rep/team leaderboard and simple trend views                 | Users can view aggregated metrics by rep/team                | Basic aggregation functions        |
| TR022 | Drill-Down            | Link metrics to transcript segments & timestamps                    | Clicking metric highlights relevant transcript parts         | Evidence spans displayed           |
| TR023 | Performance Targets   | Ensure latency and accuracy thresholds                              | 30-min call processed within T secs; WER ≤ baseline          | POC acceptance gate                |
| TR024 | Risk Handling         | Implement safeguards for noisy audio, LLM drift                     | Preprocessing + prompt constraints applied                   | Confidence scores/logging          |
| TR025 | Folder Structure      | Maintain predefined directories per file type                        | Files saved in `preprocess_chat/`, `preprocess_voice/`, etc. | Matches Table 3                    |
| TR026 | Report Navigation     | Allow toggling between current and previous reports                 | User can switch sessions from dashboard                      | History persisted                  |