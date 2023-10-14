import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import web.enterprise_wechat.sent as sent

# 读取web中的sent
app = FastAPI()
app.include_router(sent.router, prefix="/wechat", tags=["emterprise_wechat"])


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)
