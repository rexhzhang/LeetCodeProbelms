import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k is None or nums is None or k > len(nums):
            return []

        heapList = []
        hashMap = {}

        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1

        for key in hashMap:
            heapq.heappush(heapList, hashMap[key])

        value = heapq.nlargest(k, heapList)

        ans = []
        for key in hashMap:
            if hashMap[key] in value:
                ans.append(key)

        return ans


test = Solution()
test.topKFrequent([1,1,1,2,2,3], 2)