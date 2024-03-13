import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = b'_53oi3uriq9pifpff;apl'
    # WTF CSRF
    WTF_CSRF_ENABLED = True
    # database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app', 'database', 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
