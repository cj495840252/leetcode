"""
622. 设计循环队列
设计你的循环队列实现。 循环队列是一种线性数据结构，其操作表现基于 FIFO（先进先出）原则并且队尾被连接在队首之后以形成一个循环。它也被称为“环形缓冲器”。

循环队列的一个好处是我们可以利用这个队列之前用过的空间。在一个普通队列里，一旦一个队列满了，我们就不能插入下一个元素，即使在队列前面仍有空间。但是使用循环队列，我们能使用这些空间去存储新的值。

你的实现应该支持如下操作：

MyCircularQueue(k): 构造器，设置队列长度为 k 。
Front: 从队首获取元素。如果队列为空，返回 -1 。
Rear: 获取队尾元素。如果队列为空，返回 -1 。
enQueue(value): 向循环队列插入一个元素。如果成功插入则返回真。
deQueue(): 从循环队列中删除一个元素。如果成功删除则返回真。
isEmpty(): 检查循环队列是否为空。
isFull(): 检查循环队列是否已满。
"""


class Node:
    def __init__(self, val=None, last=None, next=None):
        self.val = val
        self.last = last
        self.next = next

# 纯链表实现
class CircularQueue:
    def __init__(self, k: int):
        self.head = Node()
        self.tail = self.head
        p = self.head
        i = 0
        while i < k - 1:
            new_node = Node()
            p.next = new_node
            new_node.last = p
            p = p.next
            i += 1
        p.next = self.head  # 最后p指向head的
        self.head.last = p

    def Front(self):
        if self.isEmpty():
            return -1
        return self.head.val

    def Rear(self):
        if self.isEmpty():
            return -1
        p = self.tail.last
        # self.tail = self.tail.last
        return p.val

    def enQueue(self, value):
        if self.isFull():
            return False
        self.tail.val = value
        self.tail = self.tail.next
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        self.head.val = None
        self.head = self.head.next
        return True

    def isEmpty(self):
        if self.head == self.tail and self.head.val == None:
            return True
        else:
            return False

    def isFull(self):
        if self.tail == self.head and self.head.val != None:
            return True
        else:
            return False

    def printQueue(self):
        p = self.head
        while p.next != self.head:
            print(p.val, end="  ")
            p = p.next
        print(p.val, end="  ")
        print()

class CirQueue:
    def __init__(self, k):
        self.head = 0  # 头指针
        self.tail = 0  # 尾指针
        self.nums = [0]*(k+1)  # 初始化值为0，需要一个空节点

    def enQueue(self, value):
        if self.isFull2():
            return False
        self.nums[self.tail] = value
        self.tail = (self.tail+1)%len(self.nums)
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        self.nums[self.head] = 0
        self.head = (self.head+1)%len(self.nums)
        return True

    def isEmpty(self):
        if self.head == self.tail:
            return True
        else:
            return False

    def isFull(self) -> bool:
        return (self.tail + 1) % len(self.nums) == self.tail

    def isFull2(self) -> bool:
        if (self.tail+1)%(len(self.nums)) == self.head:
            return True
        else:
            return False

    def Front(self):
        if self.isEmpty():
            return -1
        return self.nums[self.head]

    def Rear(self):
        if self.isEmpty():
            return -1
        return self.nums[(self.tail-1)%len(self.nums)]

if __name__ == '__main__':
    obj = CirQueue(3)
    print(obj.enQueue(1))
    print(obj.enQueue(2))
    print(obj.enQueue(3))
    print(obj.enQueue(4))
    print(obj.nums,obj.tail,obj.head)
    print(obj.Rear())
    print(obj.deQueue())
    print(obj.enQueue(4))
    print(obj.Rear())
