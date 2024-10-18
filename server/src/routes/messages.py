from fastapi import APIRouter

from docs import MessageDocs


router = APIRouter()


@router.post("", **MessageDocs.POST.message)
async def create_message():
    ...


@router.get("", **MessageDocs.GET.messages)
async def get_msg_history():
    ...
