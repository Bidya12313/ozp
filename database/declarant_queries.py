from sqlalchemy import select, insert, update

from .engine import session_factory
from .budget_models import DailyBudget, GeneralBudget
from .system_models import Taxes
from .queries import get_declarant_budget

from errors import BudgetExceededError


def update_delcarant_budget(declarant, budget):
    with session_factory() as session:
        query = update(DailyBudget).values(budget=budget).filter(DailyBudget.declarant==declarant)
        result = session.execute(query)
        session.commit()


def create_tax(declarant: str, payer: str, director: str, recipient: str, category: str, amount: float, document: str, comment: str):
    with session_factory() as session:
        declarant_budget = float(get_declarant_budget(declarant))
        if float(amount) > declarant_budget:
            raise BudgetExceededError
        declarant_budget -= float(amount)
        update_budget = update_delcarant_budget(declarant, declarant_budget)
        
        query = Taxes(
            typetx='На оплату',
            declarant=declarant,
            payer=payer,
            director=director,
            recipient=recipient,
            amount=amount,
            category=category,
            document=document,
            comment=comment,
            status='Надіслано'
        )
        session.add(query)
        session.commit()