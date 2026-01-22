import json
from models.event import Event
from models.category import Category
from datetime import datetime


class CalendarManager:
    def __init__(self):
        self.eventos = []
        self.categoria_default = Category(1, "Geral", "Categoria padrão")
        self.carregar_eventos()

    def carregar_eventos(self):
        try:
            with open("data/eventos.json", "r", encoding="utf-8") as f:
                dados = json.load(f)
                for e in dados:
                    evento = Event(
                        e["id"],
                        e["titulo"],
                        e["descricao"],
                        datetime.fromisoformat(e["data_inicio"]),
                        datetime.fromisoformat(e["data_fim"]),
                        e["prioridade"],
                        self.categoria_default
                    )
                    self.eventos.append(evento)
        except FileNotFoundError:
            self.eventos = []

    def guardar_eventos(self):
        with open("data/eventos.json", "w", encoding="utf-8") as f:
            json.dump(
                [
                    {
                        "id": e.id,
                        "titulo": e.titulo,
                        "descricao": e.descricao,
                        "data_inicio": e.data_inicio.isoformat(),
                        "data_fim": e.data_fim.isoformat(),
                        "prioridade": e.prioridade
                    }
                    for e in self.eventos
                ],
                f,
                indent=4,
                ensure_ascii=False
            )

    def adicionar_evento(self, evento):
        if not evento.validar_datas():
            return False

        self.eventos.append(evento)
        self.guardar_eventos()
        return True
