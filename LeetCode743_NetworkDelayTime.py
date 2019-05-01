from collections import deque, defaultdict
"""
There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal 
to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

Note:

N will be in the range [1, 100].
K will be in the range [1, N].
The length of times will be in the range [1, 6000].
All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.
"""
class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u] = [v, w]
        
        time = 0

        q = deque([K])
        visited = set([])
        visited.add(K)        
        while q:
            
            time_this_round = 0
            next_round = deque([])
            while q:
                node = q.popleft()
                if graph[node][0] not in visited:
                    visited.add(graph[node][0])
                    time_this_round = max(time_this_round, graph[node][1])
                    



