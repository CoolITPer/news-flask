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
