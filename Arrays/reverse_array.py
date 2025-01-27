#class Solution:
    #def reverseArray(self, arr):
        # code here
        #arr1 = arr[::-1]
        #return arr1
        
        
class Solution:
    def reverseArray(self, arr):
        # In-place reversal using the two-pointer approach
        left, right = 0, len(arr) - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr        
