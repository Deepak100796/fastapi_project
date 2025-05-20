from fastapi import APIRouter, HTTPException, status, Request
from uuid import uuid4
from app.schemas.user_schema import User
from app.utils.logger import logger

router = APIRouter()

# In-memory database
users = {}

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user: User, request: Request):
    user_id = str(uuid4())
    users[user_id] = user
    logger.info(f"[{request.state.request_id}] Created user: {user_id}")
    return {"id": user_id, **user.dict()}

@router.get("/{user_id}")
def get_user(user_id: str, request: Request):
    if user_id not in users:
        logger.warning(f"[{request.state.request_id}] User not found: {user_id}")
        raise HTTPException(status_code=404, detail="User not found")
    logger.info(f"[{request.state.request_id}] Fetched user: {user_id}")
    return {"id": user_id, **users[user_id].dict()}

@router.put("/{user_id}")
def update_user(user_id: str, user: User, request: Request):
    if user_id not in users:
        logger.warning(f"[{request.state.request_id}] Cannot update. User not found: {user_id}")
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id] = user
    logger.info(f"[{request.state.request_id}] Updated user: {user_id}")
    return {"id": user_id, **user.dict()}

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: str, request: Request):
    if user_id not in users:
        logger.warning(f"[{request.state.request_id}] Cannot delete. User not found: {user_id}")
        raise HTTPException(status_code=404, detail="User not found")
    del users[user_id]
    logger.info(f"[{request.state.request_id}] Deleted user: {user_id}")
    return
