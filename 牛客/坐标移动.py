import sys

for line in sys.stdin:
    l = line.split(";")
    points = []

    charset = [str(chr(x)) for x in range(65, 91)]

    for point in l:
        if len(point) < 2:
            continue
        c: str = point[0]
        char = c.upper()
        if char in charset:
            try:
                n = int(point[1:])
                points.append((char, n))
            except:
                pass

    position = [0, 0]
    for action, i in points:
        if action == "A":
            position[0] -= i
        if action == "D":
            position[0] += i
        if action == "W":
            position[1] += i
        if action == "S":
            position[1] -= i
    res = "" + str(position[0]) + "," + str(position[1])

    print(res)