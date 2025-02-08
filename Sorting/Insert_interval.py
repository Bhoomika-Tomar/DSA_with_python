
class Solution:
    def insertInterval(self, intervals, newInterval):
        # Code here
        res = []
        i = 0
        n = len(intervals)
        
        #Adding all intervals which come before new interval
        #Non - overlapping intervals
        while i<n and intervals[i][1] < newInterval[0]:
            res.append (intervals[i])
            i=i+1
            
        #Merging all overlapping intervals
        while i<n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0],newInterval[0])
            newInterval[1] = max(intervals[i][1],newInterval[1])
            i=i+1
        res.append(newInterval)
        
        #Including all remaining elements
        while i<n:
            res.append (intervals[i])
            i=i+1
            
        return res
