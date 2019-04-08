from  flask import  Flask
from werkzeug.routing import BaseConverter

class RegexConvert(BaseConverter):
    def __init__(self,url_map,*args):
        super(RegexConvert,self).__init__(url_map)
        # 将接受的第1个参数当作匹配规则进行保存
        self.regex = args[0]
