class NodoFila:

   def __init__(self, dado):
      """Nó da fila"""
      self.dado = dado
      self.proximo = None
      self.anterior = None

class filaEncadeada:  
   """Fila"""
   def __init__(self):      
      self._inicio = None
      self._fim = None
      self._contador = 0

   """@property, permite referenciar as variáveis sem ter que fazer uso dos getts"""
   @property 
   def inicio(self):
      return self._inicio
   
   @property
   def fim(self):
      return self._fim
   
   @property
   def contador(self):
      return self._contador
   
   def vazia(self):
      if self._inicio is None:
         return True
      return False
   
   """Método incerir no início"""
   def incerir(self, item):
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
   
   """Método remove no inicio"""
   def remover(self):
      if self.vazia():
         raise TypeError("A fila está vazia!")
      elif self._contador == 1:
         removido = self._fim
         self._inicio = None
         self.fim = None
         return removido
      else: 
         removido = self._fim
         self._fim = removido.anterior
         self._fim.proximo = None
         removido.anterior = None
         self._contador -= 1
         return removido.dado
      
      
   
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
            no += "---> | " + str(no_atual.dado) + " | "
            no_atual = no_atual.proximo

        print("=" * 95)
        print(no)
        print("=" * 95)


f = filaEncadeada()


f.incerir(1)
f.incerir(2)
f.incerir(3)
f.incerir(4)
f.incerir(5)
f.incerir("Fernando")
f.incerir("maria")
f.remover()
f.mostrar()