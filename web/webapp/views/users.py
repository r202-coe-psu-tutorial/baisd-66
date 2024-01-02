from flask import Flask, render_template, redirect, url_for, request, Blueprint

from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

bp = Blueprint("users", __name__, url_prefix="/users")


@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if not form.validate_on_submit():
        return render_template("login.html.j2", form=form)

    user = User.query.filter_by(username=form.username.data).first()
    if not user:
        return redirect(url_for("login", error="user not found"))

    is_valid = bcrypt.check_password_hash(user.password, form.password.data)
    if not is_valid:
        return redirect(url_for("login", error="user or password miss match"))

    login_user(user)
    return redirect(url_for("index"))


@bp.route("/register", methods=["GET", "POST"])
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


@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


@bp.route("/me")
def me():
    return "Hello World"
