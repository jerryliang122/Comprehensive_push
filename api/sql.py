import json
from sqlalchemy import create_engine

from sqlalchemy import (
    Column,
    create_engine,
    Integer,
    String,
    DateTime,
    Boolean,
    ForeignKey,
    Float,
    Text,
    LargeBinary,
    DECIMAL,
    BigInteger,
)
from sqlalchemy.ext.declarative import declarative_base

# 连接数据库
class DB:
    def __init__(self):
        self.engine = create_engine(f"sqlite:///conf/data.db", echo=True)

    def init(self):
        Base.metadata.create_all(self.engine)
        return "TRUE"


# 数据库
Base = declarative_base()


class token(Base):
    __tablename__ = "token"
    id = Column(Integer, primary_key=True)
    access_token = Column(String(255))
    expiration_time = Column(DateTime)

    def __init__(self, id, access_token, expiration_time):
        self.id = id
        self.access_token = access_token
        self.expiration_time = expiration_time


class ipset(Base):
    __tablename__ = "ipset"
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(Text)
    ip = Column(Text)

    def __init__(self, id, type, ip):
        self.id = id
        self.type = type
        self.ip = ip


# 生成数据库
db = DB().init()
