import sys

for line in sys.stdin:
    # num = "167969729"
    if "." not in line:
        number = int(line, 10)
        n1 = number >> 24
        n2 = (number - (n1 << 24)) >> 16
        n3 = (number - (n1 << 24) - (n2 << 16)) >> 8
        n4 = (number - (n1 << 24) - (n2 << 16) - (n3 << 8)) >> 0
        s = str(n1) + "." + str(n2) + "." + str(n3) + "." + str(n4)
        print(s)
    else:
        l = line.split(".")
        res = 0
        j = 3
        for i in l:
            res = res + (int(i) << 8 * j)
            j -= 1
        s = str(res)
        print(res)
