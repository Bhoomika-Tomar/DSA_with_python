#Using binary search
class Solution:
    def search(self,arr,key):
        # Complete this function
        low = 0
        high = len(arr) - 1
        
        while low <= high:
            mid = low + (high-low)//2
            
            #when key is present at mid
            if arr[mid] == key:
                return mid
                
            #When left half is sorted
            if arr[mid] >= arr[low]:
                #when key is present in left half
                if key >= arr[low] and key < arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
                    
            #When right half is sorted
            else:
                #when key is in right half
                if key > arr[mid] and key <= arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            
        return -1
