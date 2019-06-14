"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

 Notice

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Have you met this question in a real interview? Yes
Example
Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.
"""

"""
Solution:
条件1：刚好N-1条边 条件2：N个点连通
"""
from collections import defaultdict, deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # 一个图是树需要满足两个条件：
        # 1. N个点只能有N-1条边
        # 2. N 个点互相连通
        
        if n -1 != len(edges):
            return False
        
        # 用字典表示关系
        neighbors = defaultdict(list)
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)
        
        visited = set()
        visited.add(0)
        q = deque([0])
        
        while q:
            node = q.popleft()
            
            for neighbor in neighbors[node]:
                if neighbor not in visited:
                    q.append(neighbor)
                    visited.add(neighbor)
        

        return len(visited) == n