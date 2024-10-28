from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user

from database.admin_queries import (
    insert_general_budget,
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