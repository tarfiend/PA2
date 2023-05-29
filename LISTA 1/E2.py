lista = [23, 12, 4, 55, 43, 56, 17, 28, 23, 43, 10]

def bigger_smaller_than(lista, c1, c2):
    elements = 0
    for i in range(0, len(lista)):
        if lista[i] >= c1 and c2 >= lista[i]:
            elements += 1

    return elements

print(bigger_smaller_than(lista, 20, 40))