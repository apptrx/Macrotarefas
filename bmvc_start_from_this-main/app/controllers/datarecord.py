# app/controllers/datarecord.py
from app.models.evento import Evento
import json

class DataRecord:
    def __init__(self):
        self.eventos = []
        self.carregar()

    def carregar(self):
        try:
            with open("app/controllers/db/eventos.json", "r") as f:
                dados = json.load(f)
                self.eventos = [Evento(**item) for item in dados]
        except FileNotFoundError:
            self.eventos = []

    def salvar(self):
        with open("app/controllers/db/eventos.json", "w") as f:
            json.dump([vars(e) for e in self.eventos], f, indent=2)

    def listar(self):
        return self.eventos

    def adicionar(self, evento):
        self.eventos.append(evento)
        self.salvar()

    def deletar(self, nome):
        nome = nome.replace('_', ' ')
        self.eventos = [e for e in self.eventos if e.nome != nome]
        self.salvar()

