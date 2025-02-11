class Solution:
    def kthMissing(self, arr, k):
        # code here
        
        #Using binary search
        low = 0
        high = len(arr) - 1
        #if no positive no is missing from sorted array
        res = len(arr) + k
        
        while low <= high:
            mid = low + (high - low) // 2
            #applying binary search for arr[i] > [k+i]
            if arr[mid] > k + mid:
                res  = k + mid
                high = mid - 1
            else:
                low = mid + 1
                    
        return res
