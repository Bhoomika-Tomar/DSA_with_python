class Solution:   
    def peakElement(self,arr):
        # Code here
        n = len(arr)
        
        #if only one element exists
        if n == 1:
            return 0
        
        #If first element is peak element
        if arr[0] > arr[1]:
            return 0
            
        #If last element is peak element
        if arr[n-1] > arr[n-2]:
            return n - 1
            
        #USING BINARY SEARCH
        low = 1
        high = n-2
        
        while low <= high:
            mid = low + (high-low)//2
            
            #If peak element is at mid
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
                
            #If peak element is in right subarray
            if arr[mid] < arr[mid+1]:
                low = mid + 1
                
            #If peak element is in left subarray
            else:
                high = mid - 1

        return -1