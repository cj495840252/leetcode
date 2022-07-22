"""
448. 找到所有数组中消失的数字
    给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。
    请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式返回结果。
     * 要求时间复杂度为 O（n），且不使用额外空间
"""


class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        """
        1. 全局遍历，超出时间限制
        """
        n = len(nums)
        res = set()
        for i in range(1, n + 1):
            if i not in nums:
                res.add(i)
        return list(res)

    def findDisappearedNumbers1(self, nums: list[int]) -> list[int]:
        """
        2. 全局遍历(优化)，超出时间限制
        """
        n = len(nums)
        res = [x for x in range(1, n + 1)]
        for i in set(nums):
            if i <= 0 or i > n:
                continue
            res.remove(i)
        return res

    def findDisappearedNumbers2(self, nums: list[int]) -> list[int]:
        """
        3.思想：数值和下表之间的联系
        """
        res = []
        for i, value in enumerate(nums):
            if value <= len(nums):
                if value < 0:
                    value = value + len(nums)
                nums[value - 1] -= len(nums)
        for i, value in enumerate(nums):
            if value > 0:
                res.append(i + 1)
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    res = s.findDisappearedNumbers2(nums)
    print(res)
