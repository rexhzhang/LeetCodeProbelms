"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

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
     def __init__(self, k, v):
         self.key = k
         self.value = v
         self.prev = None
         self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity =capacity
        self.dic = dict()
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
            self._add(n)
            return n.value   
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self._remove(self.dic[key])
        n = ListNode(key, value)
        self._add(n)
        self.dic[key] = n
        if len(self.dic) > self.capacity:
            n = self.tail.prev
            self._remove(n)
            self.dic.pop(n.key, None)

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
    
    def _add(self, node):
        n = self.head.next
        n.prev = node
        self.head.next = node
        node.next = n
        node.prev = self.head

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)