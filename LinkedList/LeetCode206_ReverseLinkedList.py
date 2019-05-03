"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Iteratively
        prev = None
        cur = head
        
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        return prev 
    
    
    def reverseList_recursive(self, head: ListNode) -> ListNode:
        # recursively
        return self._reverse(head, None)

    def _reverse(self, cur, prev):
        
        if not cur: return prev
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
        return self._reverse(cur, prev)
        