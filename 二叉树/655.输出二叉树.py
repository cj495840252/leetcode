"""
655. 输出二叉树
给你一棵二叉树的根节点 root ，请你构造一个下标从 0 开始、大小为 m x n 的字符串矩阵 res ，用以表示树的 格式化布局 。构造此格式化布局矩阵需要遵循以下规则：

树的 高度 为 height ，矩阵的行数 m 应该等于 height + 1 。
矩阵的列数 n 应该等于 2height+1 - 1 。
根节点 需要放置在 顶行 的 正中间 ，对应位置为 res[0][(n-1)/2] 。
对于放置在矩阵中的每个节点，设对应位置为 res[r][c] ，将其左子节点放置在 res[r+1][c-2height-r-1] ，
右子节点放置在 res[r+1][c+2height-r-1] 。
继续这一过程，直到树中的所有节点都妥善放置。
任意空单元格都应该包含空字符串 "" 。
返回构造得到的矩阵 res 。
"""
import collections
import copy
from pprint import pprint
from typing import Optional
from DataType.ClassTreeNode import TreeNode, create, BFS_print

"""
思路：先求高度，根节点放在中间点，递归向下放根节点更新两边的边界
"""


class Solution:
    def printTree(self, root: Optional[TreeNode]) -> list[list[str]]:
        def dfs(root, level):
            if not root:
                return 0
            l = dfs(root.left, level + 1)
            r = dfs(root.right, level + 1)
            return max(l, r) + 1

        h = dfs(root, 0)
        n = 2 ** h - 1
        res = [copy.deepcopy([""] * n) for i in range(h)]
        pprint(res)

        def func(root, level, res, m, n):
            if not root:
                return
            t = (m + n) // 2
            print(level, t)
            res[level][t] = str(root.val)
            func(root.left, level + 1, res, m, t)
            func(root.right, level + 1, res, t, n)

        func(root, 0, res, 0, n)
        return res


if __name__ == '__main__':
    root = create([10, 5, 15, None, None, 6, 20])
    BFS_print(root)
    s = Solution().printTree(root)
    pprint(s)
