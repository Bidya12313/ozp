from flask import Blueprint, flash, redirect, url_for, request
from flask_login import login_required


operator_routes = Blueprint('operator', __name__)


# @operator_routes.route('/operator')