# from flask import Blueprint
# from flask import redirect, request
# from flask_login import login_required
# from models import Client, db
#
# bp = Blueprint('client', __name__)
#
# @bp.route("/")
# @login_required
# def client_add():
#
#     client = Client()
#
#     client.nome =  request.form.get('nome')
#     client.razao_social =  request.form.get('razao_social')
#     client.rua =  request.form.get('rua')
#     client.cep =  request.form.get('cep')
#     client.bairro =  request.form.get('bairro')
#     client.cidade =  request.form.get('cidade')
#     client.observacao =  request.form.get('observacao')
#
#     db.session.add(client)
#     db.session.commit()
#
# # @bp.before_request
# # def restrict_bp_to_admins():
# #     if not users.is_current_user_admin():
# #         return redirect(users.create_login_url(request.url))