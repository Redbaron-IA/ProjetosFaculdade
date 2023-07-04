"""Implementação de uma arvore binária"""

"""Uma arvore binária serve para armazenamento de dados na menória do
computador e su posterior recuperação.
"""

class Nodo:
    """A classe Nodo composta por dados e dois apontadores"""

    def __init__(self, dados):

        self.dados = dados
        self.direita = self.esquerda = None

class ArvoreBinaria:
    """A classe de uma arvore binária basica é composta pelos seguintes 
    métodos: inserir, remover, buscar e imprimir"""

    def __init__(self):

        self.raiz = None
    
    def inserir(self,dados):

        novo_nodo = Nodo(dados)
        if self.raiz is None:
            self.raiz = novo_nodo
        else:
            nodo = self.raiz
            while nodo is not None:
                if dados <= nodo.dados:
                    nodo.esquerda = novo_nodo
                    break
                nodo = nodo.esquerda
    
    def busca_recursiva(self, nodo, dados):
        """A maioria dos problemas em uma arvore binária podem ser resolvidos
        por recursividade"""

        if nodo is None:
            return        
        if nodo.dados == dados:
            return nodo
        if nodo > nodo.dados:
            self.busca_recursiva(nodo.direita, dados)
        else:
            self.busca_recursiva(nodo.esquerda, dados)
    
    def busca_linear(self, dados):

        nodo = self.raiz
        while nodo is not None:
            if nodo.dados == dados:
                return nodo
            elif dados > nodo.dados:
                nodo = nodo.direita
            else:
                nodo.esquerda
        return None
    
    def __get_parentes_nodo(self, dados):
        nodo = self.raiz
        parente = self.raiz
        while nodo is not None:
            if nodo.dados == dados:
                return parente
            parente = nodo
            if nodo.dados < dados:
                nodo = nodo.direita
            else:
                nodo = nodo.esquerda
        return parente

    """@staticmethod: permite chamar o metodo diretamente na classe, sem 
    precisar criar um objeto da classe antes,  pode ser útil em situações
    em que você precisa executar alguma tarefa que não depende de nenhuma 
    variável de instância da classe. """
    @staticmethod
   
    def __nivel_esquerdo(nodo):
        nodo = nodo.esqueda
        while nodo.direita is not None:
            nodo = nodo.direita
        return nodo
    
    def remover(self, dados):
        """Mais recursividade"""

        nodo = self.busca_linear(dados)

        if nodo is None:
            return False
        
        parete = self.__get_parentes_nodo(dados)

        if nodo.esquerda is None or nodo.direita is None:
            if nodo.esquerda is None:
                mov = nodo.direita
            else:
                mov = nodo.esquerda
            if parete is None:
                nodo = mov
            elif dados > parete.dados:
                parete.direita = mov
            else:
                parete.esquerda = mov
        else:
            mov = self.__nivel_esquerdo(nodo)
            nodo.dados = mov.dados
            if mov.esquerda is not None:
                nodo.esquerda = mov.esquerda
            else:
                nodo.esquerda = None
        return True
    
    def altura_arvore(self, raiz):
        if raiz is None:
            return -1
        
        altura_esquerda = self.altura_arvore(raiz.esquerda)
        altura_direita  = self.altura_arvore(raiz.direita)

        if altura_direita > altura_esquerda:
            return altura_direita + 1
        return altura_esquerda +1
    
    def niveis_ordem(self):
        altura = self.altura_arvore(self.raiz)
        for i in range(1, altura + 2):
            self.__print_nivel(self.raiz, i)
    
    def __print_nivel(self, nodo, nivel):
        if nodo is None:
            return
        if nivel == 1:
            print("%d" % nodo.dados, end=" ")
        elif nivel > 1:
            self.__print_nivel(nodo.esquerda, nivel -1)
            self.__print_nivel(nodo.direita, nivel -1)
    
    """Caminhamentos"""
    """Neste primeiro caminhamento vizitamos o filho da esquerda,
    o nó corren 'RAIZ' e o filho da direita"""

    def em_ordem(self, nodo):
        if nodo is None:
            return
        self.em_ordem(nodo.esquerda)
        print("%d" % nodo.dados, end=" ")
        self.em_ordem(nodo.direita)
    
    """Visitamos o nó corrente 'RAIZ' o filho da esquerda e o 
    filho da direita"""

    def pre_ordem(self, nodo):
        if nodo is None:
            return
        print("%d" % nodo.dados, end=" ")
        self.pre_ordem(nodo.esquerda)
        self.pre_ordem(nodo.esquerda)

    """Visitamos o filho da esquerda, o filho da direita e o nó corrente 'RAIZ' """
    def pos_ordem(self, nodo):
        if nodo is None:
            return
        self.pos_ordem(nodo.esquerda)
        self.pos_ordem(nodo.direita)
        print("%d" % nodo.dados, end=" ")