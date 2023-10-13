import httpx
import asyncio
import os
import time


class AccessTokenManager:
    async def __init__(self):
        self.id = os.environ.get("wxqy_id")
        self.secret = os.environ.get("wxqy_secret")
        self.expire_time = None

    async def get_token(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={self.id}&corpsecret={self.secret}"
        token_time = time.time()
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            data = response.json()
        if data["errcode"] == 0:
            # 获取token 日期
            self.expire_time = data["expires_in"] + token_time
            self.token = data["access_token"]
        else:
            raise Exception(f'出现错误：{data["errmsg"]}')

    async def token_manager(self):
        if self.expire_time == None or time.time() > self.expire_time:
            await self.get_token()
        return self.token
