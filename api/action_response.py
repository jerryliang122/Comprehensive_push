from api.wechat import wecat_token
import paramiko
import json5
from api.sql import DB
from sqlalchemy.orm import sessionmaker

# 路由器IPSET
class ipset(DB):
    # 初始化
    def __init__(self):
        self.config = json5.load(open("conf/ssh.json", "r", encoding="utf-8"))
        super().__init__()
        self.session = sessionmaker(bind=self.engine)

    # 查询ip是否存在
    def query_ip(self, type, ip):
        result = self.session.query(ipset).filter(ipset.ip == ip).count()
        if result == 0:
            return False
        result = self.session.query(ipset).filter(ipset.ip == ip).first()
        if result.ip == ip:
            return True

    # 添加ip进入数据库
    def add_ip(self, type, ip):
        try:
            if self.query_ip(type, ip) == True:
                return False
            self.session.add(ipset(type, ip))
            self.session.commit()
            return True
        except:
            return False

    # 删除ip
    def del_ip(self, type, ip):
        try:
            self.session.query(ipset).filter(ipset.type == type, ipset.ip == ip).delete()
            self.session.commit()
            return True
        except:
            return False

    # 回复
    def reply(self, FromUserName, text):
        # 调用微信发送插件
        wx = wecat_token()
        # 发送消息
        msg = wx.send_msg_text(text, FromUserName)

    # 向路由器添加IP
    def add_ip_to_router(self, type, ip, FromUserName):
        # 建立ssh连接
        router = paramiko.SSHClient()
        # 允许连接不在know_hosts文件中的主机
        router.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 调用connect方法连接服务器
        router.connect(
            hostname=self.config["ssh-1"]["host"],
            port=self.config["ssh-1"]["port"],
            username=self.config["ssh-1"]["user"],
            password=self.config["ssh-1"]["password"],
        )
        # 写入数据库
        if self.add_ip(type, ip) == True:
            # 回复IP已添加，无需重复添加
            self.reply(FromUserName, "IP已添加，无需重复添加")
            return False
        # 执行命令
        stdin, stdout, stderr = router.exec_command(f"ipset add {type} {ip}")
        # 获取命令结果
        result = stdout.read().decode()
        # 关闭连接
        router.close()
