"""
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
Note:
The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].

"""


class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if tasks is None or n is None or len(tasks) == 0: return -1
        if n == 0: return len(tasks)
        hashTable = [0] * 26
        intervals = []
        for char in tasks:
            hashTable[ord(char)-ord('A')] += 1

        def notFinished(array):
            for item in array:
                if item > 0:
                    return True
            return False

        def findMostElementInCurrentHashTable(array):
            most = max(array)
            key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            for char in key:
                if array[ord(char) - ord("A")] == most:
                    return char

        while notFinished(hashTable) == True:
            coolDown = n
            hashSet = set()
            majorTask = findMostElementInCurrentHashTable(hashTable)
            
