"""
641. 设计循环双端队列
设计实现双端队列。

实现 MyCircularDeque 类:

MyCircularDeque(int k) ：构造函数,双端队列最大为 k 。
boolean insertFront()：将一个元素添加到双端队列头部。 如果操作成功返回 true ，否则返回 false 。
boolean insertLast() ：将一个元素添加到双端队列尾部。如果操作成功返回 true ，否则返回 false 。
boolean deleteFront() ：从双端队列头部删除一个元素。 如果操作成功返回 true ，否则返回 false 。
boolean deleteLast() ：从双端队列尾部删除一个元素。如果操作成功返回 true ，否则返回 false 。
int getFront() )：从双端队列头部获得一个元素。如果双端队列为空，返回 -1 。
int getRear() ：获得双端队列的最后一个元素。 如果双端队列为空，返回 -1 。
boolean isEmpty() ：若双端队列为空，则返回 true ，否则返回 false  。
boolean isFull() ：若双端队列满了，则返回 true ，否则返回 false 。

"""

# 双端循环队列，数组实现
class MyCircularDeque:

    def __init__(self, k: int):
        self.queue =  [0]*(k+1)
        self.front = 0
        self.tail = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.front = (self.front - 1) % len(self.queue)
            self.queue[self.front] = value
            return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.queue[self.tail] = value
            self.tail = (self.tail + 1)%len(self.queue)
            return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.queue[self.front] = 0
            self.front = (self.front+1) % len(self.queue)
            return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.tail = (self.tail - 1) % len(self.queue)
            self.queue[self.tail] = 0
            return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[(self.tail-1)%len(self.queue)]

    def isEmpty(self) -> bool:
        if self.front == self.tail:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.front == (self.tail+1)%len(self.queue):
            return True
        else:
            return False

if __name__ == '__main__':
    circularDeque = MyCircularDeque(3)
    res1 = circularDeque.insertLast(1)  # 返回true
    res2 = circularDeque.insertLast(2)  # 返回true
    res3 = circularDeque.insertFront(3)  # 返回true
    res4 = circularDeque.insertFront(4)
    res5 = circularDeque.getRear()  # 返回 2
    res6 = circularDeque.isFull()  # 返回 true
    res7 = circularDeque.deleteLast()  # 返回 true
    res8 = circularDeque.insertFront(4)  # 返回 true
    res9 = circularDeque.getFront()
    print(res1)
    print(res2)
    print(res3)
    print(res4)
    print(res5)
    print(res6)
    print(res7)
    print(res8)
    print(res9)





