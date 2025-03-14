class Solution:
    # Function to find the next greater element for each element of the array.
    def nextLargerElement(self, arr):
        # code here
        
        n = len(arr)
        res = [-1] * n
        stack = []
        
        #Traversing from right to left
        for i in range (n-1, -1, -1):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
                
            if stack:
                res[i] = arr[stack[-1]]
                
            stack.append(i)
            
        return res
