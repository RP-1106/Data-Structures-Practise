class MinStack(object):
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        self.stack.append(val)
        if len(self.minStack)==0:
            self.minStack.append(self.stack[-1])
        else:
            if val<self.minStack[-1]:
                self.minStack.append(val)
            else:
                self.minStack.append(self.minStack[-1])
        
    def pop(self):
        val = self.stack.pop()
        self.minStack.pop()
        return val        

    def top(self):
        return self.stack[-1]
        
    def getMin(self):
        return self.minStack[-1]
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
