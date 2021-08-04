class Solution(object):
    """

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, 
replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
    """
    def isHappy(self, n):
        a = set()
        while self.sumOfTheSquareOfItsDigits(n) != 1:
            if n in a:
                return False
            a.add(n)
            n = self.sumOfTheSquareOfItsDigits(n)

        return True

    def sumOfTheSquareOfItsDigits(self, num):

        if num < 10:
            return num * num

        q = []
        while num >= 10:
            q.append(num % 10)
            num = num // 10
        q.append(num)
        ans = 0
        for n in q:
            ans += n * n
        return ans

test1 = Solution()
print(test1.isHappy(3))