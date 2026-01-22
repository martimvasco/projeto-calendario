class Category:
    """
    Categoria apenas classifica eventos e não tem regras de negócio próprias.
    """
    def __init__(self, id, nome, descricao):
        self.id = id
        self.nome = nome
        self.descricao = descricao