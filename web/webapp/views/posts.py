from flask import Flask, render_template, redirect, url_for, request, Blueprint

bp = Blueprint("posts", __name__, url_prefix="/posts")


@bp.route("/write")
@login_required
def write():
    form = MessageForm()
    return render_template("write.html.j2", form=form)


@bp.route("/save", methods=["POST"])
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
