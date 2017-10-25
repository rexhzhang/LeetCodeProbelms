class Solution(object):

    def hIndex(self, citations):
        # [ 3, 0, 6, 1, 5] hindex = 3, hash_map[citation] = # of citations > citation
        n = len(citations)
        citationsCount = [0 for _ in range(n + 1)]

        for citationNum in citations:
            if citationNum >= n:
                citationsCount[n] += 1
            else:
                citationsCount[citationNum] += 1

        i = n - 1
        ans = 0
        while i >= 0:
            citationsCount[i] += citationsCount[i+1]
            if citationsCount[i+1] >= i+1:
                return i + 1
            i -= 1

        return 0


test1 = Solution()
print(test1.hIndex([100]))