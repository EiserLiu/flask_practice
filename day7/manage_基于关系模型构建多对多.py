from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
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


class StudentCoures(db.Model):
    __tablename__ = "t_nvm_student_course_2"
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    sid = db.Column(db.Integer, db.ForeignKey("t_nvm_student_2.id"), comment="学生ID")
    cid = db.Column(db.Integer, db.ForeignKey("t_nvm_course_2.id"), comment="课程ID")
    created_time = db.Column(db.DateTime, default=datetime.now, comment="购买时间")
    # 关系模型
    student = db.relationship("Student", uselist=False, backref=backref("to_relation", uselist=True))
    course = db.relationship("Course", uselist=False, backref=backref("to_relation", uselist=True))


class Student(db.Model):
    __tablename__ = "t_nvm_student_2"

    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(15), index=True, comment="姓名")
    age = db.Column(db.SmallInteger, comment="年龄")
    sex = db.Column(db.Boolean, default=True, comment="性别")

    def __repr__(self):
        return f"<{self.name} {self.__class__.__name__}>"


class Course(db.Model):
    __tablename__ = "t_nvm_course_2"

    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(255), unique=True, comment="课程")

    def __repr__(self):
        return f"<{self.name} {self.__class__.__name__}>"


@app.route("/")
def index():
    """添加数据"""
    # student = Student(
    #     name="xiaozhao",
    #     age="13",
    #     sex=True,
    #     to_relation=[
    #         StudentCoures(course=Course(name="python入门")),
    #         StudentCoures(course=Course(name="python初级")),
    #         StudentCoures(course=Course(name="python进阶")),
    #     ]
    # )
    # db.session.add(student)
    # db.session.commit()

    student = Student.query.get(1)
    for relation in student.to_relation:
        print(relation.course.name)

    return "ok"


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
