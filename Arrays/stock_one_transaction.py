class Solution:
    def maximumProfit(self, prices):
        # code here
        res = 0 
        minSoFar = prices[0]
        
        for i in range (1,len(prices)):
            minSoFar = min (prices[i],minSoFar)
            
            res = max(res, prices[i]-minSoFar)
            
         
        return res
         