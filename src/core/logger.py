import logging
from logging.handlers import RotatingFileHandler
import os
from http import HTTPStatus
from fastapi import Request
from fastapi.responses import JSONResponse

# create logs directory if not exist
os.makedirs("logs", exist_ok=True)

# logger settings
log_format = "%(asctime)s [%(levelname)s] %(message)s"

logger = logging.getLogger("api_logger")
logger.setLevel(logging.INFO)

# console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter(log_format))
logger.addHandler(console_handler)

# file handler
file_handler = RotatingFileHandler("logs/api.log", maxBytes=5*1024*1024, backupCount=3)
file_handler.setFormatter(logging.Formatter(log_format))
logger.addHandler(file_handler)


async def logger_middleware(request: Request, call_next):
    method = request.method
    path = request.url.path

    try:
        response = await call_next(request)
        status_code = response.status_code

    except Exception as e:
        status_code = 500
        logger.exception(f"Unhandled exception in route {method} {path}: {str(e)}")
        return JSONResponse(
            status_code=500,
            content={"detail": "Internal Server Error"}
        )

    status_phrase = HTTPStatus(status_code).phrase if status_code in HTTPStatus._value2member_map_ else ""
    logger.info(f"{method} {path} -> {status_code} {status_phrase}")
    return response