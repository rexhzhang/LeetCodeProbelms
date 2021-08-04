"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.DFS(result, "", n, n)
        return result

    def DFS(self, result, string, left, right):
        if left >  right: ## When left > right, there are more ")" placed than "(". Such cases are wrong and the method stops.
            return

        if left == 0 and right == 0:
            result.append(string)

        if left > 0:
            self.DFS(result, string + "(", left - 1, right)

        if right > 0:
            self.DFS(result, string + ")", left, right -1)

test = Solution()
out = test.generateParenthesis(3)
print(out)