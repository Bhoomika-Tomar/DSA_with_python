
class Solution:
    
    # arr[] : the input array
    
    #Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self,arr):
        #code here
        
        s = set()
        length = 0
        n =len (arr)
        
        #Hash all elements of array 
        for elem in arr:
            s.add(elem)
            
        #Iterate through all elements and find longest length
        for i in range (n):
            #If current element is starting sequence
            if arr[i] - 1 not in s:
                
                #Checking for longest sequence
                j = arr[i]
                while j in s :
                    j = j + 1
                    
                length = max(length, j - arr[i])
                
        return length

