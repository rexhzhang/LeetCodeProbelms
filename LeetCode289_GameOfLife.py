"""According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised
by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its
eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia
article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.

Follow up: Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot
update some cells first and then use their updated values to update other cells. In this question, we represent the
board using a 2D array. In principle, the board is infinite, which would cause problems when the active area
encroaches the border of the array. How would you address these problems? """
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board is None:
            raise ValueError("Input board is None")

        if len(board) == 0 or len(board[0]) == 0:
            return

        row, column = len(board), len(board[0])

        def checkNeighbors(board, x, y, Row, Column):
            dX = [1, -1, 0, 0, 1, -1, 1, -1]
            dY = [0, 0, 1, -1, 1, -1, -1, 1]

            Counter = 0
            for i in range(8):
                X = x + dX[i]
                Y = y + dY[i]

                if inSide(X, Y, Row, Column) and (board[Y][X] == 1 or board[Y][X] == -1):  # -1 : alive in this cycle but dead in the next
                    Counter += 1

            return Counter

        def inSide(X, Y, Row, Column):
            return X >= 0 and Y >= 0 and X < Column and Y < Row

        for y in range(row):
            for x in range(column):
                liveNeighbours = checkNeighbors(board,x, y, row, column)
                if board[y][x] == 1 and liveNeighbours > 3:
                    board[y][x] = -1

                elif board[y][x] == 1 and (liveNeighbours == 2 or liveNeighbours == 3):
                    board[y][x] = 1

                elif board[y][x] == 1 and liveNeighbours < 2:
                    board[y][x] = -1

                elif board[y][x] == 0 and liveNeighbours == 3:
                    board[y][x] = 2 # 2: dead in this cycle but alive in next

        for y in range(row):
            for x in range(column):
                if board[y][x] == -1:
                    board[y][x] = 0

                if board[y][x] == 2:
                    board[y][x] = 1
