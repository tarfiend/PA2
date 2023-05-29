def mergeSort(lista):
    if len(lista) > 1:
        mid = len(lista) // 2
        lhs = lista[:mid]
        rhs = lista[mid:]

        mergeSort(lhs)
        mergeSort(rhs)

        i = 0
        j = 0
        k = 0

        while i < len(lhs) and j < len(rhs):
            if lhs[i] < rhs[j]:
                lista[k] = lhs[i]
                i += 1
            else:
                lista[k] = rhs[j]
                j += 1
            k += 1

        while i < len(lhs):
            lista[k] = lhs[i]
            i += 1
            k += 1

        while j < len(rhs):
            lista[k] = rhs[j]
            j += 1
            k += 1
    return lista

def compareLists(lista1, lista2):
    if mergeSort(lista1) == mergeSort(lista2):
        return True
    return False

lista1 = [2, 6, 4, 8, 10, 3]
lista2 = [10, 3, 2, 4, 6, 8]

print(compareLists(lista1, lista2))