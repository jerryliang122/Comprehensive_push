# wechat/receive.py
from sanic import Blueprint
from sanic.response import text
import xml.etree.cElementTree as ET
import json5
from api.receive_WeChat.WXBizMsgCrypt3 import WXBizMsgCrypt
from api.action_response import judge
from threading import Thread

receive = Blueprint("receive", url_prefix="/receive")
# 读取comfig.json5文件
sToken = json5.load(open("wechat.json"))["sToken"]
sEncodingAESKey = json5.load(open("wechat.json"))["sEncodingAESKey"]
sCorpID = json5.load(open("wechat.json"))["wecom_cid"]
# 实例化WXBizMsgCrypt3类
wxcpt = WXBizMsgCrypt(sToken, sEncodingAESKey, sCorpID)


@receive.get("/receive")
async def receive_Verification(request):
    # 从请求中提取出微信服务器发送过来的参数
    msg_signature = request.args.get("msg_signature")
    timestamp = request.args.get("timestamp")
    nonce = request.args.get("nonce")
    echostr = request.args.get("echostr")
    # 进入验证环节
    ret, sEchoStr = wxcpt.VerifyURL(msg_signature, timestamp, nonce, echostr)
    return text(sEchoStr)


@receive.post("/receive")
async def receive_body(request):
    # 从请求中提取出微信服务器发送过来的参数
    body = request.body.decode("utf-8")
    msg_signature = request.args.get("msg_signature")
    timestamp = request.args.get("timestamp")
    nonce = request.args.get("nonce")
    ret, sMsg = wxcpt.DecryptMsg(body, msg_signature, timestamp, nonce)
    # 解析xml
    xml_tree = ET.fromstring(sMsg)
    # 获取消息内容
    content = xml_tree.find("Content").text
    # 获取发送人
    FromUserName = xml_tree.find("FromUserName").text
    # 使用多线程发送给后端响应装置
    Thread(target=judge, args=(content, FromUserName)).start()
    return text("success")
