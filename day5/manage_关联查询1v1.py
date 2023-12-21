from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_, or_, not_, func, text
from sqlalchemy.orm import backref

app = Flask(__name__)
# 连接数据库

# 连接数据库URL
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:123456@127.0.0.1:3306/lzp?charset=utf8mb4"
# 动态追踪修改设置,如果为设置只会提示警告
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
# 查询时会显示原始SQL语句
app.config["SQLALCHEMY_ECHO"] = True

# 将SQLAlchemy组件注册到项目中
db = SQLAlchemy()
db.init_app(app)


class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(15), index=True, comment="姓名")
    age = db.Column(db.SmallInteger, comment="年龄")
    sex = db.Column(db.Boolean, default=True, comment="性别")
    email = db.Column(db.String(128), unique=True, comment="邮箱地址")
    money = db.Column(db.Numeric(10, 2), default=0.0, comment="钱包")

    # 关联属性[提供给SQLAlchemy,可以在任意一个关联的模型中]
    # info = db.relationship("StudentInfo",uselist=False,backref=backref("student",uselist=False))

    def __repr__(self):
        return f"{self.student.name} <{self.__class__.__name__}>"


class StudentInfo(db.Model):
    __tablename__ = "student_info"
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    # 外键字段[提供给数据库]
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"), comment="student的外键")
    # 关联属性[提供给SQLAlchemy]
    student = db.relationship("Student", uselist=False, backref=backref("info", uselist=False))
    address = db.Column(db.String(255), index_key=True, comment="注册地址")
    mobile = db.Column(db.String(15), index_key=True, comment="手机号码")

    def __repr__(self):
        return f"{self.student.name} <{self.__class__.__name__}>"


@app.route("/")
def data():
    """一对一"""
    # student = Student(
    #     name="张晓明",
    #     age=16,
    #     sex=True,
    #     email="zhangxiaoming@qq.com",
    #     money=1000,
    #     info=StudentInfo(
    #         address="北京大兴",
    #         mobile="13712345678"
    #     )
    # )
    # db.session.add(student)
    # db.session.commit()
    return "ok"


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
