from flask import Flask, render_template, redirect, url_for, request

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

import datetime


class Base(DeclarativeBase):
    pass


from flask_wtf import FlaskForm
from wtforms import fields, validators


class MessageForm(FlaskForm):
    message = fields.StringField(
        "Message", validators=[validators.DataRequired(), validators.Length(min=3)]
    )


class LoginForm(FlaskForm):
    username = fields.StringField(
        "Username", validators=[validators.DataRequired(), validators.Length(min=3)]
    )
    password = fields.PasswordField(
        "Password", validators=[validators.DataRequired(), validators.Length(min=3)]
    )


class RegistrationForm(FlaskForm):
    username = fields.StringField(
        "Username", validators=[validators.DataRequired(), validators.Length(min=3)]
    )
    email = fields.StringField(
        "Email",
        validators=[
            validators.DataRequired(),
            validators.Length(min=3),
            validators.Email(),
        ],
    )
    password = fields.PasswordField(
        "Password", validators=[validators.DataRequired(), validators.Length(min=3)]
    )
    password_confirm = fields.PasswordField(
        "Password Confirm",
        validators=[
            validators.DataRequired(),
            validators.Length(min=3),
            validators.EqualTo("password", message="Passwords must match"),
        ],
    )


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.secret_key = "change it when deploy"

db = SQLAlchemy(model_class=Base)
db.init_app(app)


from flask_login import LoginManager, login_required, logout_user, login_user, UserMixin, current_user

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    username: Mapped[str] = mapped_column(db.String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(db.String, nullable=False)
    email: Mapped[str] = mapped_column(db.String)

class Group(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    created_date: Mapped[datetime.datetime] = mapped_column(db.DateTime)


class Message(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    message: Mapped[str] = mapped_column(db.String)
    ip_address: Mapped[str] = mapped_column(db.String)
    created_date: Mapped[datetime.datetime] = mapped_column(db.DateTime)
    post_by_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    
    post_by: Mapped["User"] = relationship()


with app.app_context():
    db.create_all()


from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


@app.route("/")
@login_required
def index():
    messages = db.session.execute(db.select(Message)).scalars()

    return render_template("index.html.j2", messages=messages)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if not form.validate_on_submit():
        return render_template("login.html.j2", form=form)

    user = User.query.filter_by(username=form.username.data).first()
    if not user:
        return redirect(url_for("login", error="user not found"))

    print('=-->', user)
    is_valid = bcrypt.check_password_hash(user.password, form.password.data) 
    if not is_valid:
        return redirect(url_for("login", error="user or password miss match"))

    login_user(user)
    return redirect(url_for("index"))


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if not form.validate_on_submit():
        return render_template("register.html.j2", form=form)

    user = User()
    form.populate_obj(obj=user)
    user.password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")

    db.session.add(user)
    db.session.commit()
    return redirect(url_for("login"))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/me")
def me():
    return "Hello World"


@app.route("/write")
@login_required
def write():
    form = MessageForm()
    return render_template("write.html.j2", form=form)


@app.route("/save", methods=["POST"])
@login_required
def save():
    # form validation

    form = MessageForm()
    if not form.validate_on_submit():
        return redirect(url_for("write"))

    # create model
    message = Message()
    message.message = request.form.get("message", "No message")
    message.created_date = datetime.datetime.now()
    message.ip_address = request.environ["REMOTE_ADDR"]
    message.post_by_id = current_user.id
    # save model
    db.session.add(message)
    db.session.commit()
    return redirect(url_for("index"))
