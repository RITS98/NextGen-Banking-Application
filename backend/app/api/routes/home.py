from fastapi import APIRouter
from app.core.logging import get_logger

logger = get_logger()
router = APIRouter(
    prefix="/home"
)


@router.get("/")
def home():
    logger.info("Home Page accessed !!")
    return {
        "message": "Welcome to NextGen Bank",
    }