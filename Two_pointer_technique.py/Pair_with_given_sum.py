
class Solution:
    def countPairs (self, arr, target) : 
        #Complete the function
         
        n = len(arr)
        res = 0
        left = 0
        right = n - 1
         
        while left < right:
            if arr[left] + arr[right] < target:
                left = left + 1
            elif arr[left] + arr[right] > target:
                right = right - 1
            #When sum is same as target    
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
                     res = res + (count1*(count1 - 1))//2
               
                else:
                    res = res + (count1 * count2)
                    
        return res
                    
