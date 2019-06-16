class Solution(object):
    def divide(self, dividend, divisor):
        INT_MAX = 2147483647
        if divisor == 0:
            return INT_MAX
        neg = dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0
        a, b = abs(dividend), abs(divisor)
        ans, shift = 0, 31
        while shift >= 0:
            print(shift, a, b, ans)
            if a >= b << shift:
                a -= b << shift
                ans += 1 << shift
            shift -= 1
        if neg:
            ans = - ans
        if ans > INT_MAX:
            return INT_MAX
        return ans


import math
def area(radius):
    return math.pi * (radius ** 2)

l = [1,2,3,4,5,6]
x = map(area, l)

print(x)


rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
q = [(i, j) for i, row in enumerate(rooms) for j, r in enumerate(row) if not r]
print(q)