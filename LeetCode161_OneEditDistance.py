"""
Given two strings S and T, determine if they are both one edit distance apart.

"""
class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def isDel(short, long):
            for i in range(len(short)):
                if short[i] != long[i]:
                    return long[i+1:] == short[i:]
            return True

        def isOneEdit(s, t):
            diff = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    diff += 1
                    if diff > 1:
                        return False
            return diff == 1 # Must be exactly one edit distance apart


        if abs(len(s) - len(t)) > 1: return False
        elif len(s) == len(t): return isOneEdit(s,t)
        elif len(s) - len(t) == 1: return isDel(t, s)
        else: return isDel(s, t)