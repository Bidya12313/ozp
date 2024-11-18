from .engine import Base, db_engine
from .system_models import Taxes
from .budget_models import DailyBudget, GeneralBudget
from .models import Users, Payers, Categories, Banks


tables = tables=[
        # Users.__table__,
        # Payers.__table__,
        # Categories.__table__,
        # Banks.__table__,
        # Taxes.__table__,
        DailyBudget.__table__,
        GeneralBudget.__table__,
        ]


def create_table():
    Base.metadata.drop_all(db_engine, tables=tables)
    Base.metadata.create_all(db_engine, tables=tables)


if __name__ == '__main__':
    create_table()