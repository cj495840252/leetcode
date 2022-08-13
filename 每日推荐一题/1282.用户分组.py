"""
1282. 用户分组
有 n 个人被分成数量未知的组。每个人都被标记为一个从 0 到 n - 1 的唯一ID 。

给定一个整数数组 groupSizes ，其中 groupSizes[i] 是第 i 个人所在的组的大小。例如，如果 groupSizes[1] = 3 ，则第 1 个人必须位于大小为 3 的组中。

返回一个组列表，使每个人 i 都在一个大小为 groupSizes[i] 的组中。

每个人应该 恰好只 出现在 一个组 中，并且每个人必须在一个组中。如果有多个答案，返回其中 任何 一个。可以 保证 给定输入 至少有一个 有效的解。
"""

# 思路，哈希表
class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        res = []
        d = {}
        for i,v in enumerate(groupSizes):
            if d.get(v):
                d[v].append(i)
            else:
                d[v] = [i]
        print(d)
        for k,v in d.items():
            i = 0
            while i + k <= len(v):
                res.append(v[i:i+k])
                i = i+k
        return res

if __name__ == '__main__':
    s = Solution().groupThePeople([3,3,3,3,3,1,3])
    print(s)
