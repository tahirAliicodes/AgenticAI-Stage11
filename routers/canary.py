# routers/canary.py
# Canary release router - handles version routing

from fastapi import APIRouter
from canary_config import get_version, STABLE_VERSION, CANARY_VERSION, CANARY_PERCENTAGE

router = APIRouter()

@router.get("/version")
def get_app_version():
    """Returns current stable version"""
    return {
        "version": STABLE_VERSION,
        "status": "stable"
    }

@router.get("/canary/version/{user_id}")
def get_user_version(user_id: int):
    """
    ELI5: Check which version THIS user gets.
    user_id % 10 == 0 means canary (10% of users)
    """
    version = get_version(user_id)
    return {
        "user_id": user_id,
        "version": version,
        "is_canary": version == CANARY_VERSION,
        "message": f"You are on version {version}"
    }

@router.get("/canary/status")
def canary_status():
    """Shows canary release status"""
    return {
        "canary_enabled": True,
        "stable_version": STABLE_VERSION,
        "canary_version": CANARY_VERSION,
        "canary_percentage": CANARY_PERCENTAGE,
        "description": f"{CANARY_PERCENTAGE}% of users get v{CANARY_VERSION}"
    }
