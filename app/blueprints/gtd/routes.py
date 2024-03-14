from flask import render_template
from app.blueprints.gtd import gtd

@gtd.route("/gtd")
def gtd_list():
    return render_template('gtd.html')
