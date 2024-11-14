from flask import Blueprint, flash, redirect, url_for, request
from flask_login import login_required

from database.operator_queries import choose_tax_bank, pay_tax


operator_routes = Blueprint('operator', __name__)


@operator_routes.route('/choose_bank', methods=['POST'])
@login_required
def choose_bank():
    tax_id = request.form.get('request_id')
    bank = request.form.get('bank')
    try:
        choose_tax_bank(tax_id, bank)
        flash(f'Заявка {tax_id} - {bank}', 'success')
    except:
        flash('Не вдалося вибрати банк', 'danger')
    return redirect(url_for('main.bank_operator'))


@operator_routes.route('/pay', methods=['POST'])
@login_required
def pay():
    tax_id = request.form.get('request_id')
    try:
        pay_tax(tax_id)
        flash(f'Заявка {tax_id} оплачена', 'success')
    except:
        flash('Не вдалося оплачити', 'danger')
    return redirect(url_for('main.bank_operator'))