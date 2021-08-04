"""
Implement an iterator to flatten a 2d vector.

For example,
Given 2d vector =

[
  [1,2],
  [3],
  [4,5,6]
]
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,2,3,4,5,6].
"""


class Vector2D(object):
    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.arr = vec2d
        self.row = 0
        self.col = 0

    def next(self):
        """
        :rtype: int
        """
        nextVar = self.arr[self.row][self.col]
        self.col += 1
        return nextVar

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.row <= len(self.arr) - 1:
            if self.col <= len(self.arr[self.row]) - 1:
                return True
            self.col = 0
            self.row += 1

        return False


# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())

i, v = Vector2D([[1,2],[3],[4,5,6]]), []
while i.hasNext():
    v.append(i.next())
    print(v)
