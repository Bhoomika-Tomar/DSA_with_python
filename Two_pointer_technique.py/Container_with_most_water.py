class Solution:
    def maxWater(self, arr):
        # code here
        
        res = 0
        n = len(arr)
        left = 0
        right = n - 1
        
        while left < right:
            #water = height * width
            water = min(arr[left], arr[right]) * (right - left)
            res = max (res, water)
            
            if arr[left] < arr[right]:
                left = left + 1
            else:
                right = right - 1
                
        return res