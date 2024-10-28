from sqlalchemy import select, insert

from .engine import session_factory
from .budget_models import DailyBudget, GeneralBudget


def insert_general_budget(budget):
    with session_factory() as session:
        query = GeneralBudget(budget=budget)
        session.add(query)
        session.commit()