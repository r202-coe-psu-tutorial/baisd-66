from flask import Flask, render_template, redirect, url_for, request, Blueprint
from flask_login import login_required, login_user, logout_user


from . import bcrypt

from .. import forms
from .. import models

bp = Blueprint("users", __name__, url_prefix="/users")


@bp.route("/login", methods=["GET", "POST"])
def login():
    form = forms.LoginForm()

    if not form.validate_on_submit():
        return render_template("users/login.html.j2", form=form)

    user = models.User.query.filter_by(username=form.username.data).first()
    if not user:
        return redirect(url_for("users.login", error="user not found"))

    is_valid = bcrypt.check_password_hash(user.password, form.password.data)
    if not is_valid:
        return redirect(url_for("users.login", error="user or password miss match"))

    login_user(user)
    return redirect(url_for("site.index"))


@bp.route("/register", methods=["GET", "POST"])
def register():
    form = forms.RegistrationForm()
    if not form.validate_on_submit():
        return render_template("/users/register.html.j2", form=form)

    user = models.User()
    form.populate_obj(obj=user)
    user.password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")

    models.db.session.add(user)
    models.db.session.commit()
    return redirect(url_for("users.login"))


@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("site.index"))


@bp.route("/me")
def me():
    return "Hello World"
