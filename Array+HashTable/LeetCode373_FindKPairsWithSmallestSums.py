"""
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:
Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3

Return: [1,2],[1,4],[1,6]

The first 3 pairs are returned from the sequence:
[1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:
Given nums1 = [1,1,2], nums2 = [1,2,3],  k = 2

Return: [1,1],[1,1]

The first 2 pairs are returned from the sequence:
[1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:
Given nums1 = [1,2], nums2 = [3],  k = 3

Return: [1,3],[2,3]

All possible pairs are returned from the sequence:
[1,3],[2,3]
"""


class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if k > len(nums2) * len(nums1):
            # return "k pairs don't exist"
            k = len(nums2) * len(nums1)
        if k < 1: return []
        ans = [[nums1[0],nums2[0]]]
        k -= 1
        i, j = 0, 0
        while k > 0:
            while i < len(nums1) and j < len(nums2) and k > 0:
                if
                if nums1[i] + nums2[j+1] <= nums1[i+1] + nums2[j]:
                    ans.append([nums1[i], nums2[j+1]])
                    j += 1
                    k -= 1
                else:
                    ans.append([nums1[i+1], nums2[j]])
                    i += 1
                    k -= 1

            if i == len(nums1)-1 and j < len(nums2)-1:
                i = 0
                j += 1

            if j == len(nums2)-1 and i < len(nums1)-1:
                j = 0
                i += 1
        return ans

test = Solution()
nums1 = [1,2]
nums2 = [3]
k = 3
print(test.kSmallestPairs(nums1, nums2, k))
