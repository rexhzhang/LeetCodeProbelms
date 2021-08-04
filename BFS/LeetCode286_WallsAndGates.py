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
        if not rooms or not rooms[0]:
            return
        
        
        m, n = len(rooms), len(rooms[0])
        q =  deque([])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    # 把所有为0坐标一次加入队列
                    q.append((i,j))
        
        self.BFS(rooms, q)
        return
    
    
    def BFS(self, board, q):
        
        m, n = len(board), len(board[0])
        dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
        d = 0
        
        while q:
            next_level = deque([])
            d += 1
            
            while q:
                x, y = q.popleft()
                
                for k in range(4):
                    X = x + dx[k]
                    Y = y + dy[k]
                    
                    if 0 <= X < m and 0 <= Y < n and (X, Y) and (board[X][Y] > 0): 
                        # board[X][Y] > 0 包括了 INF 和 其他情况
                        
                        if board[X][Y] == 2147483647:
                            board[X][Y] = d
                            next_level.append((X,Y))
            
            q = next_level
        
        return