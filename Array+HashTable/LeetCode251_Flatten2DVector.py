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
        self.Lv1 = 0
        self.Lv2 = 0

    def next(self):
        """
        :rtype: int
        """
        result = self.arr[self.Lv1][self.Lv2]
        if self.Lv2 == len(self.arr[self.Lv1]) - 1 and self.Lv1 < len(self.arr) - 1:
            self.Lv1 += 1
            self.Lv2 = 0
        elif self.Lv2 < len(self.arr[self.Lv1]) - 1:
            self.Lv2 += 1
        elif self.Lv1 == len(self.arr) - 1 and self.Lv2 == len(self.arr[self.Lv1]) - 1:
            self.Lv2 += 1

        return result

    def hasNext(self):
        """
        :rtype: bool
        """
        end = self.Lv1 == len(self.arr) - 1 and self.Lv2 == len(self.arr[-1])
        emptyInput = (self.arr is None) or (len(self.arr) == 0) or (
            len(self.arr) == 1 and len(self.arr[0]) == 0)
        return  not emptyInput and not end


# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())

i, v = Vector2D([[1,2],[3],[4,5,6]]), []
while i.hasNext():
    v.append(i.next())
    print(v)
