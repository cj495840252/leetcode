# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 构造二叉树
def create(value_list: list):
    if not value_list:
        return
    head = TreeNode(value_list[0])
    q = deque()
    q.append(head)
    i = 1
    while q and i < len(value_list):
        p = q.popleft()
        if p.right and p.left:
            q.append(p.left)
            q.append(p.right)
        if not p.left:
            new_node = TreeNode(value_list[i]) if value_list[i] is not None else None
            i += 1
            p.left = new_node
            q.append(new_node)
            if i == len(value_list):
                break
        if not p.right:
            new_node = TreeNode(value_list[i])
            i += 1
            p.right = new_node
            q.append(new_node)
    return head


# 遍历二叉树：广度优先
def BFS_print(root, end="   "):
    q = deque()
    q.append(root)
    while q:
        p = q.popleft()
        print(p.val, end=end)
        if p.left:
            q.append(p.left)
        if p.right:
            q.append(p.right)
    print()

if __name__ == '__main__':
    root = create([2, 1, 3, None, 4, None, 7])

    BFS_print(root)
