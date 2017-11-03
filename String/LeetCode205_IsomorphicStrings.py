"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No
two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
"""


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        Smap = [None] * 256
        Tmap = [None] * 256

        for i in range(len(s)):
            if Smap[ord(s[i])] != Tmap[ord(t[i])]:
                return False
            Smap[ord(s[i])] = i
            Tmap[ord(t[i])] = i

        return True

    def isIsomorphic2(self, s, t):

        for char1, char2 in zip(s, t):
            if s.find(char1) != t.find(char2):
                return False

        return True



obj = Solution()
print(obj.isIsomorphic2("abab","ccdd"))