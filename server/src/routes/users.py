from fastapi import APIRouter

from docs import UserDocs


router = APIRouter()


@router.post("", **UserDocs.POST.user)
async def create_user():
    ...


@router.get("", **UserDocs.GET.users)
async def get_users():
    ...


@router.get("/{user_name}", **UserDocs.GET.user)
async def get_user_info():
    ...


@router.patch("/{user_name}", **UserDocs.PATCH.user)
async def update_user_info():
    ...


@router.delete("/{user_name}", **UserDocs.DELETE.user)
async def update_user():
    ...
