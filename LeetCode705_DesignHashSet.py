"""
Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

add(value): Insert a value into the HashSet. 
contains(value) : Return whether the value exists in the HashSet or not.
remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

Example:

MyHashSet hashSet = new MyHashSet();
hashSet.add(1);         
hashSet.add(2);         
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);          
hashSet.contains(2);    // returns true
hashSet.remove(2);          
hashSet.contains(2);    // returns false (already removed)

Note:

All values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashSet library.
"""

class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = 1000
        self.h = [None] * self.m

    def add(self, key: int) -> None:
        """
        Add item to the hashset
        """
        index = key % self.m
        if self.h[index] == None:
            self.h[index] = ListNode(key)
        else:
            cur = self.h[index]
            while True:
                if cur.key == key:
                    return
                if cur.next == None:
                    break
                cur = cur.next
            cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        """
        Removes the key from the hashset
        """
        index = key % self.m
        cur = prev = self.h[index]
        if cur == None:
            return
        elif cur.key == key:
            self.h[index] = cur.next
        else:
            cur = cur.next
        
            while cur:
                if cur.key == key:
                    prev.next = cur.next
                    return
                else:
                    cur, prev = cur.next, prev.next

        return
    

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        index = key % self.m
        cur = self.h[index]
        while cur:
            if cur.key == key:
                return True
            else:
                cur = cur.next

        return False 

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
