"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""

class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        """
        dict[key:int] = value: ListNode
        用dict的长度来判断长度 
        """
        self.capacity = capacity
        self.dict = {}
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def __add(self, node) -> None:
        """
        Add a node to the front of the Doubly Linked List
        """
        n = self.head.next
        p = self.head
        node.next = n
        node.prev = p
        p.next = node
        n.prev = node

    def __remove(self, node):
        """
        Remove a node from the Doubly LinkedL List
        """
        n = node.next
        p = node.prev
        p.next = n
        n.prev = p

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        node = self.dict[key]
        self.__remove(node)
        self.__add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.__remove(self.dict[key])
            node = ListNode(key, value)
            self.__add(node)
            self.dict[key] = node
            return
        else:
            node = ListNode(key, value)
            self.dict[key] = node
            self.__add(node)
            if len(self.dict) > self.capacity:
                del self.dict[self.tail.prev.key]
                self.__remove(self.tail.prev)
                
            return


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)