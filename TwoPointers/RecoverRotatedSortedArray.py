"""

Given a rotated sorted array, recover it to sorted array in-place.

Have you met this question in a real interview? Yes
Clarification
What is rotated array?

For example, the orginal array is [1,2,3,4], The rotated array of it can be [1,2,3,4], [2,3,4,1], [3,4,1,2], [4,1,2,3]
Example
[4, 5, 1, 2, 3] -> [1, 2, 3, 4, 5]

Challenge
In-place, O(1) extra space and O(n) time.

"""
class Solution:
    """
    @param nums: The rotated sorted array
    @return: nothing
    """

    def recoverRotatedSortedArray(self, nums):
        # write your code here

        k = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                k = i
                break
        # print(k)
        if k != 0:
            nums[:k+1] = reversed(nums[:k+1])
            nums[k+1:] = reversed(nums[k+1:])
            nums.reverse()