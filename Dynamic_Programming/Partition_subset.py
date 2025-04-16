class Solution:
    
    def subset(self, n , arr, sum, memo):
        if sum < 0:
            return 0
            
        if sum == 0:
            return 1
            
        if n == 0:
            return 0
            
        if memo[n][sum] != -1:
            return memo[n][sum]
            
        memo[n][sum] = self.subset(n-1,arr,sum,memo) or self.subset(n-1,arr,sum-arr[n-1],memo)
        
        
        return memo[n][sum]
            
    
    
    def equalPartition(self, arr):
        # code 
        
        n = len(arr)
        sum = 0
        
        for i in range (n):
            sum = sum+arr[i]
            
        if sum % 2 == 1:
            return 0
            
        sum =sum//2
        
        memo = [[-1] * (sum+1) for x in range (n+1)]
        #memo[n+1][sum+1]
        
        memo[n][sum] = self.subset(n, arr, sum , memo)
        
        return memo[n][sum]


#{ 
 # Driver Code Starts
import sys

input = sys.stdin.readline

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        if ob.equalPartition(arr):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends