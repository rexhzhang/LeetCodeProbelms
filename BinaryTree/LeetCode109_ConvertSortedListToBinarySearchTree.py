"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        O(nlogn) Time, O(log n) stack space

        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None: return None

        def helper(head, tail):
            if head == tail: return None
            walker, runner = head, head
            while runner != tail and runner.next != tail:
                walker = walker.next
                runner = runner.next.next

            root = TreeNode(walker.val)
            root.left = helper(head, walker)
            root.right = helper(walker.next, tail)
            return root
        return helper(head, None)

    def sortedListToBST2(self, head):
        """
        O(n) Time, O(log n) stack space
        :type head: ListNode
        :rtype: TreeNode
        """

        end = 0
        p = head

        while p:
            p = p.next
            end += 1
        self.dummy = head
        root = self.helper(0, end - 1)

        return root

    def helper(self, start, end):
        if start > end:
            return None
        mid = (start + end) / 2
        leftChild = self.helper(start, mid - 1)
        parent = TreeNode(self.dummy.val)
        self.dummy = self.dummy.next
        parent.left = leftChild
        parent.right = self.helper(mid + 1, end)
        return parent
