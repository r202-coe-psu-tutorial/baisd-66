from flask import Flask, render_template, redirect, url_for, request, Blueprint
from flask_login import login_required

from .. import models

bp = Blueprint("site", __name__)


@bp.route("/")
@login_required
def index():
    messages = models.db.session.execute(models.db.select(models.Message)).scalars()

    return render_template("site/index.html.j2", messages=messages)
