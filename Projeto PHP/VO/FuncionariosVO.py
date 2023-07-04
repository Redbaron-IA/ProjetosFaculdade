class Funcionarios:
    def __init__(self, matriculaFun, nome, email, telefone, login, senha):
        self.matriculaFun = matriculaFun
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.login = login
        self.senha = senha

    def get_matriculaFun(self):
        return self.matriculaFun

    def set_matriculaFun(self, matriculaFun):
        self.matricula = matriculaFun

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

    def get_login(self):
        return self.login

    def set_login(self, login):
        self.login = login

    def get_senha(self):
        return self.senha

    def set_senha(self, senha):
        self.senha = senha