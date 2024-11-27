from flask import Flask
from flask_login import LoginManager

from .main_routes import main_routes
from .auth_routes import auth_routes
from .admin_routes import admin_routes
from .director_routes import director_routes
from .declarant_routes import manager_routes
from .operator_routes import operator_routes

from database.queries import get_user


app = Flask(__name__)
app.config["SECRET_KEY"] = "Ignds eefsdfndsofihihdi f23"
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"
login_manager.login_message = None


@login_manager.user_loader
def load_user(user_id):
    return get_user(user_id)


app.register_blueprint(main_routes)
app.register_blueprint(auth_routes)
app.register_blueprint(admin_routes)
app.register_blueprint(director_routes)
app.register_blueprint(manager_routes)
app.register_blueprint(operator_routes)


if __name__ == "__main__":
    app.run(debug=True)
