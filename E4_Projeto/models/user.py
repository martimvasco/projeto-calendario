class User:
    """
    Representa um utilizador do sistema.
    Pode ser um utilizador normal ou administrador.
    """
    def __init__(self, id, nome, email, password, perfil):
        self.id = id
        self.nome = nome
        self.email = email
        self.password = password
        self.perfil = perfil