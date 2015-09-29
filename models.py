# -*- coding: utf-8 -*-

from hashlib import md5, sha1
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from flask_login import UserMixin


db = SQLAlchemy()

class User(db.Model, UserMixin):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(120), unique=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username

    @classmethod
    def get_user(cls, id):
        return User.query.get(id)

    @classmethod
    def check_password(cls, username, password):
        encoded_password = md5(password).hexdigest()

        user = User.query.filter_by(username=username, password=encoded_password).first()

        if user:
            return user

        return None


class Client(db.Model):

    __tablename__ = 'client'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200))
    razao_social = db.Column(db.String(200))
    rua = db.Column(db.String(200))
    cep = db.Column(db.String(200))
    bairro = db.Column(db.String(200))
    cidade = db.Column(db.String(200))
    email = db.Column(db.String(200))
    dt_cadastro = db.Column(db.DateTime, default=datetime.now())
    observacao = db.Column(db.Text)

    def __repr__(self):
        return '<Client %r>' % self.nome


    def save(self):
        db.session.add(self)
        db.session.commit()


# class Charge(db.Model):
#
#     __tablename__ = 'charge'
    