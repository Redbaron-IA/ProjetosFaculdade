def encontra_elementos_duplicados(lista, m):

    #Informa se a lista está vazia

    if not lista:
        return "A lista estã vazia."
    

    #Procura por elementos duplicados na lista
    tabela_ocorrencia = [0] * m
    duplicatas = []

    for elementos in lista:
        tabela_ocorrencia[elementos] += 1
        if tabela_ocorrencia[elementos] > 1:
            duplicatas.append(elementos)
    
    return duplicatas

elementos_duplicados = encontra_elementos_duplicados([1, 1, 20, 3, 3, 80, 7, 2, 25, 99, 75, 80], 100)

print("Estes elementos estão duplicados na lista: ", elementos_duplicados)