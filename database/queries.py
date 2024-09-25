from sqlalchemy import select, insert

from .engine import session_factory
from .models import Base, Declarants, Payers, Directors, Categories, Banks


def get_all_declarants():
    with session_factory() as session:
        query = select(Declarants.name)
        result = session.execute(query)
        declarants = result.scalars().all()
    return declarants


def get_all_payers():
    with session_factory() as session:
        query = select(Banks.bank)
        result = session.execute(query)
        banks = result.scalars().all()
    return banks


def get_all_categories():
    with session_factory() as session:
        query = select(Categories.category)
        result = session.execute(query)
        categories = result.scalars().all()
    return categories


def get_all_payers():
    with session_factory() as session:
        query = select(Payers.name)
        result = session.execute(query)
        payers = result.scalars().all()
    return payers


def get_all_directors():
    with session_factory() as session:
        query = select(Directors.name)
        result = session.execute(query)
        directors = result.scalars().all()
    return directors


def get_declarant(user: str):
    with session_factory() as session:
        query = select(Declarants).filter(Declarants.name==user)
        result = session.execute(query)
        declarant = result.scalars().first()
    return declarant


def get_password(user: str):
    with session_factory() as session:
        query = select(Declarants.password).filter(Declarants.name==user)
        result = session.execute(query)
        password = result.scalars().first()
    return password


def get_user(user_id: int):
    with session_factory() as session:
        query = select(Declarants).filter(Declarants.id==user_id)
        result = session.execute(query)
        user = result.scalars().first()
    return user