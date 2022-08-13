"""
640. 求解方程
求解一个给定的方程，将x以字符串 "x=#value" 的形式返回。该方程仅包含 '+' ， '-' 操作，变量 x 和其对应系数。

如果方程没有解，请返回 "No solution" 。如果方程有无限解，则返回 “Infinite solutions” 。

题目保证，如果方程中只有一个解，则 'x' 的值是一个整数。

"""

def func(equation):
    factor = val = 0
    i, n, sign = 0, len(equation), 1  # 等式左边默认系数为正
    while i < n:
        if equation[i] == '=':
            sign = -1
            i += 1
            continue

        s = sign
        if equation[i] == '+':  # 去掉前面的符号
            i += 1
        elif equation[i] == '-':
            s = -s
            i += 1

        num, valid = 0, False
        while i < n and equation[i].isdigit():
            valid = True
            num = num * 10 + int(equation[i])
            i += 1

        if i < n and equation[i] == 'x':  # 变量
            factor += s * num if valid else s
            i += 1
        else:  # 数值
            val += s * num

    if factor == 0:
        return "No solution" if val else "Infinite solutions"
    return f"x={-val // factor}"


def f(e):
    count = 0
    val = 0
    sign = 1
    i = 0
    while i < len(e):
        if e[i] == '=':
            sign = -1
            i += 1
            continue
        flag = sign # 最终符号
        if e[i] == '+':
            i = i+1
        if e[i] == '-':
            flag = -flag
            i = i+1

        num = 0
        f = False  # 标志x前面是否有系数
        while i < len(e) and e[i].isdigit():
            f = True
            num = num*10 + int(e[i])
            i = i + 1

        if i<len(e) and e[i] == 'x':
            count += flag * num if f else flag
            i += 1
        else:
            val += num*flag

    print(val, count)
    if count == 0:
        return "No solution" if val else "Infinite solutions"
    return f"x={-val // count}"

if __name__ == '__main__':
    equation = "x+5-3+x=6+x-2"
    r = f(equation)
    print(r)
