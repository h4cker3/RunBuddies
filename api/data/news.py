import datetime
import sqlalchemy as sqla
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class News(SqlAlchemyBase):
    __tablename__ = 'news'
    id = sqla.Column(sqla.Integer,
                     primary_key=True, autoincrement=True)
    name = sqla.Column(sqla.String(300), nullable=True)
    description = sqla.Column(sqla.String(3000), nullable=True)
    date = sqla.Column(sqla.String(300), nullable=True)
