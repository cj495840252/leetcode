import sys

for line in sys.stdin:
    a, b, c, d = 0, 0, 0, 0
    s = line
    for i in s:
        if ord("a") <= ord(i) <= ord("z"):
            a = 1
        elif ord("A") <= ord(i) <= ord("Z"):
            b = 1
        elif ord("0") <= ord(i) <= ord("9"):
            c = 1
        elif i != "\t" and i != " " and i != "\n":
            d = 1

    e = True
    for i in range(len(s) - 3):
        strs = s.split(s[i:i + 3])
        if len(strs) >= 3:
            e = False

    if e and a + b + c + d >= 3 and len(s) > 7:
        print("OK")
    else:
        print("NG")

"".r