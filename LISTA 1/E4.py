lista = [5, 2, 4, 1, 3, 2, 4]


def processa(lista):
    n = len(lista)
    mudou = True
    while mudou == True:
        mudou = False
        for i in range(1, n):
            if lista[i - 1] < lista[i]:
                val = lista[i]
                lista[i] = lista[i - 1]
                lista[i - 1] = val
                mudou = True

    return lista


print(processa(lista))

# A função implementa o algoritmo bubble sort para ordenar os elementos da lista em ordem decrescente. Mais precisamente,
# ela compara cada elemento adjacente e os troca caso estejam em ordem errada até a lista se ordenar.
