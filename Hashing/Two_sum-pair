class Solution:
	def twoSum(self, arr, target):
		# code here
		#Sort the array
		arr.sort()
		
		left = 0
		right= len(arr) - 1
		
		while left < right:
		    sum =arr[left] + arr[right]
		    
		    if sum == target:
		        return True
		        
		    elif sum < target:
		        left = left + 1
		        
		    else:
		        right = right - 1
		        
		return False
		