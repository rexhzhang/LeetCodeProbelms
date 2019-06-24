"""
We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
 

Note:

The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict, deque

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        
        graph = defaultdict(set)
        self.connect(None, root, graph)
        
        q = deque([target])
        visited = set([target])
        
        current = 0
        while q:
            next_level = deque()
            
            if current == K:
                break
            while q:
                node = q.popleft()
                
                for n in graph[node]:
                    if n not in visited:
                        next_level.append(n)
                        visited.add(n)
            
            q = next_level
            current += 1
        return [node.val for node in q]
        
        
    def connect(self, parent, node, graph):
        
        if not node:
            return
        
        if parent and node:
            graph[parent].add(node)
            graph[node].add(parent)
        
        self.connect(node, node.left,  graph)
        self.connect(node, node.right, graph)