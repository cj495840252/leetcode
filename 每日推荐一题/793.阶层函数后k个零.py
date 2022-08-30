"""
todo 793. 阶乘函数后 K 个零
 f(x) 是 x! 末尾是 0 的数量。回想一下 x! = 1 * 2 * 3 * ... * x，且 0! = 1 。

例如， f(3) = 0 ，因为 3! = 6 的末尾没有 0 ；而 f(11) = 2 ，因为 11!= 39916800 末端有 2 个 0 。
给定 k，找出返回能满足 f(x) = k 的非负整数 x 的数量。
"""
from bisect import bisect_left

"""
x！为阶层，k为0的个数，那么0的个数等于0-x之间的值//5的总和
可知：k从0开始每增加5，则末尾多一个零，所以答案不是5，就是0
0-4 :0
4-9 :1
10-14 :2
15:19 :3
20-24 :4
// 这里缺少了5,结尾5个0的阶层不存在
25-29 :5+1
30-34 :6+1
......
120：124:24+4
//缺少了29-30
125:129:25+5+1

"""
class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def f(x):
            c = 0
            while x:
                x = x // 5
                c += x
            return c

        def count(k):
            # todo 二分查找
            i,j = 0,5*k
            print(i, j)
            while i <= j:
                t = (i+j)//2
                print("i =", i, " j=",j, " f(t)=", f(t))
                if k > f(t):
                    i = t+1
                elif k < f(t):
                    j = t-1
                else:
                    return 5
            return 0
        return count(k)

    def preimageSizeFZF1(self, k: int) -> int:
        """官方答案"""
        def zeta(n: int) -> int:
            res = 0
            while n:
                n //= 5
                res += n
            return res

        def nx(k: int) -> int:
            return bisect_left(range(5 * k), k, key=zeta)

        return nx(k + 1) - nx(k)




if __name__ == '__main__':
    s = Solution().preimageSizeFZF(0)
    print(s)
