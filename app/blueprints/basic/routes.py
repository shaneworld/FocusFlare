from flask import render_template
from flask_login import login_required, current_user
from app.blueprints.basic import basic
from app.models import User

@basic.route('/')
@login_required
def home():
    return render_template('index.html')

