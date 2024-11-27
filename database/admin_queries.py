from sqlalchemy import select, update

from .engine import session_factory
from .budget_models import DailyBudget, GeneralBudget
from .queries import get_general_budget


def insert_general_budget(budget):
    with session_factory() as session:
        query = GeneralBudget(budget=budget)
        session.add(query)
        session.commit()

    
def reset_all_budget():
    with session_factory() as session:
        query = update(DailyBudget).values(budget=0)
        result = session.execute(query)
        session.commit()


def reset_user_budget(declarant):
    with session_factory() as session:
        get_current_user_budget = select(DailyBudget.budget).filter(DailyBudget.declarant==declarant)
        result = session.execute(get_current_user_budget)
        current_user_budget = float(result.scalars().first())
        general_budget = float(get_general_budget())
        general_budget += current_user_budget
        
        update_user_budget = update(DailyBudget).values(budget=0).filter(DailyBudget.declarant==declarant)
        session.execute(update_user_budget)

        update_general_budget = update(GeneralBudget).values(budget=general_budget)
        session.execute(update_general_budget)

        session.commit()