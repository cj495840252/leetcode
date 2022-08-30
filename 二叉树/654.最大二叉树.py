"""
654. 最大二叉树
给定一个不重复的整数数组 nums 。 最大二叉树 可以用下面的算法从 nums 递归地构建:

创建一个根节点，其值为 nums 中的最大值。
递归地在最大值 左边 的 子数组前缀上 构建左子树。
递归地在最大值 右边 的 子数组后缀上 构建右子树。
返回 nums 构建的 最大二叉树 。
"""
from typing import Optional

from DataType.ClassTreeNode import TreeNode,BFS_print,create
class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> Optional[TreeNode]:
        if not nums:
            return
        m = max(nums)
        index = nums.index(m)
        root = TreeNode(m)
        root.left = self.constructMaximumBinaryTree(nums[0:index])
        root.right = self.constructMaximumBinaryTree(nums[index+1:])
        return root

if __name__ == '__main__':
    nums = [3,2,1,6,0,5]
    s = Solution().constructMaximumBinaryTree(nums)
    BFS_print(s)