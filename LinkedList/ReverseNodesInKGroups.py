"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.
Only constant memory is allowed.

Example
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""

class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None


class Solution:
    """
    @param: head: a ListNode
    @param: k: An integer
    @return: a ListNode
    """
    def reverseKGroup(self, head, k):
        # write your code here
        dummy = ListNode(0)
        dummy.next = head
        head = dummy

        while True:
            head = self.reverseK(head, k)
            if head == None:
                break

        return dummy.next

    # head -> n1 -> n2...nk -> nk + 1
    # = >
    # head -> nk -> nk - 1..n1 -> nk + 1
    # return n1

    def reverseK(self, head, k):
        # 找到第k个node
        nk = head
        for i in range(k):
            if nk == None:
                return None
            nk = nk.next

        if nk == None:
            return None

        # Reverse
        n1 = head.next
        nkplus = nk.next

        prev = None
        current = n1

        while current != nkplus:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        head.next = nk
        n1.next = nkplus

        return n1