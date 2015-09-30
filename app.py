# -*- coding: utf-8 -*-

from hashlib import md5
from datetime import datetime
from flask import Flask
from flask import request, redirect, url_for
from flask.templating import render_template
from flask_login import LoginManager, login_user, login_required, logout_user
from flask import flash
from werkzeug.utils import secure_filename
from models import db, User, Client
import os
from client import client
from login import login
from config import Configuration

application = Flask(__name__)
application.config.from_object(Configuration)

application.register_blueprint(client.bp)
application.register_blueprint(login.bp)

db.init_app(application)

login_manager = LoginManager()
login_manager.init_app(application)

@login_manager.user_loader
def load_user(userid):
    return User.get_user(userid)

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('login.LoginAPIForm'))


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=os.environ.get('$PORT') or 2000)
