"""Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it.
If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A
repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.
"""


class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        # 核心思路：不断append A直到A的长度 > B的长度，如果这时A中找不到B，则A再append一次，还找不到就是找不到了

        if len(set(B)) > len(set(A)): return -1

        sb = A
        counter = 1
        while len(sb) < len(B):
            sb = sb + A
            counter += 1

        if self.indexOf(sb, B) >= 0:
            return counter

        sb = sb + A
        if self.indexOf(sb, B) >= 0:
            return counter + 1

        return -1

    def indexOf(self, s, target):
        lenS = len(s)
        lenT = len(target)

        for i in range(lenS - lenT + 1):
            j = 0
            while j < lenT:
                if target[j] != s[i + j]:
                    break
                j += 1

            if j == lenT:
                return i

        return -1