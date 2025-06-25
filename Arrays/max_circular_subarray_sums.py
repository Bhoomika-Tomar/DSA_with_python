#Complete this function
#Function to find maximum circular subarray sum.
def circularSubarraySum(arr):
    ##Your code here
    totalSum = 0
    currMaxSum = 0
    currMinSum = 0 
    maxSum = arr[0]
    minSum = arr[0]
    
    for i in range (len(arr)):
        #kadane's for max sum subarray
        currMaxSum = max(currMaxSum+arr[i], arr[i])
        maxSum = max(maxSum, currMaxSum)
        
        #kadane's for min sum subarray
        currMinSum = min(currMinSum+arr[i], arr[i])
        minSum = min(minSum, currMinSum)
        
        totalSum = totalSum + arr[i]
        
    normalSum = maxSum
    circularSum = totalSum - minSum
    
    if totalSum == minSum:
        return normalSum
        
    
    return max(circularSum, normalSum)
        
        