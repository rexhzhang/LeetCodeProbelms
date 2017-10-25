"""Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a
specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must
be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""


class Solution(object):
    def twoSumBinarySearch(self, numbers, target):
        # Binary Search VersionO(nlogn) runtime and O(1) space
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        def bsearch(wanted):
            start = 0
            end = len(numbers) - 1

            while start + 1 < end:
                mid = start + (end - start) / 2
                if numbers[mid] == wanted:
                    return mid
                elif numbers[mid] > wanted:
                    end = mid
                else:
                    start = mid
            if numbers[start] == wanted:
                return start
            elif numbers[end] == wanted:
                return end
            else:
                return -1

        for i in range(len(numbers)):
            result = bsearch(target - numbers[i])
            if result != -1 and result != i:
                return [min(result + 1, i + 1), max(result + 1, i + 1)]

    def twoSum(self, numbers, target):
        # Two Pointers O(n) time complexity and O(1) Space
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if numbers is None or target is None or len(numbers) <= 1:
            raise ValueError("Invalid Input values")

        left, right = 0, len(numbers) -1

        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return [left, right]