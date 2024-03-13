from flask import Blueprint

basic = Blueprint('basic', __name__, template_folder='templates')

from app.blueprints.basic import routes
