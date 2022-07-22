"""
121. 买卖股票的最佳时机
"""


class Solution:
    """
    暴力解法
    """

    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                max_profit = max(max_profit, prices[j] - prices[i])
        if max_profit < 0:
            max_profit = 0
        return max_profit

    def _maxProfit(self, prices: list[int]) -> int:
        """
        动态规划
        min_profit:表示0到第i天的最小价格
        """
        inf = int(1e9)
        min_profit = inf
        max_profit = 0
        for i in prices:
            max_profit = max(i - min_profit, max_profit)
            min_profit = min(i, min_profit)
        return max_profit


if __name__ == '__main__':
    s = Solution()
    nums = [7, 1, 5, 3, 6, 4]
    print(s.maxProfit(nums))
