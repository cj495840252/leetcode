"""
两数之和
"""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hastable = {}
        for i, n in enumerate(nums):
            j = target - n
            if j in hastable.keys():
                return [hastable[j], i]
            hastable[n] = i
        print(hastable)
        return []


if __name__ == '__main__':
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    res = s.twoSum(target=target, nums=nums)
    print(res)
