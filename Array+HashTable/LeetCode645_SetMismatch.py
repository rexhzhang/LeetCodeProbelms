"""The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in
the set got duplicated to another number in the set, which results in repetition of one number and loss of another
number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number
occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]
Note:
The given array size will in the range [2, 10000].
The given array's numbers won't have any order.

"""


class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #         if nums is None or len(nums) == 0:
        #             return []
        #         result = [None] * 2
        #         # https://www.youtube.com/watch?v=PEoHZOIilBI
        #         n = len(nums)
        #         for i in range(n):
        #             index = abs(nums[i])-1
        #             if nums[index] < 0:
        #                 result[0] = index + 1
        #             else:
        #                 nums[index] = -nums[index]

        #         for i in range(n):
        #             if nums[i] > 0:
        #                 result[1] = i + 1
        #                 break

        #         return result

        if nums is None or len(nums) == 0: return []
        result = [None] * 2
        n = len(nums)
        hmap = [None] * n
        for num in nums:
            if hmap[num - 1] != None:
                result[0] = num
            else:
                hmap[num - 1] = num

        for i in range(len(hmap)):
            if hmap[i] == None:
                result[1] = i + 1

        return result


s