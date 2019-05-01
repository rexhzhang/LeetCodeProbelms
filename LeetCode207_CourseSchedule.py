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
import collections


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        if numCourses > 0 and len(prerequisites) == 0:
            return True

        q = collections.deque([])
        hashMap = collections.defaultdict(int)

        for pair in prerequisites:
            hashMap[pair[0]] += 1

        for i in range(numCourses):
            if hashMap.get(i) is None:
                q.append(i)

        if len(q) == 0: return False

        topologicalOrder = []

        while q:
            course = q.popleft()
            topologicalOrder.append(course)
            for pair in prerequisites:
                if pair[1] == course:
                    hashMap[pair[0]] -= 1
                    if hashMap[pair[0]] == 0:
                        q.append(pair[0])

        return len(topologicalOrder) == numCourses