"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""


class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []
        if s is None or p is None or len(s) == 0: return result
        Pmap = [0] * 26
        for char in p:
            Pmap[ord(char) - ord("a")] += 1
        Smap = [0] * 26
        for char in s[:len(p)]:
            Smap[ord(char) - ord("a")] += 1

        if Smap == Pmap: result.append(0)

        for i in range(len(p), len(s)):
            Smap[ord(s[i])-ord("a")] += 1
            Smap[ord(s[i-len(p)]) - ord("a")] -= 1
            if Smap == Pmap:
                result.append(i-len(p)+1)

        return result