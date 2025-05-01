class Solution:
    def startStation(self, gas, cost):
        # Your code here
        
        n = len(gas)
        
        curr_gas = 0
        start_idx = 0
        
        for i in range (n):
            curr_gas = curr_gas + gas[i] - cost[i]
            
            if curr_gas < 0:
                curr_gas = 0
                start_idx = i + 1
                
        if start_idx == n:
            return -1
            
        curr_gas = 0
        
        for i in range (n):
            
            idx = (start_idx + i) % n
            
            curr_gas = curr_gas + gas[idx] - cost[idx]
            
            if curr_gas < 0:
                return -1
                
        return start_idx



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        gas = list(map(int, input().strip().split()))
        cost = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.startStation(gas, cost)
        print(ans)
        print("~")

# } Driver Code Ends