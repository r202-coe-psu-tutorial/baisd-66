from flask import Flask, render_template, redirect, url_for, request

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column

import datetime

class Base(DeclarativeBase):
  pass


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db = SQLAlchemy(model_class=Base)
db.init_app(app)




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
    created_date: Mapped[datetime.datetime] = mapped_column(db.DateTime)

with app.app_context():
    db.create_all()

@app.route("/")
def index():

    messages = db.session.execute(db.select(Message)).scalars()

    return render_template("index.html.j2", messages=messages)


@app.route("/me")
def me():
    return "Hello World"


@app.route("/write")
def write():
    return render_template("write.html.j2")


@app.route("/save", methods=["POST"])
def save():
    # create model
    message = Message()
    message.message = request.form.get('message', 'No message')
    message.created_date = datetime.datetime.now()
    # save model
    db.session.add(message)
    db.session.commit()
    return redirect(url_for("index"))
