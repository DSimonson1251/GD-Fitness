#!/usr/bin/env bash
set -euo pipefail

# Run the FastAPI app with uvicorn
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
