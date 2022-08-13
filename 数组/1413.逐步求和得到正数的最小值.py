"""
1413. 逐步求和得到正数的最小值
给你一个整数数组 nums 。你可以选定任意的 正数 startValue 作为初始值。

你需要从左到右遍历 nums 数组，并将 startValue 依次累加上 nums 数组中的值。

请你在确保累加和始终大于等于 1 的前提下，选出一个最小的 正数 作为 startValue 。
"""

class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        startValue = 0
        sumn = 0
        for i in nums:
            sumn += i
            if sumn < 0:
                startValue = max(startValue, -sumn)
        return startValue + 1

    def minStartValue1(self, nums: list[int]) -> int:
        startValue = 0
        sumn = 0
        for i in nums:
            sumn += i
            startValue = min(startValue, sumn)
        # startValue <0时，取反加一    0-1之间时 和 >1 startValue = 0
        return -startValue + 1

if __name__ == '__main__':
    s = Solution().minStartValue([-3,2,-3,4,2])
    print(s)