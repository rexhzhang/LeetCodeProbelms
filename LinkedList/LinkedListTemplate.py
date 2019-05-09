class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Template:
    
    def findMiddle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        slow, fast = head, head.next

        while head and head.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow


    def _reverse(self, head):
        prev = None

        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        
        return prev
    
    
    def addTwoList(self, h1, h2):
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
            
            cur.next  = ListNode(carry % 10)
            cur = cur.next
            carry //= 10
        
        return d.next