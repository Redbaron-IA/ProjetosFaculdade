class No:
    def __init__(self, dados):
        self.dados = dados
        self.proximo = None
        self.aterior = None

class Pilha:
    def __init__(self):
        self._inicio = None
        self._fim = None
        self._contador = 0

    @property
    def inicio(self):
        return self._inicio 
    
    @property
    def fim(self):
        return self._fim
    
    @property
    def comtador(self):
        return self._contador
    
    def incerir(self, dados):

        if self.inicio is None:
            incere = No(dados)
            self._inicio = incere
            self._fim = incere
            self._contador += 1
        
        else:
            incere = No(dados)
            incere.proximo = self._inicio
            self._inicio.aterior = incere
            self._inicio = incere
            self._contador += 1

    def mostrar(self):

        """ Mostra todos os dados da fila. """
        print("Fila Simplesmente Encadeada:")

        # O no atual eh o primeiro no da fila
        no_atual = self._inicio
        for i in range(0, self._contador):
            print(i)

        no = ""
        # Para cada no valido da fila
        while no_atual is not None:
            no += "---> | " + str(no_atual.dados) + " | "
            no_atual = no_atual.proximo

        print("=" * 95)
        print(no)
        print("=" * 95)

p = Pilha()

p.incerir(1)
p.incerir(1)
p.incerir(1)
p.mostrar()