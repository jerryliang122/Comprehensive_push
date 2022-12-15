import json
import requests
import sqlalchemy

# 获取access_token
def get_access_token():
    # sqlalchemy连接到数据库
    engine = sqlalchemy.create_engine('mysql+pymysql://root:123456@localhost:3306/wechat?charset=utf8')
    
    # 从数据库中获取access_token
    
# 推送到对应的微信机器人
def push_wechat(text):
