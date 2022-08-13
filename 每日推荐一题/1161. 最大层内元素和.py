"""
1161. 最大层内元素和
给你一个二叉树的根节点 root。设根节点位于二叉树的第 1 层，而根节点的子节点位于第 2 层，依此类推。

请返回层内元素之和 最大 的那几层（可能只有一层）的层号，并返回其中 最小 的那个。

"""
import copy
from typing import Optional
from DataType.ClassTreeNode import TreeNode, create, BFS_print
from collections import deque

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        """
        广度优先, 一个队列存放当前节点，另一个队列存放下一个节点，当前节点遍历完后，下一节点赋给当前节点
        """
        q1 = deque([root])  # 当前节点队列
        q2 = deque() # 下一层节点
        res = []
        value = 0
        while q1:
            p = q1.popleft()
            value += p.val
            if p.left:
                q2.append(p.left)
            if p.right:
                q2.append(p.right)
            if not q1:
                res.append(value)
                value = 0
                q1 = copy.deepcopy(q2)
                q2.clear()
        print(res)
        for i in range(len(res)):
            if res[i] == max(res):
                return i+1

    def maxLevelSum1(self, root: Optional[TreeNode]) -> int:
        """
        深度优先搜索
        """
        res = [] # 存放每一层的结果
        def DFS_find(root, level):
            if level == len(res):
                res.append(root.val)
            else:
                res[level] += root.val
            if root.left:
                DFS_find(root.left, level+1)
            if root.right:
                DFS_find(root.right, level+1)
        DFS_find(root, 0)
        print(res)
        for i in range(len(res)):
            if res[i] == max(res):
                return i+1
if __name__ == '__main__':
    # head = create([1, 7, 0, 7, -8, None, None])
    head = create([989,None,10250,98693,-89388,None,None,None,-32127])

    # BFS_print(head)
    s = Solution().maxLevelSum(head)
    s1 = Solution().maxLevelSum1(head)
    assert s == s1