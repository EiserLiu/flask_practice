from datetime import datetime
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_, or_, not_, func, text

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

migrate = Migrate(app,db)


class Student(db.Model):
    __tablename__ = "t_faker_student"
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(15), index=True, comment="姓名")
    age = db.Column(db.SmallInteger, comment="年龄")
    sex = db.Column(db.Boolean, default=True, comment="性别")
    email = db.Column(db.String(128), comment="邮箱地址")
    created_time = db.Column(db.DateTime, default=datetime.now)
    money = db.Column(db.Numeric(10, 2), default=0.0, comment="钱包")

    def __repr__(self):
        return f"<{self.name} {self.__class__.__name__}>"


"""基于Faker生成仿真数据的终端命令"""
# 自定义批量生成学生
import random, click
from faker import Faker

faker = Faker(locale="ZH_CN")


# 自定义终端命令
@app.cli.command("faker_user")
@click.argument("num", default=10, type=int)
def faker_user_command(num):
    """生成测试学生信息"""
    data_list = []
    for i in range(num):
        sex = bool(random.randint(0, 1))
        student = Student(
            name=faker.name_male() if sex else faker.name_male,
            age=random.randint(15, 40),
            sex=sex,
            email=faker.unique.free_email(),
            money=float(random.randint(100, 100000) / 10),
            created_time=faker.date_time(),
        )
        data_list.append(student)
    # 在循环外
    db.session.add_all(data_list)
    db.session.commit()


@app.route("/")
def index():
    return "ok"


if __name__ == '__main__':
    app.run(debug=True)
