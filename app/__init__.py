from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, current_user
from config import Config

# Create app
app = Flask(__name__)

# Load config
app.config.from_object(Config)

# login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"
login_manager.login_message = None

db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)

# register blueprints
from app.blueprints.basic import basic
app.register_blueprint(basic)

from app.blueprints.auth import auth
app.register_blueprint(auth)

from app.blueprints.gtd import gtd
app.register_blueprint(gtd)

from app.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()

@app.context_processor
def inject_username():
    if current_user.is_authenticated:
        return {'username': current_user.username}
    return {'username': None}


########################
#### error handlers ####
########################


# @app.errorhandler(401)
# def unauthorized_page(error):
#     return render_template("errors/401.html"), 401
#
#
@app.errorhandler(404)
def page_not_found(error):
    return render_template("errors/404.html"), 404
#
#
# @app.errorhandler(500)
# def server_error_page(error):
#     return render_template("errors/500.html"), 500
