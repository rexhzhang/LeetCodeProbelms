"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""

from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        
        degrees = [0 for _ in range(numCourses)]
        edges = defaultdict(list)

        for c, req in prerequisites:
            degrees[c] += 1
            edges[req].append(c)
        
        q = deque([])

        for i in range(len(degrees)):
            if degrees[i] == 0:
                q.append(i)

        count = 0
        while q:
            course = q.popleft()
            count += 1

            for node in edges[course]:

                degrees[node] -= 1
                if degrees[node] == 0:
                    q.append(node)
        
        return count == numCourses
            

