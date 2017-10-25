
class Solution():
    def squareOfsortedList(self, sortedList):
        ans = []
        pos = []
        neg = []
        for num in sortedList:
            if num <= 0:
                neg.append(num * num)
            else:
                pos.append(num * num)

        if len(neg) == 0:
            return pos

        neg = neg[::-1]

        if len(pos) == 0:
            return neg

        p = 0
        n = 0

        while p < len(pos) and n < len(neg):
            if pos[p] <= neg[n]:
                ans.append(pos[p])
                p += 1
            else:
                ans.append(neg[n])
                n += 1

        if p <= len(pos)-1: ans = ans + pos[p:]
        if n <= len(neg)-1: ans = ans + neg[n:]


        return ans

test = Solution()
result = test.squareOfsortedList([-3,-2,-1, 0,1,2,3,4])
print(result)