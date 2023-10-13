from pydantic import BaseModel, Field
from typing import Any, Dict, List, Literal, Optional, Union


class response_status(BaseModel):
    """
    响应状态
    """

    status: int


class Wechatsentece(BaseModel):
    """
    文本消息
    """

    message: str
    name: str
