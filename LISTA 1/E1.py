lista = [5, 2, 4, 1, 3, 2, 4]

def sum_to_i(lista):
    n = len(lista)
    for i in range(0, n-1):
        lista[i+1] = lista[i] + lista[i+1]

    return lista

print(sum_to_i(lista))