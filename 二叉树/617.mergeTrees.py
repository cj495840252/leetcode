"""
617. 合并二叉树
给你两棵二叉树： root1 和 root2 。

想象一下，当你将其中一棵覆盖到另一棵之上时，两棵树上的一些节点将会重叠（而另一些不会）。你需要将这两棵树合并成一棵新二叉树。合并的规则是：如果两个节点重叠，那么将这两个节点的值相加作为合并后节点的新值；否则，不为 null 的节点将直接作为新二叉树的节点。

返回合并后的二叉树。

注意: 合并过程必须从两个树的根节点开始。
"""
from collections import deque

from DataType.ClassTreeNode import TreeNode
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        """
        广度优先搜索
        """
        if not root2:
            return root1
        if not root1:
            return root2
        root = TreeNode(root1.val+root2.val)
        q = deque([root])
        q1 = deque([root1])
        q2 = deque([root2])
        while q1 and q2:
            qq1 = q1.popleft()
            qq2 = q2.popleft()
            qq = q.popleft()
            if qq1.left and qq2.left:
                new_lnode = TreeNode(qq1.left.val+qq2.left.val)
                qq.left = new_lnode
                q.append(new_lnode)
                q1.append(qq1.left)
                q2.append(qq2.left)
            elif not qq1.left:
                qq.left = qq2.left
            elif not qq2.left:
                qq.left = qq1.left

            if not qq1.right:
                qq.right = qq2.right
            elif not qq2.right:
                qq.right = qq1.right
            else:
                new_rnode = TreeNode(qq1.right.val+qq2.right.val)
                qq.right = new_rnode
                q.append(qq.right)
                q1.append(qq1.right)
                q2.append(qq2.right)
        return root

    def mergeTrees1(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        """
        深度优先(这就是递归)
        """
        if not root1:
            return root2
        if not root2:
            return root1
        root = TreeNode(root1.val + root2.val)
        root.left = self.mergeTrees1(root1.left, root2.left)
        root.right = self.mergeTrees1(root1.right, root2.right)
        return root


if __name__ == '__main__':
    root1 = [1, 3, 2, 5]
    root2 = [2, 1, 3, None, 4, None, 7]
    import DataType.ClassTreeNode as tn
    r1 = tn.create(root1)
    r2 = tn.create(root2)
    s = Solution().mergeTrees1(root1=r1, root2=r2)
    tn.BFS_print(r1)
    tn.BFS_print(r2)
    tn.BFS_print(s)
