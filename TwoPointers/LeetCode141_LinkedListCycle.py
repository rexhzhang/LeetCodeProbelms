"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 同向双指针
        if not head or not head.next:
            return False
        walker, runner = head, head.next
        
        while runner and runner.next:
            walker = walker.next
            runner = runner.next.next
            if walker == runner:
                return True
        
        return False
