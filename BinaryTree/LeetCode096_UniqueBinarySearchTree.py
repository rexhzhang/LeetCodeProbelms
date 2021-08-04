"""
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

"""


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        memory = {}
        memory[0] = 1
        memory[1] = 1
        memory[2] = 2
        memory[3] = 5

        for i in range(4, n + 1):
            memory[i] = 0
            for j in range(1, i + 1):
                memory[i] += memory[j - 1] * memory[i - j]

        return memory[n]