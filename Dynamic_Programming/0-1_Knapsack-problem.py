class Solution:
    
    def knapRec (self, W, val, wt, n, memo):
        
        if W == 0 or n == 0:
            return 0
            
        if memo[W][n] != -1:
            return memo[W][n]
            
        pick = 0
        if wt[n-1] <= W:
            pick = self.knapRec (W-wt[n-1],val,wt,n-1,memo)+val[n-1]
        
        notpick = self.knapRec (W, val, wt, n-1, memo)
        
        memo[W][n] = max(pick, notpick)
        
        return memo[W][n]
    
    def knapsack(self, W, val, wt):
        # code here
        
        n = len(wt)
        memo = [[-1]*(n+1) for x in range (W+1)]
        #memo[W+1][n+1]
        
        memo[W][n] = self.knapRec (W, val, wt, n, memo)
        
        return memo[W][n