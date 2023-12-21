from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy import and_, or_, not_

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
    # student_list = Student.query.all()
    # print(student_list)

    # paginate(page页码,per_page单页数据量,max_per_page单页最大数据量)
    # Student.query.filter().paginate()
    page = int(request.args.get("page", 1))
    size = int(request.args.get("page", 5))
    pagination = Student.query.filter().paginate(page=page, per_page=size, max_per_page=10)

    # print(pagination.total)  # 总数据量
    # print(pagination.items)  # 当前页数据
    # print(pagination.pages)  # 总页码
    #
    # print(pagination.has_prev)  # 是否有上一页
    # print(pagination.prev_num)  # 上一页的页码
    # print(pagination.prev())  # 上一页的分类器对象
    # print(pagination.prev().items)  # 上一页展示的数据列表
    #
    # print(pagination.has_next)  # 是否有上一页
    # print(pagination.next_num)  # 上一页的页码
    # print(pagination.next())  # 上一页的分类器对象
    # print(pagination.next().items)  # 上一页展示的数据列表
    return "ok"


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
