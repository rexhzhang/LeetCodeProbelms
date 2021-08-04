# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


"""
Given 1->2->3->4->5->NULL, m = 2 and n = 4, 
return 1->4->3->2->5->NULL.
解答：
1. 创建Dummynode 录下head.
2. 找到m的前节点Pre（这样做是为了方便用插入法reverse linkedlist）
3. 记录下Pre的下一个节点 reverseTail，它将会是Reversed link的尾部。
4. 翻转指定区间的链表，翻到最后一个节点时，把reverseTail.next指向它的next。这样就把翻转链表与之后
的链表接起来了。

5. 返回dummynode的下一个节点。
"""

class Solution(object):
    def reverseBetween(self, head, m, n):
        if m == n or head is None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        head = dummy # now the dummy node becomes the index zero
        for i in range(1, m):
            if head is None:
                return None
            head = head.next
        if head is None:
            return None
        mNodePreviousNode = head
        mNode = head.next
        nNode = mNode
        nNodePostNode = nNode.next

        for i in range(m, n):
            if nNodePostNode == None:
                return None
            temp = nNodePostNode.next
            nNodePostNode.next = nNode
            nNode = nNodePostNode
            nNodePostNode = temp

        mNodePreviousNode.next = nNode
        mNode.next = nNodePostNode

        return dummy.next

    def reverseBetweenII(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        Dummy = ListNode(0)
        Dummy.next = head
        Current = Dummy
        counter = 0

        # Exit While loop when current is pointing to node m-1
        while counter < m-1 and Current.next:
            Current = Current.next
            counter += 1

        OneNodeBeforeBreakUpNode = Current
        Current = Current.next
        BreakUpNode = Current
        counter += 1

        if Current.next:
            NextNodeOfCurrent = Current.next
            NextNextNodeOfCurrent = Current.next.next
        else:
            print("Current.next is None")

        while counter < n - 1:
            NextNodeOfCurrent.next = Current
            Current = NextNodeOfCurrent
            NextNodeOfCurrent = NextNextNodeOfCurrent
            NextNextNodeOfCurrent = NextNextNodeOfCurrent.next
            counter += 1

        OneNodeBeforeBreakUpNode.next = Current
        BreakUpNode.next = NextNodeOfCurrent

        if m == 1:
            return OneNodeBeforeBreakUpNode.next
        return Dummy.next

    