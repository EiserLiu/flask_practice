

import models


class Student(models.Model):
    __tablename__ = "tbstudent"
    stuid = models.Column(models.Integer, primary_key=True, autoincrement=True)
    stuname = models.Column(models.String(30))
    stusex = models.Column(models.Boolean)
    stuaddr = models.Column(models.String(255))
    stuphoto = models.Column(models.String(30))

    def __repr__(self):
        return f"<{self.stuid} {self.stuname} {self.stuaddr}>"


if __name__ == '__main__':
    pass
    ## 查询数据
    # models.Model.metadata.create_all(models.engine)
    # data_list = models.session.query(Student).all()
    # for student in data_list:
    #     print(student.stuid, student.stuaddr)

    # print(data_list)

    # student = models.session.query(Student).get(0)
    # if student:
    #     print(student)
    # else:
    #     print("查无此人")

    # # 添加数据
    # student = Student(
    #     stuid = 1,
    #     stuname="刘泽普",
    #     stusex=True,
    #     stuaddr="翻斗花园",
    #     stuphoto="17692275126"
    # )
    #
    # models.session.add(student)
    # models.session.commit()

    # #修改操作
    # student = models.session.query(Student).filter_by(stuname = "张四丰").first()
    # if student:
    #     student.stuname = "张四丰",
    #     models.session.commit()
    # print(student)

    # #删除操作
    # student = models.session.query(Student).filter_by(stuname = "张四丰").first()
    # models.session.delete(student)
    # models.session.commit()

    # #添加多条数据
    # student_list = [
    #     Student(stuname="小孩"),
    #     Student(stuname="小张"),
    #     Student(stuname="小喔")
    # ]
    # models.session.add_all(student_list)
    # models.session.commit()

    # # #更新多条数据
    # models.session.query(Student).filter(Student.stuid < 1000).update({Student.stuphoto: Student.stuphoto * 10})
    # models.session.commit()

    # # 删除多条数据
    # models.session.query(Student).filter_by(stuname="张四丰").delete()
    # models.session.commit()