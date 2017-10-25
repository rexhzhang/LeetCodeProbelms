"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

"""


class Solution(object):
    def wordBreakBackTracking(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        search_map = {}

        def helper(s):
            if len(s) == 0: return True
            if search_map.get(s, None):
                return search_map[s]

            for i in range(len(s)):
                subString = s[:i + 1]
                if subString in wordDict:
                    if i == len(s)-1: return True
                    search_map[subString] = True
                    if helper(s[i+1:]):
                        return True

                search_map[subString] = False
            return False
