class Solution:
    # @param board, a list of lists of 1 length string
    # @param words: A list of string
    # @return: A list of string
    def wordSearchII(self, board, words):
        # write your code here
        if board is None or len(board) == 0 or len(board[0]) == 0:
            return []
        if len(words) == 0:
            return []

        row, column = len(board), len(board[0])
        answer = []
        for word in words:
            for i in range(row):
                for j in range(column):
                    if board[i][j] == word[0]:
                        result = self.search(word, board, i, j, 0)
                        if result is True and word not in answer:
                            answer.append(word)

        return answer

    def search(self, word, board, i, j, index):
        if index == len(word):
            return True

        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[index]:
            return False

        board[i][j] = "#"
        result = self.search(word, board, i + 1, j, index + 1) or self.search(word, board, i - 1, j, index + 1) or self.search(word, board, i,j + 1, index + 1) or self.search(word, board, i, j - 1, index + 1)

        board[i][j] = word[index]

        return result