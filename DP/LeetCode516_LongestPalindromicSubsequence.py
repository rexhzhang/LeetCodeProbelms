"""
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".
"""


class Solution(object):
    def longestPalindromeSubseq_DFS(self, s):
        """
        :type s: str
        :rtype: int
        """

        def helper(l, r):
            if l == r:
                return 1
            if l > r:
                return 0

            return 2 + helper(l + 1, r - 1) if s[l] == s[r] else max(helper(l + 1, r), helper(l, r - 1))

        return helper(0, len(s) - 1)

    def longestPalindromeSubseq_memorialization(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        memory = [[0 for _ in range(n)] for _ in range(n)]
        def helper(l, r):
            if l == r:
                return 1
            elif l > r:
                return 0

            if memory[l][r]:
                return memory[l][r]
            else:
                memory[l][r] = 2 + helper(l + 1, r - 1) if s[l] == s[r] else max(helper(l + 1, r), helper(l, r - 1))
                return memory[l][r]

        return helper(0, n - 1)