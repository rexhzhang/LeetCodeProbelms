"""

Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between
answers, output all of them with no order requirement. You could assume there always exists an answer.

Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
Example 2:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
Note:
The length of both lists will be in the range of [1, 1000].
The length of strings in both lists will be in the range of [1, 30].
The index is starting from 0 to the list length minus 1.
No duplicates in both lists.

"""
"""

解题思路: 本题涉及到<比较>, 所以我们把一个list建成一个hashmap, key是餐厅，value是index
另外维持一个indexSum 和一个 stack，当indexSum比当前小时，清空stack，重新添加，当indexSum和当前一样时，在后面继续
append

"""

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        if list1 is None or list2 is None or len(list1) == 0 or len(list2) == 0: return []
        hmap = {}
        stack, indexSum = [], len(list1) + len(list2)
        for i in range(len(list1)):
            hmap[list1[i]] = i

        for i in range(len(list2)):
            if list2[i] in hmap:
                if i + hmap[list2[i]] < indexSum:
                    del stack[:]
                    stack.append(list2[i])
                    indexSum = i + hmap[list2[i]]
                elif i + hmap[list2[i]] == indexSum:
                    stack.append(list2[i])

        return stack
