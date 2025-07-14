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
