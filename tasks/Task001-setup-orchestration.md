## Task001: Project Setup, Folder Structure, and Orchestration

**Related TRs**: TR018, TR025, TR034

### Objective
- Ensure reproducible local development with a predefined folder structure.
- One-command startup for backend, frontend, and MongoDB.
- Clear separation of backend (FastAPI), frontend (Streamlit), and infrastructure files.

### Deliverables
- Makefile with targets:
  - `make up` → starts backend (port 8000), frontend (port 3000), MongoDB (local)
  - `make down` → stops all services
  - `make restart` → restarts services
- Predefined directories for file storage and modular backend/frontend apps.
- Baseline repo structure with Python 3.12 environment + .env templates.

### Folder Structure
```
root/
│── backend/                          # FastAPI backend
│   ├── app/
│   │   ├── main.py                   # FastAPI entrypoint
│   │   ├── api/                      # API routes (upload, analyze, dashboard)
│   │   ├── services/                 # Business logic (transcription, NLP, metrics)
│   │   ├── models/                   # MongoDB schemas / Pydantic models
│   │   ├── storage/                  # File handling (adapters, local/cloud)
│   │   ├── utils/                    # Logging, helpers
│   │   └── __init__.py
│   ├── tests/                        # Backend unit tests
│   └── requirements.txt
│
│── frontend/                         # Streamlit frontend
│   ├── app.py                        # Streamlit entrypoint
│   ├── pages/                        # Streamlit multi-page support (Upload, Metrics, Dashboard)
│   ├── components/                   # Reusable UI components
│   ├── assets/                       # CSS, images, etc.
│   └── requirements.txt
│
│── storage/                          # Uploaded and processed files
│   ├── preprocess_chat/
│   ├── preprocess_voice/
│   ├── postprocess_files/
│   └── master_script/
│
│── .env                              # Local env vars
│── env.example                       # Example env vars
│── makefile                          # Orchestration (backend, frontend, Mongo)
│── readme.md                         # Project setup & usage guide
│── requirements.txt                  # Root-level requirements (if combined)
```

### Steps
- Create the above folder structure.
- Add placeholder files (`__init__.py`, `app.py`, `main.py`, etc.) to ensure imports work.
- Implement `make up`, `make down`, `make restart` commands:
  - Backend → FastAPI (uvicorn) on port 8000
  - Frontend → Streamlit on port 3000
  - MongoDB → local instance (default port)
- Document baseline setup:
  - Python 3.12 required
  - Install from `requirements.txt`
  - Copy `.env.example` → `.env` before running

### Acceptance Criteria
- Running `make up` spins up backend, frontend, and MongoDB locally without manual steps.
- All required folders exist and are writable (`storage/*`).
- Developer can open:
  - `http://localhost:3000` → Streamlit frontend
  - `http://localhost:8000/docs` → FastAPI Swagger UI
  - `mongodb://localhost:27017` → Mongo instance accessible

### Dependencies
- Python 3.12 installed
- Make installed (Linux/Mac) or WSL (Windows)
- Local MongoDB available (default configuration)