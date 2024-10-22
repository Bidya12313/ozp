from sqlalchemy import select, insert

from .engine import session_factory
from .budget_models import DailyBudget


def get_declarants_balances():
    with session_factory() as session:
        query = select(DailyBudget)
        result = session.execute(query).scalars().all()
    return result