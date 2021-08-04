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

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""
from collections import deque

#
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) <=2 or len(board) <= 2:
            return
        row, column = len(board), len(board[0])

        for i in range(row):
            if board[i][0] == 'O':
                self.BFS(board, i, 0)
            if board[i][column-1] == 'O':
                self.BFS(board, i, column-1)
        
        for j in range(column):
            if board[0][j] == 'O':
                self.BFS(board, 0, j)
            if board[row-1][j] == 'O':
                self.BFS(board, row-1, j)
        
        for i in range(row):
            for j in range(column):
                if board[i][j] == 'B':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
                else:
                    continue
        return 
        
    def BFS(self, board: List[List[str]], i: int, j: int) -> None:
        q = deque([(i, j)])
        movement = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        board[i][j] = 'B'
        while q:
            x, y = q.popleft()
            
            for k in range(4):
                dx, dy = movement[k]
                if x + dx >= 0 and y + dy >= 0 and x + dx < len(board) and y + dy < len(board[0]) and board[x+dx][y+dy] == 'O':
                    q.append((x+dx, y+dy))
                    board[x+dx][y+dy] = 'B'
        
        return

        

# Old Solution
class Solution_O:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) <=2 or len(board) <= 2:
            return
        visited = set([])
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i, j) not in visited:
                    visited = visited.union(self.BFS(visited, board, i, j))
        
        return 
        
    def BFS(self, visited: set, board: List[List[str]], row: int, column: int) -> set:
        
        q = deque([(row, column)])
        s = set([])
        s.add((row, column))
        hit_border = False
        if row == 0 or column == 0 or row == len(board) -1 or column == len(board[0]) - 1:
            hit_border = True

        movement = [[1,0],[-1,0],[0,1],[0,-1]]
        
        
        while q:
            x,y = q.popleft()
            s.add((x,y))
            for i in range(4):

                dx, dy = movement[i][0], movement[i][1]
                
                if x+dx >=0 and y+dy >= 0 and x+dx < len(board) and y+dy < len(board[0]) and board[x+dx][y+dy] == 'O' and (x+dx, y+dy) not in s and (x+dx, y+dy) not in visited:
                    
                    if x+dx == 0 or y+dy == 0 or x+dx == len(board)-1 or y+dy == len(board[0]) - 1:
                        hit_border = True
                    
                    s.add((x+dx, y+dy))
                    q.append((x+dx, y+dy))
            
        
        if not hit_border:
            self.flip(board, s)
            return s
        else:
            return s

    
    def flip(self, board: List[List[str]], s: set):
        for coord in s:
            board[coord[0]][coord[1]] = 'X'
        