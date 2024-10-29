from sqlalchemy import select, insert, desc, update

from .engine import session_factory
from .budget_models import GeneralBudget, DailyBudget
from .queries import get_general_budget


def change_user_budget(declarant, required_budget):
    with session_factory() as session:
        get_current_user_budget = select(DailyBudget.budget).filter(DailyBudget.declarant==declarant)
        result = session.execute(get_current_user_budget)
        current_user_budget = result.scalars().first()
        general_budget = get_general_budget()

        general_budget += current_user_budget
        general_budget -= float(required_budget)
        
        general_budget_query = update(GeneralBudget).values(budget=general_budget)
        session.execute(general_budget_query)
        
        user_budget_query = update(DailyBudget).values(budget=required_budget).filter(DailyBudget.declarant==declarant)
        session.execute(user_budget_query)
        
        session.commit()

