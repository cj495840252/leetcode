"""
1460. 通过翻转子数组使两个数组相等
给你两个长度相同的整数数组 target 和 arr 。每一步中，你可以选择 arr 的任意 非空子数组 并将它翻转。你可以执行此过程任意次。

如果你能让 arr 变得与 target 相同，返回 True；否则，返回 False 。

"""
import collections


class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        count = collections.Counter()
        i = j = 0
        while i<len(target):
            count[target[i]] += 1
            i += 1
        print(count)
        while j < len(arr):
            count[arr[j]] -= 1
            if count[arr[j]] == 0:
                count.pop(arr[j])
            j += 1
        if len(count) == 0:
            return True
        else:
            return False

    def func(self,target, arr):
        """直接哈希"""
        count = {}
        for i in target:
            if count.get(i):
                count[i] += 1
            else:
                count[i] = 1
        print(count)
        for i in arr:
            if count.get(i):
                count[i] -= 1
                if count[i] == 0:
                    count.pop(i)
            else:
                count[i] = -1
        print(count)
        if len(count) == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    target = [1,1,1,1,1]
    arr = [1,1,1,1,1]
    s = Solution().canBeEqual(target,arr)
    s1 = Solution().func(target,arr)
    assert s == s1