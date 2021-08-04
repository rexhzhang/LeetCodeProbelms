"""
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
Notes:

You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
"""

# 两个stack 一个负责正序，一个负责正序的反转，当pop的时候，如果反转的stack中还有element，直接pop
# 当push时如果反转的stack中有，需将反转stack中的element pop 并 压入 正序stack，再push

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_A = []
        self.stack_B = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if self.stack_A:
            self.stack_A.append(x)
        else:
            while self.stack_B:
                self.stack_A.append(self.stack_B.pop())
            self.stack_A.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.stack_B:
            return self.stack_B.pop()
        else:
            while self.stack_A:
                self.stack_B.append(self.stack_A.pop())
            return self.stack_B.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stack_A:
            return self.stack_A[0]
        else:
            return self.stack_B[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return True if (len(self.stack_A) == 0 and len(self.stack_B) == 0 ) else False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()