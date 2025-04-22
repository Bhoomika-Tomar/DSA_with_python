class Solution:
    
    def calculate (self, l, h, arr, dp):
        dp[l] = arr[l]
        dp[l+1] = max(arr[l], arr[l+1])
        
        for i in range (l+2, h+1):
            dp[i] = max(dp[i-2]+arr[i], dp[i-1])
            
        return dp[h]
    
    def maxValue(self, arr):
        # code here
        
        n = len(arr)
        dp = [0] * (n)
        
        res1 = self.calculate(0, n-2, arr, dp)
        res2 = self.calculate(1, n-1, arr, dp)
        
        return max(res1, res2)
