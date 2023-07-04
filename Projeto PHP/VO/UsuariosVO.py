class Usuarios:
    def __init__(self, matriculaUs, nome, email, telefone):
        self.matriculaUs = matriculaUs
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def get_matriculaUs(self):
        return self.matriculaUs

    def set_matriculaUs(self, matriculaUs):
        self.matriculaUs = matriculaUs

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_telefone(self):
        return self.telefone

    def set_telefone(self, telefone):
        self.telefone = telefone
