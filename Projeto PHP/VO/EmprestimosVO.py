class Emprestimos:
    def __init__(self, id_emprestimo, matriculaFun, matriculaUs, registro, dataEmprestimo, dataDevolucao):
        self.id_emprestimo = id_emprestimo
        self.matriculaFun = matriculaFun
        self.matriculaUs = matriculaUs
        self.registro =registro
        self.dataEmprestimo = dataEmprestimo
        self.dataDevolucao = dataDevolucao

    def get_id_emprestimo(self):
        return self.id_emprestimo

    def set_id_emprestimo(self, emprestimo):
        self.id_emprestimo = emprestimo

    def get_matriculaFun(self):
        return self.matriculaFun

    def set_matriculaFun(self, matriculaFun):
        self.matriculaFun = matriculaFun

    def get_matriculaUs(self):
        return self.matriculaUs

    def set_matriculaUs(self, matriculaUs):
        self.matriculaUs = matriculaUs

    def get_registro(self):
        return self.registro

    def set_registro(self, registro):
        self.registro = registro

    def get_dataEmprestimo(self):
        return self.dataEmprestimo

    def set_dataEmprestimo(self, dataEmprestimo):
        self.dataEmprestimo = dataEmprestimo
    
    def get_dataDevolucao(self):
        return self.dataDevolucao

    def set_dataDevolucao(self, dataDevolucao):
        self.dataDevolucao = dataDevolucao


