def column_sort(matrix, ind):

    num_lines = len(matrix)

    for i in range(num_lines - 1):
        for j in range(num_lines - i - 1):
            if matrix[j][ind] > matrix[j + 1][ind]:
                matrix[j], matrix[j+1] = matrix[j+1], matrix[j]

    return matrix

matrix = [[9, 4, 3],
          [1, 7, 4],
          [2, 6, 2]]

print(column_sort(matrix, 2))