"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if not head or not head.next:
            return True
        
        mid = self._findMiddle(head)
        
            
        l2 = self._reverse(mid.next)
        l1 = head
        while l1 and l2:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next
        
        return l2 == None
        
        
    def _findMiddle(self, head):
        
        if not head or not head.next:
            return head
        
        slow, fast = head, head.next
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        return slow
        
    def _reverse(self, node):
        prev = None
        
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        
        return prev