"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .
Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites
"""


from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # Topological sort problem, return one of the possible order, if all of the possible order -> Word Ladder 2
        # 要点 有向图
        # 建立degrees 和 edges 记录入度和neighbors， 注意neighbors里 key是requirement value是course，便于反向搜索
        
        edges = {i:[] for i in range(numCourses)}
        degrees = [0 for _ in range(numCourses)]
        
        for course, requirement in prerequisites:
            edges[requirement].append(course)
            degrees[course] += 1
            
        
        q = deque([i for i in range(len(degrees)) if degrees[i] == 0])
        correct_order = []
        
        while q:
            
            current = q.popleft()
            correct_order.append(current)
            
            for c in edges[current]:
                degrees[c] -= 1
                if degrees[c] == 0:
                    q.append(c)
            
        
        return correct_order if len(correct_order) == numCourses else []
        
            