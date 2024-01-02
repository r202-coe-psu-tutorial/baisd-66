from flask import Flask, render_template, redirect, url_for, request

from . import views
from . import models
from . import acls

app = Flask(__name__)


with app.app_context():
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.secret_key = "change it when deploy"

    models.init_app(app)
    acls.init_app(app)
    views.init_app(app)
