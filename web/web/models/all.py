from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

import datetime

from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    username: Mapped[str] = mapped_column(db.String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(db.String, nullable=False)
    email: Mapped[str] = mapped_column(db.String)


class Group(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(db.String)
    created_date: Mapped[datetime.datetime] = mapped_column(db.DateTime)
    ip_address: Mapped[str] = mapped_column(db.String)

    created_by_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    created_by: Mapped["User"] = relationship("User")

    messages: Mapped[list["Message"]] = relationship(back_populates="group")


class Message(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    message: Mapped[str] = mapped_column(db.String)
    ip_address: Mapped[str] = mapped_column(db.String)
    created_date: Mapped[datetime.datetime] = mapped_column(db.DateTime)

    post_by_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    post_by: Mapped["User"] = relationship("User")

    group_id: Mapped[int] = mapped_column(ForeignKey("group.id"))
    group: Mapped["Group"] = relationship("Group")
