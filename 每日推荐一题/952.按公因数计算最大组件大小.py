"""
952. 按公因数计算最大组件大小
给定一个由不同正整数的组成的非空数组 nums ，考虑下面的图：

有 nums.length 个节点，按从 nums[0] 到 nums[nums.length - 1] 标记；
只有当 nums[i] 和 nums[j] 共用一个大于 1 的公因数时，nums[i] 和 nums[j]之间才有一条边。
返回 图中最大连通组件的大小 。
"""
# 并查集
# 第一步，初始化，每个点的父节点为自己
# 第二步找父节点，路径压缩
# 第三步合并
from collections import Counter


class UnionFind:
    def __init__(self, n: int):
        # n 为列表中的最大值，
        # 下表为0开始，表示值为下表的节点的父节点为parent[i]
        self.parant = list(range(n))
        self.rank = [0] * n  # 用来记录0到该点的最大层次

    def find(self, x: int) -> int:
        if self.parant[x] == x:
            return self.parant[x]
        else:
            self.parant[x] = self.find(self.parant[x])
            return self.parant[x]

    def merge(self, x: int, y: int):
        x = self.find(x)
        y = self.find(y)
        if x == y:  # 两个的点的祖父节点是一个则不合并
            return
        # 求最长的，那么就把长的加在短的上面
        if self.rank[x] > self.rank[y]:
            self.parant[y] = x
        elif self.rank[x] < self.rank[y]:
            self.parant[x] = y
        else:
            self.parant[y] = x
            self.rank[x] += 1


class Solution:
    def largestComponentSize(self, nums: list[int]) -> int:
        uf = UnionFind(max(nums) + 1)
        for num in nums:
            i = 2
            while i ** 2 <= num:
                if num % i == 0:
                    uf.merge(num, i)
                    uf.merge(num, num // i)  # 地板除保证为int
                i += 1
        # 这里找到nums中每个值的最顶层父节点，出现一次记一次数
        # 最大层次的rank也应该为该值。但不好找
        print(uf.find(nums[-1]))
        return max(Counter(uf.find(num) for num in nums).values())


if __name__ == '__main__':
    s = Solution().largestComponentSize([4, 6, 15, 35])
    print(s)
