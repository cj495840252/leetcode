"""
1470. 重新排列数组
给你一个数组 nums ，数组中有 2n 个元素，按 [x1,x2,...,xn,y1,y2,...,yn] 的格式排列。

请你将数组按 [x1,y1,x2,y2,...,xn,yn] 格式重新排列，返回重排后的数组。

"""

class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        i = 0
        j = n
        res = []
        while i < n:
            res.append(nums[i])
            res.append(nums[j])
            i += 1
            j += 1
        return res
if __name__ == '__main__':
    nums = [1,2]
    s = Solution().shuffle(nums,1)
    print(s)