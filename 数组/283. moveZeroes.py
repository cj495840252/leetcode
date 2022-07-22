class Solution:
    """
    Do not return anything, modify nums in-place instead.
    """

    def moveZeroes(self, nums: list[int]) -> None:
        """
        1. O(n²),n次遍历中的n次移动。效果不好
        """
        last = len(nums) - 1  # 尾指针
        i = 0
        while True:
            if nums[i] == 0:
                for j in range(i, last):
                    nums[j] = nums[j + 1]
                nums[last] = 0
                last -= 1
            else:
                i += 1
            if last < i:
                break

    def moveZeroes1(self, nums: list[int]) -> None:
        """
        优化：双指针同时从左到右，一个指向0，一个指向非0
        """
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] == 0:
                j += 1
            if nums[i] != 0:
                i += 1
            if i >= j:
                j += 1
                continue
            if j > len(nums) - 1 or i > len(nums) - 1:
                break
            if nums[i] == 0 and nums[j] != 0:
                nums[i] = nums[j]
                nums[j] = 0
        print(i, j, nums)

    def moveZeroes2(self, nums: list[int]) -> None:
        """
        3. 和第二个一样的思路，官方的写法
        """
        left = 0
        right = 0
        n = len(nums)
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
        print(nums)


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    s = Solution()
    s.moveZeroes2(nums)
