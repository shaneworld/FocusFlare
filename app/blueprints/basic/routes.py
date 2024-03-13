from flask import render_template
from flask_login import login_required
from app.blueprints.basic import basic

@basic.route('/')
@login_required
def home():
    return render_template('index.html')
