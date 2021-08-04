"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
"""


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        lenPattern = len(pattern)
        strArray = str.split(" ")
        lenStrArray = len(strArray)
        if lenPattern != lenStrArray: return False
        hashMap = {}
        for charFromPattern, word in zip(pattern, strArray):
            if charFromPattern in hashMap:
                if hashMap[charFromPattern] != word:
                    return False

            else:
                if word in hashMap.values(): # pattern = "abba", str = "dog dog dog dog" should return false.
                    return False
                hashMap[charFromPattern] = word

        return True

test = Solution()
pattern = "abba"
str = "dog cat cat dog"
result = test.wordPattern(pattern, str)
print(result)