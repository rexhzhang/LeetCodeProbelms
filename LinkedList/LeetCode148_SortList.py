"""
Sort a linked list in O(n log n) time using constant space complexity.

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 用快慢指针把linked list拆成两部分，再使用merge sort
        if not head or not head.next:
            return head
        
        mid = self.findMiddle(head)
        right = self.sortList(mid.next) # 之所以要recursion 是因为拆分出的两个链表并不是sorted
        mid.next = None
        left = self.sortList(head)
        
        return self.merge(right, left)
        
    def merge(self, head1, head2):
        # 只是merge，assume 两个链表都是sorted
        d = ListNode(0)
        tail = d
        
        while head1 and head2:
            if head1.val < head2.val:
                tail.next = head1
                head1 = head1.next
                tail = tail.next
            else:
                tail.next = head2
                head2 = head2.next
                tail = tail.next
        
        if not head1:
            tail.next = head2
        else:
            tail.next = head1
            
        return d.next
        
        
    def findMiddle(self, head):
        slow,fast = head, head.next
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        return slow