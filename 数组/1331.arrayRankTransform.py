"""
1331. 数组序号转换
给你一个整数数组 arr ，请你将数组中的每个元素替换为它们排序后的序号。

序号代表了一个元素有多大。序号编号的规则如下：

序号从 1 开始编号。
一个元素越大，那么序号越大。如果两个元素相等，那么它们的序号相同。
每个数字的序号都应该尽可能地小。
"""


class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        if not arr:
            return []
        arr1 = sorted(arr)
        d = {arr1[0]: 1}
        i = 1
        for j in range(1, len(arr1)):  # 1 - 8
            print("==>", j, i, arr1[j],arr1[j-1])
            if arr1[j - 1] < arr1[j]:
                i += 1
                d[arr1[j]] = i
            else:
                d[arr1[j]] = i
        arr = map(lambda x: d[x], arr)
        return list(arr)

    def arrayRankTransform1(self, arr: list[int]) -> list[int]:
        ranks = {v: i for i, v in enumerate(sorted(set(arr)))}
        return [ranks[x]+1 for x in arr]

if __name__ == '__main__':
    s = Solution().arrayRankTransform1([37, 12, 28, 9, 100, 56, 80, 5, 12])
    s1 = Solution().arrayRankTransform1([37, 12, 28, 9, 100, 56, 80, 5, 12])
    print(s)
    print(s1)
    assert s == s1