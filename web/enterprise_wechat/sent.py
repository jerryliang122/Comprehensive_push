from fastapi import APIRouter
from config import Wechatsentece, response_status


router = APIRouter()


@router.get("/", response_model=response_status)
async def read_root(requset: Wechatsentece):
    # 获取参数
    name = requset.name
    message = requset.message
    # 发送到后端
