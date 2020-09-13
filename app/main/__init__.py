from flask import Flask, Blueprint, request
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from app.main.routes.user import user
from app.main.routes.product import product

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:Subham@786@localhost/flipkart"

    db.init_app(app)

    app.register_blueprint(user, url_prefix='/user')
    app.register_blueprint(product, url_prefix='/product')

    return app