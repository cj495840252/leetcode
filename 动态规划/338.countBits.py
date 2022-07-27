"""
338. 比特位计数
给你一个整数 n ，对于 0 <= i <= n 中的每个 i ，
计算其二进制表示中 1 的个数 ，返回一个长度为 n + 1 的数组 ans 作为答案。

"""


class Solution:
    def countBits(self, n: int) -> list[int]:
        """
        自己想的：时间复杂度O（n²）
        """
        i = 0
        ans = [0 for i in range(0, n+1)]
        while i <= n:
            t = i
            while t:
                if t % 2 == 1:
                    ans[i] += 1
                t = t >> 1
            i += 1
        return ans

    def countBits1(self, n: int) -> list[int]:
        """
        官解1：Brian Kernighan}Brian Kernighan 算法
        时间复杂度 O（nlogn）
        """
        def countOnes(x: int) -> int:
            ones = 0
            while x > 0:
                x &= (x - 1)
                ones += 1
            return ones

        bits = [countOnes(i) for i in range(n + 1)]
        return bits

    def countBits2(self, n: int) -> list[int]:
        """
        官解2：动态规划-最高有效位，对于i的二进制，每次 i & (i-1)会消除一位1
        时间复杂度 O（n） 每一个数只需要O（1）的时间
        """
        res = [0]  # res的下表和每个值是对应的
        high_bit = 0  # 表示二进制比i小的且最高位为1，其余为为0的值
        for i in range(1, n+1):
            if i & (i-1) == 0:
                high_bit = i
            # i的二进制减去最高的的1的二进制1的位数已知，i比它多1
            res.append(res[i-high_bit]+1)
        return res

    def countBits3(self, n: int) -> list[int]:
        """
        官解3：动态规划-最低有效位，移除最低位，相当于除以2，那么i和 i//2之间相差1或0位
        奇数 res[i] = res[i//2] + 1
        偶数 res[i] = res[i//2]
        时间复杂度 O（n） 每一个数只需要O（1）的时间
        """
        res = [0]
        for i in range(1, n+1):
            if i % 2 == 1:
                res.append(res[i//2]+1)
            else:
                res.append(res[i//2])
        return res

    def countBits4(self, n: int) -> list[int]:
        """
        官解3：动态规划-最低设置位，由于对于i的二进制，每次 i & (i-1)会消除最低位的1，那么i的1的位数 = i & (i-1)的位数 + 1
        ==>函数   bits[i] = bits[i & (i-1)] + 1
        时间复杂度 O（n） 每一个数只需要O（1）的时间
        """
        bits = [0]
        for i in range(1, n + 1):
            bits.append(bits[i & (i - 1)] + 1)
        return bits


if __name__ == '__main__':
    s = Solution()
    res = s.countBits3(5)
    print(res)
