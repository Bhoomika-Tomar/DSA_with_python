class Solution:
    def maxProfit(self, prices, k):
        # code here
        
        n = len(prices)
        
        if n == 0 or k == 0:
            return 0
            
        
        
        
        
        dp = [[[0] * 2 for x in range (k+1)] for x in range (n+1)]
        
        for i in range (n-1, -1, -1):
            for l in range (1, k+1):
                
                #Buy state
                dp[i][l][1] = max(dp[i+1][l][0]-prices[i], dp[i+1][l][1])
                
                #Sell state
                dp[i][l][0] = max(prices[i]+dp[i+1][l-1][1], dp[i+1][l][0])
                
        
        return dp[0][k][1]
