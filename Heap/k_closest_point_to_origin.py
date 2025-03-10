import heapq

class Solution:
    
    def squared_dist (self, point):
        
        return point[0] * point[0] + point[1] * point[1]
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Your code here
        
        #Max-heap to store points with their squared 
        #distances
        maxheap = []
        
        for point in points:
            dist = self.squared_dist (point)
            
            if len(maxheap) < k:
                
                heapq.heappush (maxheap,(-dist, point))
            
            else:
                if -dist > maxheap[0][0]:
                    heapq.heappop (maxheap)
                    heapq.heappush (maxheap,(-dist, point))
                
        return [pair[1] for pair in maxheap]
