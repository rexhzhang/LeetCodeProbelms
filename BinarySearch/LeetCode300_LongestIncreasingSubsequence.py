"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""
class Solution:
    """
    Dp[i] 表示以第i个数字为结尾的最长上升子序列的长度。
对于每个数字，枚举前面所有小于自己的数字 j，Dp[i] = max{Dp[j]} + 1. 如果没有比自己小的，Dp[i] = 1;
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        dp = [1] * len(nums)
        longest = 1
        for i in range(1,len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
            if dp[i] > longest:
                longest = dp[i]
        return longest

    """
    O(nlgn)的贪心算法
    很trick的一个方法，做过一次之后基本就能记住。
    核心点就是创建一个递增数组，并在原数组上进行修改
    只能用于求longest 递增或递减数组

    get_insert_pos时间复杂度是nlgn
    用令狐冲的二分法就可以，唯一要注意的是，这种找pos的题目
    nums[start] 和nums[end] 可能同时大于target
    也可能同时小于target。 考虑好corner case就没问题
    """
    
    def lengthOfLIS(self, nums: List[int]) -> int:

        if nums is None or len(nums) == 0:
            return 0

        n = len(nums)
        res = []
        for num in nums:
            if len(res) == 0 or res[-1] < num:
                res.append(num)
                continue
            insert_pos = self.get_insert_pos(num, res)
            res[insert_pos] = num

        return len(res)
            
    def get_insert_pos(self, target, nums):
        if len(nums) == 0:
            return 0
            
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid
        
        if target <= nums[start]:
            return start
        if target <= nums[end]:
            return end
        
        return len(nums)