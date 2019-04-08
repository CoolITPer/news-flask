from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

app=Flask(__name__)
app.secret_key="abbc45646656165asdsfsdgsdf"
'''
点击提交方法就是get，所以methods需要有两个方法
原生用户登录代码
'''
@app.route('/wtf',methods=["get","post"])
def Wtf():
    if request.method == "POST":
        # 取到表单中提交上来的三个参数
        username = request.form.get("username")
        password = request.form.get("password")
        password2 = request.form.get("password2")

    if not all([username, password, password2]):
        # 向前端界面弹出一条提示(闪现消息)
        flash("参数不足")
    elif password != password2:
        flash("两次密码不一致")
    else:
        # 假装做注册操作
        print(username, password, password2)
        return "success"
    return  render_template('wtf.html')


'''使用wtf表单验证
首先初始化表单对象
先创建前端表单
render_kw相当于placeholder
validators表示必须输入内容
EqualTo表示比较两次值是否相等
register_form.validate_on_submit()表示验证通过
'''

class Registerform(FlaskForm):
    username = StringField("用户名：", validators=[DataRequired("请输入用户名")],
                           render_kw={"placeholder": "请输入用户名"})
    password = PasswordField("密码：", validators=[DataRequired("请输入密码")],
                             render_kw={"placeholder":"请输入密码"})
    password2 = PasswordField("确认密码：", validators=[DataRequired("请输入确认密码"),
                            EqualTo("password", "两次密码不一致")],render_kw={"placeholder":"请在此输入密码"})
    submit = SubmitField("注册")


@app.route('/register_wtf',methods=["get","post"])
def register_wtf():
    #先初始化
    register_form = Registerform()
    if register_form.validate_on_submit():
        # 如果代码能走到这个地方，那么就代码表单中所有的数据都能验证成功
        username = request.form.get("username")
        password = request.form.get("password")
        password2 = request.form.get("password2")
        # 假装做注册操作
        print(username, password, password2)
        return "success"
    else:
        if request.method == "POST":
            flash("参数有误或者不完整")
    ''' 将页面传给前端'''
    return  render_template('wtf.html',form=register_form)





if __name__ == '__main__':
    app.run(debug=True)