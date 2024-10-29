from sqlalchemy import select, insert, update

from .engine import session_factory
from .budget_models import DailyBudget, GeneralBudget
from .system_models import Taxes


def create_tax(declarant: str, payer: str, director: str, recipient: str, category: str, amount: float, document: str, comment: str):
    with session_factory() as session:
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