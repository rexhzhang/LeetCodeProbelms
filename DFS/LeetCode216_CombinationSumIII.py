"""Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be
used and each combination should be a unique set of numbers.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]
"""


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.answer = []
        self.helper(k,n,[],1)
        return self.answer

    def helper(self, k, n, valuelist, start):
        if n == 0 and k == 0:
            self.answer.append(valuelist)
            return

        for i in range(start,10):

            if n < 0 or k < 0:
                return

            self.helper(k-1, n-i, valuelist + [i], i + 1)

test = Solution()
result = test.combinationSum3(3, 15)
print(result)

# 11 : [[1, 5, 9], [1, 6, 8], [2, 4, 9], [2, 5, 8], [2, 6, 7], [3, 4, 8], [3, 5, 7], [4, 5, 6]]