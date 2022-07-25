"""
题目描述
剑指 Offer II 115. 重建序列
给定一个长度为 n 的整数数组 nums ，其中 nums 是范围为 [1，n] 的整数的排列。还提供了一个 2D 整数数组 sequences ，其中 sequences[i] 是 nums 的子序列。
检查 nums 是否是唯一的最短 超序列 。最短 超序列 是 长度最短 的序列，并且所有序列 sequences[i] 都是它的子序列。对于给定的数组 sequences ，可能存在多个有效的 超序列 。

例如，对于 sequences = [[1,2],[1,3]] ，有两个最短的 超序列 ，[1,2,3] 和 [1,3,2] 。
而对于 sequences = [[1,2],[1,3],[1,2,3]] ，唯一可能的最短 超序列 是 [1,2,3] 。[1,2,3,4] 是可能的超序列，但不是最短的。
如果 nums 是序列的唯一最短 超序列 ，则返回 true ，否则返回 false 。
子序列 是一个可以通过从另一个序列中删除一些元素或不删除任何元素，而不改变其余元素的顺序的序列。
"""
from collections import deque

from setuptools._vendor.more_itertools import pairwise


# 思想：拓扑排序;nums是1-n所有整数的排列，[1, 2, 3 4, 5......n]，sequences是子序列，里面的值也由
class Solution:
    def sequenceReconstruction(self, nums: list[int], sequences: list[list[int]]) -> bool:
        """
        1. 完全不会。看注释
        """
        n = len(nums)
        g = [[] for _ in range(n)]    # 生成nums长度的列表，内容元素全为[]
        inDeg = [0] * n               # 生成一个长度为n，全都为0的列表.存储1到n各个数的入度。存放边
        for sequence in sequences:    # 遍历每一个元素
            for x, y in pairwise(sequence):    # pairwise生成一个迭代器对象 for x,y in pairwise([1,2,3,4])
                g[x - 1].append(y - 1)    # x-1表示每个点的下表，与inDeg对应，y-1与顶点入度存放的下表对应
                inDeg[y - 1] += 1
        q = deque([i for i, d in enumerate(inDeg) if d == 0])  # 队列，入度为零加入队列
        while q:
            if len(q) > 1:   # 要求最短超序列唯一，则必定每一次都只有一个入度为0
                return False
            x = q.popleft()  # 从左到右取数据
            for y in g[x]:   #
                inDeg[y] -= 1
                if inDeg[y] == 0:
                    q.append(y)
        return True

    def sequenceReconstruction1(self, nums: list[int], sequences: list[list[int]]) -> bool:
        """
        2.用哈希表记录每个元素在子序列中的下一个元素.
        nums是唯一最短超序列的充要条件就是nums中每一个元素的下一个元素都在哈希表中出现过.
        当不在哈希表中出现时,说明此两元素交换位置也可以组成新的超序列,不满足条件.
        """
        l = len(nums)
        d = {}  # 哈希表
        for seq in sequences:
            for i in range(len(seq) - 1):
                if seq[i] not in d:
                    d[seq[i]] = set()
                d[seq[i]].add(seq[i + 1])
        for i in range(l - 1):  # 检查每个元素是否出现在前一个元素的哈希表值中
            if nums[i] not in d or nums[i + 1] not in d[nums[i]]:
                return False
        return True

    def sequenceReconstruction2(self, nums: list[int], sequences: list[list[int]]) -> bool:
        pass  # 待完成
        """
        解题思路
            对于nums中的每个相邻数对，检验其是否在sequences中出现过。
            若全部检查通过，则说明其为唯一最短超序列，否则不是。
            
            正确性说明
            这里不敢说“证明”，简单从充分性和必要性两方面来说一下吧。
            
            充分性
            若nums中的每个相邻数对都能找到，显然nums中的偏序关系都是成立的。又由于nums是n以下正整数的全排列，所以这个偏序关系一定是唯一的，否则任意交换其中的数字一定会导致偏序关系与sequences不一致。且题目已经保证了sequences中都是nums的子序列，所以不会出现自相矛盾的情况。
            
            必要性 若nums是唯一最短超序列，那么首先其中不会有多余的数字，也即[1,n]的每个数字都会在sequences中出现。又由于sequences中都是nums的子序列，所以sequences中的偏序关系一定是一致的。
            
            考虑nums中任意一对相邻数对(a,b)，若(a,b)在某个子序列中出现，a与b中间一定不会有其他的数字，否则这个数在nums中一定也在a与b中间，与nums是全排列矛盾；若(a,b)不在同一个子序列中出现，若ab可以通过中间数产生间接的偏序关系（也就是a<c<b），与之前的情况类似，中间数会产生矛盾，若ab没有间接的偏序关系，那么我们在nums中交换ab的位置，同样能够产生一个长度为n的最短超序列，与唯一性矛盾。
            
            实现细节
            为了检验数对的存在，一般用字典（集合）是比较好的。这里为了便于检索，通过位运算将相邻的两个数合成一个数，能够提高一定的哈希效率。
        """


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    sequences = [[1, 2], [1, 3, 4], [2, 3, 4]]
    s = Solution()
    res = s.sequenceReconstruction(nums, sequences)
    print(res)
