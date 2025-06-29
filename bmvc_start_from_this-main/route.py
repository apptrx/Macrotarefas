from app.controllers.application import Application
from app.models.evento import Evento
from bottle import Bottle, route, run, request, static_file, redirect, template, response

app = Bottle()
ctl = Application()

#-----------------------------------------------------------------------------
# Rotas padrão

@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./app/static')

@app.route('/helper')
def helper(info=None):
    return ctl.render('helper')

@app.route('/pagina', methods=['GET'])
def action_pagina():
    return ctl.render('pagina')

#-----------------------------------------------------------------------------
# suas rotas aqui:

@app.route('/eventos', method='GET')
def listar_eventos():
    return ctl.render('eventos')

@app.route('/eventos/adicionar', method='POST')
def adicionar_evento():
    nome = request.forms.get('nome')
    data = request.forms.get('data')
    local = request.forms.get('local')
    horario = request.forms.get('horario')
    
    if nome and data and local and horario:
        ctl.models.adicionar(Evento(nome, data, local, horario))
    
    redirect('/eventos')

@app.route('/eventos/deletar/<nome>', method='GET')
def deletar_evento(nome):
    ctl.models.deletar(nome)
    redirect('/eventos')

#-----------------------------------------------------------------------------

if __name__ == '__main__':
    run(app, host='0.0.0.0', port=8080, debug=True)
