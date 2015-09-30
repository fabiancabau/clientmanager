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


def create_app():
    application = Flask(__name__)
    application.config.from_object(Configuration)

    application.register_blueprint(client.bp)
    application.register_blueprint(login.bp)

    db.init_app(application)

    login.login_manager.init_app(application)
    return application


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=os.environ.get('$PORT') or 2000)
