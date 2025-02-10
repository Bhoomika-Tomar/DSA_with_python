def check(stalls, k, dist):
    
    #Placing 1st cow at index 0
    count = 1
    prev = stalls[0]
    
    for i in range (1, len(stalls)):
        
        #Finding min distance b/w current and previous 
        #position of cows
        if stalls[i] - prev >= dist:
            prev = stalls[i]
            count = count + 1
            
        #Return true if all cows aree placed
    return count >= k


class Solution:

    def aggressiveCows(self, stalls, k):
        # your code here
        
        #sorting array to ensure stalls in sequence
        stalls.sort()
        res = 0
        
        #Using binary search
        low = 1
        high = stalls[-1] - stalls[0]
        
        while low <= high:
            mid = low + (high-low)//2
            
            #If mid is possible then update the result and
            #search for larger distance
            if check (stalls, k, mid):
                res = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return res
        
