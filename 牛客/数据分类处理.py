import sys
from typing import List

I0 = "6396 4598 8539 6047 2019 11269 7402".replace("\n","").split(" ")
R0 = list(set("16 4 26".replace("\n","").split(" ")))
# I0 = input().replace("\n","").split(" ")[1:]
# R0 = list(set(input().replace("\n","").split(" ")[1:]))
R0.sort(key= lambda x:int(x))

# d = {}
# for i in range(10):
#     d[str(i)] = []
# for index,num in enumerate(I0):
#     for ch in num:
#         d[ch].append(index)
#
# print(d)
# res = []
# for s in R0:
#     ls = list(s)
#     temp = [0 for i in range(len(I0))]
#     for ch in ls:
#         t = d.get(ch)
#         if len(t) == 0:
#             break
#         for i in set(t):
#             temp[i] += 1
#     each = []
#     for i,var in enumerate(temp):
#         if var == len(s):
#             each.append(i)
#
#     if each == []:
#         continue
#     res.append(s)
#     res.append(str(len(each)))
#     for i in list(set(each)):
#         res.append(str(i))
#         res.append(I0[i])
#
# print(str(len(res))+" " + " ".join(res))

r_dict = {}

for i in R0:
    r_dict[i] = []
for i,v in enumerate(I0):
    for r in R0:
        if r in v:
            r_dict[r].append(i)

res = []
for t in R0:
    each = r_dict.get(t)
    if each==[]:
        continue
    res.append(t)
    res.append(str(len(each)))
    for k,v in enumerate(each):
        res.append(str(v))
        res.append(I0[v])

print(str(len(res))+" " + " ".join(res))
