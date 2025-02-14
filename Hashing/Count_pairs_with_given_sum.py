class Solution:
    #Complete the below function
    def countPairs(self,arr, target):
        #Your code here
        
        #Using Hashmap
        freq = { }
        count = 0
        
        for i in range (len(arr)):
            compliment = target - arr[i]
            if compliment in freq:
                #if compliment exists in freq then increase count
                count = count + freq[compliment]
                
            freq[arr[i]] = freq.get(arr[i], 0) + 1
            
        return count
