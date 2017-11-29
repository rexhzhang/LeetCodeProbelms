"""
Compare two strings A and B, determine whether A contains all of the characters in B.

The characters in string A and B are all Upper Case letters.

 Notice

The characters of B in A are not necessary continuous or ordered
"""

class Solution:
    """
    @param: A: A string
    @param: B: A string
    @return: if string A contains all of the characters in B return true else return false
    """

    def compareStrings(self, A, B):
        # write your code here

        setA = [0 for _ in range(26)]
        setB = [0 for _ in range(26)]

        for char in A:
            setA[ord(char) - ord("A")] += 1

        for char in B:
            setB[ord(char) - ord("A")] += 1

        for countA, countB in zip(setA, setB):
            if countA < countB:
                return False

        return True
obj = Solution()
obj.compareStrings("A","")