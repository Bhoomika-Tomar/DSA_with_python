
class Solution:
    def productExceptSelf(self, arr):
        #code here
        
        n = len(arr)
        zeros = 0
        idx = -1
        prod = 1
        
        #Keeping track of no of zeros and their indexes
        for i in range (n):
            if arr[i] == 0:
                zeros = zeros + 1
                idx = i
            else:
                prod = prod * arr[i]
        
        #When there are two zeros in array
        res = [0] * n
                
        #When there are no zeros in array
        if zeros == 0:
            for i in range(n):
                res[i] = prod // arr[i]
                
        #When there is one zero in array
        elif zeros == 1:
            res[idx] = prod
            
        return res
