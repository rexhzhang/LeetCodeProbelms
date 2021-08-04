"""
Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.

"""
# 2019-06-22
class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for char in word:
            child = node.children.get(char)
            if child is None:
                node.children[char] = TrieNode()
                child = node.children[char]
            node = child
        node.isWord = True


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for char in word:
            child = node.children.get(char)
            if child is None:
                return False
            else:
                node = child
        return node.isWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for char in prefix:
            child = node.children.get(char)
            if child is None:
                return False
            node = child
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# Use Array instead of Dictionary

class TrieNode(object):
    def __init__(self):
        self.isWord = False
        self.children = [None] * 26

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for c in word:
            if not cur.children[ord(c) - ord('a')]:
                cur.children[ord(c) - ord('a')] = TrieNode()
                cur = cur.children[ord(c) - ord('a')]
            else:
                cur = cur.children[ord(c) - ord('a')]
        cur.isWord = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        for c in word:
            if not cur.children[ord(c) - ord('a')]:
                return False
            cur = cur.children[ord(c) - ord('a')]
        
        return True if cur.isWord else False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        
        cur = self.root
        for c in prefix:
            if not cur.children[ord(c) - ord('a')]:
                return False
            cur = cur.children[ord(c) - ord('a')]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)