class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr):
		# code here
		n = len(arr)
		res = arr[0]
		currMax = arr[0]
		currMin = arr[0]
		
		for i in range (1,n):
		    temp = max(arr[i], currMax*arr[i], currMin*arr[i])
		    currMin = min((arr[i], currMax*arr[i], currMin*arr[i]))
		    
		    currMax = temp
		    res = max(res,currMax)
		    
        return res