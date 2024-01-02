from . import users
from . import posts


def init_app(app):
    app.register_blueprint(users.bp)
    app.register_blueprint(posts.bp)
