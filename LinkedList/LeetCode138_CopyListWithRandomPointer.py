"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

 

Example 1:



Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null and its random pointer points to itself.
 

Note:

You must return the copy of the given head as a reference to the cloned list.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # same as 133 clone graph
        if not head:
            return None

        old_nodes = []
        cur = head
        while cur:
            old_nodes.append(cur)
            cur = cur.next
        
        # Saves the old -> new relationship
        mapping = {}
        for node in old_nodes:
            mapping[node] = Node(node.val, None, None)
        
        for node in old_nodes:
            if node.next:
                mapping[node].next = mapping[node.next]
            
            if node.random:
                mapping[node].random = mapping[node.random]
        
        return mapping[head]
