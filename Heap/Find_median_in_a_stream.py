
import heapq

class Solution:
    def getMedian(self, arr):
        
        #Max heap to store smaller half of elements
        leftMaxHeap = []
        
        #Min heap to store greater half of elements
        rightMinHeap = [] 
        
        res = []
        
        for num in arr:
            heapq.heappush (leftMaxHeap, -num)
            
            temp = -heapq.heappop (leftMaxHeap)
            heapq.heappush (rightMinHeap, temp)
            
            #Balance if min heap has more elements
            if len(rightMinHeap) > len(leftMaxHeap): 
                temp = heapq.heappop (rightMinHeap)
                heapq.heappush (leftMaxHeap, -temp)
                
            if len(leftMaxHeap) != len(rightMinHeap):
                
                median = -leftMaxHeap[0]
            else:
                median = (-leftMaxHeap[0] + rightMinHeap[0])/2.0
            
            res.append(median)
            
        return res
