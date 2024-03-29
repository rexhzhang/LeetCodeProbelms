"""
Design a max stack that supports push, pop, top, peekMax and popMax.

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.
Example 1:
MaxStack stack = new MaxStack();
stack.push(5); 
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5
Note:
-1e7 <= x <= 1e7
Number of operations won't exceed 10000.
The last four operations won't be called when stack is empty.
"""

class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.max = -float('inf')
        

    def push(self, x: int) -> None:
        if x > self.max:
            self.max = x
            self.stack.append([x, x])
        else:
            self.stack.append([x, self.max])

    def pop(self) -> int:
        if len(self.stack) == 0:
            return None
        
        result, currentMax = self.stack.pop()
        if len(self.stack) == 0:
            self.max = -float('inf')
            return result
        elif currentMax >= self.max:
            self.max = self.stack[-1][1]
            return result
        else:
            return result


    def top(self) -> int:
        
        if len(self.stack) == 0:
            return None
        return self.stack[-1][0]

    def peekMax(self) -> int:

        if len(self.stack) == 0:
            return None
        return self.stack[-1][1]

    def popMax(self) -> int:
        
        temp = []
        while self.stack[-1][0] != self.max:
            temp.append(self.pop())
        
        result = self.pop()

        while len(temp) > 0:
            self.push(temp.pop())
        
        return result

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()