class Solution:
    def matrixMultiplication(self, arr):
        # code here
        
        n = len(arr)
        dp = [[0]*n for x in range (n)]
        
        for length in range (2, n):
            for i in range (n - length):
                j = i + length
                dp[i][j] = float('inf')
                
                for k in range (i+1, j):
                    cost = dp[i][k] + dp[k][j] + arr[i]*arr[k]*arr[j]
                    dp[i][j] = min(dp[i][j], cost)
                    
                    
        return dp[0][n-1]
                    
                    