# wechat/receive.py
from sanic import Blueprint
from sanic.response import text
import json5
from api.receive_WeChat.WXBizMsgCrypt3 import WXBizMsgCrypt

receive = Blueprint("receive", url_prefix="/receive")
# 读取comfig.json5文件
sToken = json5.load(open("wechat.json"))["sToken"]
sEncodingAESKey = json5.load(open("wechat.json"))["sEncodingAESKey"]
sCorpID = json5.load(open("wechat.json"))["wecom_cid"]


@receive.get("/receive")
async def receive(request):
    # 从请求中提取出微信服务器发送过来的参数
    msg_signature = request.args.get("msg_signature")
    timestamp = request.args.get("timestamp")
    nonce = request.args.get("nonce")
    echostr = request.args.get("echostr")
    # 实例化WXBizMsgCrypt3类
    wxcpt = WXBizMsgCrypt(sToken, sEncodingAESKey, sCorpID)
    # 进入验证环节
    ret, sEchoStr = wxcpt.VerifyURL(msg_signature, timestamp, nonce, echostr)
    return text(sEchoStr)
