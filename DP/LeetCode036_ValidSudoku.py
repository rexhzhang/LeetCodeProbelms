"""
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.
"""
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if board is None or len(board) != 9 and len(board[0]) != 9:
            return False

        for i in range(9):
            if not self.checkRow(i, board) or not self.checkColumn(i, board):
                return False


        for y in range(0 ,7 ,3):
            for x in range(0, 7, 3):
                if not self.checkSquare(x, y, board):
                    return False

        return True




    def checkRow(self, y, board):
        HS = set()
        for char in board[y]:
            if char == ".":
                continue
            elif char in HS:
                return False
            else:
                HS.add(char)

        return True

    def checkColumn(self, x, board):
        HS = set()
        for i in range(9):
            if board[i][x] == ".":
                continue
            elif board[i][x] in HS:
                return False
            else:
                HS.add(board[i][x])

        return True

    def checkSquare(self, x, y, board):
        HS = set()
        for Y in range(y, y+ 3):
            for X in range(x, x + 3):
                if board[Y][X] == ".":
                    continue
                elif board[Y][X] in HS:
                    return False
                else:
                    HS.add(board[Y][X])

        return True