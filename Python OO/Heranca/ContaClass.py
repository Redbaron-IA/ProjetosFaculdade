#Classe conta Super classe ou classe pai

class Conta:
    #Inicializa os atributos da class
    def __init__(self, Agencia, Codigo, DataDeCriacao, Titular, Senha, Saldo):
       
       self.Agencia = Agencia
       self.Codigo = Codigo
       self.DataDeCriacao = DataDeCriacao
       self.Titular = Titular
       self.Senha = Senha
       self.Saldo = Saldo
    
    #Métodos da class
    
    def depositar(self, valor):

        self.Saldo += valor
        return self.Saldo
    
    def retirar(self, valor):

        self.Saldo -= valor
        return self.Saldo
    
    def exibirSaldo(self):
        print(self.Saldo)