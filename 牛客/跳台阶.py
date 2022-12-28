class Solution:
    def numWays(self, n: int) -> int:
        if n == 0 :
            return 1
        p = 0
        q = 1
        for i in range(n) :
            t = p+q
            p = q
            q = t
        return q % 1000000007

s = Solution()
res = s.numWays(44)
print(res)

## 这个是第二题的python写法
