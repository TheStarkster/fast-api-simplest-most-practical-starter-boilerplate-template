from fastapi import FastAPI
from routes.routes import router as api_router

app = FastAPI(title="Audio-to-Video Generator")

# Routers
app.include_router(api_router, prefix="/api")
