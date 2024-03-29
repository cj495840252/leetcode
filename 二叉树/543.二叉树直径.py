"""
543. 二叉树的直径
给定一棵二叉树，你需要计算它的直径长度。
一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。
示例 :
给定二叉树

          1
         / \
        2   3
       / \
      4   5
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
"""
from typing import Optional
from DataType.ClassTreeNode import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.d = 1
        def depth(node):
            if not node:
                return 0
            R = depth(node.right)
            L = depth(node.left)
            self.d = max(self.d, R+L+1)  # 每个节点直径与当前最大值比较
            # 保证不是最大值的时候返回该节点（要包含该节点，so+1）最长直径
            return max(L, R) + 1
        depth(root)
        return self.d - 1  # 求得边数，节点数减一
