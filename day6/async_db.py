from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import *

engine = create_async_engine(
    url="mysql+aiomysql://root:123456@127.0.0.1:3306/lzp?charset=utf8mb4",
    echo=True,  # 自动打印orm语句转化成的SQL语句
    pool_size=8,  # 连接池的数据库连接数量,默认为5个,0表示无限制
    max_overflow=30,  # 连接池大小
    pool_recycle=60 * 30  # 设置时间以限制数据库多久没连接自动断开
)

# 创建数据库连接
async_session = sessionmaker(
    engine,expire_on_commit=False,class_=AsyncSession
)

# 创建数据基类
Model = declarative_base()


