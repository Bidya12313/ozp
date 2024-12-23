from errors import BudgetExceededError, FileNumberError
from .upload_document import upload_documents

from flask import Blueprint, flash, redirect, url_for, request
from flask_login import login_required, current_user

from database.declarant_queries import(
    create_tax,
    change_limit_request,
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
    document = request.files.getlist('documents')
    comment = request.form.get('comment')

    try:
        uploaded_docs = upload_documents(document)
        create_tax(declarant, payer, director, recipient, category, amount, uploaded_docs, comment)
        flash('Заявка успішно створена!', 'success')
    except FileNumberError:
        flash('Максимальна кількість файлів 5!', 'danger')
    except BudgetExceededError:
        flash('Не достатньо коштів на балансі!', 'danger')
    except:
        flash('Помилка! Не можливо створити заявку!', 'danger')
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


@manager_routes.route('/change_limit', methods=['POST'])
@login_required
def change_limit():
    declarant = current_user.name
    new_limit = request.form.get('new_limit')
    try:
        change_limit_request(declarant, new_limit)
        flash(f'Заявку на зміну ліміту успішно надіслано!', 'success')
    except:
        flash(f'Помилка! Заявку на зміну ліміту не надіслано!', 'danger')
    return redirect(url_for('main.main'))