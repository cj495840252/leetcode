"""
链表类：包含两个方法
    1.实现链表的构造
    2.打印链表的值
"""
import logging
import traceback


class ListNode:
    def __init__(self, val=0, next=None, low=None):
        self.val = val
        self.next = next

    @classmethod
    def createLink(cls, node):
        head = ListNode(node[0])
        p = head
        for i in node[1:]:
            new_node = ListNode(val=i, next=None)
            p.next = new_node
            p = p.next
        return head

    @classmethod
    def printLink(cls, head, end="   "):
        """
        head：头节点
        end: 每个输出后的分割符
        """
        try:
            p = head
            while True:
                if p:
                    print(p.val, end=end)
                    p = p.next
                else:
                    break
        except Exception as e:
            logging.error(traceback.format_exc())

    @classmethod
    def mergeTwoLists(cls, head1, head2):
        """
        官方方法2：迭代
        """
        prehead = ListNode(-1)  # 创建头节点保存结果
        prev = prehead
        while head1 and head2:
            if head1.val <= head2.val:
                prev.next = head1
                head1 = head1.next
            else:
                prev.next = head2
                head2 = head2.next
            prev = prev.next
        # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
        prev.next = head1 if head1 is not None else head2
        return prehead.next