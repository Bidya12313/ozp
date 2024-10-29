from flask import Blueprint, flash, redirect, url_for, request
from flask_login import login_required

from database.admin_queries import (
    insert_general_budget,
    reset_all_limits,
    reset_user_limit,
)

admin_routes = Blueprint('admin', __name__)


@admin_routes.route('/set_budget', methods=['POST'])
@login_required
def set_general_budget():
    general_budget = request.form.get('general_budget').replace(',', '.')

    try:
        if general_budget:
            insert_general_budget(general_budget)
            flash('Ліміт успішно додано!', 'success')
    except:
        flash('Помилка! Не можливо надіслати ліміт!', 'danger')
    return redirect(url_for('main.admin'))


@admin_routes.route('/reset_all_limits', methods=['POST'])
@login_required
def reset_page_all_limits():
    try:
        reset_all_limits()
        flash('Ліміти обнулено!', 'success')
    except:
        flash('Помилка! Ліміти не обнулено', 'danger')
    return redirect(url_for('main.admin'))


@admin_routes.route('/reset_user_limit', methods=['POST'])
@login_required
def reset_page_user_limit():
    declarant = request.form.get('declarant')
    try:
        reset_user_limit(declarant)
        flash(f'Ліміт {declarant} обнулено!', 'success')
    except:
        flash(f'Помилка! Ліміт {declarant} не обнулено!', 'danger')
    return redirect(url_for('main.admin'))