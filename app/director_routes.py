from flask import Blueprint, flash, redirect, url_for, request
from flask_login import login_required

from database.director_queries import (
    change_user_budget,
)

director_routes = Blueprint('director', __name__)


@director_routes.route('/change_budget', methods=['POST'])
@login_required
def change_budget():
    declarant = request.form.get('declarant')
    required_budget = request.form.get('required_budget').replace(',', '.')
    try:
        change_user_budget(declarant=declarant, required_budget=required_budget)
        flash(f'Заявнику {declarant} змінено бюджет!', 'success')
    except:
        flash('Не вдалося змінити ліміт!', 'danger')
    return redirect(url_for('main.director'))


