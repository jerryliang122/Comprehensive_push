from pydantic import BaseModel, Field
from typing import Any, Dict, List, Literal, Optional, Union


class Wechatsentece(BaseModel):
    """
    文本消息
    """

    message: str
    tousername: str
