class Solution:
    def countTriplets(self, arr, target):
        # code here
        
        n = len(arr)
        res = 0
        
        for i in range (n - 2):
            left = i + 1
            right = n - 1
            
            while left < right:
                sum_ = arr[left] + arr[right] + arr[i]
                if sum_ < target:
                    left = left + 1
                elif sum_ > target:
                    right = right - 1
                else:
                    elem1 = arr[left]
                    elem2 = arr[right]
                    
                    count1 = 0
                    count2 = 0
                    
                    while left <= right and arr[left] == elem1:
                        left = left + 1
                        count1 = count1 + 1
                    
                    while left <= right and arr[right] == elem2:
                        right = right - 1
                        count2 = count2 + 1   
                        
                    if elem1 == elem2:
                        res = res + (count1 * (count1-1))//2
                    else:
                        res = res + (count1 * count2) 
                        
        return re
