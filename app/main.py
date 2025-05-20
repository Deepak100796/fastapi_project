from fastapi import FastAPI
from app.middleware.request_id import RequestIDMiddleware
from app.routes.user_routes import router as user_router

app = FastAPI()

# Add custom request ID middleware
app.add_middleware(RequestIDMiddleware)

# Include user-related APIs
app.include_router(user_router, prefix="/users", tags=["Users"])

@app.get("/health")
def health_check():
    return {"status": "ok"} 
