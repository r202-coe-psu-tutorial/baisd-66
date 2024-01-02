from flask import Flask, render_template, redirect, url_for, request, Blueprint
from flask_login import login_required, current_user
import datetime

from .. import forms
from .. import models

bp = Blueprint("posts", __name__, url_prefix="/posts")


@bp.route("/write")
@login_required
def write():
    form = forms.MessageForm()
    return render_template("posts/write.html.j2", form=form)


@bp.route("/save", methods=["POST"])
@login_required
def save():
    # form validation

    form = forms.MessageForm()
    if not form.validate_on_submit():
        return redirect(url_for("post.write"))

    # create model
    message = models.Message()
    message.message = request.form.get("message", "No message")
    message.created_date = datetime.datetime.now()
    message.ip_address = request.environ["REMOTE_ADDR"]
    message.post_by_id = current_user.id
    # save model
    models.db.session.add(message)
    models.db.session.commit()
    return redirect(url_for("site.index"))
