from flask import Flask, render_template, flash, redirect, url_for
from flask_login import LoginManager, login_user, login_required, current_user

from database.queries import (
    get_all_declarants,
    get_all_payers,
    get_all_categories,
    get_all_directors,
    get_declarant,
    get_user,
)
from .forms import LoginForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "Ignds eefsdfndsofihihdi f23"
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return get_user(user_id)


@app.route("/")
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


@app.route("/login")
def login():
    login_form = LoginForm()
    return render_template("login.html", form=login_form)


@app.route("/procces_login", methods=["POST"])
def procces_login():
    form = LoginForm()

    if form.validate_on_submit():
        user = get_declarant(form.username.data)
        if user and int(form.password.data) == int(user.password):
            login_user(user)
            return redirect(url_for("main"))
        flash("Не правильне ім'я або пароль")
        return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
