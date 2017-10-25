class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        reverseHead = None

        while head:
            current = head
            head = head.next
            current.next = reverseHead
            reverseHead = current

        return reverseHead

    def addTwoNumbers(self, node1, node2):

        if node1 is None and node2 is None:
            raise ValueError("Both nodes do not exist")
        if node1 is None:
            return node2
        if node2 is None:
            return node1

        reversedNode1 = self.reverseList(node1)
        reversedNode2 = self.reverseList(node2)

        dummy = cur = ListNode(0)
        carry = 0
        while reversedNode1 or reversedNode2 or carry:
            if reversedNode1:
                carry += reversedNode1.val
                reversedNode1 = reversedNode1.next
            if reversedNode2:
                carry += reversedNode2.val
                reversedNode2 = reversedNode2.next
            cur.next = ListNode(carry % 10)
            cur = cur.next
            carry //= 10

        return self.reverseList(dummy.next)
