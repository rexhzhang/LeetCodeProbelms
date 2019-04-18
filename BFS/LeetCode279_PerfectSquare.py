"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""
from collections import deque
from math import sqrt, floor

class Solution:
    
    def numSquares(self, n: int) -> int:
        # BFS
        # Consider a graph which consists of number 0, 1,...,n as
        # its nodes. Node j is connected to node i via an edge if  
        # and only if either j = i + (a perfect square number) or 
        # i = j + (a perfect square number). Starting from node 0, 
        # do the breadth-first search. If we reach node n at step 
        # m, then the least number of perfect square numbers which 
        # sum to n is m. Here since we have already obtained the 
        # perfect square numbers, we have actually finished the 
        # search at step 1

        if n <= 0:
            return 0
        
        perfectSquare = []
        cntPerfectSquare = [None] * n
        for i in range(1, floor(sqrt(n))+1):
            perfectSquare.append(i*i)
            cntPerfectSquare[i*i - 1] = 1
        
        if perfectSquare[-1] == n:
            return 1
        
        
        searchQ = deque([])
        for item in perfectSquare:
            searchQ.append(item)
        
        currentStep = 1

        while searchQ:
            
            currentStep += 1
            new_q = deque([])

            while searchQ:
                
                existing_node = searchQ.popleft()

                for j in perfectSquare:
                    
                    if existing_node + j == n:
                        return currentStep
                    
                    elif existing_node + j < n and cntPerfectSquare[existing_node + j - 1] == None:
                        cntPerfectSquare[existing_node + j - 1] = currentStep
                        new_q.append(existing_node + j)
                    
                    elif existing_node + j > n:
                        break
            

            searchQ = new_q


    # DP
    def _numSquares(self, n: int) -> int:

        if n <= 0:
            return 0
        
        dp = [None] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n+1):
            
            local_res = float('inf')
            j = 1

            while (i - j* j >=0):
                local_res = min(local_res, dp[i -j*j]+1)
                j += 1
            
            dp[i] = local_res
        

        return dp[n]