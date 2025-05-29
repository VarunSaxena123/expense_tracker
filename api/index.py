import sys
import os
from pathlib import Path

current_dir = Path(_file_).parent
parent_dir = current_dir.parent
sys.path.insert(0, str(parent_dir))

try:
    from expense_tracker_backend.main import app
    
except ImportError as e:
    from fastapi import FastAPI
    from fastapi.responses import JSONResponse
    
    app = FastAPI(title="Expense Tracker API")
    
    @app.get("/")
    def read_root():
        return {"message": "Expense Tracker API is running", "error": f"Import error: {str(e)}"}
    
    @app.get("/api/health")
    def health_check():
        return {"status": "healthy", "message": "API is working"}

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from fastapi import FastAPI
from fastapi.routing import APIRoute

def add_api_prefix():
    routes = []
    for route in app.routes:
        if isinstance(route, APIRoute):
            if not route.path.startswith("/api"):
                route.path = "/api" + route.path
                route.path_regex = route.path_regex

handler = app