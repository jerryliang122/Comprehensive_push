import requests
import json
from api.sql import DB , token
from sqlalchemy.orm import sessionmaker
import datetime


class wecat_token(DB):
    def __init__(self):
        super().__init__()
        data = json.loads(open('conf/wechat.json', 'r', encoding='utf-8').read())
        self.wecom_cid = data['wecom_cid']
        self.wecom_secre = data['wecom_secre']
        self.wecom_aid = data['wecom_aid']
        self.wecom_touid = data['wecom_touid']
        Session  = sessionmaker(bind=self.engine)
        self.session = Session()
    
    # 获取token
    def get_token(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={}&corpsecret={}'.format(self.wecom_cid, self.wecom_secre)
        r = requests.get(url)
        #检查是否已经存在数据
        if self.session.query(token).filter(token.id == 1).count() == 0:
            #写入数据库
            self.session.add(token(1,r.json()['access_token'],datetime.datetime.now()))
        else:
            #更新数据库
            self.session.query(token).filter(token.id == 1).update({token.access_token:r.json()['access_token'],token.expiration_time:datetime.datetime.now()})
        self.session.commit()
        return r.json()['access_token']
    
    # 检查token是否过期
    def check_token(self):
        tokern = self.session.query(token).filter(token.id == 1).first()
        if tokern.expiration_time < datetime.datetime.now():
            return self.get_token()
        return tokern.access_token
    # 发送消息
    def send_msg(self,msg):
        token = self.check_token()
        url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}'.format(token)
        data = {
            "touser": self.wecom_touid,
            "msgtype": "text",
            "agentid": self.wecom_aid,
            "text": {
                "content": msg
            },
            "safe": 0
        }
        r = requests.post(url,json.dumps(data))
        return r.json()
    
 

        
        