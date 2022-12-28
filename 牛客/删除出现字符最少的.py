line = "assssa"
d = {}
for i in line:
    if d.get(i):
        d[i] += 1
    else:
        d[i] = 1

min1 = min(d.values())
print(min1)
res = []
for k, v in d.items():
    if min1 == v:
        res.append(k)
res_s = line
for i in res:
    res_s = res_s.replace(i, "")
print(res_s)