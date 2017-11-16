"""

This is a follow up of Shortest Word Distance. The only difference is now word1 could be the same as word2.

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “makes”, word2 = “coding”, return 1.
Given word1 = "makes", word2 = "makes", return 3.

Note:
You may assume word1 and word2 are both in the list.
"""


class Solution(object):
    def shortestWordDistance_short(self, words, word1, word2):
        shortDistance = len(words)
        Index1, Index2 = None, None
        for i in range(len(words)):
            if words[i] == word1:
                Index1 = i
            if words[i] == word2:
                if word1 == word2:
                    Index1 = Index2
                Index2 = i
            if Index1 != None and Index2 != None:

                shortDistance = min(shortDistance, abs(Index1 - Index2))

        return shortDistance


    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        shortestDistance = len(words)
        Index1, Index2 = None, None
        flag = True
        areWordssame = word1 == word2
        for i in range(len(words)):
            if areWordssame:
                if flag and words[i] == word1:
                    Index1 = i
                    flag = not flag
                elif not flag and words[i] == word2:
                    Index2 = i
                    flag = not flag
            else:
                if words[i] == word1:
                    Index1 = i
                elif words[i] == word2:
                    Index2 = i
            if Index1 != None and Index2 != None:
                shortestDistance = min(shortestDistance, abs(Index2 - Index1))

        return shortestDistance