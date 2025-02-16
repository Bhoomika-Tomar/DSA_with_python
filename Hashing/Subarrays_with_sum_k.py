
class Solution:
    def countSubarrays(self, arr, k):
        # code here
        
        #Using dictionary to store prefix sum frequecies
        prefixSum = { }
        res = 0
        currSum = 0
        
        for val in arr:
            currSum = currSum + val
            
            if currSum == k:
                res = res + 1
                
            if currSum - k in prefixSum:
                res = res + prefixSum[currSum - k]
                
            #Adding prefix sum to dictionary
            prefixSum[currSum] = prefixSum.get(currSum , 0) + 1
            
        return res

