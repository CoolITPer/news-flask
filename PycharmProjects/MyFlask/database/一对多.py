from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

#设置连接数据库的URL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:20110923@127.0.0.1:3306/test27'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

'''使用面向对象的方法创建表
1的一方用relashion绑定多的一方
backref为类User申明新属性的方法
绑定之后可以用role.users user.role
'''
class Role(db.Model):
    name = db.Column(db.String(64), unique=True)
    # 定义表名
    __tablename__ = 'roles'
    # 定义列对象
    id = db.Column(db.Integer, primary_key=True)
    users = db.relationship('User', backref='role')

    #repr()方法显示一个可读字符串
    def __repr__(self):
        return 'Role:%s'% self.name
'''
多的一方
'''
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64),unique=True)
    password = db.Column(db.String(64))
    #外键关联喊着Role.id
    role_id = db.Column(db.Integer, db.ForeignKey(Role.id))

    def __repr__(self):
        return 'User:%s'%self.name
if __name__ == '__main__':
    db.drop_all()
    db.create_all()

    role1=Role(name="admin")
    role2 = Role(name="usr")
    db.session.add_all([role1,role2])

    user1=User(name="lw",role_id=role1.id)
    user2 = User(name="ll",role_id=role1.id)
    user3 = User(name="lz",role_id=role2.id)
    db.session.add_all([user1,user2,user3])

    db.session.commit()

    app.run(debug=True)