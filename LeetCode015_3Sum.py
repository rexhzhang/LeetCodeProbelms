"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
"""
                    nums
 #######(nums[i])(start)##########(end)#######
         target
 变化i, 在序号 start 和 end 之间寻找 nums[start] + nums[end] = 0 - nums[i] 的组合
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = []
        if nums is None or len(nums) == 0:
            return answer
        nums.sort()

        n = len(nums)

        for i in range(n - 2): # n - 2 是为了在i = n-2 时，给start = i 给 end 留出空间
            if i > 0 and nums[i] == nums[i-1]:
                continue  # this is for reason of nums[i]
            start, end, target = i+1, n-1, 0 - nums[i]

            while start < end:
                if nums[start] + nums[end] == target:
                    answer.append([nums[i], nums[start], nums[end]])
                    while start < end and nums[start] == nums[start+1]: start += 1
                    while start < end and nums[end] == nums[end - 1]: end -= 1
                    # 上面的两个while loop 是把 start,end 移到了最后一个（对于start）和最前一个（对于end）和nums[start] 和
                    # nums[end]相同的数字，所以还要将 start 和 end 向后，向前移动一位
                    start += 1
                    end -= 1
                elif nums[start] + nums[end] < target:
                    start += 1
                else: # nums[start] + nums[end] > target
                    end -= 1

        return answer

test = Solution()
result = test.threeSum([-1, 0, 1, 2, -1, -4])
print(result)