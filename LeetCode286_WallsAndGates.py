"""
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example: 

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF

After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
"""
from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if len(rooms) == 0 or len(rooms[0]) == 0:
            return
        
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    self.findPath(rooms, i, j)
    
    def findPath(self, rooms: List[List[int]], row: int, column:int):

        q = deque([(row, column)])
        visited = set((row, column))
        movement = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        d = 1
        
        while q:
            next_level = deque([])
            
            
            while q:
                x, y = q.popleft()
                visited.add((x,y))
                for i in range(4):
                    dx, dy = movement[i][0], movement[i][1]
                    if x + dx >=0 and x + dx < len(rooms) and y + dy >= 0 and y + dy < len(rooms[0]) and rooms[x+dx][y+dy] != -1 and rooms[x+dx][y+dy] != 0 and (x+dx, y+dy) not in visited:
                        next_level.append((x+dx, y+dy))
                        if rooms[x+dx][y+dy] > d:
                            rooms[x+dx][y+dy] = d
            
            d += 1
            q = next_level
        
    # def wallsAndGates(self, rooms: 'List[List[int]]') -> 'None':
    #     """
    #     Do not return anything, modify rooms in-place instead.
    #     """
    #     q = collections.deque()
    #     if not len(rooms) or not len(rooms[0]):
    #         return None

    #     row, col = len(rooms), len(rooms[0])
                
    #     for i in range(row):
    #         for j in range(col):
    #             if rooms[i][j] == 0:
    #                 q.append((i,j))
                    
    #     while q:
    #         (i,j) = q.popleft()
    #         if (i > 0) and (rooms[i-1][j] == 2147483647):
    #             rooms[i-1][j] = rooms[i][j] + 1
    #             q.append((i-1,j))
    #         if (j > 0) and (rooms[i][j-1] == 2147483647):
    #             rooms[i][j-1] = rooms[i][j] + 1
    #             q.append((i,j-1))
    #         if (i < (row-1)) and (rooms[i+1][j] == 2147483647):
    #             rooms[i+1][j] = rooms[i][j] + 1
    #             q.append((i+1,j))
    #         if (j < (col-1)) and (rooms[i][j+1] == 2147483647):
    #             rooms[i][j+1] = rooms[i][j] + 1
    #             q.append((i,j+1))