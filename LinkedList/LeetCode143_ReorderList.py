"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.


"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        # 思路：
        # 1. 找中间点
        # 2. 反转后半个list
        # 3. 构造list
        if head is None: return None
        mid = self.findMid(head)
        l2 = mid.next
        mid.next = None
        l2 = self.reverseList(l2)
        l1 = head

        # L0→Ln→L1→Ln - 1→L2→Ln - 2→…
        while l1 and l2:
            next = l1.next
            l1.next = l2
            l2 = l2.next
            l1.next.next = next
            l1 = next

        return head

    # linkedlist 找中间点
    def findMid(self, node):

        slow, fast = node, node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow

    # reverse linkedlist
    def reverseList(self, head):
        newHead = None

        while head:
            next = head.next
            head.next = newHead
            newHead = head
            head = next

        return newHead