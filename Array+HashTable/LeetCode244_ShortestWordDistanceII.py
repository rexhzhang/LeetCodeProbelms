"""
This is a follow up of Shortest Word Distance. The only difference is now you are given the list of words and your method will be called repeatedly many times with different parameters. How would you optimize it?

Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""
from collections import defaultdict

class WordDistance(object):
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.words = defaultdict(list)
        for i in range(len(words)):
            self.words[words[i]].append(i)


    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        shortestDistance = float('inf')
        for index1 in self.words[word1]:
            for index2 in self.words[word2]:
                shortestDistance = min(shortestDistance, abs(index1 - index2))

        return shortestDistance



        # Your WordDistance object will be instantiated and called as such:
        # obj = WordDistance(words)
        # param_1 = obj.shortest(word1,word2)