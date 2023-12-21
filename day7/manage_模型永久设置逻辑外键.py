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
app.config["SQLALCHEMY_ECHO"] = False

# 将SQLAlchemy组件注册到项目中
db = SQLAlchemy()
db.init_app(app)


class StudentCourse(db.Model):
    __tablename__ = "t_virtual_foreign_key_student_course_2"
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    student_id = db.Column(db.Integer, index=True, comment="学生ID")
    course_id = db.Column(db.Integer, index=True, comment="课程ID")
    created_time = db.Column(db.DateTime, default=datetime.now, comment="购买时间")
    # 关联属性
    student = db.relationship("Student", uselist=False, backref=backref("to_relation", uselist=True, lazy="dynamic"),
                              primaryjoin="Student.id == foreign(StudentCourse.student_id)")
    course = db.relationship("Course", uselist=False, backref=backref("to_relation", uselist=True, lazy="dynamic"),
                             primaryjoin="Course.id == foreign(StudentCourse.course_id)")


class Student(db.Model):
    __tablename__ = "t_virtual_foreign_key_student_2"

    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(15), index=True, comment="姓名")
    age = db.Column(db.SmallInteger, comment="年龄")
    sex = db.Column(db.Boolean, default=True, comment="性别")

    def __repr__(self):
        return f"<{self.name} {self.__class__.__name__}>"


class Course(db.Model):
    __tablename__ = "t_virtual_foreign_key_course_2"

    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(255), unique=True, comment="课程")

    def __repr__(self):
        return f"<{self.name} {self.__class__.__name__}>"


@app.route("/")
def index():
    # """添加数据"""
    # stu0 = Student(name="xiaohong", age=18, sex=True)
    # stu1 = Student(name="xiaobai", age=28, sex=False)
    # stu2 = Student(name="xiaolan", age=18, sex=True)
    # stu3 = Student(name="xiaolv", age=30, sex=False)
    # stu4 = Student(name="xiaohei", age=16, sex=True)
    # db.session.add_all([stu0, stu1, stu2, stu3, stu4])
    #
    # course1 = Course(name="python基础")
    # course2 = Course(name="python进阶")
    # course3 = Course(name="python高级")
    # course4 = Course(name="python实战")
    # db.session.add_all([course1, course2, course3, course4])
    #
    # data = [
    #     StudentCourse(student_id=1, course_id=1),
    #     StudentCourse(student_id=1, course_id=2),
    #     StudentCourse(student_id=1, course_id=3),
    #     StudentCourse(student_id=2, course_id=2),
    #     StudentCourse(student_id=3, course_id=3),
    #     StudentCourse(student_id=3, course_id=4),
    #     StudentCourse(student_id=5, course_id=1),
    #     StudentCourse(student_id=5, course_id=2)
    # ]
    #
    # db.session.add_all(data)
    # db.session.commit()

    # student = Student.query.get(1)
    # print([relation.course.name for relation in student.to_relation.all()])
    #

    course = Course.query.get(3)
    print([relation.student.name for relation in course.to_relation.all()])

    return "ok"


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
