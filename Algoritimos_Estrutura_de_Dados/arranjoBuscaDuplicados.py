def encontra_elementos_duplicados(lista, m):
    
    #Retorna zero se alista estiver vazia.
    if not lista:
        return "A lista está vazia."
    
    duplicatas = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                duplicatas.append(lista[j])
    
    # A saida é a lista de elementos repetidos.
    return duplicatas

elementos_duplicados = encontra_elementos_duplicados([], 100)

print ("Elementos duplicados na lista: ", elementos_duplicados)