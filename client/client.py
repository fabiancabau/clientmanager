from flask import Blueprint
from flask import redirect, request
from flask_login import login_required
from models import Client, db
from flask.templating import render_template

bp = Blueprint('client', __name__)


@bp.route("/", methods=['GET', 'POST'])
def client_add():


    if request.method == "POST":

        client = Client()

        client.nome =  request.form.get('nome')
        client.razao_social =  request.form.get('razao_social')
        client.rua =  request.form.get('rua')
        client.cep =  request.form.get('cep')
        client.bairro =  request.form.get('bairro')
        client.cidade =  request.form.get('cidade')
        client.observacao =  request.form.get('observacao')

        db.session.add(client)
        db.session.commit()

    elif request.method == "GET":

        return render_template('client_add.html')



# @bp.before_request
# def restrict_bp_to_admins():
#     if not users.is_current_user_admin():
#         return redirect(users.create_login_url(request.url))