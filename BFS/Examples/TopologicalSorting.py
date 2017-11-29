"""
Given an directed graph, a topological order of the graph nodes is defined as follow:

For each directed edge A -> B in graph, A must before B in the order list.
The first node in the order can be any node in the graph with no nodes direct to it.
Find any topological order for the given graph.
"""
"""
Graph
For example:
{1,2,4#2,1,4#3,5#4,1,2#5,3} represents follow graph:
1------2  3
 \     |  | 
  \    |  |
   \   |  |
    \  |  |
      4   5
we use # to split each node information.
1,2,4 represents that 2, 4 are 1's neighbors
2,1,4 represents that 1, 4 are 2's neighbors
3,5 represents that 5 is 3's neighbor
4,1,2 represents that 1, 2 are 4's neighbors
5,3 represents that 3 is 5's neighbor
"""

from collections import deque
# Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbours = []

class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        if graph is None or len(graph) == 0: return []

        topoOrder = []
        hashMap = {}

        """ 生成关系字典 """
        for node in graph:
            for neighbour in node.neighbours:
                hashMap[node] = hashMap.get(node, 0) + 1

        q = deque([])
        """找到入度为0的点，并存入queue中"""
        for node in graph:
            if hashMap.get(node) == None:
                topoOrder.append(node)
                q.append(node)

        """ 开始BFS """
        while q:
            node = q.popleft()

            for neighbour in node.neighbours:
                hashMap[neighbour] -= 1
                if hashMap[neighbour] == 0:
                    q.append(neighbour)
                    topoOrder.append(neighbour)

        return topoOrder