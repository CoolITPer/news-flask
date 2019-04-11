<<<<<<< HEAD
"""
配置信息:
1.数据库配置
2.redis配置
3.session配置: 主要是用来保存用户登陆信息(登陆的时候再来看)
4.csrf配置: 当修改服务器资源的时候保护(post,put,delete,dispatch)
5.日志文件: 记录程序运行的过程,如果使用print来记录,控制台没有保存数据,线上上线print不需要打印了.
6.迁移配置

"""""
import logging   #库文件
from info import create_app,db,models
# from info import create_app,db,models
from flask import current_app
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager

#调用方法,获取到app对象,app对象身上已经有配置相关信息了
app = create_app('develop')

#配置数据库迁移
manager = Manager(app)
Migrate(app,db)
manager.add_command('db',MigrateCommand)


if __name__ == '__main__':
    manager.run()
=======
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_session import Session
from flask_wtf import CSRFProtect

from config import Config
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)


app.config.from_object(Config)
#初始化数据库
db = SQLAlchemy(app)
#初始化redis
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
Session(app)
#开启当前项目的csrf保护
CSRFProtect(app)

manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)

@app.route('/')
def index():
    return  '222'
if __name__ == '__main__':
    app.run()
>>>>>>> d9abfa5f2784845bb4dbbf3c93745a0973863db6
