#模糊相似矩阵计算

import math

def caculate(i,j,mat):
    k = 0
    temp = 0.0
    while True:
        temp = temp + math.pow(float(mat[i][k]) - float(mat[j][k]),2)
        k = k + 1
        if k >= 6:
            return math.sqrt(temp)
