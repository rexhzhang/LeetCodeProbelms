"""
Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

Example :

Input: [1,2,3]
Output: [1,2,4]
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        
        l1  = self._reverse(head)
        l2 = ListNode(1)
        
        return self._reverse(self.addLists(l1, l2))
        
    
    def addLists(self, h1, h2):
        d = ListNode(0)
        cur = d
        carry = 0
        
        while h1 or h2 or carry:
            
            if h1:
                carry += h1.val
                h1 = h1.next
            
            if h2:
                carry += h2.val
                h2 = h2.next
            
            cur.next = ListNode(carry % 10)
            carry //= 10
            cur = cur.next
        
        return d.next
    
    
    def _reverse(self, head: ListNode) -> ListNode:
        
        if not head or not head.next:
            return head
        
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        
        return prev
            
        