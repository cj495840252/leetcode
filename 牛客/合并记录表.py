import sys
from pprint import pprint

for line in sys.stdin:
    s = ""
    for i in range(int(line)):
        s += str(input()) + "\n"
    items = s.split("\n")
    d = {}
    for kv in items:
        if len(kv) < 3:
            continue
        kv_ = kv.replace("\n","").split(" ")
        i = int(kv_[0])
        j = int(kv_[1])
        if d.get(i):
            d[i] += j
        else:
            d[i] = j

    rr = sorted(d.items(), key=lambda x: x[0])
    # pprint(rr)
    res = ""
    for k, v in rr:
        res += str(k) + " " + str(v) + "\n"
    print(res)

