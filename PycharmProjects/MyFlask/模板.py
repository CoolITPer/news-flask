from flask import Flask, render_template
'''模板循环中常用的属性
loop.index 	当前循环迭代的次数（从 1 开始）
loop.index0 	当前循环迭代的次数（从 0 开始）
loop.revindex 	到循环结束需要迭代的次数（从 1 开始）
loop.revindex0 	到循环结束需要迭代的次数（从 0 开始）
loop.first 	如果是第一次迭代，为 True 。
loop.last 	如果是最后一次迭代，为 True 。
loop.length 	序列中的项目数。
'''


app=Flask(__name__)

@app.route('/')
def index():
    return render_template('tem_dem01.html')

@app.route('/html')
def html_info():
    '''后台给前端传数据'''
    my_str = 'Hello 黑马程序员'
    my_int = 10
    my_array = [3, 4, 2, 1, 7, 9]
    my_dict = {
        'name': 'xiaoming',
        'age': 18
    }
    return render_template('tem_dem02.html',
                           my_str=my_str,
                           my_int=my_int,
                           my_array=my_array,
                           my_dict=my_dict
                           )

@app.template_filter('lireverse')
def do_listreverse(li):
    '''自定义转换器'''
    temp_li=list(li)
    temp_li.reverse()
    return  temp_li
# 添加自定义模板
app.add_template_filter(do_listreverse,'lireverse')

@app.route('/ControlHtml')
def ControlHtml():
    my_list = [
        {
            "id": 1,
            "value": "我爱工作"
        },
        {
            "id": 2,
            "value": "工作使人快乐"
        },
        {
            "id": 3,
            "value": "沉迷于工作无法自拔"
        },
        {
            "id": 4,
            "value": "日渐消瘦"
        },
        {
            "id": 5,
            "value": "以梦为马，越骑越傻"
        }
    ]
    return render_template('tem_dem03.html',my_list=my_list)

@app.route('/macro')
def Html_macro():
    return render_template('tem_dem04.html')

@app.route('/son')
def Html_son():
    return render_template('son.html')

if __name__ == '__main__':
    app.run(debug=True)