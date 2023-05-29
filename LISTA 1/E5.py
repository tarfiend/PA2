matrix = [[1, 2],
          [3, 4]]

def column_splitter(matrix):
    column1 = []
    column2 = []

    for row in matrix:
        column1.append(row[0])
        column2.append(row[1])

    return column1, column2

print(column_splitter(matrix))