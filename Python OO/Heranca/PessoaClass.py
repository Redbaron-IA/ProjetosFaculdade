#Classe pessoa super classe ou classe pai

class Pessoa:

    #Método construtor, inializa os atributos da Class
    def __init__(self, Codigo, Nome, Altura, Idade, Nascimento, Escolaridade, Salario):
        
        self.Codigo = Codigo
        self.Nome = Nome
        self.Altura = Altura
        self.Idade = Idade
        self.Nascimento = Nascimento
        self.Escolaridade = Escolaridade
        self.Salario = Salario

    
    #Método destrutor quando chamado deleta objetos da classe que foram inicializado   
    def __del__(self):
        print("Objeto {} esclutido com sucesso".format(self))