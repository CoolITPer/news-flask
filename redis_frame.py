from redis import *
if __name__=="__main__":
    try:
        #创建StrictRedis对象，与redis服务器建⽴连接
        sr=StrictRedis()
        #添加
        result = sr.set('name', 'itheima')
        #获取
        name=sr.get('name')
        #修改
        sr.set('name','hhh')
        #追加
        sr.append('name','哈哈哈')
        sr.set('gender','男')
    # 输出响应结果，如果添加成功则返回True，否则返回False
        print(result)
    except Exception as e:
        print(e)