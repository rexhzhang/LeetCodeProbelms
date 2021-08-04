"""
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

For example,
add(1); add(3); add(5);
find(4) -> true
find(7) -> false
"""


class TwoSum(object):
    """
    When # of Add operations >> than # Find operations
    O(1): add
    O(n): find
    O(n): space
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashTable = {}

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        self.hashTable[number] = self.hashTable.get(number, 0) + 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for key in self.hashTable:
            target = value - key
            if target == key:
                if self.hashTable[key] >= 2:
                    return True
            elif target in self.hashTable:
                return True

        return False

        # Your TwoSum object will be instantiated and called as such:
        # obj = TwoSum()
        # obj.add(number)
        # param_2 = obj.find(value)

class TwoSum2(object):
    """
    When # of Find operations >> than # Add operations
    O(n): add
    O(1): find
    O(n^2): space + O(n) space
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = set()
        self.resultList = set()

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        if number in self.arr:
            for num in self.arr:
                self.resultList.add(num + number)
        else:
            for num in self.arr:
                self.resultList.add(num + number)
            self.arr.add(number)

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        return value in self.resultList