""" 
FastAPI App
"""
from fastapi import FastAPI
from typing import Dict

app = FastAPI()

@app.get("/")
def root() -> Dict[str, str]:
    """Root endpoint that returns a greeting message"""
    return {"message": "Hello World"}

@app.get("/health")
def health_check() -> Dict[str, str]:
    """Health check endpoint"""
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)