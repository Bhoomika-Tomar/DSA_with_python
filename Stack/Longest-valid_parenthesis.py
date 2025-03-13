class Solution:
    def maxLength(self, s):
        # code here
        
        stack = []
        n = len(s)
        maxLen = 0
        
        #Initialize by stack -1
        stack.append(-1)
        
        for i in range (n):
            if s[i] == '(':
                stack.append(i)
                
            else:
                stack.pop()
                
                if not stack:
                    stack.append(i)
                else:
                    maxLen = max(maxLen, i - stack[-1])
                    
        return maxLen
