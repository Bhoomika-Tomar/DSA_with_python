class Solution:
    def lcs(self, s1, s2):
        # code here
        
        m = len(s1)
        n = len(s2)
        
        #Initializing matrix of (m+1)*(n+1)
        dp = [[0] * (n+1) for x in range (m+1)]
        
        #Building in bottom-up approach
        for i in range (1, m+1):
            for j in range (1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
                    
        return dp[m][n]

