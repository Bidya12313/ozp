from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from config import db_url


engine = create_engine(
    url=db_url,
    pool_size=5,
    echo=True
)

session_factory = sessionmaker(engine)


class Base(DeclarativeBase):
    pass