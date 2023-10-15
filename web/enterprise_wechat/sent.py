from fastapi import APIRouter, Query
from config import Wechatsentece, response_status
import api.wechat.message as messages

router = APIRouter()


@router.get("/", response_model=response_status)
async def read_root(name: str = Query(...), message: str = Query(...)):
    # 发送到后端
    res = messages.sent_message()
    data = await res.send_text_message(name, message)
    if data == False:
        return {"code": 400, "msg": "发送失败"}
    else:
        return {"code": 200, "msg": "发送成功"}
