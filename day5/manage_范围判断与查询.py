from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_, or_,not_

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

    def __repr__(self):
        return f"{self.name} <{self.__class__.__name__}>"


class Course(db.Model):
    __tablename__ = "coures"
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(15), index=True, comment="课程")
    price = db.Column(db.Numeric(8, 2), comment="价格")

    def __repr__(self):
        return f"{self.name} <{self.__class__.__name__}>"


class Teacher(db.Model):
    __tablename__ = "teachers"
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(15), index=True, comment="姓名")
    option = db.Column(db.Enum("讲师", "助教", "班主任"), default="讲师")

    def __repr__(self):
        return f"{self.name} <{self.__class__.__name__}>"


@app.route("/data")
def data():
    """查询是否存在"""
    # q = Student.query.filter(Student.name=="小黑").exists()
    # ret = db.session.query(q).scalar()
    # print(ret)
    #
    # student = Student.query.filter(Student.name=="小明").first()
    # print(bool(student))

    """in 范围查询"""
    # student_list = Student.query.filter(Student.id.in_([1,2,3])).all()
    # print(student_list)

    """is 范围查询"""
    # student_list = Student.query.filter(Student.id.is_(None)).all()
    # print(student_list)

    return "ok"


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
