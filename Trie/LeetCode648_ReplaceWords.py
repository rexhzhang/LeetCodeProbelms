# In English, we have a concept called root, which can be followed by some other words to form another longer word -
# let's call this word successor. For example, the root an, followed by other, which can form another word another.
#
# Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the
# sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the
# shortest length.
#
# You need to output the sentence after the replacement.
#
# Example 1:
# Input: dict = ["cat", "bat", "rat"]
# sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"
# Note:
# The input will only have lower-case letters.
# 1 <= dict words number <= 1000
# 1 <= sentence words number <= 1000
# 1 <= root length <= 100
# 1 <= sentence words length <= 1000

class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        prefix = set(dict)
        wordList = sentence.split()
        for i in range(len(wordList)):
            word = wordList[i]
            for j in range(len(word)):
                partialWord = word[:j]
                if partialWord in prefix:
                    wordList[i] = partialWord
                    break

        return " ".join(wordList)

    def replaceWordsCache(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """

        def replace(word):
            best = word
            for r in cache[ord(word[0]) - ord('a')]:
                if len(r) < len(best) and word.startswith(r):
                    best = r
            return best

        # cache = collections.defaultdict(list)
        cache = [[] for _ in range(26)]
        for r in dict:
            cache[ord(r[0]) - ord('a')] += [r]
        return ' '.join(map(replace, sentence.split()))

dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
test = Solution()
print(test.replaceWords(dict, sentence))