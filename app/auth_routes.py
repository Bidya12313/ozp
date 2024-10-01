from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user
from .forms import LoginForm

from database.queries import get_declarant


auth_routes = Blueprint('auth', __name__)

@auth_routes.route("/login")
def login():
    login_form = LoginForm()
    return render_template("login.html", form=login_form)


@auth_routes.route("/procces_login", methods=["POST"])
def procces_login():
    form = LoginForm()

    if form.validate_on_submit():
        user = get_declarant(form.username.data)
        if user and int(form.password.data) == int(user.password):
            login_user(user)
            return redirect(url_for("main.main"))
        flash("Не правильне ім'я або пароль")
        return redirect(url_for("auth.login"))