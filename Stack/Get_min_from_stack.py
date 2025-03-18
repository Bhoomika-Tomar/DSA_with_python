class Solution:

    def __init__(self):
        # code here
        self.s = []
        self.minElem = -1
    # Add an element to the top of Stack
    def push(self, x):
        # code here
        if not self.s:
            self.minElem = x
            self.s.append(x)
            
        elif x < self.minElem:
            self.s.append (2 * x - self.minElem)
            self.minElem = x
            
        else:
            self.s.append (x)

    # Remove the top element from the Stack
    def pop(self):
        # code here
        if not self.s:
            return
        
        top = self.s.pop()
        
        if top < self.minElem:
            self.minElem = 2 * self.minElem - top

    # Returns top element of Stack
    def peek(self):
        # code here
        if not self.s:
            return -1
        
        top = self.s[-1]
        
        return self.minElem if self.minElem > top else top

    # Finds minimum element of Stack
    def getMin(self):
        # code here
        if not self.s:
            return -1
            
        return self.minElem

