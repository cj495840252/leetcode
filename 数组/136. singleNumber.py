class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        """
        自己第一次想的思路：排序，再遍历一边，每两个元素的值必定相等，若不相等，则第一个为单独的数
        若数组为奇书，那么必有一个，且若在最后需要特殊出来
        """
        nums = sorted(nums)
        print(nums)
        for i in range(0, len(nums), 2):
            if i == len(nums)-1 or nums[i] != nums[i+1]:
                return nums[i]
        return 0

    def singleNumber2(self, nums: list[int]) -> int:
        """
        参考答案：位运算
        两个相同的数异或为0，且异或运算满足交换律和结合律
        """
        res = 0
        for i in nums:
            res = i ^ res
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [4, 1, 2, 1, 2]
    res = s.singleNumber2(nums)
    print(res)