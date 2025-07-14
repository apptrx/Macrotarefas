from app.models.evento import Evento
from app.models.user_account import UserAccount
import uuid
import json

class DataRecord:
    def __init__(self):
        self.eventos = []
        self.__user_accounts = []
        self.__authenticated_users = {}
        self.carregar_usuarios()

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
    def carregar_usuarios(self):
        try:
            with open("app/controllers/db/usuarios.json", "r", encoding="utf-8") as f:
                dados = json.load(f)
                self.__user_accounts = [UserAccount(**u) for u in dados]
        except FileNotFoundError:
            self.__user_accounts = [UserAccount("admin", "admin")]

    def check_user(self, username, password):
        for user in self.__user_accounts:
            if user.username == username and user.password == password:
                session_id = str(uuid.uuid4())
                self.__authenticated_users[session_id] = user
                return session_id
        return None

    def get_username(self, session_id):
        if session_id in self.__authenticated_users:
            return self.__authenticated_users[session_id].username
        return None

    def logout(self, session_id):
        if session_id in self.__authenticated_users:
            del self.__authenticated_users[session_id]

