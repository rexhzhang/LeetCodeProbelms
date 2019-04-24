"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index
"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        # Greedy
        last_max_pos, cur_max_pos = 0, 0
        n_steps = 0
        i = 0
        

        while cur_max_pos < len(nums) - 1: # can't be <= because that will introduce one additional step, since it's already at the end
            
            # find the max position it can reach from position i
            while i <= last_max_pos:
                cur_max_pos = max(i+nums[i], cur_max_pos)
                i += 1
            
            if cur_max_pos == last_max_pos:
                return -1
            
            last_max_pos = cur_max_pos
            n_steps += 1
        
        return n_steps

    
    def jump(self, nums: List[int]) -> int:
        # DP
        # Each cell contains the minimum number of jumps to reach
        dp = [float('inf')] * (len(nums))
        dp[0] = 0
        
        for i in range(len(nums)):
            for j in range(1, nums[i]+1):
                if i + j < len(nums):
                    dp[i+j] = min(dp[i+j], dp[i] + 1)
        print(dp)
        return dp[-1]
            
        
            
        