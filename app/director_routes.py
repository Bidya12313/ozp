from flask import Blueprint, flash, redirect, url_for, request, send_from_directory
from flask_login import login_required

from database.director_queries import (
    change_user_budget,
    confirm_tax,
    cancel_tax,
)
from errors import BudgetExceededError


director_routes = Blueprint('director', __name__)


@director_routes.route('/change_budget', methods=['POST'])
@login_required
def change_budget():
    declarant = request.form.get('declarant')
    required_budget = request.form.get('required_budget').replace(',', '.')
    try:
        change_user_budget(declarant=declarant, required_budget=required_budget)
        flash(f'Заявнику {declarant} змінено бюджет!', 'success')
    except BudgetExceededError:
        flash('Запитуваний бюджет перевищує загальний бюджет!', 'danger')
    except Exception:
        flash('Не вдалося змінити ліміт!', 'danger')
    return redirect(url_for('main.director'))


@director_routes.route('/approve_tax', methods=['POST'])
@login_required
def approve_tax():
    tax_id = request.form.get('request_id')
    try:
        confirm_tax(tax_id)
        flash(f'Заявка підтверджена!', 'success')
    except BudgetExceededError:
        flash('Запитуваний бюджет перевищує загальний бюджет!', 'danger')
    except Exception:
        flash('Не вдалося змінити ліміт!', 'danger')
    return redirect(url_for('main.director'))


@director_routes.route('/reject_tax', methods=['POST'])
@login_required
def reject_tax():
    tax_id = request.form.get('request_id')
    try:
        cancel_tax(tax_id)
        flash('Заявка відхилена!', 'success')
    except BudgetExceededError:
        flash('Запитуваний бюджет перевищує загальний бюджет!', 'danger')
    except Exception:
        flash('Не вдалося змінити ліміт!', 'danger')
    return redirect(url_for('main.director'))


@director_routes.route('/uploads/<docname>')
def open_document(docname):
    return send_from_directory('../uploads', docname)

