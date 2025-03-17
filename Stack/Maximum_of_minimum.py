class Solution:
    def maxOfMins(self, arr):
       # code here
       
        n = len(arr)
        res1 = [0] * n #prev
        res2 = [0] * n #next
        stack = []
        ans = [0] * n
       
        for i in range (n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            
            if stack:
                res2[i] = stack[-1]
            else:
                res2[i] = n 
               
            stack.append(i)
            
        while stack:
            stack.pop()
        
        for i in range (n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            
            if stack:
                res1[i] = stack[-1]
            else:
                res1[i] = -1 
               
            stack.append(i)
                        
        for i in range (n):
            l = res2[i] - res1[i] - 1
            ans[l-1] = max(ans[l-1], arr[i])
            
        for i in range (n-2, -1, -1):
            ans[i] = max (ans[i], ans[i+1])
            
        return ans
