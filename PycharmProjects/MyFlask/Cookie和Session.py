from flask import Flask, make_response, request, session, url_for
from werkzeug.utils import redirect
from flask_script import Manager

app=Flask(__name__)
# 把 Manager 类和应用程序实例进行关联
manager = Manager(app)

@app.route('/cookie')
def set_cookie():
    '''设置cookie'''
    resp = make_response('this is to set cookie')
    resp.set_cookie('username', 'itcast')
    return resp

@app.route('/getcookie')
def get_cookie():
    '''获取cookie,用request'''
    resp=request.cookies.get('username')
    return  resp

@app.route('/session')
def set_session():
    '''设置session'''
    session['user_id']='1'
    session['user_name']-'Tom'
    return  redirect (url_for('set_cookie'))


if __name__ == '__main__':
    app.run()