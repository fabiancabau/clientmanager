# -*- coding: utf-8 -*-

from hashlib import md5
from datetime import datetime
from flask import Flask
from flask import request, redirect, url_for
from flask.templating import render_template
from flask_login import LoginManager, login_user, login_required, logout_user
from flask import flash
from werkzeug.utils import secure_filename
from models import db, User
import os

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/clientmanager'
application.secret_key = '0mG`itS4s3cr3t'

# This is the path to the upload directory
application.config['UPLOAD_FOLDER'] = 'static/uploads/'
# These are the extension that we are accepting to be uploaded

db.init_app(application)

login_manager = LoginManager()
login_manager.init_app(application)

@login_manager.user_loader
def load_user(userid):
    return User.get_user(userid)

@application.route('/')
def index():

    return render_template('index.html')


@application.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        user = User.check_password(request.form.get('username'), request.form.get('password'))
        if user:
            login_user(user)
            return redirect(url_for('admin'))
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')


@application.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():

    return render_template('admin.html')


@application.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('login')


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=os.environ.get('$PORT') or 2000)
