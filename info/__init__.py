import logging
from logging.handlers import RotatingFileHandler
from flask import Flask,session
from flask_session import Session #用来指定session保存数据的位置
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_wtf.csrf import CSRFProtect
from config import config_dict

#创建db对象
db =  SQLAlchemy()

#定义redis_store
redis_store = None

#工厂方法,根据参数产生不同的app对象
def create_app(config_name):

    #创建app对象
    app = Flask(__name__)

    #通过config_name获取配置类
    config = config_dict.get(config_name)

    #日志信息,传递日志级别
    log_file(config.LEVEL)

    #加载配置类到app
    app.config.from_object(config)

    #创建SQLAlchemy对象,关联app
    db.init_app(app)

    #创建redis对象
    global redis_store
    redis_store = redis.StrictRedis(host=config.REDIS_HOST,port=config.REDIS_PORT,decode_responses=True)

    #初始化session
    Session(app)

    #设置应用程序csrf保护状态
    CSRFProtect(app)

    #注册index_blu蓝图到app
    from info.modules.index import index_blu
    app.register_blueprint(index_blu)

    #注册passport_blu蓝图到app
    from info.modules.passport import passport_blu
    app.register_blueprint(passport_blu)

    print(app.url_map)
    return app

#记录日志信息方法
def log_file(level):
    # 设置日志的记录等级,常见等级有: DEBUG<INFO<WARING<ERROR
    logging.basicConfig(level=level)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)