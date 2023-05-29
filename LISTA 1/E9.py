def binSearch(lista, valor):
    ini = 0
    fim = len(lista) - 1

    while ini <= fim:
        mid = (ini + fim) // 2

        if lista[mid] == valor:
            return True
        elif lista[mid] < valor:
            ini = mid + 1
        else:
            fim = mid - 1

    return False


def compare(lista1, lista2):
    for element in lista1:
        if binSearch(lista2, element):
            return True

    return False

lista1 = [1, 3, 6, 7, 8, 10]
lista2 = [2, 5, 8, 13, 15, 21]

print(compare(lista1, lista2))