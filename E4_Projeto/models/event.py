from datetime import datetime


class Event:
    def __init__(self, id, titulo, descricao, data_inicio, data_fim, prioridade, categoria):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.prioridade = prioridade
        self.categoria = categoria

    def validar_datas(self):
        """
        Valida se a data/hora de fim é posterior à data/hora de início.
        """
        return self.data_fim > self.data_inicio
