"""
Given a list, rotate the list to the right by k places, where k is non-negative.


Example:

Given 1->2->3->4->5->NULL and k = 2,

return 4->5->1->2->3->NULL.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or k is None: return "Invalid Input"

        def getLen(node):
            length = 0
            while node:
                length += 1
                node = node.next

            return length


        length = getLen(head)
        k = k % length
        if k == length: return head

        counter = length - k
        current = head

        while current:

            while counter > 1:
                current = current.next
                counter -= 1
                if counter == 1:
                    newHead = current.next
                    current.next = None

            current = newHead
            if current.next is None:
                break

        current.next = head

        return newHead