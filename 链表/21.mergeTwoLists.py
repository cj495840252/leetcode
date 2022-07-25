"""
21. 合并两个有序链表
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
"""
from typing import Optional
from DateType.ClassListNode import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p = list1
        q = list2
        if not p:
            return q
        if not q:
            return p
        if p.val > q.val:  # 保证p节点开头为最小的，最后返回p所在头节点
            p, q = q, p
            list1 = p
        while True:
            if p.next and q:
                if p.next.val <= q.val:
                    p = p.next
                else:
                    last = q
                    q = q.next
                    last.next = p.next
                    p.next = last
            elif q:
                p.next = q
                q = None
            else:
                break
        return list1


    def mergeTwoLists1(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        官方方法：递归
        """
        if list1:
            return list2
        elif list2:
            return list1
        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists1(list1.next,list2)
        else:
            list2.next = self.mergeTwoLists1(list2,list2.next)
            return list2

    def mergeTwoLists2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        官方方法2：迭代
        """
        prehead = ListNode(-1)  # 创建头节点保存结果
        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
        prev.next = l1 if l1 is not None else l2
        return prehead.next


if __name__ == '__main__':
    l1 = [1, 2, 4, 5, 6, 7, 19, 20]
    l2 = [1, 3, 4, 3.5, 100]
    node_l1 = ListNode.createLink(l1)
    node_l2 = ListNode.createLink(l2)
    s = Solution()
    res = s.mergeTwoLists(node_l1, node_l2)
    ListNode.printLink(head=res, end=" ==> ")
    print("****"*5)
