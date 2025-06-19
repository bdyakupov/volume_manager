from fastapi import FastAPI
from src.core.setup import lifespan
from src.volumes.router import router as volume_router
from src.core.logger import logger_middleware
from starlette.middleware.base import BaseHTTPMiddleware


# FastAPI app
app = FastAPI(lifespan=lifespan)

# add logging middleware
app.add_middleware(BaseHTTPMiddleware, dispatch=logger_middleware)

app.include_router(volume_router)
