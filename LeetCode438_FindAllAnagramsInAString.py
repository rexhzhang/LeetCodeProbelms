class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if s is None or p is None or len(s) == 0 or len(p) == 0:
            return []
        def CompareTwoDictionaries(S, P):
            for char_count_s, char_count_p in zip(S,P):
                if char_count_s != char_count_p:
                    return False
            return True

        lenS = len(s)
        lenP = len(p)

        Array_P = [0 for _ in range(26)]
        Array_S = [0 for _ in range(26)]

        ans = []
        for char in p:
            Array_P[ord(char) - ord('a')] += 1

        for char in s[:lenP]:
            Array_S[ord(char) - ord('a')] += 1

        if CompareTwoDictionaries(Array_S, Array_P):
            ans.append(0)

        for i in range(1, lenS - lenP + 1):
            if Array_S[ord(s[i-1]) - ord('a')] - 1 >= 0:
                Array_S[ord(s[i-1]) - ord('a')] -= 1
            Array_S[ord(s[i+lenP-1]) - ord('a')] += 1

            if CompareTwoDictionaries(Array_S, Array_P):
                ans.append(i)

        return ans

test = Solution()
print(test.findAnagrams("cbaebabacd", "abc"))
