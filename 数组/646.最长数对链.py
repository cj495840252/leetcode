"""
todo 646. 最长数对链
给出 n 个数对。 在每一个数对中，第一个数字总是比第二个数字小。

现在，我们定义一种跟随关系，当且仅当 b < c 时，数对(c, d) 才可以跟在 (a, b) 后面。我们用这种形式来构造一个数对链。

给定一个数对集合，找出能够形成的最长数对链的长度。你不需要用到所有的数对，你可以以任何顺序选择其中的一些数对来构造。

"""
from math import inf


class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        """
        todo 贪心算法
        要挑选最长数对链的第一个数对时，最优的选择是挑选第二个数字最小的，
        这样能给挑选后续的数对留下更多的空间。挑完第一个数对后，要挑第二个数对时，
        也是按照相同的思路，是在剩下的数对中，第一个数字满足题意的条件下，
        挑选第二个数字最小的。按照这样的思路，可以先将输入按照第二个数字排序，
        然后不停地判断第一个数字是否能满足大于前一个数对的第二个数字即可。
        """
        cur,res = -inf,0
        for x,y in sorted(pairs,key=lambda p:p[1]):
            if cur < x:
                cur = y
                res += 1
        return res
    def findLongestChain1(self, pairs: list[list[int]]) -> int:
        # TODO 动态规划
        pairs.sort()
        dp = [1] * len(pairs)
        for i in range(len(pairs)):
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp[-1]

if __name__ == '__main__':
    pass