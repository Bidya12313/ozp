from flask import Blueprint, render_template
from flask_login import login_required, current_user

from database.queries import (
    get_daily_budget,
    get_all_payers,
    get_all_categories,
    get_all_directors,
    get_all_user_taxes,
)


main_routes = Blueprint('main', __name__)

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