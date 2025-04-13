class Solution:
    
    def mincoinsRec (self, sum, n, coins, memo):
        if sum < 0:
            return float('inf')
            
        if sum == 0 :
            return 0
            
        if n == 0:
            return float('inf')
            
        if memo[n][sum] != -1:
            return memo[n][sum]
            
        take = self.mincoinsRec (sum-coins[n-1], n, coins, memo)
        if take != float('inf'):
            take += 1
            
        nottake = self.mincoinsRec (sum, n-1, coins, memo)
        
        memo[n][sum] = min(take, nottake)
        
        return memo[n][sum]
    
    
	def minCoins(self, coins, sum):
		# code here
		
		n = len(coins)
		memo = [[-1] * (sum+1) for x in range (n+1)]
		#memo[n+1][sum+1]
		
		memo[n][sum] = self.mincoinsRec (sum, n, coins, memo)
		
		if memo[n][sum] == float('inf'):
		    return -1
		    
		return memo[n][sum]

