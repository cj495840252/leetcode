from typing import Optional
from DataType.ClassTreeNode import TreeNode,create,BFS_print

"""
654. 最大二叉树
给定一个不重复的整数数组 nums 。 最大二叉树 可以用下面的算法从 nums 递归地构建:

创建一个根节点，其值为 nums 中的最大值。
递归地在最大值 左边 的 子数组前缀上 构建左子树。
递归地在最大值 右边 的 子数组后缀上 构建右子树。



998. 最大二叉树 II
最大树 定义：一棵树，并满足：其中每个节点的值都大于其子树中的任何其他值。

给你最大树的根节点 root 和一个整数 val 。
将val插入到树中
题意：将val加入到最大树，实现效果同将val加入到创建树的列表中的末尾，重新创建最大树
"""




class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # todo 思路:若val大于current.val则插入右子树，则将该节点的左子树加入新节点的右节点，
        #  小于则向左右节点移动，没有右节点时，直接插入最后叶子节点的右节点
        p = root
        if root.val < val:
            root = TreeNode(val)
            root.left = p
            return root
        last = None
        while True:
            if val > p.val:
                last.right = TreeNode(val)
                last.right.left = p
                break
            else:
                if p.right:
                    last = p
                    p = p.right
                else:
                    p.right = TreeNode(val)
                    break
        return root

    def constructMaximumBinaryTree(self, nums: list[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        root = TreeNode(max(nums))
        root.left = self.constructMaximumBinaryTree(nums[:nums.index(max(nums))])
        root.right = self.constructMaximumBinaryTree(nums[nums.index(max(nums))+1:])
        return root

if __name__ == '__main__':
    root = [2,1,5,3]
    val = 4
    s = Solution()
    root = s.constructMaximumBinaryTree(root)
    BFS_print(root)
    res = s.insertIntoMaxTree(root,val)
    BFS_print(res)
