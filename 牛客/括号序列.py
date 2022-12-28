def maxDepth(s: str) -> int:
    stack = []
    count = 0
    m = 0
    for i in s:
        if m < count:
            m = count
        if i == "(":
            count += 1
            stack.append(i)
        if i == ")":
            count -= 1
            stack.pop(-1)
    return m


if __name__ == '__main__':
    s = "(1+(2*3)+((8)/4))+1"
    res = maxDepth(s)
    print(res)
