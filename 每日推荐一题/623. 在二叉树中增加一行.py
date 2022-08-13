import collections
from typing import Optional

from DataType.ClassTreeNode import TreeNode,create,BFS_print
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        """
        深度优先
        """
        if depth==1 or root is None:
            new_node = TreeNode(val)
            new_node.left = root
            return new_node

        if depth == 2:
            new_node_l = TreeNode(val)
            new_node_r = TreeNode(val)
            if root.left:
                new_node_l.left = root.left
            if root.right:
                new_node_r.right = root.right
            root.left = new_node_l
            root.right = new_node_r
        print(root.left,"---->", root.right)
        self.addOneRow(root.left, val, depth-1)
        self.addOneRow(root.right, val, depth-1)
        return root

    def bfs(self, root, val, depth):
        if depth==1:
            new_node = TreeNode(val, left=root)
            return new_node
        q = collections.deque([root])
        p = root
        while q:
            curr = q.popleft()
            if p.left==curr or p.right==curr:
                p = curr
                depth-=1
            if depth == 2:
                new_node_l = TreeNode(val, curr.left)
                new_node_r = TreeNode(val, right=curr.right)
                curr.left = new_node_l
                curr.right = new_node_r
        return root

    def bfs2(self, root, val, depth):
        if depth == 1:
            return TreeNode(val,root)
        res = [root]
        for i in range(depth-2):
            temp=[]
            for node in res:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            res = temp
        for node in res:
            new_l = TreeNode(val,left=node.left)
            new_r = TreeNode(val,right=node.right)
            node.left = new_l
            node.right = new_r
        return root

if __name__ == '__main__':
    root = [4,2,None,3,1]
    val = 1
    depth = 3
    root = create(root)
    BFS_print(root)
    s = Solution().bfs2(root, val, depth)
    ss = Solution().addOneRow(root, val, depth)
    BFS_print(ss)
    BFS_print(s)

