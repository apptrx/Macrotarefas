# app/controllers/datarecord.py
from app.models.evento import Evento
import json

class DataRecord:
    def __init__(self):
        self.eventos = []
        self.carregar()

    def carregar(self):
        try:
            with open("app/controllers/db/eventos.json", "r", encoding="utf-8") as f:
                dados = json.load(f)
                self.eventos = [Evento(**item) for item in dados]
        except FileNotFoundError:
            self.eventos = []

    def salvar(self):
        with open("app/controllers/db/eventos.json", "w", encoding="utf-8") as f:
            json.dump([vars(e) for e in self.eventos], f, indent=2, ensure_ascii=False)

    def listar(self):
        return self.eventos

    def adicionar(self, evento):
        self.eventos.append(evento)
        self.salvar()

    def deletar(self, nome):
        nome = nome.replace('_', ' ')
        self.eventos = [e for e in self.eventos if e.nome != nome]
        self.salvar()

    def adicionar_evento_manual(self, data):
        nome = data.get("nome")
        data_evento = data.get("data")
        local = data.get("local")
        horario = data.get("horario")

        if not nome or not data_evento or not local or not horario:
            raise ValueError("Dados incompletos para o evento.")

        evento = Evento(nome, data_evento, local, horario)
        self.adicionar(evento)

