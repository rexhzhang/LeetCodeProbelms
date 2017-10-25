"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]
"""
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        Solution.answer = []
        self.dfs(s, [])
        return Solution.answer

    def isPalindrome(self, s):
        for i in range(len(s)):
            if s[i] != s[len(s)-1-i]:
                return False
        return True

    def dfs(self, remainingS, stringlist):
        if len(remainingS) == 0:
            Solution.answer.append(stringlist)

        for i in range(1, len(remainingS)+1):
            # len(remainingS) + 1 because i is the end index of the remainingS
            if self.isPalindrome(remainingS[:i]):
                self.dfs(remainingS[i:], stringlist + [remainingS[:i]])

test = Solution()
result = test.partition("aab")
print(result)