import datetime
import sqlalchemy as sqla
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Trophies(SqlAlchemyBase):
    __tablename__ = 'trophies'
    id = sqla.Column(sqla.Integer,
                     primary_key=True, autoincrement=True)
    name = sqla.Column(sqla.String(300), nullable=True)
    description = sqla.Column(sqla.String(3000), nullable=True)
    rate = sqla.Column(sqla.Integer, default=100)
    condition = sqla.Column(sqla.String(3000), nullable=True)
