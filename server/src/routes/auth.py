from fastapi import APIRouter

from docs import AuthDocs


router = APIRouter()


@router.post("/login", **AuthDocs.POST.login)
async def login():
    ...


@router.post("/logout", **AuthDocs.POST.logout)
async def logout():
    ...
