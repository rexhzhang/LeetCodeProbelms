class Solution(object):
    """
    Given an int array, which contains positive and negative numbers, requirement is to create an outout array which alternate
    positive and negative numbers and preserve the order within positive numbers and negative numbers

    e.g.
    [1, 8, 2, 4, -3, -4, -6, -1] to
    [1, -3, 8, -4, 2, -6, 4, -1]

    """
    def alterIntArray(self, nums):
        if nums is None or len(nums) == 0:
            raise ValueError("The input is invalid")

        if 0 in nums:
            raise ValueError("The input contains 0")

        pos, neg, ans = [], [], []

        for item in nums:
            if item > 0:
                pos.append(item)
            if item < 0:
                neg.append(item)

        if abs(len(pos) - len(neg)) > 1:
            raise ValueError("length of Positive and Negative differs more than 1!")

        if len(pos) > len(neg):
            ans.append(pos.pop(0))
            while pos:
                ans.append(neg.pop(0))
                ans.append(pos.pop(0))

        if len(pos) < len(neg):
            ans.append(neg.pop(0))
            while neg:
                ans.append(pos.pop(0))
                ans.append(neg.pop(0))

        else:
            while neg:
                ans.append(pos.pop(0))
                ans.append(neg.pop(0))

        print(ans)
        return ans

    def alterIntArray2(self, nums):
        if nums is None or len(nums) == 0:
            raise ValueError("The input is invalid")

        n = len(nums)
        ans = []
        pos, neg = 0, 0

        for element in nums:
            if element == 0:
                raise ValueError("The input contains 0")
            if element > 0:
                pos += 1
            if element < 0:
                neg += 1

        if abs(pos - neg) > 1:
            raise ValueError("length of Positive and Negative differs more than 1!")

        i, j = 0, 0
        if pos > neg: # add "+" first
            while len(ans) < len(nums):
                if pos > 0:
                    while nums[i] < 0:
                        i += 1
                    ans.append(nums[i])
                    i += 1
                    pos -= 1

                if neg > 0:
                    while nums[j] > 0:
                        j += 1
                    ans.append(nums[j])
                    j += 1
                    neg -= 1

        else: # add "-" first
            while len(ans) < len(nums):

                if neg > 0:
                    while nums[j] > 0:
                        j += 1
                    ans.append(nums[j])
                    j += 1
                    neg -= 1

                if pos > 0:
                    while nums[i] < 0:
                        i += 1
                    ans.append(nums[i])
                    i += 1
                    pos -= 1

        print ("alterIntArray2")
        print (ans)
        return ans
test = Solution()
# test.alterIntArray([1, 8, 2, 4, -3, -4, -6, -1])
test.alterIntArray2([1, 8, 2, 4, -3, -4, -6, -1])