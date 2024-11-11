from errors import BudgetExceededError

from flask import Blueprint, flash, redirect, url_for, request
from flask_login import login_required, current_user

from database.declarant_queries import(
    create_tax,
)

from database.admin_queries import(
    reset_user_budget,
)

manager_routes = Blueprint('manager', __name__)


@manager_routes.route('/create_tax', methods=['POST'])
@login_required
def create_tax_route():
    declarant = request.form.get('declarant')
    payer = request.form.get('payer')
    director = request.form.get('director')
    recipient = request.form.get('recipient')
    category = request.form.get('category')
    amount = request.form.get('amount')
    document = request.form.get('document')
    comment = request.form.get('comment')

    try:
        create_tax(declarant, payer, director, recipient, category, amount, document, comment)
        flash('Заявка успішно створена!', 'success')
    except BudgetExceededError:
        flash('Не достатньо коштів на балансі!', 'danger')
    except:
        flash('Помилка! Не можливо створити заявку!')
    return redirect(url_for('main.main'))


@manager_routes.route('/reset_limit', methods=['POST'])
@login_required
def reset_limit():
    declarant = current_user.name
    try:
        reset_user_budget(declarant)
        flash(f'Ліміт обнулено!', 'success')
    except:
        flash(f'Помилка! Ліміт не обнулено!', 'danger')
    return redirect(url_for('main.main'))