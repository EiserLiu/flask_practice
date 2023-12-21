from day6 import db
from datetime import datetime


# 1.创建一个与数据库对应的模型类对象


class Student(db.Model):
    """学生表模型"""
    # 1.把当前模型与数据库中指定的表明进行关联
    __tablename__ = "student"

    # 2.绑定字段信息
    # id模型属性 = db.Column字段(db.Integer数据类型,primary_key=True字段约束)
    id = db.Column(db.Integer, primary_key=True, )  # 默认自增
    name = db.Column(db.String(20))
    sex = db.Column(db.Boolean)
    # 当字段名是py关键字是,则需要给name参数(别名使用)
    classes = db.Column(db.String(255), name="class")
    # Text表示设置当前字段为文本格式
    description = db.Column(db.Text)
    status = db.Column(db.Boolean, default=1)
    # 注意:如果设置当前日期时间为默认值,不能在now后加小括号
    addtime = db.Column(db.DateTime, default=datetime.now)
    orders = db.Column(db.SMALLINT, default=1)


if __name__ == '__main__':
    # 如果没有提前声明模型中的数据表,则可以使用一下代码生成数据表,这个操作叫数据迁移
    # 如果数据库中已经声明了数据表,则不会继续生成新的数据表
    db.Model.metadata.create_all(db.engine)
