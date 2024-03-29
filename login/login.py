# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import redirect, request
from flask.globals import session
from flask.helpers import url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user
from models import User, db
from flask.templating import render_template
from flask.views import MethodView
from messages import LoginMessages, CssMessages

bp = Blueprint('login', __name__)

login_manager = LoginManager()

@login_manager.user_loader
def load_user(userid):
    return User.get_user(userid)

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('login.LoginAPIForm'))

class LoginAPIForm(MethodView):

    def post(self):

        user = User.check_password(request.form.get('username'), request.form.get('password'))
        if user:
            login_user(user)
            session['username'] = user.username
            return redirect(url_for('client.ClientAPIList'))
        else:
            flash(LoginMessages.LOGIN_ERROR, CssMessages.ERROR)
            return render_template('login.html')

    def get(self):
        return render_template('login.html')


bp.add_url_rule('/login', view_func=LoginAPIForm.as_view('LoginAPIForm'))


class LogoutAPI(MethodView):

    def get(self):
        logout_user()
        return redirect(url_for('login.LoginAPIForm'))


bp.add_url_rule('/logout', view_func=LogoutAPI.as_view('LogoutAPI'))


