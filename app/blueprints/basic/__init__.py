from flask import Blueprint

basic = Blueprint('basic', __name__)

from app.blueprints.basic import routes
