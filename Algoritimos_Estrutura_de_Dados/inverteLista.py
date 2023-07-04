from listaDuplamenteEncadeada import FilaEncadeada
def inverte(nus):
    
    #Inverte o conteúdo de uma lista
    if not nus:
        return "Não ha elementos na lista."
    
    inicio = 0
    fim = len(nus) - 1

    while inicio < fim:
        nus[inicio], nus[fim] = nus[fim], nus[inicio]
        inicio += 1
        fim -= 1
    
    return nus

print(mostrar(self))