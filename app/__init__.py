from flask import Flask
from app.web.model import db

def create_app():
    app = Flask(__name__)
#传入配置文件的模块路径，该模块与yushu于同一级。
    app.config.from_object("config")
    register_blueprint(app)
# 初始化SQLalchemy，app
    db.init_app(app)
    db.create_all(app=app)
    return app

# 注册蓝图
def register_blueprint(app):
    from app.web.blue_book import web
    app.register_blueprint(web)