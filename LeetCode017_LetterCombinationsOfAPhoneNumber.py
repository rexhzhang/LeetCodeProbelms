class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        answer = []
        if len(digits) == 0 or digits is None:
            return answer

        dictionary = {}
        dictionary["1"] = "1"
        dictionary["2"] = "abc"
        dictionary["3"] = "def"
        dictionary["4"] = "ghi"
        dictionary["5"] = "jkl"
        dictionary["6"] = "mno"
        dictionary["7"] = "pqrs"
        dictionary["8"] = "tuv"
        dictionary["9"] = "wxyz"
        dictionary["0"] = "0"

        def DFS(index, currentString, answerList, dictionary, digits):

            if index == len(digits)-1:
                for char in dictionary[digits[index]]:
                    answerList.append(currentString + char)

            else:
                for char in dictionary[digits[index]]:
                    DFS(index + 1, currentString + char, answerList, dictionary, digits)

        DFS(0, "", answer, dictionary, digits)

        return answer

test = Solution()
digits = "23"
result = test.letterCombinations(digits)
print(result)