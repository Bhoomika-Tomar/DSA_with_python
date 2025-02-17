class Solution:
    #Complete the below function
    def countPairs(self, arr, target):
        #Your code here
        
        n = len(arr)
        count = 0
        
        arr.sort()
        
        left = 0
        right = n - 1
        
        while left < right:
            if arr[left] + arr[right] < target:
                count = count + (right - left)
                left = left + 1
                
            else:
                right = right - 1
                
        return count
