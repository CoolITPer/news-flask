from flask import Flask, jsonify
from werkzeug.routing import BaseConverter
from werkzeug.utils import redirect
'''
1.定义app  app = Flask(__name__)
2.定义视图函数 @app.route('/demon4')
              def demon4():
3.启动main函数
'''

app = Flask(__name__)

class Config(object):
    DEBUG = True
# 从配置对象中加载配置
app.config.from_object(Config)

@app.route('/index')
def index():
    return 'Hello World'

@app.route('/demon4')
def demon4():
    '''返回json数据格式'''
    json_dict = {
        "user_id": 10,
        "user_name": "laowang"
    }
    return  jsonify(json_dict)

#自定义转换器
class RegexConverter(BaseConverter):
    def __init__(self, url_map, *args):
        super(RegexConverter, self).__init__(url_map)
        # 将接受的第1个参数当作匹配规则进行保存
        self.regex = args[0]

# 将自定义转换器添加到转换器字典中，并指定转换器使用时名字为: re
app.url_map.converters['re'] = RegexConverter

@app.route('/user/<re("[0-9]{3}"):user_id>')
def user_info(user_id):
    return "user_id 为 %s" % user_id

# 重定向
@app.route('/demo5')
def demo5():
    return redirect('http://www.itheima.com')

#捕获异常
@app.errorhandler(ZeroDivisionError)
def zero_division_error(e):
    return '除数不能为0'

if __name__ == '__main__':
    app.run()