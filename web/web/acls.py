from flask_login import (
    LoginManager,
    login_required,
    logout_user,
    login_user,
    UserMixin,
    current_user,
)

from . import models

login_manager = LoginManager()
login_manager.login_view = "users.login"


def init_app(app):
    login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return models.User.query.filter_by(id=user_id).first()
