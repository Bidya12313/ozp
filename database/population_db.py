from .engine import Base, db_engine
from .system_models import Taxes
from .budget_models import DailyBudget


def create_table():
    Base.metadata.drop_all(db_engine, tables=[DailyBudget.__table__])
    Base.metadata.create_all(db_engine, tables=[DailyBudget.__table__])


if __name__ == '__main__':
    create_table()