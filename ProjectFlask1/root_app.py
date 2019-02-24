# -*- coding: utf-8 -*-
from flask import Flask, render_template, render_template_string, abort, redirect, url_for, g, request
from firebase.firebase import FirebaseAuthentication, FirebaseApplication
from Project.Imprimir import print_pedido
import getpass
import requests
import sys
import os



app = Flask(__name__)
dbfire = FirebaseApplication('https://vegans2godatabase.firebaseio.com', authentication=None)
authentication = FirebaseAuthentication('Wg6XvS7W0UftiQlBnCM1tt8gVSIE7exereBXcYx0', 'thegambiarra2@gmail.com', extra={'id': 123})
dbfire.authentication = authentication
s = requests.Session()


@app.route('/')
def page():
    return redirect(url_for('pagelogin'))


@app.route('/login')
def pagelogin():
    return render_template('login.html')


@app.route('/index')
def pageindex():
    produto = dbfire.get("/", "Produtos")
    return render_template('index.html', prod=produto)


@app.route('/confirmacao')
def pageconfirmacao():
    prod = {}
    total = .0
    # user = str(request.form['systemUser']).replace(".", "").replace("@", "").replace(" ", "")
    # print(user)
    user = 'humbertovsouza'
    pedido = dbfire.get("/Pedidos", user)
    produto = dbfire.get("/", "Produtos")
    if pedido is None:
        return render_template('vazio.html', user=user.replace("_", " "))
    else:
        for cod in pedido.keys():
            prod[cod] = produto[cod]
            prod[cod]['Quantidade'] = pedido[cod]
            total += (prod[cod]['Valor'] * pedido[cod])
        return render_template('confirmacao.html', prod=prod, total=total, user=user.replace("_", " "))


@app.route('/details')
def pagedetails():
    return render_template('details.html')


@app.route('/sucess')
def imprimir():
    user = str(getpass.getuser())
    if user == 'humberto':
        user = 'humbe'
    path = r"C:\Users/" + user + "\PycharmProjects\Vegans2go\Project\produtos.txt"
    print_pedido(path)
    return render_template('sucesso.html')
