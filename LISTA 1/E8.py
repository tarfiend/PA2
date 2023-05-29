lista = [3, 1, 2, 4]


def sortList(lista):
    n = len(lista)

    is_increasing = True

    for i in range(1, n):
        if lista[i] < lista[i - 1]:
            is_increasing = False
            break

    is_decreasing = True

    for i in range(1, n):
        if lista[i] > lista[i - 1]:
            is_decreasing = False
            break

    if is_increasing or is_decreasing:
        return lista
    lista.sort()
    return lista


print(sortList(lista))
