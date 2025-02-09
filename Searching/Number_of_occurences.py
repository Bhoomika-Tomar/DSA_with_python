#Creating lower bound function
def lower_bound (arr,target):
    res = len(arr)
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = low + (high-low)//2
        if arr[mid] >= target:
            res = mid
            high = mid -1
        else:
            low = mid + 1
    
    return res
    
#Creating upper bound function
def upper_bound (arr,target):
    res = len(arr)
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = low + (high-low)//2
        if arr[mid] > target:
            res = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return res


class Solution:
    def countFreq(self, arr, target):
        #code here
        return upper_bound(arr,target)-lower_bound(arr,target)
        
