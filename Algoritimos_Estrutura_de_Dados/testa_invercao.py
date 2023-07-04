import random

from inverteLista import inverte

def confere_inversao(n, m):
   
    """Checa o resultado da função `inverte` em n listas de tamanho m geradas aleatoriamente."""
    for _ in range(n):
        
        # Cria uma lista com números aleatórios no intervalo [0, m].
        nums1 = [random.randint(0, m) for _ in range(m)]

        # Cria uma lista com os mesmos elementos de nums1.
        nums2 = list(nums1)

        # Inverte a lista nums1 usando a biblioteca padrão de Python.
        nums1.reverse()

        # Invoca nosso algoritmo para inverter nums2 e confere o resultado.
        assert (inverte(nums2) == (nums1))

    print("Sucesso!")

# Checa o resultado do nosso algoritmo em 500 listas geradas aleatoriamente.

confere_inversao(10, 10)