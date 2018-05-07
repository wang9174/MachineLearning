#模糊等价矩阵计算

def caculate2(mat):
    return_temp = []
    for i in range(24):
        j_mat = []
        for j in range(24):
            k = 0
            r_ij = 0
            min_temp = []
            while True:
                r_ik = round(float(mat[i][k]),3)
                r_kj = round(float(mat[k][j]),3)
                if r_ik>=r_kj:
                   min_temp.append(r_kj)
                else:
                   min_temp.append(r_ik)
                k += 1
                if k >= 24:
                    break
            for temp in min_temp:
                if temp > r_ij:
                    r_ij = temp
            j_mat.append(r_ij)
        return_temp.append(j_mat)
    return return_temp
