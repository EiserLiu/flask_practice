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


class StudentAddress(db.Model):
    __tablename__ = "student_address"
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(50), default="默认", comment="地址名称")
    province = db.Column(db.String(50), comment="省份")
    city = db.Column(db.String(50), comment="城市")
    area = db.Column(db.String(50), comment="地区")
    address = db.Column(db.String(255), comment="详细地址")
    mobile = db.Column(db.String(15), comment="收货人电话")

    # 外键字段[提供给数据库]
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"), comment="student的外键")
    # 关联属性[提供给SQLAlchemy]
    # 外键模型-->主模型 StudentAddress.student 结果是对象
    # 主模型-->外键模型 Student.address_list   结果是列表
    student = db.relationship("Student", uselist=False, backref=backref("address_list", uselist=True, lazy="dynamic"))

    def __repr__(self):
        return f"{self.student.name} <{self.__class__.__name__}>"


@app.route("/")
def data():
    """添加操作"""
    student = Student(name="张晓明", age=17, sex=True, email="zhangxiaomingd@qq.com", money=1000)
    db.session.add(student)
    db.session.commit()

    student.address_list.append(StudentAddress(name="公司",province="北京",city="北京市",area="昌平区",address="白沙路12345",mobile="13012345678"))
    db.session.commit()

    return "ok"


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
