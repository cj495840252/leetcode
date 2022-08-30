"""
todo 172. 阶乘后的零
给定一个整数 n ，返回 n! 结果中尾随零的数量。

提示 n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1
"""

"""
知识补充：fx = (x-a)*(x-b)*(x-c)
==> x-a, x-b, x-c 为fx的因子

n! = 10*k * 另一个因子；
阶层0的个数，即n!中因子10的数量k；
又 10 = 2*5
所以因子10的个数==因子5的个数
"""
class Solution:
    def trailingZeroes(self, x: int) -> int:
        c = 0
        while x:
            x = x // 5
            c += x
        return c

if __name__ == '__main__':
    s = Solution().trailingZeroes(130)
    print(s)