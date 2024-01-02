from flask import Flask, render_template, redirect, url_for, request, Blueprint
from flask_login import login_required, current_user
import datetime

from . import bcrypt

from .. import forms
from .. import models

bp = Blueprint("groups", __name__, url_prefix="/groups")


@bp.route("/create", methods=["GET", "POST"], defaults=dict(group_id=None))
@bp.route("/<group_id>/edit", methods=["GET", "POST"])
@login_required
def create_or_edit(group_id):
    group = None
    if group_id:
        group = models.User.query.filter_by(id=group_id).first()

    form = forms.GroupForm()
    if group and request.method == "GET":
        form = forms.GroupForm(obj=group)

    if not form.validate_on_submit():
        return render_template("/groups/create_or_edit.html.j2", form=form)

    if not group:
        group = models.Group()
        group.created_by = current_user
        group.created_date = datetime.datetime.now()

    form.populate_obj(obj=group)
    group.ip_address = request.environ.get("REMOTE_ADDR", "")

    models.db.session.add(group)
    models.db.session.commit()
    return redirect(url_for("groups.view", group_id=group.id))


@bp.route("/<group_id>")
@login_required
def view(group_id):
    form = forms.MessageForm()
    group = models.Group.query.filter_by(id=group_id).first()
    return render_template("/groups/view.html.j2", form=form, group=group)


@bp.route("/<group_id>/write", methods=["POST", "GET"])
@login_required
def write(group_id):
    form = forms.MessageForm()

    group = models.Group.query.filter_by(id=group_id).first()

    if not form.validate_on_submit():
        return render_template("groups/view.html.j2", form=form, groups=group)

    # create model

    message = models.Message()
    message.message = request.form.get("message", "No message")
    message.created_date = datetime.datetime.now()
    message.ip_address = request.environ["REMOTE_ADDR"]
    message.post_by = current_user
    message.group = group
    # save model
    models.db.session.add(message)
    models.db.session.commit()

    return redirect(url_for("groups.view", group_id=group_id))
