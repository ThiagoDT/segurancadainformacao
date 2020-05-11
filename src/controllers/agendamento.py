from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user

import datetime

from src import db
from src.models.tabelas import *

agendamento_module = Blueprint('agendamento', __name__, url_prefix="/agendamento",
                    template_folder='../templates')



@agendamento_module.route("/create", methods=["GET"])
@login_required
def agendamento():
    if current_user.funcionario:
        servicos = Servicos.query.all()
        usuarios = Usuario.query.all()
        return servicos, usuarios  #enviar para o front listar
    else:
        servicos = Servicos.query.all()
        return servicos, current_user #enviar para o front listar usuario pre checado


    
@agendamento_module.route("/create", methods=["POST"])
@login_required
def criar_agendamento():
    id_usuario = request.form.get('id_usuario')
    id_servico = request.form.get('id_servico')
    novo_agendamento = Agendamento(id_usuario = id_usuario, id_servico = id_servico)
    db.session.add(novo_agendamento)
    db.session.commit()
    return 'pagina de agendamento'