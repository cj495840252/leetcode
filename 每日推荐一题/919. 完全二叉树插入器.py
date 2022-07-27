"""
919. 完全二叉树插入器
完全二叉树 是每一层（除最后一层外）都是完全填充（即，节点数达到最大）的，并且所有的节点都尽可能地集中在左侧。

设计一种算法，将一个新节点插入到一个完整的二叉树中，并在插入后保持其完整。

实现 CBTInserter 类:

CBTInserter(TreeNode root) 使用头节点为 root 的给定树初始化该数据结构；
CBTInserter.insert(int v)  向树中插入一个值为 Node.val == val的新节点 TreeNode。使树保持完全二叉树的状态，并返回插入节点 TreeNode 的父节点的值；
CBTInserter.get_root() 将返回树的头节点。
"""

from DataType.ClassTreeNode import TreeNode, create, BFS_print
from collections import deque


# 不是二叉排序树，思想：广度优先搜索
class CBTInserter:
    def __init__(self, root: TreeNode):
        self.root = root

    def insert(self, val: int) -> int:
        new_node = TreeNode(val=val)
        q = deque()
        q.append(self.root)
        while q:
            p = q.popleft()
            if p.left:
                q.append(p.left)
            else:
                p.left = new_node
                return p.val
            if p.right:
                q.append(p.right)
            else:
                p.right = new_node
                return p.val

    def get_root(self) -> TreeNode:
        return self.root


# 官方版本：思路一样，优化了查询次数。用类属性保存了可以插入的点，第二次后就不用遍历了
class CBTInserter1:
    def __init__(self, root: TreeNode):
        self.root = root
        self.candidate = deque()

        q = deque([root])
        while q:
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if not (node.left and node.right):
                self.candidate.append(node)

    def insert(self, val: int) -> int:
        candidate_ = self.candidate

        child = TreeNode(val)
        node = candidate_[0]
        ret = node.val

        if not node.left:
            node.left = child
        else:
            node.right = child
            candidate_.popleft()

        candidate_.append(child)
        return ret

    def get_root(self) -> TreeNode:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
root = create([1, 4])
BFS_print(root)
print("\n==========================")

obj = CBTInserter(root)
param_1 = obj.insert(2)
# BFS_print(obj.get_root())
param_2 = obj.insert(3)
print("\n==========================")

BFS_print(obj.get_root())
