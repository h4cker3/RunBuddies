import datetime
import sqlalchemy as sqla
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Events(SqlAlchemyBase):
    __tablename__ = 'events'
    id = sqla.Column(sqla.Integer,
                     primary_key=True, autoincrement=True)
    users = sqla.Column(sqla.String(3000), nullable=True)
    name = sqla.Column(sqla.String(300), nullable=True)
    description = sqla.Column(sqla.String(3000), nullable=True)
    data = sqla.Column(sqla.String(300), nullable=True)
    diff = sqla.Column(sqla.Integer, default=1)
