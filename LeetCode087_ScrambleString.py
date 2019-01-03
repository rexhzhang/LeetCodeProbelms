class Solution:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 is None or s2 is None: return False
        if s1 == s2: return True
        if len(s1) != len(s2): return False

        letters = [0] * 26
        for i in range(len(s1)):
            letters[ord(s1[i]) - ord('a')] += 1
            letters[ord(s2[i]) - ord('a')] -= 1

        for i in range(26):
            if letters[i] != 0: return False

        length = len(s1)

        for i in range(1,length):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]): return True
            if self.isScramble(s1[:i], s2[length - i:]) and self.isScramble(s1[i:], s2[:length - i]): return True

        return False


o1 = Solution()
print(o1.isScramble("gre", "rge"))

