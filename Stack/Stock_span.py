class Solution:
    def calculateSpan(self, arr):
        #write code here
        
        n = len(arr)
        res = [0] * n
        stack = []
        
        for i in range (n):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
                
            if stack:
                res[i] = i - stack[-1]
            else:
                res[i] = i + 1
                
            stack.append(i)
            
        return res
    
         