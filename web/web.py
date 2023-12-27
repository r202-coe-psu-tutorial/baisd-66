from flask import Flask, render_template, redirect, url_for, request

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column

import datetime

class Base(DeclarativeBase):
  pass


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.secret_key = "change it when deploy"

db = SQLAlchemy(model_class=Base)
db.init_app(app)


from flask_login import LoginManager, login_required, logout_user
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    print('-->',)
    return User.get(user_id)


class User(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    username: Mapped[str] = mapped_column(db.String, unique=True, nullable=False)
    email: Mapped[str] = mapped_column(db.String)

class Group(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    created_date: Mapped[datetime.datetime] = mapped_column(db.DateTime)

class Message(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    message: Mapped[str] = mapped_column(db.String)
    ip_address: Mapped[str] = mapped_column(db.String)
    created_date: Mapped[datetime.datetime] = mapped_column(db.DateTime)

with app.app_context():
    db.create_all()

@app.route("/")
@login_required
def index():
    messages = db.session.execute(db.select(Message)).scalars()

    return render_template("index.html.j2", messages=messages)

@app.route("/login")
def login():
    return "Login Page"


@app.route("/register")
def register():
    return "Register Page"

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/me")
def me():
    return "Hello World"


@app.route("/write")
@login_required
def write():
    return render_template("write.html.j2")


@app.route("/save", methods=["POST"])
@login_required
def save():
    # create model
    message = Message()
    message.message = request.form.get('message', 'No message')
    message.created_date = datetime.datetime.now()
    message.ip_address = request.environ['REMOTE_ADDR']
    # save model
    db.session.add(message)
    db.session.commit()
    return redirect(url_for("index"))
