from sqlalchemy import select, insert

from engine import engine, session_factory
from orm_models import Base, Declarants, Payers, Directors, Categories, Banks


# def create_table():
#     Base.metadata.create_all(engine)


def get_declarants():
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
    
print(get_declarants())