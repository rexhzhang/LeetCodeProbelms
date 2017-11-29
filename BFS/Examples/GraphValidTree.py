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
    """
    @param: n: An integer
    @param: edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        if len(edges) != n - 1: return False
        neighbours = defaultdict(list)
        for u, v in edges:
            neighbours[u].append(v)
            neighbours[v].append(u)

        visited = set()
        q = deque([0])
        while q:
            node = q.popleft()
            visited.add(node)
            for neighbour in neighbours[node]:
                if neighbour not in visited:
                    q.append(neighbour)
                    visited.add(neighbour)

        return len(visited) == n
