
import re
import math
from FuzzySimilarMatrix import caculate
from FuzzyEquivalenceMatrix import caculate2

orig = []
after = []
terminal = []

#读取数据
f = open("data.txt",encoding="utf-8")
lines = f.readlines()

#格式化预处理
for line in lines:
    orig.append(re.split("\s+",line))
#print(orig)

#欧几里得距离法计算模糊相似矩阵
for i in range(24):
    j_mat = []
    for j in range(24):
        rij = round(1- 0.5*caculate(i,j,orig),3)
        j_mat.append(rij)
    after.append(j_mat)
#for i in range(24):
#    print(after[i])
rk = caculate2(after)

#传递闭包法计算模糊等价矩阵
while True:
    if rk == caculate2(rk):
        terminal = rk
        break
    rk = caculate2(rk)

#打印预览
for i in range(24):
    print(terminal[i])

#数据输出
f2 = open("out.txt","w",encoding="utf-8")
for line in terminal:
    f2.write(str(line).strip("[]")+"\n")
f2.close()

f3 = open("out2.txt","w",encoding="utf-8")
for line in after:
    f3.write(str(line).strip("[]")+"\n")
f3.close()
