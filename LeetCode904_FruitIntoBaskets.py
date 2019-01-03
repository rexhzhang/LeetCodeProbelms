"""
In a row of trees, the i-th tree produces fruit with type tree[i].

You start at any tree of your choice, then repeatedly perform the following steps:

Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?



Example 1:

Input: [1,2,1]
Output: 3
Explanation: We can collect [1,2,1].
Example 2:

Input: [0,1,2,2]
Output: 3
Explanation: We can collect [1,2,2].
If we started at the first tree, we would only collect [0, 1].
Example 3:

Input: [1,2,3,2,2]
Output: 4
Explanation: We can collect [2,3,2,2].
If we started at the first tree, we would only collect [1, 2].
Example 4:

Input: [3,3,3,1,2,1,1,2,3,3,4]
Output: 5
Explanation: We can collect [1,2,1,1,2].
If we started at the first tree or the eighth tree, we would only collect 4 fruits.


Note:

1 <= tree.length <= 40000
0 <= tree[i] < tree.length
"""


class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        # length = len(tree)
        # answer = 0
        #
        # for i in range(length):
        #
        #     lastType = tree[i]
        #     count = 1
        #     fruittype = [tree[i], '#']
        #     j = i + 1
        #     while j <= length - 1:
        #         if tree[j] in fruittype:
        #             count += 1
        #             j += 1
        #         elif fruittype[1] == '#':
        #             fruittype[1] = tree[j]
        #             count += 1
        #             j += 1
        #         else:
        #             break
        #
        #     answer = max(count, answer)
        #
        # return answer

        answer = 0
        length = len(tree)
        fruitType = [[tree[0], 0], '#', [tree[0], 0]]
        for i in range(length):
            #
            if tree[i] == fruitType[0][0]:
                fruitType[0][1] += 1

                if fruitType[1] == '#':
                    answer = max(answer, fruitType[0][1])
                else:
                    answer = max(answer, fruitType[0][1] + fruitType[1][1])

                if fruitType[2][0] == tree[i]:
                    fruitType[2][1] += 1
                else:
                    fruitType[2] = [tree[i], 1]

            #
            elif fruitType[1] == '#':
                fruitType[1] = [tree[i], 1]
                answer = max(answer, fruitType[0][1] + fruitType[1][1])

                if fruitType[2][0] == tree[i]:
                    fruitType[2][1] += 1
                else:
                    fruitType[2] = [tree[i], 1]


            elif tree[i] == fruitType[1][0]:
                fruitType[1][1] += 1
                answer = max(answer, fruitType[0][1] + fruitType[1][1])

                if fruitType[2][0] == tree[i]:
                    fruitType[2][1] += 1
                else:
                    fruitType[2] = [tree[i], 1]

            else:
                fruitType[0] = fruitType[2]
                fruitType[1] = [tree[i], 1]
                fruitType[2] = [tree[i], 1]

                answer = max(answer, fruitType[0][1] + fruitType[1][1])

        return answer

a = Solution()
a.totalFruit([0,1,6,6,4,4,6])