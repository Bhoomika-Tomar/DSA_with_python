import heapq

class Solution:
	def kLargest(self, arr, k):
		# Your code here
		
		#Creating a min heap for k elements
		minH = arr [ : k]
		
		heapq.heapify (minH)
		
		for x in arr[k : ]:
		    if x > minH[0]:
		        heapq.heapreplace (minH, x)
		        
		res = []
		while minH:
		    res.append (heapq.heappop(minH))
		     
		res.reverse()
		 
		return res
