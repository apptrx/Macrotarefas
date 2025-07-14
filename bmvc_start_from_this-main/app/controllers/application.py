from app.controllers.datarecord import DataRecord
from bottle import template, redirect, request, response



class Application:
    def __init__(self):
        self.models = DataRecord()
        self.pages = {
            'pagina': self.pagina
        }

    def render(self, page, parameter=None):
        content = self.pages.get(page, self.helper)
        if not parameter:
            return content()
        else:
            return content(parameter)

    def pagina(self):
        lista = self.models.listar()
        return template('app/views/html/pagina', eventos=lista)

    def helper(self):
        return template('app/views/html/helper')
    
    def get_session_id(self):
        return request.get_cookie("session_id")

    def is_authenticated(self, username):
        return username == self.models.get_username(self.get_session_id())

    def authenticate_user(self, username, password):
        session_id = self.models.check_user(username, password)
        if session_id:
            response.set_cookie("session_id", session_id, httponly=True, secure=False)
            return session_id
        return None

    def logout_user(self):
        self.models.logout(self.get_session_id())

    def portal(self):
        return template("app/views/html/portal")

    def pagina_restrita(self, username):
        if self.is_authenticated(username):
            lista = self.models.listar()
            return template("app/views/html/pagina", eventos=lista)
        else:
            redirect("/portal")
