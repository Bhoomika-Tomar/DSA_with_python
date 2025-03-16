class Solution:
    def getMaxArea(self,arr):
        #code here
        
        n = len(arr)
        res1 = [0] * n
        res2 = [0] * n
        stack = []
        
        for i in range (n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            
            if stack:
                res1[i] = stack[-1]
            else:
                res1[i] = n
                
            stack.append(i)
            
        while stack:
            stack.pop()
        
        for i in range (0, n):
            
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
             
            if stack:
                res2[i] = stack[-1]
            else:
                res2[i] = -1
                
            stack.append(i)
            
        ans = 0
        
        for i in range (0, n):
            ans = max(ans, arr[i]*(res1[i]-res2[i]-1))
        
        
        return ans
        