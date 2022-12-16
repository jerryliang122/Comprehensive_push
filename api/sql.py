import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
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

init_data = json.loads(open('conf/sql.json', 'r', encoding='utf-8').read())
# 连接数据库
class DB:
    def __init__(self, db):
        self.engine = create_engine(f'mysql+pymysql://{init_data["name"]}:{init_data["password"]}@localhost:3306/comprehensive_push',max_overflow=2,pool_pre_ping=True,pool_recycle=1600,pool_use_lifo=True)
        DBsession = sessionmaker(bind=self.engine)
        self.db = DBsession()
    
    def init(self):
        Base.metadata.create_all(self.engine)
        return self.db
    

# 数据库
Base = declarative_base()
class token(Base):
    __tablename__ = 'token'
    id = Column(Integer, primary_key=True)
    access_token = Column(String(255))
    expiration_time = Column(DateTime)

# 生成数据库
db = DB().init()