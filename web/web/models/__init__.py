from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

import datetime


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

from .all import *


def init_app(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
