from app.controllers.application import Application
from app.models.evento import Evento
from bottle import Bottle, route, run, request, static_file, redirect, template, response

app = Bottle()
ctl = Application()

# -----------------------------------------------------------------------------
# Rotas padrão

@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./app/static')

@app.route('/helper')
def helper(info=None):
    return ctl.render('helper')

@app.route('/pagina', method='GET')
def action_pagina():
    return ctl.render('pagina')

# -----------------------------------------------------------------------------
# Suas rotas aqui:

@app.route('/eventos', method='GET')
def listar_eventos():
    return ctl.render('eventos')

@app.route('/eventos/adicionar', method='POST')
def adicionar_evento():
    import json
    try:
        raw_data = request.body.read().decode('utf-8')
        data = json.loads(raw_data)
        ctl.models.adicionar_evento_manual(data)
        return {"status": "ok"}
    except Exception as e:
        response.status = 500
        return {"status": "erro", "detalhe": str(e)}

@app.route('/eventos/deletar/<nome>', method='GET')
def deletar_evento(nome):
    ctl.models.deletar(nome)
    redirect('/pagina')

@app.route('/portal', method='GET')
def show_login():
    return ctl.portal()

@app.route('/portal', method='POST')
def do_login():
    username = request.forms.get("username")
    password = request.forms.get("password")
    session_id = ctl.authenticate_user(username, password)
    if session_id:
        redirect(f"/restrito/{username}")
    else:
        return "<h2>Login inválido</h2>"

@app.route('/restrito/<username>', method='GET')
def acessar_area(username):
    return ctl.pagina_restrita(username)

@app.route('/logout', method='POST')
def sair():
    ctl.logout_user()
    response.delete_cookie("session_id")
    redirect("/portal")

#-----------------------------------------------------------------------------

if __name__ == '__main__':
    run(app, host='0.0.0.0', port=8080, debug=True)
