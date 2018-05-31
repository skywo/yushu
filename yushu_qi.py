# 一个flask练习项目
# 目标实现搜素，注册，留言板等功能，加深基础知识

from app import create_app


app=create_app()



#host=0.0.0.0使得多网卡多ip也能访问到，接受外网访问。
#debug=Ture开启调试模式，生产环境下不安全，使用配置文件可以比较好的解决。
#if，只有本文件执行时，app.run才启动。
if __name__ == '__main__':
    #app.config为地点dict的子类
    app.run(host="0.0.0.0",debug=app.config["DEBUG"])

#生产环境下用nginx+uwsgi启动