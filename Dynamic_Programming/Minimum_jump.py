class Solution:
	def minJumps(self, arr):
	    # code here
	    
	    n = len(arr)
	    dp = [n+1]*n
	    
	    dp[0] = 0
	    
	    for i in range (1, n):
	        for j in range (i):
	            if arr[j] + j >= i:
	                dp[i] = min(dp[i], dp[j] + 1)
	                
	    
	    if dp[n-1] == n+1:
	        return -1
	        
	    return dp[n-1]