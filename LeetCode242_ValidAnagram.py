import collections
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        """
        Given two strings s and t, write a function to determine if t is an anagram of s.
        
        For example,
        s = "anagram", t = "nagaram", return true.
        s = "rat", t = "car", return false.
        """

        s_count = collections.Counter(s)
        t_count = collections.Counter(t)

        s_count.subtract(t_count)
        print(s_count)
        for key in s_count:
            if s_count[key] != 0:
                return False

        return True


test = Solution()
print(test.isAnagram("ab", "a"))