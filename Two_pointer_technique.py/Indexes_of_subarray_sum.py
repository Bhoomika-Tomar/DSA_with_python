class Solution:
    def subarraySum(self, arr, target):
        # code here
        
        res = []
        curr = 0
        start = 0 
        end = 0
        
        for i in range (len(arr)):
            curr = curr + arr[i]
            
            if curr >= target:
                end = i
                
                while curr > target and start < end:
                    curr = curr - arr[start]
                    start = start + 1
                    
                if curr == target:
                    res.append (start + 1)
                    res.append (end + 1)
                    return res
                    
        return [-1]
