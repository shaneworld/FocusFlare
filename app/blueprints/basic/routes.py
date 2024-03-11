from flask import render_template
from app.blueprints.basic import basic

@basic.route('/')
def index():
    return render_template('index.html')
