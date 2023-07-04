from ContaClass import Conta

#Classe herda atributos e métodos da classe pai

class ContaCorent(Conta):

    def __init__(self, Agencia, Codigo, DataDeCriacao, Titular, Senha, Saldo, Limite):

        super().__init__(Agencia, Codigo, DataDeCriacao, Titular, Senha, Saldo) #herda os atributos da classe conta

        self.Limite = Limite #Inicializa uma nova variavel conforme a nescessidade da class.

    def retirar(self, valor):

        self.CPMF = 0.05

        Quantia = self.Saldo + self.Limite

        if Quantia >= valor:
            return super().retirar(valor * self.CPMF) #herda métodos da classe Pai
        
        else:
            print("Retirada não Permitida")
            return False