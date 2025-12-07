class Solution:
    
    def subsetRec (self, arr, target, n, memo):
        
        if target < 0:
            return 0
            
        if target == 0:
            return 1
            
        if n == 0:
            return 0
            
        if memo[n][target] != -1:
            return memo[n][target]
            
        memo[n][target] = self.subsetRec(arr, target, n-1, memo) or self.subsetRec(arr, target-arr[n-1], n-1, memo) 
        
        return memo[n][target]
    
    def isSubsetSum (self, arr, target):
        # code here
        
        n = len(arr)
        memo = [[-1] * (target+1) for x in range (n+1)]
        #memo[n+1][target+1]
        
        memo[n][target] = self.subsetRec (arr, target, n, memo)
        
        return memo[n][target
        