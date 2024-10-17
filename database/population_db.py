from .engine import Base, db_engine
from .system_models import Taxes
from .budget_models import DailyBudget, GeneralBudget
from .models import Declarants


def create_table():
    Base.metadata.drop_all(db_engine, tables=[GeneralBudget.__table__])
    Base.metadata.create_all(db_engine, tables=[GeneralBudget.__table__])


if __name__ == '__main__':
    create_table()