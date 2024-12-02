from .engine import session_factory
from .queries import get_tax


def choose_tax_bank(tax_id: int, bank: str):
    with session_factory() as session:
        tax = get_tax(tax_id, session)
        tax.status = 'Банк'
        tax.bank = bank
        session.commit()

    
def pay_tax(tax_id: int):
    with session_factory() as session:
        tax = get_tax(tax_id, session)
        tax.status = 'Оплачено'
        session.commit()