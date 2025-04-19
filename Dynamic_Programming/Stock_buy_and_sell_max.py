class Solution:
    def maxProfit(self, prices):
        # code here
        
        n = len(prices)
        
        if n == 0:
            return 0
            
        curr = [[0] * 2 for x in range(3)]
        next = [[0] * 2 for x in range(3)]
        
        for i in range (n-1, -1, -1):
            for k in range (1, 3):
                
                #Buy state
                curr[k][1] = max(next[k][0]-prices[i], next[k][1])
                
                #Sell state
                curr[k][0] = max(next[k-1][1]+prices[i], next[k][0])
            
            next = [row[:] for row in curr]
            
        return curr[2][1]
