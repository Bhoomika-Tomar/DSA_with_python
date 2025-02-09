
class Solution:
    def findMin(self, arr):
        #complete the function here
        #Using binary search
        low = 0
        high = len(arr)-1
        
        while low < high:
            
            #When the subarray is sorted
            if arr[low] < arr[high]:
                return arr[low]
                
            #when the current subarray is rotated
            mid = (low+high)//2
            
            #when right half is not sorted then min element
            #is present in right subarray
            if arr[mid] > arr[high]:
                low = mid + 1
            #when right half of subarray is sorted
            else:
                high = mid

        return arr[low]