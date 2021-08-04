"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. 
Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. 
Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""

from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        """
        方法1:

        在记录每个节点是否访问过的前提下, 依次从每个 'O' 开始BFS/DFS, 并且只访问未访问过的 'O'.

        如果从一个 'O' 可以访问到边界, 那么不做任何操作; 否则便将这个 'O' 可以访问到的所有的 'O' 替换为 'X'.

        """

        if not board or not board[0]:
            return
        
        visited = set([])

        m, n = len(board), len(board[0])
        
        for i in range(m):
            for j in range(n):
                if (i, j) in visited:
                    continue
                elif board[i][j] == 'O':
                    result = self.search(board, (i,j))
                    if result:
                        visited = visited | result

    
    def search(self, board, coor):
        
        q = deque([coor])
        visited = set([coor])
        dx, dy = [1,0,0,-1],[0,1,-1,0]
        m, n = len(board), len(board[0])
        hit_border = False
        if coor[0] == 0 or coor[0] == m-1 or coor[1] == 0 or coor[1] == n - 1:
            hit_border = True
        
        while q:
            x, y = q.popleft()

            for i in range(4):
                X, Y = x + dx[i], y + dy[i]

                if 0 <= X < m and 0 <= Y < n and board[X][Y] == 'O' and (X, Y) not in visited:
                    visited.add((X,Y))
                    q.append((X,Y))
                    if X == 0 or X == m-1 or Y == 0 or Y == n -1:
                        hit_border = True
        
        if hit_border:
            return visited
        else:
            for x, y in visited:
                board[x][y] = 'X'

            
        """
        方法2:

            从每个边界的 'O' 开始遍历, 只访问 'O', 先都暂时设置为 'T' 或其他字符.

            遍历结束之后, 将剩下的 'O' 替换为 'X' 然后再将 'T' 还原即可.
        """

        if not board or not board[0]:return
            
        m,n = len(board), len(board[0])
        
        for i in range(m):
            if board[i][0] == 'O':
                self.BFS(board, i, 0)
            if board[i][n-1] == 'O':
                self.BFS(board, i, n-1)
        
        for j in range(n):
            if board[0][j] == 'O':
                self.BFS(board, 0, j)
            
            if board[m-1][j] == 'O':
                self.BFS(board, m-1, j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'
        
    
    def BFS(self, board, i, j):
        
        
        q = deque([(i,j)])
        
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        m, n = len(board), len(board[0])
        board[i][j] = 'T'
        while q:
            x, y = q.popleft()
            
            for k in range(4):
                
                X, Y = x+dx[k], y + dy[k]
                
                if 0 <= X < m and 0 <= Y < n and board[X][Y] == 'O':
                    q.append((X,Y))
                    board[X][Y] = 'T'