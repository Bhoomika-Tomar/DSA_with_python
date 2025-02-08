
class Solution:
    def minRemoval(self, intervals):
        # Code here
        count  = 0
        
        #Sorting with asc order of end points
        intervals.sort (key = lambda x:x[1])
        end = intervals[0][1]
        
        for i in range (1,len(intervals)):
            
            #If there is overlap increment the count by 1
            if intervals[i][0]<end:
                count = count+1
                
            #If there is no overlap then update the end value
            else:
                end = intervals[i][1]
                
        return count
            