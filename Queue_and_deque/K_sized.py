from  collections import deque

class Solution:
    def maxOfSubarrays(self, arr, k):
        # code here
        
        n = len(arr)
        res = []
        dq = deque()
        
        for i in range (0, k):
            while dq and arr[i] >= arr[dq[-1]]:
                dq.pop()
                
            dq.append(i)
            
        for i in range (k, n):
            res.append(arr[dq[0]])
            
            while dq and dq[0] <= i-k:
                dq.popleft()
                
            while dq and arr[i] >= arr[dq[-1]]:
                dq.pop()
                
            dq.append(i)
            
        res.append(arr[dq[0]])
        
        return res
                
        