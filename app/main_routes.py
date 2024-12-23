from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user

from database.queries import (
    get_daily_budget,
    get_all_payers,
    get_all_categories,
    get_all_directors,
    get_all_user_taxes,
    get_declarants_balances,
    get_all_banks,
)

from database.director_queries import (
    get_general_budget,
    get_requested_taxes,
)


main_routes = Blueprint('main', __name__)


def get_user_status(user):
    return {
        'is_operator': user.operator_status,
        'is_admin': user.admin_status == '+',
        'is_director': user.director_status == '+'
    }


# main page
@main_routes.route('/')
@login_required
def main():
    declarant = current_user
    user_status = get_user_status(declarant)
    return render_template(
        "main.html",
        declarant=declarant.name,
        daily_budget=get_daily_budget(declarant.name),
        payers=get_all_payers(),
        directors=get_all_directors(),
        categories=get_all_categories(),
        user_taxes=get_all_user_taxes(declarant.name),
        **user_status
    )


# admin page
@main_routes.route('/admin')
@login_required
def admin():
    declarant = current_user
    user_status = get_user_status(declarant)
    if user_status['is_admin']:
        return render_template(
            "admin.html",
            declarant=declarant.name,
            daily_user_budget = get_declarants_balances(),
            **user_status
        )
    flash('Ви повинні бути адміністратором')
    return redirect(url_for('main.main'))


# director page
@main_routes.route('/director')
@login_required
def director():
    declarant = current_user
    user_status = get_user_status(declarant)
    if user_status['is_director']:
        return render_template(
            "director.html",
            declarant=declarant.name,
            general_budget = get_general_budget(),
            daily_user_budget = get_declarants_balances(),
            taxes = get_requested_taxes('Надіслано'),
            **user_status
        )
    flash('Ви повинні бути керівником')
    return redirect(url_for('main.main'))


# bank operator page
@main_routes.route('/operator')
@login_required
def bank_operator():
    operator = current_user
    user_status = get_user_status(operator)
    if user_status['is_operator']:
        return render_template(
            "operator.html",
            declarant=operator.name,
            banks = get_all_banks(),
            bank_taxes = get_requested_taxes('Банк'),
            taxes = get_requested_taxes('На оплаті'),
            **user_status,
        )
    flash('Ви повинні бути оператором')
    return redirect(url_for('main.main'))