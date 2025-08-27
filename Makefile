ROOT := $(CURDIR)
PYTHON := $(shell if [ -x "$(ROOT)/venv/bin/python" ]; then echo "$(ROOT)/venv/bin/python"; else command -v python3; fi)
BACKEND_DIR := backend
FRONTEND_DIR := frontend
ENV_FILE := .env
BACKEND_PORT := 8000
FRONTEND_PORT := 8501

.PHONY: up down restart install-backend install-frontend ensure-env

ensure-env:
	@if [ ! -f $(ENV_FILE) ]; then \
		echo "Creating $(ENV_FILE) from template"; \
		echo "MONGODB_URI=mongodb://localhost:27017/sales_analyzer" > $(ENV_FILE); \
		echo "APP_NAME=Sales Analyzer Backend" >> $(ENV_FILE); \
	fi

install-backend:
	cd $(BACKEND_DIR) && "$(PYTHON)" -m pip install -r requirements.txt

install-frontend:
	cd $(FRONTEND_DIR) && "$(PYTHON)" -m pip install -r requirements.txt

up: ensure-env install-backend install-frontend
	@echo "Starting backend on :$(BACKEND_PORT)"
	@bash -lc 'cd $(BACKEND_DIR) && nohup "$(PYTHON)" -m uvicorn app.main:app --host 0.0.0.0 --port $(BACKEND_PORT) > ../backend.out 2>&1 & echo $! > ../backend.pid'
	@echo "Starting frontend on :$(FRONTEND_PORT)"
	@bash -lc 'cd $(FRONTEND_DIR) && nohup "$(PYTHON)" -m streamlit run app.py --server.headless true --server.port $(FRONTEND_PORT) --server.address 0.0.0.0 --browser.serverAddress localhost --browser.gatherUsageStats false --server.enableCORS false --server.enableXsrfProtection false > ../frontend.out 2>&1 & echo $! > ../frontend.pid'
	@echo "Ensure MongoDB is running locally on default port (27017)."

down:
	@echo "Stopping backend (if running)"
	@if [ -f backend.pid ]; then \
		kill `cat backend.pid` || true; \
		rm -f backend.pid; \
	else \
		BACK_PIDS=$$(lsof -t -i :$(BACKEND_PORT) 2>/dev/null | tr '\n' ' '); \
		if [ -n "$$BACK_PIDS" ]; then echo "Killing backend on port $(BACKEND_PORT): $$BACK_PIDS"; kill $$BACK_PIDS || true; fi; \
	fi
	@echo "Stopping frontend (if running)"
	@if [ -f frontend.pid ]; then \
		kill `cat frontend.pid` || true; \
		rm -f frontend.pid; \
	else \
		FRONT_PIDS=$$(lsof -t -i :$(FRONTEND_PORT) 2>/dev/null | tr '\n' ' '); \
		if [ -n "$$FRONT_PIDS" ]; then echo "Killing frontend on port $(FRONTEND_PORT): $$FRONT_PIDS"; kill $$FRONT_PIDS || true; fi; \
	fi

restart: down up


