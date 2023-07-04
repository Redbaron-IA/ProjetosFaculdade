def remover_fim(self):
    if self.vazia():
        raise TypeError("Lista vazia!")
    elif self.tamanho == 1:
         self.inicio = None
         self.fim == None
    else:
        self.fim.anterior == None
        self.fim.proximo = None
    self.tamano -=1

 def _remover_ultimo(self):
        if self.quantidade == 1:
            removido = self.inicio
            self._inicio = None
            self._fim = None
            self._quantidade -= 1
            return removido.conteudo
        
p.add_Inicio(12)
p.add_Inicio(25)
p.add_Inicio(38)
p.add_Inicio(49)
p.add_Inicio("Maria")
p.add_Inicio("Fernando")
p.add_fim("Marcolino")
p.remover_fim()
p.mostrar()