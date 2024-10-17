from sqlalchemy import select, insert

from .engine import session_factory
from .models import Base, Declarants, Payers, Directors, Categories, Banks
from .system_models import Taxes
from .budget_models import DailyBudget, GeneralBudget


def get_declarants_balances():
    with session_factory() as session:
        query = select(DailyBudget)
        result = session.execute(query).scalars().all()
    return result