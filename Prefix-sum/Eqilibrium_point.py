class Solution:
    #Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        # code here
        
        n = len(arr)
        left_sum = 0
        total_sum = sum (arr)
        
        for i in range (n):
            
            #Removing ith element from right hand side
            total_sum = total_sum - arr[i]
            
            if left_sum == total_sum:
                return i
                
            #Adding ith element to left hand side
            left_sum = left_sum + arr[i]
            
        return -1
