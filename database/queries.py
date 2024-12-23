from sqlalchemy import select, desc

from .engine import session_factory
from .models import Base, Users, Payers, Categories, Banks
from .system_models import Taxes
from .budget_models import DailyBudget, GeneralBudget


def get_daily_budget(declarant: str) -> float:
    with session_factory() as session:
        query = select(DailyBudget.budget).filter(DailyBudget.declarant==declarant)
        result = session.execute(query)
        daily_budget = result.scalars().first()
    return daily_budget


def get_all_declarants() -> list:
    with session_factory() as session:
        query = select(Users.name)
        result = session.execute(query)
        declarants = result.scalars().all()
    return declarants


def get_all_banks() -> list:
    with session_factory() as session:
        query = select(Banks.bank)
        result = session.execute(query)
        banks = result.scalars().all()
    return banks


def get_all_categories() -> list:
    with session_factory() as session:
        query = select(Categories.category)
        result = session.execute(query)
        categories = result.scalars().all()
    return categories


def get_all_payers() -> list:
    with session_factory() as session:
        query = select(Payers.name)
        result = session.execute(query)
        payers = result.scalars().all()
    return payers


def get_all_directors() -> list:
    with session_factory() as session:
        query = select(Users.name).filter(Users.director_status=='+')
        result = session.execute(query)
        directors = result.scalars().all()
    return directors


def get_declarant(user: str) -> str:
    with session_factory() as session:
        query = select(Users).filter(Users.name==user)
        result = session.execute(query)
        declarant = result.scalars().first()
    return declarant


def get_password(user: str):
    with session_factory() as session:
        query = select(Users.password).filter(Users.name==user)
        result = session.execute(query)
        password = result.scalars().first()
    return password


def get_user(user_id: int) -> str:
    with session_factory() as session:
        query = select(Users).filter(Users.id==user_id)
        result = session.execute(query)
        user = result.scalars().first()
    return user


def get_all_user_taxes(declarant) -> list:
    with session_factory() as session:
        query = select(Taxes).filter(Taxes.declarant==declarant).order_by(Taxes.id.desc())
        result = session.execute(query)
        user_taxes = result.scalars().all()
    return user_taxes


def get_declarants_balances() -> list:
    with session_factory() as session:
        query = select(DailyBudget)
        result = session.execute(query).scalars().all()
    return result


def get_general_budget() -> float:
    with session_factory() as session:
        query = select(GeneralBudget.budget).order_by(desc(GeneralBudget.id))
        result = session.execute(query)
        general_budget = result.scalars().first()
    return general_budget


def get_declarant_budget(declarant) -> float:
    with session_factory() as session:
        get_current_user_budget = select(DailyBudget.budget).filter(DailyBudget.declarant==declarant)
        result = session.execute(get_current_user_budget)
        current_user_budget = result.scalars().first()
    return current_user_budget


def get_tax(tax_id: int, session):
    get_tax = select(Taxes).filter(Taxes.id==tax_id)
    result = session.execute(get_tax)
    tax = result.scalar_one()
    return tax