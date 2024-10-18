from fastapi import APIRouter

from .auth import router as auth_router
from .users import router as users_router
from .messages import router as messages_router


router = APIRouter()

router.include_router(auth_router,     prefix="/auth",     tags=["AUTH"])
router.include_router(users_router,    prefix="/users",    tags=["USERS"])
router.include_router(messages_router, prefix="/messages", tags=["MESSAGES"])
