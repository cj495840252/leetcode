"""
7. 整数反转
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

假设环境不允许存储 64 位整数（有符号或无符号）。
"""
class Solution:
    def reverse(self, x: int) -> int:

        res = 0
        sign = 1

        if x < 0:
            sign = -1
        x = abs(x)
        while x:
            res = res*10 + x % 10
            x = x // 10
        res = sign * res
        if res > 2**31 -1 or res < -2**31:
            return 0
        return res

if __name__ == '__main__':
    s = Solution().reverse(1563847412)
    print(s)
    print("2的32",2**31)