class NodoFila:

   def __init__(self, dado):
      
      self.dado = dado
      self.anterior = None
      self.proximo = None

class FilaEncadeada:  
   
   def __init__(self):      
      self._inicio = None
      self._fim = None
      self._contador = 0
   
   @property 
   def cabeca(self):
      return self._inicio
   
   @property 
   def calda(self):
      return self._fim
   
   @property
   def contador(self):
      return self._contador
   
   def vazia(self):

      if self._inicio is None:
         return True
      return False

   def add_inicio(self, item):

      if self.vazia():
         celula = NodoFila(item)
         self._inicio = celula
         self._fim = celula
         self._contador += 1
      else:
         celula = NodoFila(item)
         celula.proximo = self._inicio
         self._inicio.anterior = celula
         self._inicio = celula
         self._contador += 1
   
   def add_fim(self, item):

      novo_nodo = NodoFila(item)
      if self.vazia():
         self._inicio = self._fim = novo_nodo
      else:
         self._fim.proximo = novo_nodo
         novo_nodo.anterior = self._fim
         novo_nodo.proximo = None
         self._fim = novo_nodo
      self._contador +=1
   
   def remover_inicio(self):

      if self.vazia():
         raise TypeError ("A lista está vazia!")
      removido = self._inicio
      self._inicio = self._inicio.proximo
      removido.proximo = None
      self._contador -= 1
      return removido
   
   def remover_fim(self):

      if self.vazia():
         raise TypeError ("A lista está vazia!")
      elif self._contador == 1:
         removido = self._fim
         self._inicio = None
         self._fim = None
         self._contador -= 1
         return removido
      else:
        removido = self._fim
        self._fim = removido.anterior
        self._fim.proximo = None
        removido.anterior = None        
        self._contador -= 1
        return removido.dado
   
   """permite icerir elemento na posiçao referenciada"""
   def incerirNaPosicao(self, posicao, item):

      if posicao == 0:
         return self.add_inicio(item)      
      if posicao == self._contador:
         return self.add_fim(item)
      esquerda = self._celula(posicao - 1)
      direita = esquerda.proximo
      celula = NodoFila(item)
      celula.proximo = direita
      celula.anterior = esquerda
      esquerda.proximo = celula
      direita.anterior = celula
      self._contador +=1

   """Permite remover elementos em qualque posição da fila"""
   def removerNaposicao(self, posicao):

      if posicao == 0:
         return self.remover_inicio()
      if posicao == self._contador -1:
         return self.remover_fim()
      removido = self._celula(posicao)
      esquerda = removido.anterior
      direita = removido.proximo
      esquerda.proximo = direita
      direita.anterior = esquerda
      self._contador -= 1
      return removido.dado
   
   def busca(self, item):

      celula = self._inicio
      while celula and celula.dado != item:
            celula = celula.proximo
      if celula:
         print("\n\n")
         print("-" * 117)
         print("Elemento {} se enconta na lista".format(celula.dado))
         print("=" * 117)
      else:
         print("Elemento não se encontra na lista")
      return celula
   
      """Recebe uma posição da fila e retorna verdadeiro"""
   def _validar_posicao(self, posicao):

      if 0 <= posicao < self.contador:
         return True
      else:
         print("Posição inválida: {}", posicao)
         exit()
   
   def _celula(self, posicao):

      self._validar_posicao(posicao)
      metade = self._contador // 2
      if posicao < metade:
         atual = self._inicio
         for i in range(0, posicao):
            atual = atual.proximo
         return atual
      atual = self._fim
      for i in range(posicao + 1, self._contador):
         atual = atual.anterior
      return atual

   def mostrar(self):
        
        """ Mostra todos os dados da lista. """
        print("Fila Duplamente Encadeada:")
        no_atual = self._inicio
        for i in range(0, self._contador):
           print(i, end="  ")
        print("\n")
        no = ""
        
        while no_atual is not None:
            if no_atual.anterior is None:
                no += "None "
            no += "<---> | " + str(no_atual.dado) + " | "
            if no_atual.proximo is None:
                no += "<---> None"
            no_atual = no_atual.proximo
        print("=" * 117)
        print(no)
        print("=" * 117)

l = FilaEncadeada()

l.add_inicio(422)
l.add_inicio(25)
l.add_inicio(38)
l.add_inicio(49)
l.add_inicio("Maria")
l.add_inicio("Fernando")
l.add_fim("Funciona")
l.add_inicio("Funciona")
l.incerirNaPosicao(2, "Severino")
#l.removerNaposicao(0)
#l.remover_inicio()
#l.remover_fim()
l.busca(-2)
l.mostrar()
