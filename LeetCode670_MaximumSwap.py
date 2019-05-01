"""
Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
Note:
The given number is in the range [0, 10^8]
"""
class Solution:
    def maximumSwap(self, num: int) -> int:
        num_s = str(num)
        a = [int(c) for c in num_s]
        
        for i in range(len(a)-1):
            max_num = [a[i+1], i +1]
            for j in range(i+1, len(a)): 
                # At each digit, if there is a larger digit that occurs later, we want the swap it with the largest such digit that occurs the latest.
                # "=" is for making sure it use the last occurance
                # Example 1993
                if a[j] >= max_num[0]:
                    max_num[0], max_num[1] = a[j], j
            if max_num[0] > a[i]:
                    temp = a[i]
                    a[i] = max_num[0]
                    a[max_num[1]] = temp
                    
                    return int("".join(map(str, a)))

        return int("".join(map(str, a)))