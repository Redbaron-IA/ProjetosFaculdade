from ContaClass import Conta

#Classe herda atributos e métodos da classe pai

class ContaPoupanca(Conta):

    def __init__(self, Agencia, Codigo, DataDeCriacao, Titular, Senha, Saldo, Aniversario):

        #chamada do método construtor da classe-pai
        super().__init__(Agencia, Codigo, DataDeCriacao, Titular, Senha, Saldo)
        
        #variável pertencente apenas a classe Poupança
        self.Aniversario = Aniversario
    
    #Classe hedou método da classe Pai
    def retirar(self, valor):
        if self.Saldo >= valor:
            return super().retirar(valor)
        
        else:
            print("Retirada não permitida")
            return False