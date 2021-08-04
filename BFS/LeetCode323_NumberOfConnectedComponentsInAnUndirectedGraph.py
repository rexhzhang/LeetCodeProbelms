"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), 
write a function to find the number of connected components in an undirected graph.

Example 1:

Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4 

Output: 2
Example 2:

Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output:  1
Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, 
[0, 1] is the same as [1, 0] and thus will not appear together in edges.
"""
from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # 1.建立一个字典，记录无向图的边
        # 2. 遍历每个点并BFS，用集记录每个点是否被访问

        neighbors = {i:[] for i in range(n)}

        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)
        
        visited = set()
        components = 0

        for i in range(n):
            if i in visited:
                continue
            
            components += 1

            self.search_neighbors(i, neighbors,visited)

        return components

    def search_neighbors(self, node, neighbors, visited):

        q = deque([node])

        while q:

            current = q.popleft()
            visited.add(current)
            for neighbor in neighbors[current]:
                if neighbor not in visited:
                    q.append(neighbor)
                    visited.add(neighbor)

    

                    
