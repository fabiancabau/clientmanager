# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import redirect, request
from flask.helpers import url_for, flash
from flask_login import login_required
from flask.templating import render_template
from flask.views import MethodView
from models import Client


bp = Blueprint('sale', __name__)


class SaleAPIForm(MethodView):

    def post(self, id):

        flash({"message": 'Cliente adicionado com sucesso!', "title": "Sucesso!"}, 'success')
        return redirect(url_for('sale.SaleAPIForm'))

    def get(self, id):

        client = Client.get_client(id=id)

        return render_template('sale_add.html', client_id=id)


bp.add_url_rule('/client/<id>/sale', view_func=SaleAPIForm.as_view('SaleAPIForm'))

#
# class ClientAPI(MethodView):
#
#     def get(self, id=None):
#
#         client = Client.query.get(id)
#
#         if client:
#             return render_template('client_update.html', client=client)
#         else:
#             return render_template('page_404.html')
#
#     def post(self, id=None):
#
#         client = Client.query.get(id)
#
#         client.nome =  request.form.get('nome')
#         client.razao_social =  request.form.get('razao_social')
#         client.rua =  request.form.get('rua')
#         client.cep =  request.form.get('cep')
#         client.bairro =  request.form.get('bairro')
#         client.cidade =  request.form.get('cidade')
#         client.email = request.form.get('email')
#         client.observacao =  request.form.get('observacao')
#
#         client.save()
#
#         return redirect(url_for('.ClientAPI', id=id))
#
#
# bp.add_url_rule('/client/<id>', view_func=ClientAPI.as_view('ClientAPI'), methods=['GET', 'POST'])
#
#
# class ClientAPIList(MethodView):
#
#     def get(self, id=None):
#
#         if id:
#             clients = Client.query.filter_by(id=id)
#         else:
#             clients = Client.query.all()
#
#         return render_template('client_list.html', clients=clients)
#
#
# bp.add_url_rule('/clients', view_func=ClientAPIList.as_view('ClientAPIList'))





# @bp.before_request
# def restrict_bp_to_admins():
#     if not users.is_current_user_admin():
#         return redirect(users.create_login_url(request.url))