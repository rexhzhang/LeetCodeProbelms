"""
Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.
"""


class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hashTable = {}
        for char in s:
            hashTable[char] = hashTable.get(char, 0) + 1

        singleCount = 0
        for key in hashTable:
            if hashTable[key] % 2 != 0:
                singleCount += 1

            if singleCount > 1:
                return False

        return True