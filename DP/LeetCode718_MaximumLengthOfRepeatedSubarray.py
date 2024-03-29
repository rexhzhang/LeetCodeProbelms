"""
Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:

Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation: 
The repeated subarray with maximum length is [3, 2, 1].
 

Note:

1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100
"""

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        # 二维dp记住 从每个A,B位置开始最长的长度
        # O(mn) 时间和空间
        # Python知识点： max()的用法
        dp = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
        
        for i in range(1,len(A)+1):
            for j in range(1, len(B) + 1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1

        return max(max(row) for row in dp)