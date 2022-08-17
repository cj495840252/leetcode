"""
todo 1302. 层数最深叶子节点的和
给你一棵二叉树的根节点 root ，请你返回 层数最深的叶子节点的和 。
              1
            /   \
           2     3
         /  \      \
        4    5      6
       /             \
      7               8
      输出：15
"""
from collections import deque
from typing import Optional
from DataType.ClassTreeNode import TreeNode,create,BFS_print


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        """
        广度优先，两个队列
        """
        res = []
        temp = 0
        q1 = deque()
        q2 = []
        q1.append(root)
        while q1:
            p = q1.popleft()
            temp += p.val
            if p.left:
                q2.append(p.left)
            if p.right:
                q2.append(p.right)
            if not q1:
                res.append(temp)
                temp = 0
                q1.extend(q2)
                q2 = []
        return res[-1]

    def deepestLeavesSum1(self, root: Optional[TreeNode]) -> int:
        """优化广度，一个队列"""
        q = deque([root])
        res = 0
        while q:
            res = 0
            for _ in range(len(q)):
                p = q.popleft()
                res += p.val
                if p.left:
                    q.append(p.left)
                if p.right:
                    q.append(p.right)
        return res

    def deepestLeavesSum2(self, root: Optional[TreeNode]) -> int:
        """
        深度优先遍历,用全局遍历维护层次和值
        """
        maxlevel = 0
        res = 0
        def dfs(root,level):
            if not root:
                return
            nonlocal maxlevel,res
            if level > maxlevel:
                maxlevel = level
                res = root.val
            elif level == maxlevel:
                res += root.val
            dfs(root.left,level+1)
            dfs(root.right,level+1)
        dfs(root,0)
        return res


if __name__ == '__main__':
    root = [1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8]
    head = create(root)
    BFS_print(head)
    s = Solution().deepestLeavesSum2(head)
    print(s)