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

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        d = ListNode(0)
        d.next = head
        head = d
        
        while True:
            
            head = self._reverseK(head, k)
            if not head:
                break
        
        return d.next
    
    # head -> n1 -> n2 ... nk -> nk+1
    # head -> nk - nk-1 ... n1 -> nk + 1
    # return n1
    def _reverseK(self, head, k):
        nk = head
        for _ in range(k):
            if not nk:
                return None
            nk = nk.next
        
        if not nk: return None
        
        # Reverse
        n1 = head.next # head is dummy
        nk_next = nk.next
        prev = None
        cur = n1
        
        while cur != nk_next:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        

        # connect
        head.next = nk
        n1.next = nk_next
        
        return n1
        