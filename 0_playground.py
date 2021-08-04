# class Solution(object):
#     def divide(self, dividend, divisor):
#         INT_MAX = 2147483647
#         if divisor == 0:
#             return INT_MAX
#         neg = dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0
#         a, b = abs(dividend), abs(divisor)
#         ans, shift = 0, 31
#         while shift >= 0:
#             print(shift, a, b, ans)
#             if a >= b << shift:
#                 a -= b << shift
#                 ans += 1 << shift
#             shift -= 1
#         if neg:
#             ans = - ans
#         if ans > INT_MAX:
#             return INT_MAX
#         return ans


# import math
# def area(radius):
#     return math.pi * (radius ** 2)

# l = [1,2,3,4,5,6]
# x = map(area, l)

# print(x)


# rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
# q = [(i, j) for i, row in enumerate(rooms) for j, r in enumerate(row) if not r]
# print(q)



"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""




def sum_three(nums):
    results = []
    list.sort(nums)
    for x in range(len(nums)-2):
        head_ptr = x + 1
        tail_ptr = len(nums) - 1
        curr_sum = nums[x] + nums[head_ptr] + nums[tail_ptr]
        while curr_sum != 0:
            while nums[head_ptr - 1] == nums[head_ptr]:
                head_ptr += 1
            while nums[tail_ptr -1] == nums[tail_ptr]:
                tail_ptr -= 1
            if head_ptr >= tail_ptr:
                break
            if curr_sum > 0:
                tail_ptr -= 1
            else:
                head_ptr += 1    
            curr_sum = nums[x] + nums[head_ptr] + nums[tail_ptr]  
        if curr_sum == 0:
            results.append([nums[x], nums[head_ptr], nums[tail_ptr]])
    return results
    
    
    
t1 = [-1,0,1,2,-1,-4]

print(sum_three(t1))