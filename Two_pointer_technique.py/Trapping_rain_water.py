class Solution:
    def maxWater(self, arr):
        # code here
        
        n = len(arr)
        res = 0 
        
        left = 1
        right = n - 2
        
        lmax = arr[left - 1]
        rmax = arr[right + 1]
        
        while left <= right:
            
            if rmax <= lmax:
                res = res + max(0, rmax - arr[right])
                rmax = max(rmax, arr[right])
                right = right - 1
                
            else:
                res = res + max(0, lmax - arr[left])
                lmax = max(lmax, arr[left])
                left = left + 1
                
        return res
