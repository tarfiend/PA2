m1 = [[1, 2, 0],
      [3, 1, 2],
      [2, 2, 1]]
v1 = [[1],
      [2],
      [3]]

def multiplier(m1, v1):
    lin_m1 = len(m1)
    col_m1 = len(m1[0])
    col_v1 = len(v1[0])
    res = []

    for i in range(lin_m1):
        res_linha = []
        for j in range(col_v1):
            soma = 0
            for k in range(col_m1):
                soma += m1[i][k]*v1[k][j]
            res_linha.append(soma)
        res.append(res_linha)

    return res

print(multiplier(m1, v1))
