from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from uuid import uuid4
from app.utils.logger import logger

class RequestIDMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_id = str(uuid4())
        request.state.request_id = request_id
        logger.info(f"[{request_id}] Incoming request: {request.method} {request.url.path}")
        response = await call_next(request)
        response.headers["X-Request-ID"] = request_id
        return response
