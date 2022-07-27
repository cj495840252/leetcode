"""
1206. 设计跳表
不使用任何库函数，设计一个 跳表 。

跳表 是在 O(log(n)) 时间内完成增加、删除、搜索操作的数据结构。跳表相比于树堆与红黑树，其功能与性能相当，并且跳表的代码长度相较下更短，其设计思想与链表相似。

例如，一个跳表包含 [30, 40, 50, 60, 70, 90] ，然后
"""
import random
MAX_LEVEL = 32
P_FACTOR = 0.25  # 增加一层的概率，表示每四个将会建立一个索引

def random_level() -> int:
    lv = 1
    while lv < MAX_LEVEL and random.random() < P_FACTOR:
        lv += 1
    return lv

class SkiplistNode:
    __slots__ = 'val', 'forward'

    def __init__(self, val: int, max_level=MAX_LEVEL):
        self.val = val
        self.forward = [None] * max_level  # 列表中的每一个元素都将指向一个节点

class Skiplist:
    """
    官方答案
    """
    def __init__(self):
        self.head = SkiplistNode(-1)
        self.level = 0

    def search(self, target: int) -> bool:
        curr = self.head
        for i in range(self.level - 1, -1, -1):
            # 找到第 i 层小于且最接近 target 的元素
            while curr.forward[i] and curr.forward[i].val < target:
                # forward[i]是一个一个链表，跳跃指向下一个。但是每一个数据都会有level个空间
                curr = curr.forward[i]
        # i是应该循环到0的，这里保证不发生意外,上边判断条件没有等号。最后一行的下一个才可能相等，不相等说明找不到
        curr = curr.forward[0]
        # 检测当前元素的值是否等于 target
        return curr is not None and curr.val == target

    def add(self, num: int) -> None:
        # 有max_level列，所以需要记住插入列的每一个的前一节点
        update = [self.head] * MAX_LEVEL
        curr = self.head
        for i in range(self.level - 1, -1, -1):
            # 找到第 i 层小于且最接近 num 的元素
            while curr.forward[i] and curr.forward[i].val < num:
                curr = curr.forward[i]
            update[i] = curr
        lv = random_level()
        self.level = max(self.level, lv)
        new_node = SkiplistNode(num, lv)
        for i in range(lv):  # 从下往上更新
            # 对第 i 层的状态进行更新，将当前元素的 forward 指向新的节点
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def erase(self, num: int) -> bool:
        update = [None] * MAX_LEVEL
        curr = self.head
        for i in range(self.level - 1, -1, -1):
            # 找到第 i 层小于且最接近 num 的元素
            while curr.forward[i] and curr.forward[i].val < num:
                curr = curr.forward[i]
            update[i] = curr
        curr = curr.forward[0]
        if curr is None or curr.val != num:  # 值不存在
            return False
        for i in range(self.level):
            if update[i].forward[i] != curr:
                break
            # 对第 i 层的状态进行更新，将 forward 指向被删除节点的下一跳
            update[i].forward[i] = curr.forward[i]
        # 更新当前的 level
        while self.level > 1 and self.head.forward[self.level - 1] is None:
            self.level -= 1
        return True

class SkiplistNode1:
    def __init__(self, val, maxlevel):
        self.val = val
        self.next = [None]*maxlevel

class Skiplist1:
    """
    自己复现
    """
    def __init__(self):
        self.level = 0  # 表示当前跳表的最大层次
        self.head = SkiplistNode1(-1, MAX_LEVEL)

    def serach(self, target):
        p = self.head
        for i in range(self.level-1, -1, -1):
            while p.next[i] and p.next[i].val < target:
                p = p.next[i]
        p = p.next[0]
        return p and p.val == target

    def insert(self, target):
        update = [self.head]*MAX_LEVEL
        p = self.head
        for i in range(self.level-1, -1, -1):
            while p.next[i] and p.next[i].val < target:
                p = p.next[i]
            update[i] = p
        lv = random_level()
        self.level = max(lv, self.level)
        new_node = SkiplistNode1(target, lv)
        for i in range(lv):
            new_node.next[i] = update[i].next[i]
            update[i].next[i] = new_node

    def erase(self, target):
        update = [self.head]*MAX_LEVEL
        p = self.head
        for i in range(self.level-1, -1, -1):
            while p.next[i] and p.next[i].val < target:
                p = p.next[i]
            update[i] = p
        p = p.next[0]
        if not p and p.val != target:
            return False
        for i in range(self.level):
            if update[i].next[i] != p:
                break
            update[i].next[i] = p.next[i]
        # self.level = 1时成为单链表，当最顶层的头节点下一个为空时，层次减一
        while self.level > 1 and not self.head.next[self.level-1]:
            self.level -= 1
        return True


class Skiplist3:
    """
    回家等通知的写法：这他妈单纯为了满足True or False
    """
    def __init__(self):
        self.dct = {}

    def search(self, target: int) -> bool:
        return self.dct.get(target, 0) != 0

    def add(self, num: int) -> None:
        self.dct[num] = self.dct.get(num, 0) + 1
        return

    def erase(self, num: int) -> bool:
        if self.dct.get(num, 0) == 0:
            return False
        self.dct[num] -= 1
        return True


if __name__ == '__main__':
    r1 = [ "add", "add", "add", "add", "add", "add", "add", "add", "add", "erase", "search", "add", "erase",
     "erase", "erase", "add", "search", "search", "search", "erase", "search", "add", "add", "add", "erase", "search",
     "add", "search", "erase", "search", "search", "erase", "erase", "add", "erase", "search", "erase", "erase",
     "search", "add", "add", "erase", "erase", "erase", "add", "erase", "add", "erase", "erase", "add", "add", "add",
     "search", "search", "add", "erase", "search", "add", "add", "search", "add", "search", "erase", "erase", "search",
     "search", "erase", "search", "add", "erase", "search", "erase", "search", "erase", "erase", "search", "search",
     "add", "add", "add", "add", "search", "search", "search", "search", "search", "search", "search", "search",
     "search"]
    r2 = [ [16], [5], [14], [13], [0], [3], [12], [9], [12], [3], [6], [7], [0], [1], [10], [5], [12], [7], [16], [7],
     [0], [9], [16], [3], [2], [17], [2], [17], [0], [9], [14], [1], [6], [1], [16], [9], [10], [9], [2], [3], [16],
     [15], [12], [7], [4], [3], [2], [1], [14], [13], [12], [3], [6], [17], [2], [3], [14], [11], [0], [13], [2], [1],
     [10], [17], [0], [5], [8], [9], [8], [11], [10], [11], [10], [9], [8], [15], [14], [1], [6], [17], [16], [13], [4],
     [5], [4], [17], [16], [7], [14], [1]]
    table = Skiplist1()
    for i in r1:
        res = table
    print()
