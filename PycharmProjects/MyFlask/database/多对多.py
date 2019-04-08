from flask import Flask
from flask_sqlalchemy import SQLAlchemy
'''
1. 首先定义两个表
2.再定义一个中间表
3.定义两个表的映射关系，然后加上secondary=中间表的表名
'''

app=Flask(__name__)
#设置连接数据库的URL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:20110923@127.0.0.1:3306/test27'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

tb_student_course = db.Table('tb_student_course',
    db.Column('student_id', db.Integer, db.ForeignKey('students.student_id')),
    db.Column('course_id', db.Integer, db.ForeignKey('courses.course_id'))
)

'''
多的一方
'''
class Course(db.Model):
    __tablename__ = 'courses'
    course_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    #外键关联喊着Role.id

class Students(db.Model):
    name = db.Column(db.String(64), unique=True)
    # 定义表名
    __tablename__ = 'students'
    # 定义列对象
    student_id = db.Column(db.Integer, primary_key=True)
    courses=db.relationship('Course',backref='students',lazy='dynamic',secondary=tb_student_course)
    #role_id = db.Column(db.Integer, db.ForeignKey(Role.id))
    co_st_id=db.Column(db.Integer,db.ForeignKey(Course.course_id))
    #repr()方法显示一个可读字符串
    def __repr__(self):
        return 'student:%s'% self.name


if __name__ == '__main__':
    db.drop_all()
    db.create_all()

    co1=Course(name='Chinese')
    co2 = Course(name='Math')
    co3 = Course(name='English')

    st1 = Students(name='Tom')
    st2 = Students(name='JJJ')
    st3 = Students(name='Alice')
    st1.courses=[co1,co2]
    st2.courses=[co1,co2,co3]
    st3.courses=[co2]

    db.session.add_all([st1,st2,st3,co1,co2,co3])
    db.session.commit()

    app.run(debug=True)
