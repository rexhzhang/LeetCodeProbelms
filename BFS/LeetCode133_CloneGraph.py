"""
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

1 ----- 2
|       |
|       |
4 ------3
 

Example:



Input:
{"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}

Explanation:
Node 1's value is 1, and it has two neighbors: Node 2 and 4.
Node 2's value is 2, and it has two neighbors: Node 1 and 3.
Node 3's value is 3, and it has two neighbors: Node 2 and 4.
Node 4's value is 4, and it has two neighbors: Node 1 and 3.
 

Note:

The number of nodes will be between 1 and 100.
The undirected graph is a simple graph, which means no repeated edges and no self-loops in the graph.
Since the graph is undirected, if node p has node q as neighbor, then node q must have node p as neighbor too.
You must return the copy of the given node as a reference to the cloned graph.

"""
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
from collections import deque

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        # 第一步：找到所有的点
        # 第二步：复制所有的点，将映射关系存起来
        # 第三步：找到所有的边，复制每一条边
        
        if not node:
            return None
        
        root = node
        
        # old_nodes是包含所有old nodes 的hash set
        old_nodes = self.BFS(node)
        
        # mapping stores the old -> new relationship
        mapping = {}
        
        for n in old_nodes:
            mapping[n] = Node(n.val, [])
        
        for n in old_nodes:
            for neighbor in n.neighbors:
                mapping[n].neighbors.append(mapping[neighbor])
        
        return mapping[root]
        

    def BFS(self, node):
        result = set([node])
        q = deque([node])
        
        while q:
            
            v = q.popleft()
            for e in v.neighbors:
                if e not in result:
                    result.add(e)
                    q.append(e)
        
        return result