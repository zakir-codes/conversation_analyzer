# Sales Analyzer - POC

## Requirements
- Python 3.12
- Local MongoDB (default localhost:27017)
- make

## Setup
```
make up
```
This installs backend and frontend requirements (user site), creates `.env` if missing, and starts:
- FastAPI backend on http://localhost:8000 (docs at /docs)
- Streamlit frontend on http://localhost:3000

## Stop
```
make down
```

## Restart
```
make restart
```

### Env
A minimal `.env` is auto-created with:
- `MONGODB_URI`
- `APP_NAME`

### Storage layout
See `storage/` folders created for uploaded/processed files.

