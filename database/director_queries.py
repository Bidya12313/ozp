from sqlalchemy import select, insert, desc

from .engine import session_factory
from .budget_models import GeneralBudget


def get_general_budget():
    with session_factory() as session:
        query = select(GeneralBudget.budget).order_by(desc(GeneralBudget.id))
        result = session.execute(query)
        general_budget = result.scalars().first()
    return general_budget

