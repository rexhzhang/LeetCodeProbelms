"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""
"""
使用九章算法班中讲过的相向型双指针算法。
整个算法的思想是计算每个位置上可以盛放的水，累加起来。

记录如下几个值：

left, right => 左右指针的位置
left_max, right_max => 从左到右和从右到左到 left, right 为止，找到的最大的 height
每次比较 left_max 和 right_max，如果 left_max 比较小，就挪动 left 到 left + 1。
与此同时，查看 left 这个位置上能够盛放多少水，这里有两种情况：

一种是 left_max > heights[left]，这种情况下，水可以盛放 left_max - heights[left] 那么多。因为右边有 right_max 挡着，左侧可以到 left_max。
一种是 left_max <= heights[left]，这种情况下，水无法盛放，会从左侧流走，此时更新 left_max 为 heights[left]
left_max >= right_max 的情况类似处理。

时间复杂度：O(n)O(n)，空间复杂度 O(1)O(1)
"""
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        
        left, right = 0, len(height)-1
        left_max, right_max = 0, 0
        
        water = 0
        
        while left <= right:
            
            if left_max <= right_max:
                
                if left_max < height[left]:
                    left_max = height[left]
                    
                else: # left_max >= height[left]
                    if left_max - height[left]>0:
                        water += left_max - height[left]
                
                left += 1
            
            else:
                
                if right_max < height[right]:
                    right_max = height[right]
                
                else:
                    if right_max - height[right] > 0:
                        water += right_max - height[right]
                
                right -= 1
            
        
        return water