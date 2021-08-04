"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # [#ofOccurance, index]
        hmap = [[0, None] for _ in range(26)]

        for i in range(len(s)):
            hmap[ord(s[i]) - ord("a")][0] += 1
            hmap[ord(s[i]) - ord("a")][1] = i

        ans = float("inf")
        flag = False
        for Occurance, index in hmap:
            if Occurance == 1:
                ans = min(ans,index)
                flag = True

        return ans if flag else -1