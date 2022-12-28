"""
todo 687. 最长同值路径
给定一个二叉树的 root ，返回 最长的路径的长度 ，这个路径中的 每个节点具有相同值 。 这条路径可以经过也可以不经过根节点。

两个节点之间的路径长度 由它们之间的边数表示。
"""
from typing import Optional

from DataType.ClassTreeNode import TreeNode,create,BFS_print


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        max_len = 0
        def fun(root):
            nonlocal max_len
            if not root:
                return 0
            l = fun(root.left)   # 代表左边的长度
            r = fun(root.right)  # 代表右边的长度
            # 如果当前节点val等于左子节点val加上一
            l1 = l + 1 if root.left and root.left.val == root.val else 0
            # 如果当前节点val等于右子节点val加上一
            r1 = r + 1 if root.right and root.right.val == root.val else 0
            # todo 都相等则需要加上  2
            max_len = max(l1+r1,max_len) # 更新记录
            return max(l1,r1)
        fun(root)
        return max_len



if __name__ == '__main__':
    r = create([1,1,1])
    BFS_print(r)
    s = Solution().longestUnivaluePath(r)
    print(s)
