from flask import Blueprint

gtd = Blueprint('gtd', __name__, template_folder='templates')

from app.blueprints.gtd import routes
