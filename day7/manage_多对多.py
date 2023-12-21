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

# 关系表[无法提供给flask进行数据操作,仅仅用于在数据库中记录两个模型之间的关系]
student_course_table = db.Table(
    "t_nvm_student_coures",
    db.Column("id", db.Integer, primary_key=True, comment="主键"),
    db.Column("sid", db.Integer, db.ForeignKey("t_nvm_student.id"), comment="学生ID"),
    db.Column("cid", db.Integer, db.ForeignKey("t_nvm_coures.id"), comment="课程ID"),
    db.Column("created", db.DateTime, default=datetime.now, comment="购买时间")
)


class Student(db.Model):
    __tablename__ = "t_nvm_student"

    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(15), index=True, comment="姓名")
    age = db.Column(db.SmallInteger, comment="年龄")
    sex = db.Column(db.Boolean, default=True, comment="性别")
    # 只有设置了关联属性后,flask中才提供模型关联的操作
    coures_list = db.relationship("Coures", secondary=student_course_table, backref=backref("student_list"),
                                  lazy="dynamic")

    def __repr__(self):
        return f"<{self.name} {self.__class__.__name__}>"


class Coures(db.Model):
    __tablename__ = "t_nvm_coures"

    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(255), unique=True, comment="课程")

    def __repr__(self):
        return f"<{self.name} {self.__class__.__name__}>"


@app.route("/")
def index():
    # student = Student(
    #     name="xiaozhao",
    #     age="13",
    #     sex=True,
    #     coures_list=[
    #         Coures(name="python入门"),
    #         Coures(name="python初级"),
    #         Coures(name="python进阶")
    #     ]
    # )
    #为已有的人员添加课程
    # student = Student(
    #     name="xiaohong",
    #     age="14",
    #     sex=False,
    # )
    #
    # db.session.add(student)
    # db.session.commit()
    #
    # student = Student.query.filter(Student.name == "xiaohong").first()
    # student.coures_list.append(Coures.query.get(3))
    # student.coures_list.append(Coures(name="python高级"))
    # db.session.commit()
    """让学生一次报读多个已有课程"""
    # student1=Student.query.get(2)
    # coures_list=Coures.query.filter(Coures.id.in_([3,2])).all()
    # db.session.commit()
    # student1.coures_list.extend(coures_list)
    """查询操作"""
    # student = Student.query.get(1)
    # print(student.coures_list)
    #
    # coures = Coures.query.get(4)
    # print(coures.student_list)

    # coures = Coures.query.get(3)
    # for student in coures.student_list:
    #     student.money += 200
    # db.session.commit()


    return "ok"


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
