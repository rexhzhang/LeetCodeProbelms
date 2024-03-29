"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head: 
            return
        
        lt = ListNode(0)
        gt = ListNode(0)
        
        lcur = lt
        gcur = gt
        
        while head:
            if head.val < x:
                lcur.next = head
                lcur = lcur.next
                head = head.next
            else:
                gcur.next = head
                gcur = gcur.next
                head = head.next
        
        lcur.next = gt.next
        gcur.next = None
        return lt.next
        