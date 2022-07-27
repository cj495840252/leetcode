"""
206. 反转链表

给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
"""
from DataType.ClassListNode import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        p = head
        q = head
        while p.next:
            p = p.next
        while q != p:
            t = q
            q = q.next
            t.next = p.next
            p.next = t
        return p

    def reverseList1(self, head: ListNode) -> ListNode:
        """
        迭代
        """
        if not head or head.next:
            return head
        p = head
        q = head.next
        p.next = None
        while q.next:
            t = q.next
            q.next = p
            p = q
            q = t
        q.next = p
        return q

    def reverseList2(self, head: ListNode) -> ListNode:
        """
        递归
        """
        if head or head.next:
            return head
        new_head = self.reverseList2(head.next)
        head.next.next = head
        head.next = None
        return new_head


if __name__ == '__main__':
    res = ListNode.createLink([1, 2, 3, 4, 5])
    ListNode.printLink(res)
    print()
    s = Solution().reverseList2(res)
    ListNode.printLink(s)
