from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

from . import site
from . import users
from . import posts
from . import groups


def init_app(app):
    bcrypt.init_app(app)
    app.register_blueprint(site.bp)
    app.register_blueprint(users.bp)
    app.register_blueprint(posts.bp)
    app.register_blueprint(groups.bp)
