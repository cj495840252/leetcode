"""
662. 二叉树最大宽度
给你一棵二叉树的根节点 root ，返回树的 最大宽度 。

树的 最大宽度 是所有层中最大的 宽度 。

每一层的 宽度 被定义为该层最左和最右的非空节点（即，两个端点）之间的长度。将这个二叉树视作与满二叉树结构相同，两端点间会出现一些延伸到这一层的 None 节点，这些 None 节点也计入长度。

题目数据保证答案将会在  32 位 带符号整数范围内。
"""
from collections import deque
from typing import Optional

from DataType.ClassTreeNode import TreeNode,create


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q1 = deque([[root, 1]])
        q2 = deque()
        wide = 0
        while(q1):
            for i in range(len(q1)):
                leftindex = q1[0][1]
                rightindex = q1[-1][1]
                wide = max(wide, rightindex - leftindex + 1)
                p = q1.popleft()
                if p[0].left:
                    q2.append([p[0].left,p[1]*2])
                if p[0].right:
                    q2.append([p[0].right,p[1]*2+1])
            q1,q2 = q2,q1
        return wide

    def widthOfBinaryTree1(self, root: Optional[TreeNode]) -> int:
        level_min = {}  # 每一层的最左边节点的序列
        def dfs(node,depth,index):
            if node is None:
                return 0
            if depth not in level_min:
                level_min[depth] = index
            return max(index-level_min[depth]+1,
                       dfs(node.left, depth+1, index*2),
                       dfs(node.right,depth+1,index*2+1))
        return dfs(root,1,1)



if __name__ == '__main__':
    root = [0,0,0,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None,None,0,0,None]
    root = create(root)
    s = Solution().widthOfBinaryTree(root)
    s1 = Solution().widthOfBinaryTree1(root)
    print(s1)
    print(s)