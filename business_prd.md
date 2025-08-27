## Business PRD: Multi-Modal Sales Conversation Analytics (POC)

### 1) Feature Requirements (POC Backlog Format)
| ID | Feature Requirement (User Story) | Description | Acceptance Criteria | Priority | Notes |
| --- | --- | --- | --- | --- | --- |
| FR001 | As a user, I want a simple upload interface | Clean UI for audio, video, transcript, and script files. | - Upload button + drag & drop<br>- Progress and success/failure states | High | Formats: .wav, .mp3, .mp4, .txt |
| FR002 | As a user, I want file validation | Prevent invalid formats and oversized uploads. | - Clear error messaging<br>- Configurable size limits enforced | High | Admin-configurable |
| FR003 | As a user, I want reliable storage | Store uploaded files correctly and uniquely. | - Saved by type<br>- Unique filenames<br>- Directory mapping consistent | High | Local adapter (POC), extendable to cloud |
| FR004 | As a user, I want to upload playbooks/scripts | Provide rules/guidelines for adherence analysis. | - Accept .txt / .md<br>- Link to analysis jobs | High | Multiple scripts allowed |
| FR005 | As a user, I want to choose metrics | Select analysis metrics before running. | - List view<br>- Multi-select<br>- Preset defaults | High | Configurable presets |
| FR006 | As a user, I want to trigger analysis | Start processing when ready. | - Analyze button active only when valid<br>- Job created with ID | High | Background queue |
| FR007 | As a user, I want visibility into progress | Track real-time job states. | - Status: Uploading / Transcribing / Analyzing / Complete / Failed<br>- Updated via metadata store | High | MongoDB progress tracker |
| FR008 | As a user, I want accurate transcription | Convert audio to text reliably. | - Baseline word error rate (WER) met<br>- Processing within latency target | High | Whisper (POC baseline) |
| FR009 | As a user, I want script adherence scoring | Measure coverage against expected scripts. | - Coverage % displayed<br>- Missing/extra sections flagged | High | Evidence spans surfaced |
| FR010 | As a user, I want conversational quality metrics | Provide interaction analytics. | - Metrics include talk ratio, interruptions, empathy markers | High | Extendable metric library |
| FR011 | As a user, I want actionable insights | Summaries of call effectiveness. | - 3–5 key insights (objections, CTAs, next steps) | High | Structured output |
| FR012 | As a user, I want a diagnostics dashboard | Interactive per-call reporting. | - Dashboard loads<br>- Charts render correctly<br>- Export available | High | Plotly/Altair baseline |
| FR013 | As a manager, I want history and filters | Browse and filter previous analyses. | - History list<br>- Filter by date, rep, campaign | Medium | Pagination required |
| FR015 | As a user, I want robust error handling | Errors must be transparent and traceable. | - User-friendly messages<br>- Job ID provided | High | System + user logs |
| FR021 | As an engineer, I want observability | End-to-end tracing and monitoring. | - Structured logs<br>- Spans visible in Langfuse | High | Standardized logging |
| FR022 | As a user, I want exports | Download analysis results. | - CSV and PDF export available | Medium | Configurable formats |

### 2) Problem Statement & Use Cases
| Item | Details |
| --- | --- |
| Core problems (ranked) | 1) Lack of objective sales call metrics; 2) Script/compliance adherence gaps; 3) Manual review is time-consuming; 4) Hard to link behaviors to outcomes |
| Primary use cases (POC) | Upload → transcribe → analyze; compare rep behavior to scripts; generate coaching insights; track rep/team trends |
| Top user questions | Conversion likelihood; objection handling quality; engagement level (talk ratios, response time, sentiment shifts) |

### 3) Ingestion & Data Sources (POC Constraints)
| Item | Details |
| --- | --- |
| Modalities | .wav, .mp3, .mp4, .txt (baseline for POC) |
| Pipeline | Audio/video → transcription → NLP metrics → dashboard |

### 4) Metrics & Analytics Definitions
| Metric | Definition |
| --- | --- |
| Conversion Likelihood / Intent Score | Probability prospect moves to next stage |
| Objection Handling Quality | Effectiveness of response to concerns |
| Engagement Level | Talk ratio, latency of responses, sentiment trajectory |
| Script Adherence | Coverage of required sections in expected script |
| Conversation Quality | Empathy, interruptions, clarity, professionalism |

### 5) Reporting & Insights
| Item | Details |
| --- | --- |
| Dashboards | Per-call diagnostics; leaderboard by rep/team; simple trend views |
| Export/Share | CSV + PDF export; link sharing (future scope) |
| Drill-downs | Metrics linked to transcript segments and timestamps (audio snippet optional) |

### 6) Workflow & UX (aligned to flows)
| Flow Step | Key Questions |
| --- | --- |
| Page 1 – Upload | File size/type limits? Max concurrent uploads? Script scope (team vs campaign)? Quotas/retries? |
| Page 2 – Select metrics & analyze | Default presets? Save user presets? Standard status messages? Target time-to-first-result? |
| Page 3 – Diagnostics dashboard | Must-have widgets? Filters (rep/team/date)? Export options and supported formats? |

### 7) Success Criteria & Acceptance Tests (POC)
| Category | Criteria |
| --- | --- |
| Functional | Upload succeeds for N test files; WER ≥ baseline; metrics computed within T seconds for a 30-min call; actionable error messages delivered |
| User | ≥ X pilot users access dashboards weekly for 3 weeks; ≥ Y% of users report actionable coaching insights |
| Quality Gates | Data privacy enforced; PII handling verified; explicit user consent for recordings |

### 8) Model Strategy & Evaluation
| Item | Details |
| --- | --- |
| Vendors | OpenAI, Google Vertex, Whisper (baseline STT) integrated via LangChain |
| Fallbacks | Degraded mode if LLM unavailable (return transcription + basic metrics) |
| Evaluation | WER benchmarks + business relevance scoring of insights |

### 9) Dependencies & Constraints
| Area | Details |
| --- | --- |
| Tech Stack | Streamlit, FastAPI, Uvicorn, MongoDB, LangChain, Plotly/Altair, Langfuse |
| Access | API keys for model vendors; compute quotas (GPU/CPU) |
| People | Sales managers (pilot users), annotators (for evaluation), PM/engineer approvals |
| Timeline | Define POC end date; milestone 1 = ingestion + transcription; milestone 2 = metrics; milestone 3 = dashboard/reporting |

### 10) Risks & Mitigations
| Risk | Mitigation |
| --- | --- |
| Data quality (noise, accents, crosstalk) | Preprocessing, diarization, confidence scoring |
| Script/playbook drift | Version scripts + metric mappings |
| LLM hallucinations | Prompt constraints, retrieval-augmented adherence checks, evidence spans |
| Adoption risk | Tie insights directly to coaching/next steps; showcase quick wins in early pilot |