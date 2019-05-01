"""
In a given 2D binary array A, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)

 

Example 1:

Input: [[0,1],[1,0]]
Output: 1


Example 2:

Input: [[0,1,0],[0,0,0],[0,0,1]]
Output: 2


Example 3:

Input: [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
 

Note:

1 <= A.length = A[0].length <= 100
A[i][j] == 0 or A[i][j] == 1
"""
from collections import deque

class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        if len(A) == 0 or len(A[0]) == 0: return -1
        
        row, column = len(A), len(A[0])
        visited = False
        for i in range(row):
            for j in range(column):
                
                if A[i][j] == 1 and visited:
                    return self.search(A, i, j)

                if A[i][j] == 1:
                    self.flip(A, i, j)
                    visited == True
                
    
    def flip(self, A, row, column):
        
        q = deque([(row, column)])

        while q:
            x, y = q.popleft()
            A[x][y] = 'X'
            if x-1 >= 0  and A[x-1][y] == 1:
                q.append((x-1, y))
                A[x-1][y] = 'X'
            if y-1 >= 0  and A[x][y-1] == 1:
                q.append((x, y-1))
                A[x][y-1] = 'X'
            if x+1 < len(A) and A[x+1][y] == 1:
                q.append((x+1, y))
                A[x+1][y] = 'X'
            if y+1 < len(A[0]) and A[x][y+1] == 1:
                q.append((x, y+1))
                A[x][y+1] = 'X'
        
    def search(self, A, row, column):

        q = deque([(row, column)])
        visited = set((row, column))

        while q:
            x, y = q.popleft()
        
            if x-1 >= 0 and  A[x-1][y] == 1 and (x-1, y) not in visited:
                q.append((x-1, y))
                visited.add((x-1, y))
                
            if y-1 >= 0  and A[x][y-1] == 1 and (x, y-1) not in visited:
                q.append((x, y-1))
                visited.add((x, y-1))

            if x+1 < len(A) and A[x+1][y] == 1 and (x+1, y) not in visited:
                q.append((x+1, y))
                visited.add((x+1, y))

            if y+1 < len(A[0]) and A[x][y+1] == 1 and (x, y+1) not in visited:
                q.append((x, y+1))
                visited.add((x, y+1))
        
        q = deque(visited)
        visited = set()
        d = 0
        while q:
            
            d += 1
            next_around = deque([])
            
            while q:
                x, y = q.popleft()
                if x-1 >= 0 and (x-1, y) not in visited:
                    if A[x-1][y] == 'X':
                        return d 
                    next_around.append((x-1, y))
                    visited.add((x-1, y))
                    
                if y-1 >= 0  and (x, y-1) not in visited:
                    if A[x][y-1] == 'X':
                        return d
                    next_around.append((x, y-1))
                    visited.add((x, y-1))

                if x+1 < len(A) and (x+1, y) not in visited:
                    if A[x+1][y] == 'X':
                        return d 
                    next_around.append((x+1, y))
                    visited.add((x+1, y))

                if y+1 < len(A[0]) and (x, y+1) not in visited:
                    if A[x][y+1] == 'X':
                        return d 
                    next_around.append((x, y+1))
                    visited.add((x, y+1))

            q = next_around