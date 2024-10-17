from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user

from database.queries import (
    get_daily_budget,
    get_all_payers,
    get_all_categories,
    get_all_directors,
    get_all_user_taxes
)

from database.admin_queries import (
    get_declarants_balances
)


main_routes = Blueprint('main', __name__)


# main page
@main_routes.route('/')
@login_required
def main():
    declarant = current_user
    return render_template(
        "main.html",
        declarant=declarant.name,
        daily_budget=get_daily_budget(declarant.name),
        payers=get_all_payers(),
        directors=get_all_directors(),
        categories=get_all_categories(),
        user_taxes=get_all_user_taxes(declarant.name),
    )


# admin page
@main_routes.route('/admin')
@login_required
def admin():
    declarant = current_user
    admin_status = declarant.admin_status
    if admin_status == '+':
        return render_template(
            "admin.html",
            daily_user_budget = get_declarants_balances()
        )
    flash('Ви повинні бути адміністратором')
    return redirect(url_for('main.main'))