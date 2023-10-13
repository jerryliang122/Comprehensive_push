import httpx
import os
from api.wechat.accesstoken import AccessTokenManager


class sent_message:
    async def __init__(self):
        token = AccessTokenManager()
        self.token = await token.token_manager()
        self.wecom_aid = os.environ.get("wecom_aid")

    async def send_text_message(self, name, text):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={self.token}"
        data = {
            "touser": name,
            "msgtype": "text",
            "agentid": self.wecom_aid,
            "text": {"content": text},
            "safe": 0,
        }
        # POST请求
        try:
            with httpx.AsyncClient() as client:
                response = await client.post(url, json=data)
                print(str(response.json()), flush=True)
                return True
        except Exception as e:
            print("出现发送错误:" + e, flush=True)
            return False
