from engine import engine, session_factory
from models import Base, Test


def create_table():
    Base.metadata.create_all(engine)

create_table()