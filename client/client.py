from flask import Blueprint
from flask import redirect, request
from flask.helpers import url_for, flash
from flask_login import login_required
from models import Client, db
from flask.templating import render_template
from flask.views import MethodView


bp = Blueprint('client', __name__)


class ClientAPIForm(MethodView):

    def post(self):

        client = Client()

        client.nome =  request.form.get('nome')
        client.razao_social =  request.form.get('razao_social')
        client.rua =  request.form.get('rua')
        client.cep =  request.form.get('cep')
        client.bairro =  request.form.get('bairro')
        client.cidade =  request.form.get('cidade')
        client.observacao =  request.form.get('observacao')

        client.save()

        flash('Cliente adicionado com sucesso!', 'Sucesso!')
        return redirect(url_for('.ClientAPIForm'))

    def get(self):
        return render_template('client_add.html')


bp.add_url_rule('/client', view_func=ClientAPIForm.as_view('ClientAPIForm'))


class ClientAPI(MethodView):

    def get(self, id=None):

        client = Client.query.get(id)

        return render_template('client_update.html', client=client)

    def post(self, id=None):

        client = Client.query.get(id)

        client.nome =  request.form.get('nome')
        client.razao_social =  request.form.get('razao_social')
        client.rua =  request.form.get('rua')
        client.cep =  request.form.get('cep')
        client.bairro =  request.form.get('bairro')
        client.cidade =  request.form.get('cidade')
        client.observacao =  request.form.get('observacao')


bp.add_url_rule('/client/<id>', view_func=ClientAPI.as_view('ClientAPI'), methods=['GET', 'POST'])


class ClientAPIList(MethodView):

    def get(self, id=None):

        return render_template('client_list.html')


bp.add_url_rule('/clients', view_func=ClientAPIList.as_view('ClientAPIList'))





# @bp.before_request
# def restrict_bp_to_admins():
#     if not users.is_current_user_admin():
#         return redirect(users.create_login_url(request.url))