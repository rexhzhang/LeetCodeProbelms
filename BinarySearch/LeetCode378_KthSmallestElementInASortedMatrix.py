"""
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n2.

"""
import heapq


class Solution(object):

    def kthSmallest_BinarySearch(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        

    def kthSmallest_heap(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        row, column = len(matrix), len(matrix[0])
        visited = [[False] * row for _ in range(column)]
        visited[0][0] = True
        queue = [(matrix[0][0], 0, 0)]

        result = None

        for _ in range(k):
            result, i, j = heapq.heappop(queue)
            if i + 1 < row and not visited[i + 1][j]:
                visited[i + 1][j] = True
                heapq.heappush(queue, (matrix[i + 1][j], i + 1, j))

            if j + 1 < row and not visited[i][j + 1]:
                visited[i][j + 1] = True
                heapq.heappush(queue, (matrix[i][j + 1], i, j + 1))

        return result