from sqlalchemy import select, insert, desc, update

from .engine import session_factory
from .budget_models import GeneralBudget, DailyBudget
from .system_models import Taxes
from .queries import get_general_budget, get_declarant_budget

from errors import BudgetExceededError


def change_user_budget(declarant, required_budget):
    with session_factory() as session:
        current_user_budget = get_declarant_budget(declarant)
        general_budget = get_general_budget()

        available_budget = general_budget + current_user_budget

        if float(required_budget) > float(available_budget):
            raise BudgetExceededError
        
        general_budget += current_user_budget
        general_budget -= float(required_budget)
        
        general_budget_query = update(GeneralBudget).values(budget=general_budget)
        session.execute(general_budget_query)
        
        user_budget_query = update(DailyBudget).values(budget=required_budget).filter(DailyBudget.declarant==declarant)
        session.execute(user_budget_query)
        
        session.commit()


def get_requested_taxes():
    with session_factory() as session:
        get_taxes = select(Taxes).filter(Taxes.status=='Надіслано')
        result = session.execute(get_taxes)
        taxes = result.scalars().all()
    return taxes


def get_tax(tax_id: int, session):
    get_tax = select(Taxes).filter(Taxes.id==tax_id)
    result = session.execute(get_tax)
    tax = result.scalar_one()
    return tax


def confirm_tax(tax_id: int):
    with session_factory() as session:
        tax = get_tax(tax_id, session)
        if tax.typetx == 'На оплату':
            tax.status = 'На оплаті'
        if tax.typetx == 'Зміна ліміту':
            general_budget = get_general_budget()
            current_user_budget = get_declarant_budget(tax.declarant)
            general_budget += current_user_budget

            if float(tax.amount) > float(general_budget):
                raise BudgetExceededError
            
            general_budget -= tax.amount

            general_budget_query = update(GeneralBudget).values(budget=general_budget)
            session.execute(general_budget_query)
            
            user_budget_query = update(DailyBudget).values(budget=tax.amount).filter(DailyBudget.declarant==tax.declarant)
            session.execute(user_budget_query)
            
            tax.status = 'Змінено'
        session.commit()


def cancel_tax(tax_id: int):
    with session_factory() as session:
        tax = get_tax(tax_id, session)
        if tax.typetx == 'На оплату':
            tax.status = 'Відхилено'

            current_user_budget = get_declarant_budget(tax.declarant)
            user_budget_query = update(DailyBudget).values(budget=tax.amount).filter(DailyBudget.declarant==tax.declarant)
            session.execute(user_budget_query)

            current_user_budget += tax.amount
        if tax.typetx == 'Зміна ліміту':
            tax.status = 'Відхилено'
        session.commit()