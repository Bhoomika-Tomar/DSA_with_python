class Solution:
    
    def maxRec (self, n, arr, memo):
        if memo[n] != -1:
            return memo[n]
            
        if n == 1:
            memo[n] = arr[n-1]
            
        elif n == 2:
            memo[n] = max(arr[n-1], arr[n-2])
            
        else:
            memo[n] = max(arr[n-1] + self.maxRec(n-2, arr, memo), self.maxRec(n-1,arr,memo))
            
        return memo[n]
            
    
    def findMaxSum(self,arr):
        # code here
        
        n = len(arr)
        memo = [-1] * (n+1)
        
        memo[n] = self.maxRec (n, arr, memo)
        
        return memo[n]


#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):

        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.findMaxSum(a))
        print("~")

# } Driver Code Ends