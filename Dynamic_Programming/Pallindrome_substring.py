class Solution:

    def countPS(self, s):
        # code here
        
        n = len(s)
        dp = [[0] * n for x in range (n)]
        ans = 0
        
        for i in range (n):
            dp[i][i] = True
            
        for i in range (n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                
        for l in range (3, n+1):
            for i in range (n-l+1):
                if s[i] == s[i+l-1] and dp[i+1][i+l-2] == True:
                    dp[i][i+l-1] = True
                    
        for i in range (n):
            for j in range (i+1, n):
                if dp[i][j] == True:
                    ans += 1
                    
        return ans

