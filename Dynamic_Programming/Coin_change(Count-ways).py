class Solution:
    
    def func (self,sum,n,coins,memo):
        
        if sum < 0:
            return 0
                
        if sum == 0:
            return 1
                
        if n == 0:
            return 0
            
        if memo[sum][n] != -1:
            return memo[sum][n]
                
        memo[sum][n] = self.func(sum-coins[n-1], n, coins, memo) + self.func(sum, n-1, coins, memo)
            
        return memo[sum][n]
        
    
    def count(self, coins, sum):
        # code here
        
        n = len(coins)
        
        memo = [[-1] * (n+1) for x in range (sum+1)]
        #memo[sum+1][n+1]
        
        memo[sum][n] = self.func (sum, n, coins, memo)
        
        return memo[sum][n

