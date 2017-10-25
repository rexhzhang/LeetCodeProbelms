class Solution (object):

    def __init__(self, s, t):
        self.s = s
        self.t = t


    def inSnotT(self):
        arrS = self.s.split(" ")
        arrT = self.t.split(" ")
        ans = []
        for word in arrS:
            if word not in arrT:
                ans.append(word)

        print(ans)

test1 = Solution("I like cheese","like")
test1.inSnotT()
test2 = Solution("","")
test2.inSnotT()