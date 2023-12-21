from day6 import db
from datetime import datetime


class Student(db.Model):
    __tablename__ = "student"

    id = db.Column(db.Integer, primary_key=True, )
    name = db.Column(db.String(20))
    sex = db.Column(db.Boolean)
    classes = db.Column(db.String(255), name="class")
    description = db.Column(db.Text)
    status = db.Column(db.Boolean, default=1)
    addtime = db.Column(db.DateTime, default=datetime.now)
    orders = db.Column(db.SMALLINT, default=1)


if __name__ == '__main__':
    """添加一条数据"""
    student = Student(
        name = "小明一号",

    )