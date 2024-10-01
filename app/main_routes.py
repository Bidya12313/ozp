from flask import Blueprint, render_template
from flask_login import login_required, current_user

from database.queries import (
    get_all_payers,
    get_all_categories,
    get_all_directors,
    get_declarant,
    get_user,
)


main_routes = Blueprint('main', __name__)

@main_routes.route('/')
@login_required
def main():
    declarant = current_user
    return render_template(
        "main.html",
        declarant=declarant.name,
        payers=get_all_payers(),
        directors=get_all_directors(),
        categories=get_all_categories(),
    )