from filaEncadeada import filaEncadeada


class Pilha:

    def __init__(self):
        self.pilha = filaEncadeada()

    def empilhar(self, item):
        self.pilha.incerir(item)

    def desempilhar(self):
        return self.pilha.remover()

    @property
    def topo(self):
        return self.pilha.item(0)

    @property
    def vazia(self):
        return self.pilha._contador == 0

