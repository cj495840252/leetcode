"""
26. 删除有序数组中的重复项
双指针
"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[i] != nums[j]:
                if i - j > 1:
                    nums[j+1] = nums[i]
                j += 1
        return j + 1




if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    nums2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    nums3 = [1, 1, 2]
    # print(func(nums2))
    s = Solution()
    res = s.removeDuplicates(nums=nums)
    print(res)
    # print([x for x in range(5,0,-1)])