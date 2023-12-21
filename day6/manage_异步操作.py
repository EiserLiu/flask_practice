import asyncio

from day6 import async_db
from datetime import datetime


class Student(async_db.Model):
    __tablename__ = "student"

    id = async_db.Column(async_db.Integer, primary_key=True, )
    name = async_db.Column(async_db.String(20))
    sex = async_db.Column(async_db.Boolean)
    classes = async_db.Column(async_db.String(255), name="class")
    description = async_db.Column(async_db.Text)
    status = async_db.Column(async_db.Boolean, default=1)
    addtime = async_db.Column(async_db.DateTime, default=datetime.now)
    orders = async_db.Column(async_db.SMALLINT, default=1)

    def __repr__(self):
        return f"<{self.stuid} {self.stuname} {self.stuaddr}>"


async def main():
    async with async_db.engine.begin() as conn:
        # 删除当前程序中所有的模型对应的数据表
        # await conn.run_sync(async_db.Model.metadata.drop_all)

        # 创建当前程序中所有的模型的数据表,如果数据表不存在的情况下
        await conn.run_sync(async_db.Model.metadata.create_all)

    async with async_db.async_session() as session:
        async with session.begin():
            # 拼接SQL语句
            sql = async_db.Select(Student).filter(Student.classes == 300).order_by(Student.id)
            print(sql)
            # 异步执行SQL语句
            student = await session.execute(sql)
            # 获取一个结果
            print(student.first())
            # 获取多个结果
            # print(student.all())


if __name__ == '__main__':
    # asyncio.run(main())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
