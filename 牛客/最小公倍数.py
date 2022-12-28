import sys

for line in sys.stdin:
    a = line.split()
    m = int(a[0])
    n = int(a[1])
    for i in range(m):
        t = m*i
        t % m == 0
        break
    print(t)