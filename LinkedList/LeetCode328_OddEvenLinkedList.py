"""Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are
talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 方法一: 不区分odd 和 even， 只是把even接到odd最后
        prev = head
        first = head.next

        while first and first.next:
            second = first.next
            first.next = second.next
            second.next = prev.next
            prev.next = second
            first = first.next
            prev = prev.next

        return head

    def oddEvenList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 方法二：分开odd, even
        dummy1 = odd = ListNode(0)
        dummy2 = even = ListNode(0)

        while head:
            odd.next = head
            even.next = head.next
            odd = odd.next
            even = even.next
            head = head.next.next if even else None

        odd.next = dummy2.next
        return dummy1.next