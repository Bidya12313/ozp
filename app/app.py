from flask import Flask, render_template, flash, redirect, url_for
from flask_login import LoginManager, login_user, login_required, current_user

from .main_routes import main_routes
from .auth_routes import auth_routes

from database.queries import get_user


app = Flask(__name__)
app.config["SECRET_KEY"] = "Ignds eefsdfndsofihihdi f23"
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"


@login_manager.user_loader
def load_user(user_id):
    return get_user(user_id)


app.register_blueprint(main_routes)
app.register_blueprint(auth_routes)


if __name__ == "__main__":
    app.run(debug=True)
