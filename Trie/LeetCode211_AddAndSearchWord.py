class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
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

    def find(self, word, index, CurrentNode):
        if index == len(word):
            return CurrentNode.isWord
        currentChar = word[index]
        if currentChar == ".":
            if len(CurrentNode.children) == 0:
                return False
            for key in CurrentNode.children:
                if self.find(word, index + 1, CurrentNode.children[key]):
                    return True
            return False

        elif CurrentNode.children.get(currentChar) != None:
            return self.find(word, index + 1, CurrentNode.children[currentChar])
        else:
            return False

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.find(word, 0, self.root)



        # Your WordDictionary object will be instantiated and called as such:
        # obj = WordDictionary()
        # obj.addWord(word)
        # param_2 = obj.search(word)