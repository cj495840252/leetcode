""" todo 面试题 17.09. 第 k 个数
有些数的素因子只有 3，5，7，请设计一个算法找出第 k 个数。
注意，不是必须有这些素因子，而是必须不包含其他的素因子。
例如，前几个数按顺序应该是 1，3，5，7，9，15，21。
"""

def func(k):
    p7 = 0
    p5 = 0
    p3 = 0
    arr = [1]*k
    for i in range(1, k):
        num3 = [p3]*3
        num5 = arr[p5]*5
        num7 = arr[p7]*7
        arr[i] = min(num7, num5, num3)
        if arr[i] == num3:
            p3 += 1
        if arr[i] == num5:
            p5 += 1
        if arr[i] == num7:
            p7 += 1
    return arr[k-1]

if __name__ == '__main__':
    r = func(7)
    print(r)