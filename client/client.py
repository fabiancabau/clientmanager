# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import redirect, request
from flask.helpers import url_for, flash
from flask_login import login_required
from models import Client, db
from flask.templating import render_template
from flask.views import MethodView
from messages import ClientMessages, CssMessages


bp = Blueprint('client', __name__)


class ClientAPIForm(MethodView):

    @login_required
    def post(self):

        client = Client()

        client.nome =  request.form.get('nome')
        client.razao_social =  request.form.get('razao_social')
        client.rua =  request.form.get('rua')
        client.cep =  request.form.get('cep')
        client.bairro =  request.form.get('bairro')
        client.cidade =  request.form.get('cidade')
        client.email = request.form.get('email')
        client.observacao =  request.form.get('observacao')

        client.save()

        flash(ClientMessages.CLIENT_ADD_SUCCESS, CssMessages.SUCCESS)
        return redirect(url_for('.ClientAPIForm'))

    @login_required
    def get(self):
        return render_template('client_add.html')


bp.add_url_rule('/client', view_func=ClientAPIForm.as_view('ClientAPIForm'))


class ClientAPI(MethodView):

    @login_required
    def get(self, id=None):

        client = Client.query.get(id)

        if client:
            return render_template('client_update.html', client=client)
        else:
            return render_template('page_404.html')

    @login_required
    def post(self, id=None):

        client = Client.query.get(id)

        client.nome =  request.form.get('nome')
        client.razao_social =  request.form.get('razao_social')
        client.rua =  request.form.get('rua')
        client.cep =  request.form.get('cep')
        client.bairro =  request.form.get('bairro')
        client.cidade =  request.form.get('cidade')
        client.email = request.form.get('email')
        client.observacao =  request.form.get('observacao')

        client.save()

        flash(ClientMessages.CLIENT_UPDATE_SUCCESS, 'success')

        return redirect(url_for('.ClientAPI', id=id))


bp.add_url_rule('/client/<id>', view_func=ClientAPI.as_view('ClientAPI'), methods=['GET', 'POST'])


class ClientAPIList(MethodView):

    @login_required
    def get(self, id=None):

        if id:
            clients = Client.query.filter_by(id=id)
        else:
            clients = Client.query.all()

        return render_template('client_list.html', clients=clients)


bp.add_url_rule('/clients', view_func=ClientAPIList.as_view('ClientAPIList'))





# @bp.before_request
# def restrict_bp_to_admins():
#     if not users.is_current_user_admin():
#         return redirect(users.create_login_url(request.url))