"""

Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n and return all possible combinations of its factors.

Note:
You may assume that n is always positive.
Factors should be greater than 1 and less than n.
Examples:
input: 1
output:
[]
input: 37
output:
[]
input: 12
output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]
input: 32
output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]


"""


class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = []

        def helper(n, factorsList, start):
            if n <= 1:
                if len(factorsList) > 1:
                    temp = list(factorsList)
                    result.append(temp)
                return
            else:
                for i in range(start, n+1):
                    if n % i == 0:
                        factorsList.append(i)
                        helper(n // i, factorsList, i)
                        factorsList.pop()

        helper(n, [], 2)
        return result


test = Solution()
print(test.getFactors(12))
