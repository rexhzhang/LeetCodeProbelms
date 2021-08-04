"""
For an undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1 :

Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3 

Output: [1]
Example 2 :

Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5 

Output: [3, 4]
Note:

According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”
The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
"""

from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        """
        用拓扑排序即可
        首先我们将所有的叶子节点都放入队列中
        之后每次有点从队列中出来，就将和这个点相邻的没有入队过的点加入到队列中
        容易想到，答案的数量最多不超过两个，所以只要比较最后两个出队的点即可
        """

        # Tree: number of edges must == n-1
        if len(edges) != n-1:
            return []

         
        Neighbors = {i: set() for i in range(n)}
        
        for u, v in edges:
            Neighbors[u].add(v)
            Neighbors[v].add(u)
        
        leaf = [i for i in range(n) if len(Neighbors[i]) == 1]
        
        count = n
        
        while count > 2:
            new_leaf = []
            count -= len(leaf)
            
            while leaf:
                leaf_node = leaf.pop()
                
                for node in Neighbors[leaf_node]:
                    Neighbors[node].remove(leaf_node)
                    if len(Neighbors[node]) == 1:
                        new_leaf.append(node)
                
                del Neighbors[leaf_node]
        
            leaf = new_leaf
        
        return list(Neighbors.keys())