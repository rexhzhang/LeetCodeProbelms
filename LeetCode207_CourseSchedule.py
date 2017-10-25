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