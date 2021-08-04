"""
Given an array of integers, remove the duplicate numbers in it.

You should:
1. Do it in place in the array.
2. Move the unique numbers to the front of the array.
3. Return the total number of the unique numbers.
"""
"""
Example
Given nums = [1,3,1,4,4,2], you should:

Move duplicate integers to the tail of nums => nums = [1,3,4,2,?,?].
Return the number of unique integers in nums => 4.
Actually we don't care about what you place in ?, we only care about the part which has no duplicate integers.

Challenge 
Do it in O(n) time complexity.
Do it in O(nlogn) time without extra space.
"""


class Solution:
    # @param {int[]} nums an array of integers
    # @return {int} the number of unique integers
    def deduplication(self, nums):
        # Write your code here
        hashset = set()
        slow, fast = 0, 0

        while fast < len(nums):

            while fast < len(nums) and nums[fast] in hashset:
                fast += 1

            if fast < len(nums):
                temp = nums[slow]
                nums[slow] = nums[fast]
                nums[fast] = temp
                hashset.add(nums[fast])
                fast += 1
                slow += 1

        return slow + 1