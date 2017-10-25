"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation
sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note: Return 0 if there is no such transformation sequence. All words have the same length. All words contain only
lowercase alphabetic characters. You may assume no duplicates in the word list. You may assume beginWord and endWord
are non-empty and are not the same. UPDATE (2017/1/20): The wordList parameter had been changed to a list of strings
(instead of a set of strings). Please reload the code definition to get the latest changes.
"""
from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        dictionary = set()
        for word in wordList:
            dictionary.add(word)

        queue = deque([(beginWord,1)])

        while queue:
            element = queue.popleft()
            currentWord = element[0]
            currentLength = element[1]
            for i in range(len(currentWord)):
                if currentWord == endWord:
                    return currentLength

                left = currentWord[:i]
                middle = currentWord[i]
                right = currentWord[i+1:]
                for j in "abcdefghijklmnopqrstuvwxyz":
                    if j != middle:
                        newWord = left + j + right
                        if newWord in dictionary:
                            queue.append((newWord, currentLength+1))
                            if currentLength > 1:
                                dictionary.remove(newWord)

        return 0

test = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
result = test.ladderLength(beginWord,endWord,wordList)
print(result)