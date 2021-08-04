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
        dictionary = set([])
        for word in wordList:
            dictionary.add(word)
        
        q =  deque([beginWord])
        step = 1
        visited = set([beginWord])
        
        while q:
            step += 1
            next_round = deque([])
            
            while q:
                word = q.popleft()
            
                for i in range(len(word)):
                    left = word[:i]
                    right = word[i+1:]
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        new_word = left + c + right

                        if new_word in dictionary and new_word == endWord:
                            return step

                        elif new_word in dictionary and new_word not in visited:
                            visited.add(new_word)
                            next_round.append(new_word)
                
            
            q = next_round
        
        return 0

test = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
result = test.ladderLength(beginWord,endWord,wordList)
print(result)