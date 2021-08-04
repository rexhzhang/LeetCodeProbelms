class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        """
        Thoughts:
            1. Make a new matrix, each cell is a turple ("",""), if the cell can connect to Pacific Ocean and Atlantic
            Ocean the turple will be ("P","A")
        """

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        row, column = len(matrix), len(matrix[0])
        myMatrix = [[["", ""] for _ in range(column)] for _ in range(row)]

        for x in range(column):
            myMatrix[0][x][0] = "P"
            myMatrix[row - 1][x][1] = "A"

        for y in range(row):
            myMatrix[y][0][0] = "P"
            myMatrix[y][column - 1][1] = "A"


        for y in range(row):
            for x in range(column):
                if self.BFS(x, y, row, column, matrix, myMatrix, 'A'):
                    myMatrix[y][x][1] = "A"

                if self.BFS(x, y, row, column, matrix, myMatrix, 'P'):
                    myMatrix[y][x][0] = "P"

        ans = []
        for y in range(row):
            for x in range(column):
                if myMatrix[y][x][0] == "P" and myMatrix[y][x][1] == "A":
                    ans.append([y, x])

        # print(myMatrix)
        return ans

    def BFS(self, x, y, row, column, matrix, myMatrix, target):

        dX = [0, 1, -1, 0]
        dY = [1, 0, 0, -1]
        q = [(x, y)]
        visited = [[False for _ in range(column)] for _ in range(row)]
        while q:
            new_q = []
            for u, v in q:
                if target == "A" and myMatrix[v][u][1] == "A":
                    return True
                if target == "P" and myMatrix[v][u][0] == "P":
                    return True

                visited[v][u] = True

                for i in range(4):
                    X = u + dX[i]
                    Y = v + dY[i]


                    if X >= 0 and X < column and Y >= 0 and Y < row and matrix[Y][X] <= matrix[v][u] and not visited[Y][
                        X]:
                        new_q.append((X, Y))

            q = new_q

        return False


test = Solution()
print(test.pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))
