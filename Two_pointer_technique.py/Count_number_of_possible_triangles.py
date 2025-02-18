
class Solution:
    #Function to count the number of possible triangles.
    def countTriangles(self, arr):
        # code here
        
        res = 0
        n = len(arr)
        
        arr.sort()
        
        for i in range (2, n):
            
            left = 0
            right = i - 1
            
            while left < right:
                if arr[left] + arr[right] > arr[i]:
                    res = res + (right - left)
                    
                    right =right - 1
                    
                else:
                    left = left + 1
                    
        return res

