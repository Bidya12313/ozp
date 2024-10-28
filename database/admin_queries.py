from sqlalchemy import select, insert, update

from .engine import session_factory
from .budget_models import DailyBudget, GeneralBudget


def insert_general_budget(budget):
    with session_factory() as session:
        query = GeneralBudget(budget=budget)
        session.add(query)
        session.commit()

    
def reset_all_limits():
    with session_factory() as session:
        query = update(DailyBudget).values(budget=0)
        result = session.execute(query)
        session.commit()


def reset_user_limit(declarant):
    with session_factory() as session:
        query = update(DailyBudget).values(budget=0).filter(DailyBudget.declarant==declarant)
        result = session.execute(query)
        session.commit()