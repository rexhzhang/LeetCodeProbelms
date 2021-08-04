"""
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.

Notes:

You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is
empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque
(double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
"""

from collections import deque


class MyStack(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque([])
        self.q2 = deque([])

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        if x is None:
            raise ValueError("Invalid Input")
        if len(self.q1) > 0:
            self.q1.append(x)
        else:
            self.q2.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if len(self.q1) == 0 and len(self.q2) == 0: raise ValueError("The stack is empty")
        if len(self.q1) == 0:
            while len(self.q2) > 1:
                self.q1.append(self.q2.popleft())
            return self.q2.popleft()
        else:
            while len(self.q1) > 1:
                self.q2.append(self.q1.popleft())
            return self.q1.popleft()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if len(self.q1) == 0 and len(self.q2) == 0: raise ValueError("The stack is empty")
        if len(self.q1) != 0:
            return self.q1[-1]
        else:
            return self.q2[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.q1) == 0 and len(self.q2) == 0

        # Your MyStack object will be instantiated and called as such:
        # obj = MyStack()
        # obj.push(x)
        # param_2 = obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.empty()

