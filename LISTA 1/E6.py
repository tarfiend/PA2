matrix = [["nome1", 27],
          ["nome2", 43],
          ["nome3", 18],
          ["nome4", 19]]


def age_bubble(matrix):

    n = len(matrix)

    for i in range(n - 1): # itera n -1 vezes pois o maior número sempre ficará em último, tornando desnecessário chechar o último elemento.
        for j in range(0, n - i - 1): # o mesmo vale para n - i - 1.
            if matrix[j][1] > matrix[j + 1][1]: # bubble sort
                matrix[j], matrix[j + 1] = matrix[j + 1], matrix[j]

    return matrix


print(age_bubble(matrix))