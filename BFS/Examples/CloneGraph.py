"""
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.

How we serialize an undirected graph:

Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.

As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

   1
  / \
 /   \
0 --- 2
     / \
     \_/
"""


class Solution:
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """

    def cloneGraph(self, node):
        # write your code here
        root = node
        if node is None:
            return None

        def BFS(node):
            q = [node]
            result = set([node])
            while q:
                current = q.pop(0)
                for neighbour in node.neighbors:
                    if neighbour not in result:
                        result.add(neighbour)
                        q.append(neighbour)

            return result

            """
            q = collections.deque([node])
            result = set([node])
            while q:
                head = q.popleft()
                for neighbor in head.neighbors:
                    if neighbor not in result:
                        result.add(neighbor)
                        q.append(neighbor)
            return result
            """

        # use bfs algorithm to traverse the graph and get all nodes.
        nodes = BFS(node)

        relationMap = {}
        for node in nodes:
            relationMap[node] = UndirectedGraphNode(node.label)

        for node in nodes:
            new_node = relationMap[node]
            for neighbour in node.neighbors:
                new_neighbour = relationMap[neighbour]
                new_node.neighbors.append(new_neighbour)

        return relationMap[root]

