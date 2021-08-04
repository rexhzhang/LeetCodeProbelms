"""
Implement a magic directory with buildDict, and search methods.

For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.

For the method search, you'll be given a word, and judge whether if you modify exactly one character into another character in this word, the modified word is in the dictionary you just built.

Example 1:
Input: buildDict(["hello", "leetcode"]), Output: Null
Input: search("hello"), Output: False
Input: search("hhllo"), Output: True
Input: search("hell"), Output: False
Input: search("leetcoded"), Output: False

class MagicDictionary(object):

    def __init__(self):
        \"""
        Initialize your data structure here.
        \"""
        

    def buildDict(self, dict):
        \"""
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: None
        \"""
        

    def search(self, word):
        \"""
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        \"""
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)

"""

from collections import defaultdict

class MagicDictionary(object):

    # Time: Build: O(n * m), Search O(m)


    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Create a dict with default value set to an empty set
        self.d = defaultdict(set)


    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: None
        """
        for item in dict:
            for i in range(len(item)):
                key = item[:i] + '*' + item[i+1:]
                value = item[i]
                self.d[key].add(value)
        
    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for i in range(len(word)):
            key = word[:i] + '*' + word[i+1:]
            if key in self.d:
                if word[i] not in self.d[key]:
                    return True
                elif word[i] in self.d[key] and len(self.d[key]) > 1:
                    return True
        
        return False