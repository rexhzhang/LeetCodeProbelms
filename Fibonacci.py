"""
The Fibonacci numbers are the numbers in the following integer sequence.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..

In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation

    Fn = Fn-1 + Fn-2
with seed values

   F0 = 0 and F1 = 1.
"""

# 1. Recursion
class Solution():
    def FibonacciSolver(self, n):
        if n < 0:
            print("Incorrect input, n must be greater than 0")
        elif n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.FibonacciSolver(n-1) + self.FibonacciSolver(n-2)

# 2. DP
    def FibonacciSolverDP(self, n):
        dP = [0 for _ in range(n)]
        if n == 0:
            return dP[n]
        dP[1] = 1
        if n == 1:
            return dP[1]
        for i in range(2, n):
            dP[i] = dP[i-1]+dP[i-2]
        return dP[n-1]

# 3. DP with rolling index array
    def FibonacciSolverDP2(self, n):
        dP = [0, 1]

        if n == 0:
            return dP[0]
        elif n == 1:
            return dP[1]

        for i in range(2,n):
            dP[i%2] = dP[0] + dP[1]

        return dP[(n-1)%2]



test = Solution()
# result = test.FibonacciSolver(45)
resultDP = test.FibonacciSolverDP(45)
print(resultDP)
resultDP2 = test.FibonacciSolverDP2(45)
print(str(resultDP2))