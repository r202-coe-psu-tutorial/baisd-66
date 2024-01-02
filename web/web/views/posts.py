from flask import Flask, render_template, redirect, url_for, request, Blueprint
from flask_login import login_required, current_user
import datetime

from .. import forms
from .. import models

bp = Blueprint("posts", __name__, url_prefix="/posts")


@bp.route("/post_by_user/<user_id>")
@login_required
def post_by(user_id):
    user = models.User.query.filter_by(id=user_id).first()
    messages = models.db.session.execute(
        models.db.select(models.Message).filter_by(post_by_id=user.id)
    ).scalars()
    return render_template("posts/post_by.html.j2", messages=messages, user=user)
