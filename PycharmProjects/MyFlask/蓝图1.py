from flask import Flask
from publishBlue import publish_blue

app=Flask(__name__)
app.register_blueprint(publish_blue)
'''publish代码放到publishBlue当中'''

@app.route('/')
def index():
    return 'index'

@app.route('/list')
def list():
    return 'list'

@app.route('/detail')
def detail():
    return 'detail'

@app.route('/')
def admin_home():
    return 'admin_home'

@app.route('/new')
def new():
    return 'new'

@app.route('/edit')
def edit():
    return 'edit'

# @app.route('/publish')
# def publish():
#     return 'publish'

if __name__=='__main__':
    app.run()