"""
169. 多数元素
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。
"""
import random


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """
        1. 哈希表，（python里面字典记录每一个元素出现的次数，大于数组长度一半则返回）
        两次遍历O(2n),但是需要额外的空间。考虑增加一个数保存最大值，消除哈希表的遍历
        """
        max_value = 0
        hastable = {}
        for i in range(len(nums)):
            if nums[i] in hastable:
                hastable[nums[i]] += 1
            else:
                hastable[nums[i]] = 1
        for i, k in hastable.items():
            if k > len(nums) / 2:
                return i
        return 0

    def majorityElement1(self, nums: list[int]) -> int:
        """
        2. 众数：有序的列表，n/2处一定是众数。时间复杂度取决于排序函数
        """
        nums = sorted(nums)
        n = int(len(nums)/2)
        return nums[n]

    def majorityElement2(self, nums: list[int]) -> int:
        """
        3. 随机化，随机取一个数，有1/2的概率是众数。再判断是不是众数（ 时间复杂度O(n) ）
            最差时间复杂度：O(无穷大)
            最优时间复杂度：O(n), 计数筛选的数，大于数组长度的一半，则为众数
        """
        while True:
            n = random.choice(nums)
            count = 0
            for i in nums:
                if i == n:
                    count += 1
            if count > len(nums)/2:
                return n

    def majorityElement3(self, nums: list[int]) -> int:
        """
        4. 分治：待补充
        """
        pass


if __name__ == '__main__':
    nums = [2, 2, 1, 1, 1, 2, 2]
    s = Solution()
    res = s.majorityElement2(nums)
    print(res)
