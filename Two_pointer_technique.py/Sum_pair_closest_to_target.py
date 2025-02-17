class Solution:
    def sumClosest(self, arr, target):
        # code here
        
        n = len(arr)
        res = []
        minDiff = float('inf')
        
        arr.sort()
        
        left = 0
        right = n - 1
        
        while left < right:
            sum = arr[left] + arr[right]
            if abs(sum - target) < minDiff:
                minDiff = abs(sum- target)
                res = [arr[left], arr[right]]
                
            elif abs(sum - target) == minDiff:
                if arr[right] - arr[left] > res[1] - res[0]:
                    res = [arr[left], arr[right]]
                    
            if sum > target:
                right = right - 1
            elif sum < target:
                left = left + 1
            else:
                break
            
        return res

