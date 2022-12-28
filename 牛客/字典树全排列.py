from typing import List

a = "aba"
l = list(a)
temp = []
res= []

def func(l,temp:List):
    if len(temp) ==len(l):
        res.append("".join(temp))
        return
    for i in l:
        if i in temp:
            continue
        else:
            temp.append(i)
            func(l,temp)
            temp.pop(-1)


func(l,temp)
print(set(res))