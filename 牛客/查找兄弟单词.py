
import sys


for line in sys.stdin:
    a = line.replace("\n","").split(" ")
    if len(a) < 3:
        exit(0)
    x = a[-2]
    nums = a[1:-2]
    n3 = 0
    data4 = []
    for word in nums:
        if word == x:
            continue
        elif sorted(word) == sorted(x):
            n3 = n3 + 1
            data4.append(word)
    print(n3)
    data5 = sorted(data4)
    print(data5[int(a[-1]) - 1])