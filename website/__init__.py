from unicodedata import name
from flask import Flask, render_template


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "andh346isname3467356isj356621ohnce9980na"

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')
    return app
