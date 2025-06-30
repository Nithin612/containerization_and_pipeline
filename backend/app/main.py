from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.routes.health import router as health_router

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Backend is running"}

app.include_router(health_router)
