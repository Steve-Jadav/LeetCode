class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.min_stack = list()
        
    def push(self, x: int) -> None:
        if (len(self.stack) == 0):
            self.min_stack.append(x)
        elif x <= self.min_stack[-1]:
            self.min_stack.append(x)
        
        self.stack.append(x)

    def pop(self) -> None:
        if (len(self.stack) == 0):
            return None
        
        if (self.stack[-1] == self.min_stack[-1]):
            self.min_stack.pop()
            
        self.stack.pop()

    def top(self) -> int:
        if (len(self.stack) == None):
            return None
        
        return self.stack[-1]

    def getMin(self) -> int:
        if (len(self.min_stack) == 0):
            return None
        
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
