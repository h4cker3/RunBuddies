import datetime
import sqlalchemy as sqla
from .db_session import SqlAlchemyBase
from sqlalchemy import orm
from flask_login import LoginManager, UserMixin, login_user, logout_user


class Users(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'
    id = sqla.Column(sqla.Integer,
                     primary_key=True, autoincrement=True)
    name = sqla.Column(sqla.String(300), unique=True)
    email = sqla.Column(sqla.String(300), unique=True)
    password = sqla.Column(sqla.String(300))
    link = sqla.Column(sqla.String(300), nullable=True)
    penalty = sqla.Column(sqla.Integer, nullable=True)
    trophies = sqla.Column(sqla.String(3000), nullable=True)
    events = sqla.Column(sqla.String(3000), nullable=True)
    bio = sqla.Column(sqla.String(3000), nullable=True)
