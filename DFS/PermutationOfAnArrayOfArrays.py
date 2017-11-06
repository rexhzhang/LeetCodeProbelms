"""Given a list of array, return a list of arrays, each array is a combination of one element in each given array.
Let me give you an example to help you understand the question Suppose the input is [[1, 2, 3], [4], [5, 6]],
the output should be [[1, 4, 5], [1, 4, 6], [2, 4, 5], [2, 4, 6], [3, 4, 5], [3, 4, 6]]. """

class Solution:
    def PermuArrays(selfself, arrays):
        """

        :param arrays: List[List[int]]
        :return: List[List[Int]]
        """
        def helper(arrays, index):
            if index == len(arrays): return [[]]

            resultNext = helper(arrays, index+1)
            result = []

            for n in arrays[index]:
                for array in resultNext:
                    result.append([n] + array)

            return result

        return helper(arrays, 0)


obj = Solution()
result = obj.PermuArrays([[1, 2, 3], [4], [5, 6]])
print(result)